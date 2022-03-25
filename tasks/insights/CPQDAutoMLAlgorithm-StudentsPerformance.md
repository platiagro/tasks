<h1>CPQD AutoML Algorithm - StudentsPerformance</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 1000 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">math score</th>
<th align="right">reading score</th>
<th align="right">writing score</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">1000.00</td>
<td align="right">1000.00</td>
<td align="right">1000.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">66.09</td>
<td align="right">69.17</td>
<td align="right">68.05</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">15.16</td>
<td align="right">14.60</td>
<td align="right">15.20</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">17.00</td>
<td align="right">10.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">57.00</td>
<td align="right">59.00</td>
<td align="right">57.75</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">66.00</td>
<td align="right">70.00</td>
<td align="right">69.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">77.00</td>
<td align="right">79.00</td>
<td align="right">79.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">race/ethnicity</th>
<th align="left">parental level of education</th>
<th align="left">test preparation course</th>
<th align="left">gender</th>
<th align="left">lunch</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">1000</td>
<td align="left">1000</td>
<td align="left">1000</td>
<td align="left">1000</td>
<td align="left">1000</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">group C</td>
<td align="left">some college</td>
<td align="left">none</td>
<td align="left">female</td>
<td align="left">standard</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">319</td>
<td align="left">226</td>
<td align="left">642</td>
<td align="left">518</td>
<td align="left">645</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-StudentsPerformance/figures/a8e63aba-6671-4cdf-a70b-e7a439482ef9.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 50 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">math score</th>
<th align="right">reading score</th>
<th align="right">writing score</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">50.00</td>
<td align="right">50.00</td>
<td align="right">50.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">64.56</td>
<td align="right">69.42</td>
<td align="right">67.98</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">34.39</td>
<td align="right">33.64</td>
<td align="right">34.24</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">17.00</td>
<td align="right">10.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">29.00</td>
<td align="right">34.00</td>
<td align="right">33.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">87.00</td>
<td align="right">96.00</td>
<td align="right">93.50</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">96.00</td>
<td align="right">100.00</td>
<td align="right">99.75</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">race/ethnicity</th>
<th align="left">parental level of education</th>
<th align="left">test preparation course</th>
<th align="left">gender</th>
<th align="left">lunch</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">50</td>
<td align="left">50</td>
<td align="left">50</td>
<td align="left">50</td>
<td align="left">50</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">group E</td>
<td align="left">some high school</td>
<td align="left">none</td>
<td align="left">female</td>
<td align="left">standard</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">13</td>
<td align="left">11</td>
<td align="left">30</td>
<td align="left">37</td>
<td align="left">29</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-StudentsPerformance/figures/72c9e71e-0dad-4b2e-b1f1-b42da3f1e925.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['math score', 'reading score', 'writing score'] com uma quantidade de 2 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(73.6, 86.8]</td>
<td align="right">0.02</td>
<td align="right">0.98</td>
</tr>
<tr>
<td align="left">(60.4, 73.6]</td>
<td align="right">0.44</td>
<td align="right">0.56</td>
</tr>
<tr>
<td align="left">(33.934, 47.2]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(47.2, 60.4]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(86.8, 100.0]</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['math score', 'reading score', 'writing score'] com uma quantidade de 2 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(73.6, 86.8]</td>
<td align="right">0.98</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">(60.4, 73.6]</td>
<td align="right">0.56</td>
<td align="right">0.44</td>
</tr>
<tr>
<td align="left">(33.934, 47.2]</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">(47.2, 60.4]</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">(86.8, 100.0]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Comparação dos Métodos</h3>
<p>Na tabela abaixo podemos observar a comparação de todos os métodos de clustering testados. O método com o maior score será considerado o melhor método, sendo este utilizado nas próximas análises.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Feature Permutation 3 dim.</th>
<th align="right">Multidimensional</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">math score - reading score - writing score</td>
<td align="right">0.48</td>
<td align="right">0.48</td>
</tr>
</tbody>
</table><p><em>Análise de score do agrupamento.</em></p>
<h3>Insights - Variáveis Numéricas</h3>
<p>Insights obtidos das variáveis numéricas estão disponíveis nas tabelas de médias e variâncias abaixo, onde são apresentadas as diferenças das médias e variâncias entre a população geral e cada um dos grupos. A idéia é facilitar a observação de tendências distintas em cada um dos grupos, em relação a população geral. A tabela de variância é importante de um ponto de vista de análise da variação das features dentro de cada um dos grupos. A ideia é que a variância dentro de um grupo específico seja menor em relação a população em geral.</p>
<p>Figuras também são aliadas importantes na visualização de dados. Nas figuras de médias e variâncias abaixo estão presentes duas figuras que representam a variação de média e variância de cada grupo em relação a população geral. Dados variando para a cor azul significam que a variação é negativa, enquanto dados variando para cores vermelhas significam que a variação é positiva.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">math score</td>
<td align="right">8.84</td>
<td align="right">-11.02</td>
<td align="right">-1.61</td>
</tr>
<tr>
<td align="left">reading score</td>
<td align="right">9.23</td>
<td align="right">-11.49</td>
<td align="right">0.26</td>
</tr>
<tr>
<td align="left">writing score</td>
<td align="right">9.56</td>
<td align="right">-11.90</td>
<td align="right">-0.08</td>
</tr>
</tbody>
</table><p><em>Diferença de Média entre População - Grupos</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">math score</td>
<td align="right">0.66</td>
<td align="right">-0.82</td>
<td align="right">-0.12</td>
</tr>
<tr>
<td align="left">reading score</td>
<td align="right">0.72</td>
<td align="right">-0.89</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">writing score</td>
<td align="right">0.71</td>
<td align="right">-0.88</td>
<td align="right">-0.01</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-StudentsPerformance/figures/c07b4261-cf9a-4ae2-9488-c8ed124c4ef5.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-StudentsPerformance/figures/343ee6af-aa4f-4391-934c-4d63c242903f.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature writing score e no grupo 0, com valor de 9.56. A maior variação negativa foi na feature writing score e no grupo 1, com o valor registrado de -11.90</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">race/ethnicity</th>
<th align="left">parental level of education</th>
<th align="left">test preparation course</th>
<th align="left">gender</th>
<th align="left">lunch</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">group C</td>
<td align="left">high school</td>
<td align="left">none</td>
<td align="left">male</td>
<td align="left">standard</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">174</td>
<td align="left">103</td>
<td align="left">315</td>
<td align="left">236</td>
<td align="left">390</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.3301707779886148</td>
<td align="left">0.24349881796690306</td>
<td align="left">0.7446808510638298</td>
<td align="left">0.557919621749409</td>
<td align="left">0.7400379506641366</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.0059602516728253785</td>
<td align="left">0.04665671270374516</td>
<td align="left">0.1004703247480403</td>
<td align="left">0.06423541122309323</td>
<td align="left">0.09161689803255768</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">race/ethnicity</th>
<th align="left">parental level of education</th>
<th align="left">test preparation course</th>
<th align="left">gender</th>
<th align="left">lunch</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">group C</td>
<td align="left">associate's degree</td>
<td align="left">none</td>
<td align="left">female</td>
<td align="left">standard</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">134</td>
<td align="left">127</td>
<td align="left">297</td>
<td align="left">294</td>
<td align="left">226</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.31678486997635935</td>
<td align="left">0.2409867172675522</td>
<td align="left">0.5635673624288425</td>
<td align="left">0.5578747628083491</td>
<td align="left">0.5342789598108747</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.007425656339430098</td>
<td align="left">0.013618296214920611</td>
<td align="left">-0.08064316388694692</td>
<td align="left">0.05155897333466497</td>
<td align="left">-0.1141420928207042</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: math score<br>&emsp;Média maior que a população: reading score<br>&emsp;Média maior que a população: writing score</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: math score<br>&emsp;Média menor que a população: reading score<br>&emsp;Média menor que a população: writing score<br>&emsp;Presença maior de população na feature test preparation course: none</p>
