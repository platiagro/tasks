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
<th align="left">Author</th>
<th align="left">Genre</th>
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
<td align="left">248</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Jeff Kinney</td>
<td align="left">Non Fiction</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">12</td>
<td align="left">310</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/6ffee5d2-af07-488e-8133-a095e57d32bc.png" alt="Visualização dos outliers: DBscan" /></p>

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
<td align="right">4.35</td>
<td align="right">32085.21</td>
<td align="right">33.43</td>
<td align="right">2014.14</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.44</td>
<td align="right">27605.06</td>
<td align="right">27.59</td>
<td align="right">3.06</td>
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
<td align="right">8104.75</td>
<td align="right">12.75</td>
<td align="right">2012.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">4.50</td>
<td align="right">25417.00</td>
<td align="right">20.00</td>
<td align="right">2014.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">4.72</td>
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
<th align="left">Author</th>
<th align="left">Genre</th>
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
<td align="left">19</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Gillian Flynn</td>
<td align="left">Fiction</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">3</td>
<td align="left">18</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/46547d71-6db8-4594-80d1-6a645794cb38.png" alt="Visualização dos outliers: Isolation Forest" /></p>

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
<td align="left">(4.7, 4.9]</td>
<td align="right">0.13</td>
<td align="right">0.15</td>
<td align="right">0.01</td>
<td align="right">0.06</td>
<td align="right">0.09</td>
<td align="right">0.09</td>
<td align="right">0.04</td>
<td align="right">0.17</td>
<td align="right">0.10</td>
<td align="right">0.17</td>
</tr>
<tr>
<td align="left">(3.899, 4.1]</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
<td align="right">0.56</td>
<td align="right">0.06</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(4.5, 4.7]</td>
<td align="right">0.07</td>
<td align="right">0.11</td>
<td align="right">0.01</td>
<td align="right">0.06</td>
<td align="right">0.15</td>
<td align="right">0.04</td>
<td align="right">0.03</td>
<td align="right">0.23</td>
<td align="right">0.09</td>
<td align="right">0.20</td>
</tr>
<tr>
<td align="left">(4.1, 4.3]</td>
<td align="right">0.03</td>
<td align="right">0.19</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.25</td>
<td align="right">0.22</td>
<td align="right">0.03</td>
<td align="right">0.22</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">(4.3, 4.5]</td>
<td align="right">0.03</td>
<td align="right">0.14</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
<td align="right">0.27</td>
<td align="right">0.05</td>
<td align="right">0.00</td>
<td align="right">0.20</td>
<td align="right">0.06</td>
<td align="right">0.17</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['User Rating', 'Reviews', 'Price', 'Year'] com uma quantidade de 8 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(4.7, 4.9]</td>
<td align="right">0.10</td>
<td align="right">0.16</td>
<td align="right">0.12</td>
<td align="right">0.23</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
<td align="right">0.13</td>
<td align="right">0.20</td>
</tr>
<tr>
<td align="left">(3.899, 4.1]</td>
<td align="right">0.25</td>
<td align="right">0.06</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
<td align="right">0.00</td>
<td align="right">0.62</td>
</tr>
<tr>
<td align="left">(4.5, 4.7]</td>
<td align="right">0.19</td>
<td align="right">0.14</td>
<td align="right">0.10</td>
<td align="right">0.22</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
<td align="right">0.09</td>
<td align="right">0.22</td>
</tr>
<tr>
<td align="left">(4.1, 4.3]</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.22</td>
<td align="right">0.19</td>
<td align="right">0.00</td>
<td align="right">0.03</td>
<td align="right">0.03</td>
<td align="right">0.28</td>
</tr>
<tr>
<td align="left">(4.3, 4.5]</td>
<td align="right">0.29</td>
<td align="right">0.13</td>
<td align="right">0.11</td>
<td align="right">0.18</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.05</td>
<td align="right">0.24</td>
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
<td align="right">0.58</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">User Rating - Reviews - Year</td>
<td align="right">0.57</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">User Rating - Reviews - Price</td>
<td align="right">0.55</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">User Rating - Reviews - Price - Year</td>
<td align="right">nan</td>
<td align="right">0.56</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">User Rating</td>
<td align="right">-0.07</td>
<td align="right">0.05</td>
<td align="right">-0.01</td>
<td align="right">0.03</td>
<td align="right">0.11</td>
<td align="right">0.04</td>
<td align="right">0.10</td>
<td align="right">-0.05</td>
<td align="right">-0.28</td>
</tr>
<tr>
<td align="left">Reviews</td>
<td align="right">-9034.23</td>
<td align="right">13014.61</td>
<td align="right">1514.13</td>
<td align="right">-2382.30</td>
<td align="right">39130.99</td>
<td align="right">20526.77</td>
<td align="right">7250.83</td>
<td align="right">-6120.10</td>
<td align="right">21211.81</td>
</tr>
<tr>
<td align="left">Price</td>
<td align="right">1.42</td>
<td align="right">-2.89</td>
<td align="right">-1.94</td>
<td align="right">1.65</td>
<td align="right">-1.01</td>
<td align="right">-0.07</td>
<td align="right">-1.18</td>
<td align="right">0.49</td>
<td align="right">21.42</td>
</tr>
<tr>
<td align="left">Year</td>
<td align="right">-2.42</td>
<td align="right">1.59</td>
<td align="right">0.80</td>
<td align="right">0.79</td>
<td align="right">0.41</td>
<td align="right">0.24</td>
<td align="right">1.16</td>
<td align="right">-0.57</td>
<td align="right">0.15</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">User Rating</td>
<td align="right">-0.37</td>
<td align="right">0.25</td>
<td align="right">-0.03</td>
<td align="right">0.16</td>
<td align="right">0.54</td>
<td align="right">0.19</td>
<td align="right">0.52</td>
<td align="right">-0.23</td>
<td align="right">-1.41</td>
</tr>
<tr>
<td align="left">Reviews</td>
<td align="right">-1.00</td>
<td align="right">1.43</td>
<td align="right">0.17</td>
<td align="right">-0.26</td>
<td align="right">4.31</td>
<td align="right">2.26</td>
<td align="right">0.80</td>
<td align="right">-0.67</td>
<td align="right">2.34</td>
</tr>
<tr>
<td align="left">Price</td>
<td align="right">0.18</td>
<td align="right">-0.37</td>
<td align="right">-0.25</td>
<td align="right">0.21</td>
<td align="right">-0.13</td>
<td align="right">-0.01</td>
<td align="right">-0.15</td>
<td align="right">0.06</td>
<td align="right">2.74</td>
</tr>
<tr>
<td align="left">Year</td>
<td align="right">-0.76</td>
<td align="right">0.50</td>
<td align="right">0.25</td>
<td align="right">0.25</td>
<td align="right">0.13</td>
<td align="right">0.08</td>
<td align="right">0.36</td>
<td align="right">-0.18</td>
<td align="right">0.05</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/222df2ba-98cf-4205-b8b7-689a1bdbfb60.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-bestsellerswithcategories/figures/f263a8e6-7f9d-4408-939d-8ccac80edf32.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Reviews e no grupo 4, com valor de 39130.99. A maior variação negativa foi na feature Reviews e no grupo 0, com o valor registrado de -9034.23</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Author</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">John Green</td>
<td align="left">Fiction</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">3</td>
<td align="left">5</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.6</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.592</td>
<td align="left">0.575</td>
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
<th align="left">Author</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Patrick Lencioni</td>
<td align="left">Non Fiction</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">5</td>
<td align="left">64</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.052</td>
<td align="left">0.593</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.043</td>
<td align="left">0.018</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Author</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Adam Gasiewski</td>
<td align="left">Non Fiction</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">1.0</td>
<td align="left">0.257</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">7</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Author</th>
<th align="left">Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Adam Gasiewski</td>
<td align="left">Fiction</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">1.0</td>
<td align="left">0.023</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: Reviews<br>&emsp;Média menor que a população: Year<br>&emsp;Presença maior de população na feature Genre: Non Fiction</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: Reviews<br>&emsp;Média maior que a população: Year<br>&emsp;Presença maior de população na feature Genre: Fiction</p>
<p>Grupo 2: <br>&emsp;Presença maior de população na feature Genre: Fiction</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: User Rating<br>&emsp;Média maior que a população: Reviews<br>&emsp;Presença maior de população na feature Author: John Green<br>&emsp;Presença maior de população na feature Genre: Fiction</p>
<p>Grupo 5: <br>&emsp;Média maior que a população: Reviews<br>&emsp;Presença maior de população na feature Author: Laura Hillenbrand<br>&emsp;Presença maior de população na feature Genre: Fiction</p>
<p>Grupo 6: <br>&emsp;Média maior que a população: User Rating<br>&emsp;Média maior que a população: Reviews<br>&emsp;Presença maior de população na feature Author: Eric Carle</p>
<p>Grupo 7: <br>&emsp;Média menor que a população: Reviews</p>
<p>Grupo outlier: <br>&emsp;Média menor que a população: User Rating<br>&emsp;Média maior que a população: Reviews<br>&emsp;Média maior que a população: Price</p>
