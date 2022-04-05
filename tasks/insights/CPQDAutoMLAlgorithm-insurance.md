<h1>CPQD AutoML Algorithm - insurance</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 1338 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">age</th>
<th align="right">bmi</th>
<th align="right">children</th>
<th align="right">charges</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">39.21</td>
<td align="right">30.66</td>
<td align="right">1.09</td>
<td align="right">13270.42</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">14.05</td>
<td align="right">6.10</td>
<td align="right">1.21</td>
<td align="right">12110.01</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">15.96</td>
<td align="right">0.00</td>
<td align="right">1121.87</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">27.00</td>
<td align="right">26.30</td>
<td align="right">0.00</td>
<td align="right">4740.29</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">39.00</td>
<td align="right">30.40</td>
<td align="right">1.00</td>
<td align="right">9382.03</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">51.00</td>
<td align="right">34.69</td>
<td align="right">2.00</td>
<td align="right">16639.91</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">64.00</td>
<td align="right">53.13</td>
<td align="right">5.00</td>
<td align="right">63770.43</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">smoker</th>
<th align="left">region</th>
<th align="left">sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">1338</td>
<td align="left">1338</td>
<td align="left">1338</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">no</td>
<td align="left">southeast</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">1064</td>
<td align="left">364</td>
<td align="left">676</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-insurance/figures/dfe99269-1a26-4d83-b3b1-51ebc04f4cb9.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 67 outliers neste dataset, correspondendo a uma proporção de 5.01% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">age</th>
<th align="right">bmi</th>
<th align="right">children</th>
<th align="right">charges</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">67.00</td>
<td align="right">67.00</td>
<td align="right">67.00</td>
<td align="right">67.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">40.52</td>
<td align="right">36.45</td>
<td align="right">2.39</td>
<td align="right">32283.06</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">15.88</td>
<td align="right">8.55</td>
<td align="right">1.87</td>
<td align="right">18808.02</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">17.29</td>
<td align="right">0.00</td>
<td align="right">1163.46</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">25.50</td>
<td align="right">30.95</td>
<td align="right">1.00</td>
<td align="right">11207.49</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">39.00</td>
<td align="right">37.00</td>
<td align="right">2.00</td>
<td align="right">39611.76</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">55.50</td>
<td align="right">42.30</td>
<td align="right">4.00</td>
<td align="right">47280.45</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">64.00</td>
<td align="right">53.13</td>
<td align="right">5.00</td>
<td align="right">63770.43</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">smoker</th>
<th align="left">region</th>
<th align="left">sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">67</td>
<td align="left">67</td>
<td align="left">67</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">yes</td>
<td align="left">southeast</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">43</td>
<td align="left">33</td>
<td align="left">42</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-insurance/figures/b2f91f44-a17a-4c29-a13a-05594fd22f0e.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['age', 'children', 'charges'] com uma quantidade de 9 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
<th align="right">3</th>
<th align="right">4</th>
<th align="right">5</th>
<th align="right">6</th>
<th align="right">7</th>
<th align="right">8</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(21150.948, 31165.485]</td>
<td align="right">0.00</td>
<td align="right">0.74</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.26</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(11136.411, 21150.948]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.43</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.32</td>
</tr>
<tr>
<td align="left">(31165.485, 41180.022]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.19</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.81</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(1071.801, 11136.411]</td>
<td align="right">0.33</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.29</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.26</td>
<td align="right">0.13</td>
</tr>
<tr>
<td align="left">(41180.022, 51194.559]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['age', 'bmi', 'children', 'charges'] com uma quantidade de 9 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
<th align="right">3</th>
<th align="right">4</th>
<th align="right">5</th>
<th align="right">6</th>
<th align="right">7</th>
<th align="right">8</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(21150.948, 31165.485]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.36</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.64</td>
</tr>
<tr>
<td align="left">(11136.411, 21150.948]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.32</td>
<td align="right">0.19</td>
<td align="right">0.00</td>
<td align="right">0.49</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(31165.485, 41180.022]</td>
<td align="right">0.00</td>
<td align="right">0.91</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.08</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">(1071.801, 11136.411]</td>
<td align="right">0.30</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.28</td>
<td align="right">0.09</td>
<td align="right">0.00</td>
<td align="right">0.33</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(41180.022, 51194.559]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
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
<td align="left">age - children - charges</td>
<td align="right">0.56</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">age - bmi - charges</td>
<td align="right">0.56</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">bmi - children - charges</td>
<td align="right">0.55</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">age - bmi - children - charges</td>
<td align="right">nan</td>
<td align="right">0.55</td>
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
<th align="right">2</th>
<th align="right">3</th>
<th align="right">4</th>
<th align="right">5</th>
<th align="right">6</th>
<th align="right">7</th>
<th align="right">8</th>
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">age</td>
<td align="right">-5.57</td>
<td align="right">-8.25</td>
<td align="right">5.45</td>
<td align="right">-2.14</td>
<td align="right">6.46</td>
<td align="right">15.22</td>
<td align="right">9.79</td>
<td align="right">-17.11</td>
<td align="right">12.04</td>
<td align="right">1.38</td>
</tr>
<tr>
<td align="left">bmi</td>
<td align="right">0.00</td>
<td align="right">2.65</td>
<td align="right">-1.26</td>
<td align="right">-2.58</td>
<td align="right">0.22</td>
<td align="right">0.84</td>
<td align="right">4.87</td>
<td align="right">-0.73</td>
<td align="right">-1.45</td>
<td align="right">6.09</td>
</tr>
<tr>
<td align="left">children</td>
<td align="right">0.41</td>
<td align="right">-0.11</td>
<td align="right">-0.03</td>
<td align="right">0.13</td>
<td align="right">0.27</td>
<td align="right">-0.04</td>
<td align="right">0.13</td>
<td align="right">-0.66</td>
<td align="right">0.21</td>
<td align="right">1.36</td>
</tr>
<tr>
<td align="left">charges</td>
<td align="right">-7029.65</td>
<td align="right">24392.33</td>
<td align="right">3026.51</td>
<td align="right">8304.83</td>
<td align="right">-3874.74</td>
<td align="right">-549.95</td>
<td align="right">31675.64</td>
<td align="right">-9887.37</td>
<td align="right">14466.30</td>
<td align="right">20014.88</td>
</tr>
</tbody>
</table><p><em>Diferença de Média entre População - Grupos</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
<th align="right">3</th>
<th align="right">4</th>
<th align="right">5</th>
<th align="right">6</th>
<th align="right">7</th>
<th align="right">8</th>
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">age</td>
<td align="right">-0.40</td>
<td align="right">-0.59</td>
<td align="right">0.39</td>
<td align="right">-0.15</td>
<td align="right">0.46</td>
<td align="right">1.09</td>
<td align="right">0.70</td>
<td align="right">-1.23</td>
<td align="right">0.86</td>
<td align="right">0.10</td>
</tr>
<tr>
<td align="left">bmi</td>
<td align="right">0.00</td>
<td align="right">0.46</td>
<td align="right">-0.22</td>
<td align="right">-0.45</td>
<td align="right">0.04</td>
<td align="right">0.15</td>
<td align="right">0.84</td>
<td align="right">-0.13</td>
<td align="right">-0.25</td>
<td align="right">1.05</td>
</tr>
<tr>
<td align="left">children</td>
<td align="right">0.36</td>
<td align="right">-0.10</td>
<td align="right">-0.02</td>
<td align="right">0.11</td>
<td align="right">0.24</td>
<td align="right">-0.03</td>
<td align="right">0.12</td>
<td align="right">-0.59</td>
<td align="right">0.19</td>
<td align="right">1.22</td>
</tr>
<tr>
<td align="left">charges</td>
<td align="right">-0.65</td>
<td align="right">2.27</td>
<td align="right">0.28</td>
<td align="right">0.77</td>
<td align="right">-0.36</td>
<td align="right">-0.05</td>
<td align="right">2.94</td>
<td align="right">-0.92</td>
<td align="right">1.34</td>
<td align="right">1.86</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-insurance/figures/e5e38caa-003f-49ce-8b68-d7f1c5bc44c0.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-insurance/figures/b0add6c6-d61e-46b8-9597-c052791a50c9.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature charges e no grupo 6, com valor de 31675.64. A maior variação negativa foi na feature charges e no grupo 7, com o valor registrado de -9887.37</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">smoker</th>
<th align="left">region</th>
<th align="left">sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">yes</td>
<td align="left">southeast</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">44</td>
<td align="left">19</td>
<td align="left">48</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">1.0</td>
<td align="left">0.432</td>
<td align="left">0.686</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.818</td>
<td align="left">0.171</td>
<td align="left">0.187</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">smoker</th>
<th align="left">region</th>
<th align="left">sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">no</td>
<td align="left">southwest</td>
<td align="left">female</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">33</td>
<td align="left">59</td>
<td align="left">118</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.524</td>
<td align="left">0.273</td>
<td align="left">0.511</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.294</td>
<td align="left">0.03</td>
<td align="left">0.01</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">8</td>
<td align="left">4</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">smoker</th>
<th align="left">region</th>
<th align="left">sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">yes</td>
<td align="left">southeast</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.286</td>
<td align="left">0.221</td>
<td align="left">0.205</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">7</td>
<td align="left">7</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">smoker</th>
<th align="left">region</th>
<th align="left">sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">yes</td>
<td align="left">southeast</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.13</td>
<td align="left">0.057</td>
<td align="left">0.039</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">8</td>
<td align="left">6</td>
<td align="left">6</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: charges<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: age<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature smoker: yes<br>&emsp;Presença maior de população na feature sex: male</p>
<p>Grupo 2: <br>&emsp;Presença maior de população na feature region: northeast<br>&emsp;Presença maior de população na feature sex: female</p>
<p>Grupo 3: <br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature smoker: yes</p>
<p>Grupo 4: <br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 5: <br>&emsp;Média maior que a população: age<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 6: <br>&emsp;Média maior que a população: age<br>&emsp;Média maior que a população: bmi<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature smoker: yes<br>&emsp;Presença maior de população na feature region: southeast</p>
<p>Grupo 7: <br>&emsp;Média menor que a população: age<br>&emsp;Média menor que a população: children<br>&emsp;Média menor que a população: charges<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 8: <br>&emsp;Média maior que a população: age<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature region: northwest</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: bmi<br>&emsp;Média maior que a população: children<br>&emsp;Média maior que a população: charges</p>
