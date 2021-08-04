from re import compile as cmp
import numpy as np
import pandas as pd


class Preprocess:
    def __init__(self):
        self.exp_reg = {'Chapter': cmp(' \d{1,2}\. [A-Z]{4}'),
                        'Section': cmp(' \d{1,2}\.\d{1,2} '),
                        'Sub-section': cmp('\d{1,2}\.\d{1,2}\.\d{1,2} '),
                        'Table': cmp('Tabela \d{1,2}\.'),
                        'Figure': cmp('Figura \d{1,2}\.'),
                        'Anexos': cmp(' \d{1,2}\. Anexos'),
                        'Anexo': cmp(' Anexo \d{1,2}\.')}
        
        self._rodape = cmp('Fundação ABC \| [^\|]+ \| [^\|]+ \| Página [0-9]+ de [0-9]+')

    def get_structure(self, pages: list):
        for p in pages:
            assert isinstance(p, str)
        
        _joined = ('').join(pages).replace('\n', '')
        res = self.exp_reg
        
        struc = {}
        
        p = res['Anexos']
        for m in p.finditer(_joined):
            ch = m.group().split('.')[1][1:]
            struc[ch] = {'pos': m.start()}

        p = res['Chapter']
        for m in p.finditer(_joined):
            ch = m.group().split('.')[0][1:]
            struc[ch] = {'pos': m.start()}

        p = res['Section']
        for m in p.finditer(_joined):
            ch, sec = m.group().split('.')[:2]
            ch = ch[1:]
            sec = sec[:-1]
            if ch not in struc:
                continue
            struc[ch][sec] = {'pos': m.start()}

        p = res['Sub-section']
        for m in p.finditer(_joined):
            ch, sec, sub = m.group().split('.')[:3]
            sub = sub[:-1]
            struc[ch][sec][sub] = {'pos': m.start()}
        
        p = res['Table']
        for m in p.finditer(_joined):
            tab = m.group().split('.')[0]
            struc[tab] = {'pos': m.start()}
        
        p = res['Figure']
        for m in p.finditer(_joined):
            tab = m.group().split('.')[0]
            struc[tab] = {'pos': m.start()}
        
        p = res['Anexo']
        for m in p.finditer(_joined):
            ch = m.group().split('.')[0]
            struc[ch] = {'pos': m.start()}
        
        return struc
    
    def get_strcuture_content(self, pages: list, struc: dict):
        for p in pages:
            assert isinstance(p, str)
        
        _joined = ('').join(pages).replace('\n', '')
        
        _struc = set()
        def _fill(curr, name):
            b = (curr['pos'], name)
            _struc.add(b)

            for k in sorted(curr.keys()):
                if k not in ['pos', 'type']:
                    _fill(curr[k], f'{name}.{k}')
        
        struc['pos'] = 0
        _fill(struc, '')
        
        _struc = list(_struc)
        _struc = sorted(_struc, key=lambda x: x[0]) # Sort by reading order
        
        cont = {}
        prev = _struc[0]
        for pos in _struc[1:]:
            num = prev[1][1:]
            cont[num] = _joined[prev[0]: pos[0]]
            
            p = self._rodape
            for m in p.finditer(cont[num]):
                cont[num] = cont[num].replace(m.group(), '')
            
            prev = pos
        
        num = prev[1][1:]
        cont[num] = _joined[prev[0]:]
        
        return cont


class TablePreprocess:
    def __init__(self):
        self.tab_start = cmp('[\s]*[^\s]+\s{5}[\s]+')
        self.tab_token = cmp('([^\s]+(\s{0,3}[^\s]+)*)|(\s{4}[\s]*)')
        pat1 = [['token' for _ in range(15)] for _ in range(3)]
        pat1[1][4:10] = ['empty' for _ in range(4, 10)]
        pat1[1][11] = 'empty'
        pat1[1][13:15] = ['empty' for _ in range(13, 15)]
        self._tab_pat = {'Table content 1': pat1}
    
    def parse_table(self, cont: str): # , tipo: str
        ''' cont must be spaced pdf format, extracted with
            pdftotext -layout
        '''
        
        # Get line tokens
        tokens = cont.split('\n')
        
        # Get compiled regex for table start and table cell token
        p = self.tab_start
        p_token = self.tab_token

        tab = []
        curr_tab = []
        last_row = 0
        is_table = False
        _dfs = []
        for i, t in enumerate(tokens):
            ms = p.finditer(t)
            if any(True for _ in ms):
                if 'Tabela' in t or 'Figura' in t:
                    if len(curr_tab) > 1:
                        tab.append(curr_tab)
                    curr_tab = []
                    is_table = ('Tabela' in t)
                else:
                    _ms = p_token.finditer(t)
                    curr_tab.append([])
                    for _m in _ms:
                        curr_tab[-1].append(_m.group())
                last_row = i
            else:
                if i - last_row > 5:
                    if len(curr_tab) > 1 and is_table:
                        tab.append(curr_tab)
                    curr_tab = []
                    is_table = False

        tab2 = []

        for t in tab:
            if len(t) == 0:
                continue

            t2 = []
            space_mu = np.inf
            n_cols = 0
            r_cols = []
            width = 0
            for row in t:
                spacings = [_tok for _tok in row if all([ch == ' ' for ch in _tok])]
                toks = [_tok for _tok in row if not all([ch == ' ' for ch in _tok])]

                _space_mu = np.mean([len(_tok) for _tok in spacings])
                space_mu = min(space_mu, _space_mu)

                _n_cols = len(toks)
                r_cols.append(_n_cols)
                n_cols = max(n_cols, _n_cols)

                width = max(width, np.sum([len(_tok) for _tok in toks])
                                   + np.sum([len(_tok) for _tok in spacings]))
            space_mu = int(space_mu) + 1
            n_cols += 1

            t_grid = []
            for row in t:
                _row = []
                for _tok in row:
                    if not all([ch == ' ' for ch in _tok]):
                        _row.append(_tok.replace(' ', '_'))
                    else:
                        _row.append(_tok)
                t_grid.append(''.join(_row) + ' ' * (width - len(''.join(row))))

            divs = [0 for _ in range(width)]
            for row in t_grid:
                for c in range(width):
                    divs[c] += int(row[c] != ' ')

            _med = np.median(divs)
            dmed = [0 for _ in divs]
            for i in range(len(divs)):
                _med = np.median(divs[max(0, i - 20): i + 20])
                if divs[i] > _med:
                    dmed[i] = 1

            lakes = []
            _curr = 0
            while _curr < len(divs):
                while _curr < len(divs) and dmed[_curr] == 0:
                    _curr += 1

                if _curr == len(divs):
                    break

                lake0 = _curr
                while _curr < len(divs) and dmed[_curr] == 1:
                    _curr += 1

                lake1 = _curr - 1

                lakes.append((lake0, lake1))

            col_start = [0]
            for i in range(len(lakes) - 1):
                _pos = (lakes[i][1] + lakes[i + 1][0]) // 2
                col_start.append(_pos)

            t_csv = []
            t_pd = []
            for i, row in enumerate(t):
                row2 = []
                t_pos = 0
                for _tok in row:
                    if not all([ch == ' ' for ch in _tok]):
                        for j in range(len(col_start)):
                            if col_start[j] > t_pos:
                                break
                            if len(row2) < j + 1:
                                row2.append(';')
                        __tok = _tok.replace('_', ' ')
                        row2[j - 1] = f'{row2[j - 1][:-1]} {__tok};'
                    t_pos += len(_tok)
                t_csv.append(''.join(row2))
                t_pd.append([_rt.replace(';', '') for _rt in row2])
            
            t_pd_cols = max([len(_row) for _row in t_pd])
            t_pd = [_row + ['' for _ in range(t_pd_cols - len(_row))] for _row in t_pd]
            
            _df = pd.DataFrame(t_pd[1:], columns=t_pd[0])
            _dfs.append(_df)
        return _dfs


class _Preprocess:
    def __init__(self):
        pass
    
    def remove_header(self, pages: list, size: int = 71):
        no_header = []
        for index, page in enumerate(pages):
            no_header.append(page[size:])
        return no_header
    
    def find_sections(self, pages: list):
        sections = []
        sec_index = 1
        for page in pages:
            splitted = page.split('\n \n \n')
            for s in splitted:
                s = s.replace('\n', '').strip()
                try:
                    if s[0].isnumeric() and int(s[0]) == sec_index and s.split(' ')[1].isupper():
                        sections.append(s)
                        sec_index += 1
                except IndexError:
                    pass
        return sections

    def split_by_section(self, pages: list, sections: list):
        sections_data = {}
        for s in sections:
            sections_data[s] = []
        last_section = sections[0]
        for page in pages:
            p = page.replace('\n', '').strip()
            found = False
            for s in sections:
                if s in p:
                    sections_data[s].append(page)
                    last_section = s
                    found = True
            if not found:
                sections_data[last_section].append(page)
        return sections_data

    def get_paragraphs(self, data):
        # Separate by paragraph
        aux = data.split('\n \n \n')
        return [a.replace('\n', '').strip() for a in aux]

    def split_paragraphs(self, data: dict):
        for section in data:
            for index, page in enumerate(data[section]):
                data[section][index] = self.get_paragraphs(page)
        return data

    def remove_duplicated(self, data: dict):
        # Remove duplicated left
        for section in data:
            removed = False
            for page in data[section]:
                while True:
                    try:
                        if section not in page[0]:
                            rm = page.pop(0)
                            removed = True
                        else:
                            break
                    except IndexError:
                        break
                if removed:
                    break

        # Remove duplicated right
        sections = list(data.keys())
        for index, section in enumerate(sections):
            for sec_aux in sections[index+1:]:
                for k, page in enumerate(data[section]):
                    if sec_aux in page:
                        data[section] = data[section][:k+1]
                        par_index = data[section][k].index(sec_aux)
                        data[section][k] = data[section][k][:par_index]
        return data
    
    def clean(self, data:dict):
        for section in data:
            data[section] = [a for a in data[section] if a != []]
            for indx, page in enumerate(data[section]):
                data[section][indx] = [p for p in page if p != '']
    
        return data