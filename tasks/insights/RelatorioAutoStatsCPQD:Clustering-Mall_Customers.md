<h1>Relatorio AutoStats CPQD: Clustering - Mall_Customers</h1>
<h2>Análise Geral</h2>
<p>Uma análise geral pode gerar insighs interessantes, no ponto de vista de dados gerais do banco fornecido. Nas tabelas a seguir serão apresentados dados como média, frequencia, maior valor, etc.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Age</th>
<th align="right">Annual Income (k$)</th>
<th align="right">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">200.00</td>
<td align="right">200.00</td>
<td align="right">200.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">38.85</td>
<td align="right">60.56</td>
<td align="right">50.20</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">13.97</td>
<td align="right">26.26</td>
<td align="right">25.82</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">15.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">28.75</td>
<td align="right">41.50</td>
<td align="right">34.75</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">36.00</td>
<td align="right">61.50</td>
<td align="right">50.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">49.00</td>
<td align="right">78.00</td>
<td align="right">73.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">70.00</td>
<td align="right">137.00</td>
<td align="right">99.00</td>
</tr>
</tbody>
</table><p><em>Tabela de descrição geral dos dados fornecidos.</em></p>
<p>A análise por agrupamento pode trazer insights interessantes por considerar uma variável alvo como um ponto em comum dos dados. Assim possibilitando a comparação de quais features mais caracterizam cada um dos grupos alvo.</p>
<table>
<thead>
<tr>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="right">Annual Income (k$)</th>
<th align="right">Spending Score (1-100)</th>
<th align="right">Age</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(0.902, 20.6]</td>
<td align="right">66.11</td>
<td align="right">10.92</td>
<td align="right">43.50</td>
</tr>
<tr>
<td align="left">(20.6, 40.2]</td>
<td align="right">61.41</td>
<td align="right">32.44</td>
<td align="right">40.26</td>
</tr>
<tr>
<td align="left">(40.2, 59.8]</td>
<td align="right">54.88</td>
<td align="right">49.74</td>
<td align="right">43.46</td>
</tr>
<tr>
<td align="left">(59.8, 79.4]</td>
<td align="right">58.60</td>
<td align="right">71.34</td>
<td align="right">30.57</td>
</tr>
<tr>
<td align="left">(79.4, 99.0]</td>
<td align="right">69.07</td>
<td align="right">89.77</td>
<td align="right">30.60</td>
</tr>
</tbody>
</table><p><em>Tabela de agrupamento geral dos dados numéricos, por média.</em></p>
<table>
<thead>
<tr>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="right">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(0.902, 20.6]</td>
<td align="right">0.18</td>
</tr>
<tr>
<td align="left">(20.6, 40.2]</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">(40.2, 59.8]</td>
<td align="right">0.36</td>
</tr>
<tr>
<td align="left">(59.8, 79.4]</td>
<td align="right">0.17</td>
</tr>
<tr>
<td align="left">(79.4, 99.0]</td>
<td align="right">0.15</td>
</tr>
</tbody>
</table><p><em>Tabela de agrupamento geral dos dados categóricos, por moda.</em></p>
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
<th align="right">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">200.00</td>
<td align="right">200.00</td>
<td align="right">200.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">38.85</td>
<td align="right">60.56</td>
<td align="right">50.20</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">13.97</td>
<td align="right">26.26</td>
<td align="right">25.82</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">15.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">28.75</td>
<td align="right">41.50</td>
<td align="right">34.75</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">36.00</td>
<td align="right">61.50</td>
<td align="right">50.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">49.00</td>
<td align="right">78.00</td>
<td align="right">73.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">70.00</td>
<td align="right">137.00</td>
<td align="right">99.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="left">Genre</th>
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
<td align="left">5</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">(40.2, 59.8]</td>
<td align="left">Female</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">72</td>
<td align="left">112</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-Mall_Customers/figures/aed742e6-f98f-49fc-8043-6a5ae66e1834.png" alt="Visualização dos outliers: DBscan" /></p>

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
<th align="right">Spending Score (1-100)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">10.00</td>
<td align="right">10.00</td>
<td align="right">10.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">40.60</td>
<td align="right">75.60</td>
<td align="right">41.30</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">17.77</td>
<td align="right">55.65</td>
<td align="right">38.61</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">16.00</td>
<td align="right">3.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">30.50</td>
<td align="right">21.75</td>
<td align="right">8.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">35.00</td>
<td align="right">73.00</td>
<td align="right">23.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">56.25</td>
<td align="right">126.00</td>
<td align="right">80.75</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">67.00</td>
<td align="right">137.00</td>
<td align="right">92.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="left">Genre</th>
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
<td align="left">4</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">(0.902, 20.6]</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">5</td>
<td align="left">7</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-Mall_Customers/figures/72354e54-8b38-4c86-af6b-10ba1766bb30.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'] com uma quantidade de 2 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(0.902, 20.6]</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">(79.4, 99.0]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(59.8, 79.4]</td>
<td align="right">0.97</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(20.6, 40.2]</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">(40.2, 59.8]</td>
<td align="right">0.29</td>
<td align="right">0.71</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'] com uma quantidade de 2 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="left">(0.902, 20.6]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(79.4, 99.0]</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">(59.8, 79.4]</td>
<td align="right">0.03</td>
<td align="right">0.97</td>
</tr>
<tr>
<td align="left">(20.6, 40.2]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(40.2, 59.8]</td>
<td align="right">0.71</td>
<td align="right">0.29</td>
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
<td align="left">Age - Annual Income (k$) - Spending Score (1-100)</td>
<td align="right">0.30</td>
<td align="right">0.30</td>
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
<td align="right">7.31</td>
<td align="right">-9.83</td>
<td align="right">1.84</td>
</tr>
<tr>
<td align="left">Annual Income (k$)</td>
<td align="right">-0.32</td>
<td align="right">0.43</td>
<td align="right">15.83</td>
</tr>
<tr>
<td align="left">Spending Score (1-100)</td>
<td align="right">-16.64</td>
<td align="right">22.39</td>
<td align="right">-9.37</td>
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
<td align="right">0.53</td>
<td align="right">-0.71</td>
<td align="right">0.13</td>
</tr>
<tr>
<td align="left">Annual Income (k$)</td>
<td align="right">-0.01</td>
<td align="right">0.02</td>
<td align="right">0.67</td>
</tr>
<tr>
<td align="left">Spending Score (1-100)</td>
<td align="right">-0.67</td>
<td align="right">0.90</td>
<td align="right">-0.38</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-Mall_Customers/figures/af32cc28-04a3-4a1f-a646-226050226ff9.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-Mall_Customers/figures/58b00f9e-bbf9-43e1-9af3-96ef467a5c4d.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Spending Score (1-100) e no grupo 1, com valor de 22.39. A maior variação negativa foi na feature Spending Score (1-100) e no grupo 0, com o valor registrado de -16.64</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">(59.8, 79.4]</td>
<td align="left">Female</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">33</td>
<td align="left">63</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.407</td>
<td align="left">0.578</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.228</td>
<td align="left">0.004</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">(40.2, 59.8]</td>
<td align="left">Female</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">51</td>
<td align="left">46</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.468</td>
<td align="left">0.568</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.089</td>
<td align="left">-0.006</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">(0.902, 20.6]</td>
<td align="left">Female</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">1.0</td>
<td align="left">0.578</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Spending Score (1-100) categorizado</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">(0.902, 20.6]</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">1.0</td>
<td align="left">0.432</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: Age<br>&emsp;Média menor que a população: Spending Score (1-100)</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: Age<br>&emsp;Média maior que a população: Spending Score (1-100)<br>&emsp;Presença maior de população na feature Spending Score (1-100) categorizado: (59.8, 79.4]</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: Annual Income (k$)</p>
