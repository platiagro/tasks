<h1>CPQD AutoML Algorithm: 4</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 200 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Age</th>
<th align="right">Annual Income (k$)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">200.00</td>
<td align="right">200.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">38.85</td>
<td align="right">60.56</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">13.97</td>
<td align="right">26.26</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">15.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">28.75</td>
<td align="right">41.50</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">36.00</td>
<td align="right">61.50</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">49.00</td>
<td align="right">78.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">70.00</td>
<td align="right">137.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">200</td>
<td align="left">200</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">5</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Female</td>
<td align="left">(40.2, 59.8]</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">112</td>
<td align="left">72</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:4/figures/a081f7dd-4cb5-4323-b709-17024e47015d.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 10 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Age</th>
<th align="right">Annual Income (k$)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">10.00</td>
<td align="right">10.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">49.10</td>
<td align="right">73.50</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">17.45</td>
<td align="right">53.94</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">19.00</td>
<td align="right">15.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">35.25</td>
<td align="right">19.25</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">52.50</td>
<td align="right">71.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">62.75</td>
<td align="right">124.50</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">70.00</td>
<td align="right">137.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">10</td>
<td align="left">10</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">4</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Male</td>
<td align="left">(0.902, 20.6]</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">7</td>
<td align="left">6</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:4/figures/d243e117-8831-4d51-8fd4-8076eeb9b099.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 2 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Age', 'Annual Income (k$)'] com uma quantidade de 3 grupos. A análise multidimensional em 2 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(79.4, 99.0]</td>
<td align="right">0.31</td>
<td align="right">0.69</td>
</tr>
<tr>
<td align="left">(0.902, 20.6]</td>
<td align="right">0.30</td>
<td align="right">0.70</td>
</tr>
<tr>
<td align="left">(20.6, 40.2]</td>
<td align="right">0.40</td>
<td align="right">0.60</td>
</tr>
<tr>
<td align="left">(59.8, 79.4]</td>
<td align="right">0.46</td>
<td align="right">0.54</td>
</tr>
<tr>
<td align="left">(40.2, 59.8]</td>
<td align="right">0.54</td>
<td align="right">0.46</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Age', 'Annual Income (k$)'] com uma quantidade de 3 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="left">(79.4, 99.0]</td>
<td align="right">0.31</td>
<td align="right">0.69</td>
</tr>
<tr>
<td align="left">(0.902, 20.6]</td>
<td align="right">0.30</td>
<td align="right">0.70</td>
</tr>
<tr>
<td align="left">(20.6, 40.2]</td>
<td align="right">0.40</td>
<td align="right">0.60</td>
</tr>
<tr>
<td align="left">(59.8, 79.4]</td>
<td align="right">0.46</td>
<td align="right">0.54</td>
</tr>
<tr>
<td align="left">(40.2, 59.8]</td>
<td align="right">0.54</td>
<td align="right">0.46</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Comparação dos Métodos</h3>
<p>Na tabela abaixo podemos observar a comparação de todos os métodos de clustering testados. O método com o maior score será considerado o melhor método, sendo este utilizado nas próximas análises.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Feature Permutation 2 dim.</th>
<th align="right">Multidimensional</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Age - Annual Income (k$)</td>
<td align="right">0.43</td>
<td align="right">0.43</td>
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
<td align="left">Age</td>
<td align="right">0.95</td>
<td align="right">-0.72</td>
<td align="right">10.79</td>
</tr>
<tr>
<td align="left">Annual Income (k$)</td>
<td align="right">-22.55</td>
<td align="right">17.12</td>
<td align="right">13.62</td>
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
<td align="left">Age</td>
<td align="right">0.07</td>
<td align="right">-0.05</td>
<td align="right">0.80</td>
</tr>
<tr>
<td align="left">Annual Income (k$)</td>
<td align="right">-0.94</td>
<td align="right">0.71</td>
<td align="right">0.57</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:4/figures/b152f3dc-3cd2-4bb9-aaf6-211240208d5d.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:4/figures/97fdaa1f-3182-48c1-808b-c1c10132c049.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Annual Income (k$) e no grupo 1, com valor de 17.12. A maior variação negativa foi na feature Annual Income (k$) e no grupo 0, com o valor registrado de -22.55</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Female</td>
<td align="left">(40.2, 59.8]</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">50</td>
<td align="left">38</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.6097560975609756</td>
<td align="left">0.4634146341463415</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.0360718870346598</td>
<td align="left">0.0897304236200257</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Female</td>
<td align="left">(40.2, 59.8]</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">59</td>
<td align="left">33</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.5462962962962963</td>
<td align="left">0.3055555555555556</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.027387914230019517</td>
<td align="left">-0.0681286549707602</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: Média menor que a população: Annual Income (k$)</p>
<p>Grupo 1: Média maior que a população: Annual Income (k$)</p>
<p>Grupo outlier: Média maior que a população: Age, Média maior que a população: Annual Income (k$)</p>
