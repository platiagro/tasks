<h1>CPQD AutoML Algorithm - bestsellers with categories</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 550 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">User Rating</th>
<th align="right">Reviews</th>
<th align="right">Price</th>
<th align="right">Year</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">550.00</td>
<td align="right">550.00</td>
<td align="right">550.00</td>
<td align="right">550.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">4.62</td>
<td align="right">11953.28</td>
<td align="right">13.10</td>
<td align="right">2014.00</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.23</td>
<td align="right">11731.13</td>
<td align="right">10.84</td>
<td align="right">3.17</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">3.30</td>
<td align="right">37.00</td>
<td align="right">0.00</td>
<td align="right">2009.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">4.50</td>
<td align="right">4058.00</td>
<td align="right">7.00</td>
<td align="right">2011.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">4.70</td>
<td align="right">8580.00</td>
<td align="right">11.00</td>
<td align="right">2014.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">4.80</td>
<td align="right">17253.25</td>
<td align="right">16.00</td>
<td align="right">2017.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">4.90</td>
<td align="right">87841.00</td>
<td align="right">105.00</td>
<td align="right">2019.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Author</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">550</td>
<td align="left">550</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">248</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Non Fiction</td>
<td align="left">Jeff Kinney</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">310</td>
<td align="left">12</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/56366220-792e-46cb-a15e-8b17fc392ed4.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 28 outliers neste dataset, correspondendo a uma proporção de 5.09% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">User Rating</th>
<th align="right">Reviews</th>
<th align="right">Price</th>
<th align="right">Year</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">28.00</td>
<td align="right">28.00</td>
<td align="right">28.00</td>
<td align="right">28.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">4.31</td>
<td align="right">29899.43</td>
<td align="right">34.04</td>
<td align="right">2013.71</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.43</td>
<td align="right">28257.21</td>
<td align="right">27.49</td>
<td align="right">3.13</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">3.30</td>
<td align="right">807.00</td>
<td align="right">7.00</td>
<td align="right">2009.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">4.00</td>
<td align="right">6476.00</td>
<td align="right">13.50</td>
<td align="right">2012.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">4.45</td>
<td align="right">14226.50</td>
<td align="right">20.00</td>
<td align="right">2014.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">4.70</td>
<td align="right">57271.00</td>
<td align="right">46.00</td>
<td align="right">2016.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">4.90</td>
<td align="right">87841.00</td>
<td align="right">105.00</td>
<td align="right">2019.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Author</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">28</td>
<td align="left">28</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">18</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Fiction</td>
<td align="left">Gillian Flynn</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">16</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/bf142abc-fc2b-4a22-8d58-7366924b35a6.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Reviews', 'Price', 'Year'] com uma quantidade de 10 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<th align="right">9</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(4.5, 4.7]</td>
<td align="right">0.23</td>
<td align="right">0.11</td>
<td align="right">0.02</td>
<td align="right">0.19</td>
<td align="right">0.15</td>
<td align="right">0.03</td>
<td align="right">0.04</td>
<td align="right">0.03</td>
<td align="right">0.12</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">(4.1, 4.3]</td>
<td align="right">0.22</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.09</td>
<td align="right">0.25</td>
<td align="right">0.03</td>
<td align="right">0.19</td>
<td align="right">0.00</td>
<td align="right">0.19</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(3.899, 4.1]</td>
<td align="right">0.53</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.27</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(4.3, 4.5]</td>
<td align="right">0.21</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.10</td>
<td align="right">0.26</td>
<td align="right">0.07</td>
<td align="right">0.05</td>
<td align="right">0.00</td>
<td align="right">0.22</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(4.7, 4.9]</td>
<td align="right">0.17</td>
<td align="right">0.10</td>
<td align="right">0.01</td>
<td align="right">0.17</td>
<td align="right">0.09</td>
<td align="right">0.10</td>
<td align="right">0.09</td>
<td align="right">0.00</td>
<td align="right">0.14</td>
<td align="right">0.13</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['User Rating', 'Reviews', 'Price', 'Year'] com uma quantidade de 7 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(4.5, 4.7]</td>
<td align="right">0.22</td>
<td align="right">0.08</td>
<td align="right">0.08</td>
<td align="right">0.24</td>
<td align="right">0.02</td>
<td align="right">0.23</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">(4.1, 4.3]</td>
<td align="right">0.28</td>
<td align="right">0.03</td>
<td align="right">0.19</td>
<td align="right">0.38</td>
<td align="right">0.00</td>
<td align="right">0.09</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(3.899, 4.1]</td>
<td align="right">0.60</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.27</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">(4.3, 4.5]</td>
<td align="right">0.18</td>
<td align="right">0.07</td>
<td align="right">0.08</td>
<td align="right">0.40</td>
<td align="right">0.00</td>
<td align="right">0.20</td>
<td align="right">0.08</td>
</tr>
<tr>
<td align="left">(4.7, 4.9]</td>
<td align="right">0.19</td>
<td align="right">0.10</td>
<td align="right">0.12</td>
<td align="right">0.17</td>
<td align="right">0.01</td>
<td align="right">0.22</td>
<td align="right">0.19</td>
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
<td align="left">Reviews - Price - Year</td>
<td align="right">0.57</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">User Rating - Reviews - Price</td>
<td align="right">0.57</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">User Rating - Reviews - Year</td>
<td align="right">0.56</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">User Rating - Reviews - Price - Year</td>
<td align="right">nan</td>
<td align="right">0.57</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">User Rating</td>
<td align="right">-0.05</td>
<td align="right">0.03</td>
<td align="right">0.03</td>
<td align="right">-0.06</td>
<td align="right">0.09</td>
<td align="right">0.03</td>
<td align="right">0.09</td>
<td align="right">-0.32</td>
</tr>
<tr>
<td align="left">Reviews</td>
<td align="right">-5180.74</td>
<td align="right">16891.35</td>
<td align="right">4313.43</td>
<td align="right">-8640.02</td>
<td align="right">37575.49</td>
<td align="right">-1313.67</td>
<td align="right">10520.23</td>
<td align="right">18908.78</td>
</tr>
<tr>
<td align="left">Price</td>
<td align="right">-0.69</td>
<td align="right">-1.62</td>
<td align="right">-1.45</td>
<td align="right">1.31</td>
<td align="right">-0.98</td>
<td align="right">2.16</td>
<td align="right">-2.72</td>
<td align="right">22.06</td>
</tr>
<tr>
<td align="left">Year</td>
<td align="right">0.29</td>
<td align="right">1.10</td>
<td align="right">1.47</td>
<td align="right">-2.20</td>
<td align="right">0.13</td>
<td align="right">0.48</td>
<td align="right">1.27</td>
<td align="right">-0.30</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">User Rating</td>
<td align="right">-0.25</td>
<td align="right">0.17</td>
<td align="right">0.13</td>
<td align="right">-0.29</td>
<td align="right">0.47</td>
<td align="right">0.17</td>
<td align="right">0.47</td>
<td align="right">-1.64</td>
</tr>
<tr>
<td align="left">Reviews</td>
<td align="right">-0.56</td>
<td align="right">1.83</td>
<td align="right">0.47</td>
<td align="right">-0.94</td>
<td align="right">4.07</td>
<td align="right">-0.14</td>
<td align="right">1.14</td>
<td align="right">2.05</td>
</tr>
<tr>
<td align="left">Price</td>
<td align="right">-0.09</td>
<td align="right">-0.21</td>
<td align="right">-0.19</td>
<td align="right">0.17</td>
<td align="right">-0.13</td>
<td align="right">0.28</td>
<td align="right">-0.35</td>
<td align="right">2.85</td>
</tr>
<tr>
<td align="left">Year</td>
<td align="right">0.09</td>
<td align="right">0.35</td>
<td align="right">0.47</td>
<td align="right">-0.69</td>
<td align="right">0.04</td>
<td align="right">0.15</td>
<td align="right">0.40</td>
<td align="right">-0.10</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/a72791b1-fdc5-4565-8fc7-2653b7cac5b2.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/34d7c6f3-6c7b-4e9e-9d5e-3e1ad6ca6eaf.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Reviews e no grupo 4, com valor de 37575.49. A maior variação negativa foi na feature Reviews e no grupo 3, com o valor registrado de -8640.02</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Author</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Fiction</td>
<td align="left">John Green</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">7</td>
<td align="left">4</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">1.0</td>
<td align="left">0.5714285714285714</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.5708812260536398</td>
<td align="left">0.5618500273672687</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">4</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Genre</th>
<th align="left">Author</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Non Fiction</td>
<td align="left">Gary Chapman</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">26</td>
<td align="left">6</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.5098039215686274</td>
<td align="left">0.045112781954887216</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.061077304485012474</td>
<td align="left">0.024039985020021314</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: Reviews</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: Reviews<br>&emsp;Presença maior de população na feature Author: Suzanne Collins</p>
<p>Grupo 3: <br>&emsp;Média menor que a população: Reviews<br>&emsp;Média menor que a população: Year<br>&emsp;Presença maior de população na feature Genre: Non Fiction</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: Reviews<br>&emsp;Presença maior de população na feature Genre: Fiction<br>&emsp;Presença maior de população na feature Author: John Green</p>
<p>Grupo 6: <br>&emsp;Média maior que a população: Reviews<br>&emsp;Presença maior de população na feature Genre: Fiction<br>&emsp;Presença maior de população na feature Author: Dr. Seuss</p>
<p>Grupo outlier: <br>&emsp;Média menor que a população: User Rating<br>&emsp;Média maior que a população: Reviews<br>&emsp;Média maior que a população: Price</p>
