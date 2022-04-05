<h1>CPQD AutoML Algorithm - Iris</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 8 outliers neste dataset, correspondendo a uma proporção de 5.33% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">sepal.length</th>
<th align="right">sepal.width</th>
<th align="right">petal.length</th>
<th align="right">petal.width</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">8.00</td>
<td align="right">8.00</td>
<td align="right">8.00</td>
<td align="right">8.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">6.25</td>
<td align="right">3.19</td>
<td align="right">4.19</td>
<td align="right">1.35</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">1.54</td>
<td align="right">0.84</td>
<td align="right">2.61</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">4.30</td>
<td align="right">2.00</td>
<td align="right">1.10</td>
<td align="right">0.10</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">4.88</td>
<td align="right">2.52</td>
<td align="right">1.45</td>
<td align="right">0.38</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">6.45</td>
<td align="right">3.30</td>
<td align="right">4.80</td>
<td align="right">1.50</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">7.70</td>
<td align="right">3.80</td>
<td align="right">6.48</td>
<td align="right">2.23</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">7.90</td>
<td align="right">4.40</td>
<td align="right">6.90</td>
<td align="right">2.50</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">variety</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">8</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Virginica</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Iris/figures/e6bd4b21-ec77-4033-950f-fd9a2e0a9d1d.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['sepal.width', 'petal.length', 'petal.width'] com uma quantidade de 3 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Setosa</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">Versicolor</td>
<td align="right">0.94</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">Virginica</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.93</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['sepal.length', 'sepal.width', 'petal.length', 'petal.width'] com uma quantidade de 3 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Setosa</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">Versicolor</td>
<td align="right">0.94</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">Virginica</td>
<td align="right">0.28</td>
<td align="right">0.00</td>
<td align="right">0.72</td>
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
<td align="left">sepal.width - petal.length - petal.width</td>
<td align="right">0.60</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">sepal.length - petal.length - petal.width</td>
<td align="right">0.57</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">sepal.length - sepal.width - petal.length</td>
<td align="right">0.55</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">sepal.length - sepal.width - petal.length - petal.width</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sepal.length</td>
<td align="right">0.08</td>
<td align="right">-0.80</td>
<td align="right">0.92</td>
<td align="right">0.43</td>
</tr>
<tr>
<td align="left">sepal.width</td>
<td align="right">-0.30</td>
<td align="right">0.39</td>
<td align="right">-0.02</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">petal.length</td>
<td align="right">0.66</td>
<td align="right">-2.26</td>
<td align="right">1.87</td>
<td align="right">0.45</td>
</tr>
<tr>
<td align="left">petal.width</td>
<td align="right">0.23</td>
<td align="right">-0.95</td>
<td align="right">0.85</td>
<td align="right">0.16</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sepal.length</td>
<td align="right">0.10</td>
<td align="right">-1.04</td>
<td align="right">1.19</td>
<td align="right">0.56</td>
</tr>
<tr>
<td align="left">sepal.width</td>
<td align="right">-0.74</td>
<td align="right">0.97</td>
<td align="right">-0.05</td>
<td align="right">0.34</td>
</tr>
<tr>
<td align="left">petal.length</td>
<td align="right">0.38</td>
<td align="right">-1.32</td>
<td align="right">1.10</td>
<td align="right">0.27</td>
</tr>
<tr>
<td align="left">petal.width</td>
<td align="right">0.31</td>
<td align="right">-1.27</td>
<td align="right">1.14</td>
<td align="right">0.21</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Iris/figures/c1386584-827d-4b25-a039-cd6994f0cc4e.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Iris/figures/d4d482cc-ecdd-4449-8b42-357628465756.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature petal.length e no grupo 2, com valor de 1.87. A maior variação negativa foi na feature petal.length e no grupo 1, com o valor registrado de -2.26</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">variety</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Setosa</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">47</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.669</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">variety</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Versicolor</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">46</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.78</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.435</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">variety</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Setosa</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">variety</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Virginica</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.717</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: sepal.width<br>&emsp;Presença maior de população na feature variety: Versicolor</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: sepal.length<br>&emsp;Média maior que a população: sepal.width<br>&emsp;Média menor que a população: petal.length<br>&emsp;Média menor que a população: petal.width<br>&emsp;Presença maior de população na feature variety: Setosa</p>
<p>Grupo 2: <br>&emsp;Média maior que a população: sepal.length<br>&emsp;Média maior que a população: petal.length<br>&emsp;Média maior que a população: petal.width<br>&emsp;Presença maior de população na feature variety: Virginica</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: sepal.length</p>
