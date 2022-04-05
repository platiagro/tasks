<h1>CPQD AutoML Algorithm - winequality-white</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 4888 outliers neste dataset, correspondendo a uma proporção de 99.80% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">fixed acidity</th>
<th align="right">volatile acidity</th>
<th align="right">citric acid</th>
<th align="right">residual sugar</th>
<th align="right">chlorides</th>
<th align="right">free sulfur dioxide</th>
<th align="right">total sulfur dioxide</th>
<th align="right">density</th>
<th align="right">pH</th>
<th align="right">sulphates</th>
<th align="right">alcohol</th>
<th align="right">quality</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
<td align="right">4888.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">6.86</td>
<td align="right">0.28</td>
<td align="right">0.33</td>
<td align="right">6.40</td>
<td align="right">0.05</td>
<td align="right">35.33</td>
<td align="right">138.42</td>
<td align="right">0.99</td>
<td align="right">3.19</td>
<td align="right">0.49</td>
<td align="right">10.51</td>
<td align="right">5.88</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.84</td>
<td align="right">0.10</td>
<td align="right">0.12</td>
<td align="right">5.07</td>
<td align="right">0.02</td>
<td align="right">17.02</td>
<td align="right">42.52</td>
<td align="right">0.00</td>
<td align="right">0.15</td>
<td align="right">0.11</td>
<td align="right">1.23</td>
<td align="right">0.89</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">3.80</td>
<td align="right">0.08</td>
<td align="right">0.00</td>
<td align="right">0.60</td>
<td align="right">0.01</td>
<td align="right">2.00</td>
<td align="right">9.00</td>
<td align="right">0.99</td>
<td align="right">2.72</td>
<td align="right">0.22</td>
<td align="right">8.00</td>
<td align="right">3.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">6.30</td>
<td align="right">0.21</td>
<td align="right">0.27</td>
<td align="right">1.70</td>
<td align="right">0.04</td>
<td align="right">23.00</td>
<td align="right">108.00</td>
<td align="right">0.99</td>
<td align="right">3.09</td>
<td align="right">0.41</td>
<td align="right">9.50</td>
<td align="right">5.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">6.80</td>
<td align="right">0.26</td>
<td align="right">0.32</td>
<td align="right">5.20</td>
<td align="right">0.04</td>
<td align="right">34.00</td>
<td align="right">134.00</td>
<td align="right">0.99</td>
<td align="right">3.18</td>
<td align="right">0.47</td>
<td align="right">10.40</td>
<td align="right">6.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">7.30</td>
<td align="right">0.32</td>
<td align="right">0.39</td>
<td align="right">9.90</td>
<td align="right">0.05</td>
<td align="right">46.00</td>
<td align="right">167.00</td>
<td align="right">1.00</td>
<td align="right">3.28</td>
<td align="right">0.55</td>
<td align="right">11.40</td>
<td align="right">6.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">14.20</td>
<td align="right">1.10</td>
<td align="right">1.66</td>
<td align="right">65.80</td>
<td align="right">0.35</td>
<td align="right">289.00</td>
<td align="right">440.00</td>
<td align="right">1.04</td>
<td align="right">3.82</td>
<td align="right">1.08</td>
<td align="right">14.20</td>
<td align="right">9.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="right"></th>
<th align="right">0</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">0.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-winequality-white/figures/4e51b171-af18-4b1a-ac3d-939719e37931.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 245 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">fixed acidity</th>
<th align="right">volatile acidity</th>
<th align="right">citric acid</th>
<th align="right">residual sugar</th>
<th align="right">chlorides</th>
<th align="right">free sulfur dioxide</th>
<th align="right">total sulfur dioxide</th>
<th align="right">density</th>
<th align="right">pH</th>
<th align="right">sulphates</th>
<th align="right">alcohol</th>
<th align="right">quality</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
<td align="right">245.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">6.97</td>
<td align="right">0.39</td>
<td align="right">0.39</td>
<td align="right">6.40</td>
<td align="right">0.07</td>
<td align="right">37.59</td>
<td align="right">141.93</td>
<td align="right">0.99</td>
<td align="right">3.19</td>
<td align="right">0.54</td>
<td align="right">10.76</td>
<td align="right">5.64</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">1.53</td>
<td align="right">0.19</td>
<td align="right">0.23</td>
<td align="right">6.95</td>
<td align="right">0.06</td>
<td align="right">30.81</td>
<td align="right">65.82</td>
<td align="right">0.00</td>
<td align="right">0.22</td>
<td align="right">0.19</td>
<td align="right">1.71</td>
<td align="right">1.48</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">3.80</td>
<td align="right">0.11</td>
<td align="right">0.00</td>
<td align="right">0.80</td>
<td align="right">0.01</td>
<td align="right">3.00</td>
<td align="right">9.00</td>
<td align="right">0.99</td>
<td align="right">2.72</td>
<td align="right">0.25</td>
<td align="right">8.00</td>
<td align="right">3.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">5.80</td>
<td align="right">0.24</td>
<td align="right">0.23</td>
<td align="right">1.50</td>
<td align="right">0.03</td>
<td align="right">17.00</td>
<td align="right">97.00</td>
<td align="right">0.99</td>
<td align="right">3.00</td>
<td align="right">0.39</td>
<td align="right">9.30</td>
<td align="right">5.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">6.70</td>
<td align="right">0.36</td>
<td align="right">0.37</td>
<td align="right">3.20</td>
<td align="right">0.04</td>
<td align="right">32.00</td>
<td align="right">135.00</td>
<td align="right">0.99</td>
<td align="right">3.16</td>
<td align="right">0.50</td>
<td align="right">10.10</td>
<td align="right">5.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">8.00</td>
<td align="right">0.50</td>
<td align="right">0.50</td>
<td align="right">10.00</td>
<td align="right">0.06</td>
<td align="right">52.00</td>
<td align="right">184.00</td>
<td align="right">1.00</td>
<td align="right">3.36</td>
<td align="right">0.67</td>
<td align="right">12.40</td>
<td align="right">7.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">11.80</td>
<td align="right">1.10</td>
<td align="right">1.23</td>
<td align="right">65.80</td>
<td align="right">0.35</td>
<td align="right">289.00</td>
<td align="right">440.00</td>
<td align="right">1.04</td>
<td align="right">3.79</td>
<td align="right">1.00</td>
<td align="right">14.05</td>
<td align="right">9.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="right"></th>
<th align="right">0</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">0.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-winequality-white/figures/e3aba7ac-d828-431c-9dbb-b338c03753de.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['fixed acidity', 'chlorides', 'free sulfur dioxide'] com uma quantidade de 10 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(5.4, 6.6]</td>
<td align="right">0.02</td>
<td align="right">0.12</td>
<td align="right">0.12</td>
<td align="right">0.18</td>
<td align="right">0.10</td>
<td align="right">0.18</td>
<td align="right">0.05</td>
<td align="right">0.00</td>
<td align="right">0.17</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">(6.6, 7.8]</td>
<td align="right">0.01</td>
<td align="right">0.13</td>
<td align="right">0.11</td>
<td align="right">0.24</td>
<td align="right">0.05</td>
<td align="right">0.24</td>
<td align="right">0.03</td>
<td align="right">0.00</td>
<td align="right">0.17</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(2.994, 4.2]</td>
<td align="right">0.02</td>
<td align="right">0.04</td>
<td align="right">0.15</td>
<td align="right">0.13</td>
<td align="right">0.02</td>
<td align="right">0.08</td>
<td align="right">0.37</td>
<td align="right">0.01</td>
<td align="right">0.14</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(4.2, 5.4]</td>
<td align="right">0.02</td>
<td align="right">0.14</td>
<td align="right">0.11</td>
<td align="right">0.13</td>
<td align="right">0.12</td>
<td align="right">0.14</td>
<td align="right">0.11</td>
<td align="right">0.00</td>
<td align="right">0.14</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">(7.8, 9.0]</td>
<td align="right">0.01</td>
<td align="right">0.16</td>
<td align="right">0.11</td>
<td align="right">0.26</td>
<td align="right">0.08</td>
<td align="right">0.22</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
<td align="right">0.11</td>
<td align="right">0.02</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality'] com uma quantidade de 9 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="left">(5.4, 6.6]</td>
<td align="right">0.06</td>
<td align="right">0.09</td>
<td align="right">0.13</td>
<td align="right">0.12</td>
<td align="right">0.18</td>
<td align="right">0.06</td>
<td align="right">0.08</td>
<td align="right">0.13</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">(6.6, 7.8]</td>
<td align="right">0.07</td>
<td align="right">0.04</td>
<td align="right">0.15</td>
<td align="right">0.08</td>
<td align="right">0.24</td>
<td align="right">0.01</td>
<td align="right">0.06</td>
<td align="right">0.13</td>
<td align="right">0.21</td>
</tr>
<tr>
<td align="left">(2.994, 4.2]</td>
<td align="right">0.18</td>
<td align="right">0.12</td>
<td align="right">0.08</td>
<td align="right">0.03</td>
<td align="right">0.17</td>
<td align="right">0.02</td>
<td align="right">0.16</td>
<td align="right">0.23</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">(4.2, 5.4]</td>
<td align="right">0.06</td>
<td align="right">0.16</td>
<td align="right">0.15</td>
<td align="right">0.12</td>
<td align="right">0.09</td>
<td align="right">0.09</td>
<td align="right">0.12</td>
<td align="right">0.14</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">(7.8, 9.0]</td>
<td align="right">0.05</td>
<td align="right">0.04</td>
<td align="right">0.09</td>
<td align="right">0.12</td>
<td align="right">0.23</td>
<td align="right">0.04</td>
<td align="right">0.06</td>
<td align="right">0.14</td>
<td align="right">0.23</td>
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
<td align="left">fixed acidity - chlorides - free sulfur dioxide</td>
<td align="right">0.49</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">residual sugar - total sulfur dioxide - sulphates</td>
<td align="right">0.41</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">residual sugar - density - alcohol</td>
<td align="right">0.40</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">fixed acidity - volatile acidity - citric acid - residual sugar - chlorides - free sulfur dioxide - total sulfur dioxide - density - pH - sulphates - alcohol - quality</td>
<td align="right">nan</td>
<td align="right">0.31</td>
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
<td align="left">fixed acidity</td>
<td align="right">-0.02</td>
<td align="right">0.06</td>
<td align="right">0.05</td>
<td align="right">-0.06</td>
<td align="right">-0.08</td>
<td align="right">0.11</td>
<td align="right">0.19</td>
<td align="right">0.02</td>
<td align="right">-0.14</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">volatile acidity</td>
<td align="right">-0.00</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.01</td>
<td align="right">0.02</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
<td align="right">-0.02</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">citric acid</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">-0.00</td>
<td align="right">0.02</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.00</td>
<td align="right">-0.01</td>
<td align="right">-0.00</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">residual sugar</td>
<td align="right">-3.19</td>
<td align="right">3.17</td>
<td align="right">0.29</td>
<td align="right">1.97</td>
<td align="right">-2.45</td>
<td align="right">3.37</td>
<td align="right">1.23</td>
<td align="right">-1.75</td>
<td align="right">-0.24</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">chlorides</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">-0.00</td>
<td align="right">-0.00</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">free sulfur dioxide</td>
<td align="right">-20.09</td>
<td align="right">19.63</td>
<td align="right">-4.06</td>
<td align="right">19.02</td>
<td align="right">-9.54</td>
<td align="right">17.62</td>
<td align="right">-4.15</td>
<td align="right">-14.07</td>
<td align="right">5.01</td>
<td align="right">2.40</td>
</tr>
<tr>
<td align="left">total sulfur dioxide</td>
<td align="right">-70.68</td>
<td align="right">51.46</td>
<td align="right">7.44</td>
<td align="right">17.39</td>
<td align="right">-42.77</td>
<td align="right">85.98</td>
<td align="right">36.90</td>
<td align="right">-18.37</td>
<td align="right">-17.14</td>
<td align="right">3.76</td>
</tr>
<tr>
<td align="left">density</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">pH</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">-0.01</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">-0.00</td>
</tr>
<tr>
<td align="left">sulphates</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">-0.00</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">0.03</td>
<td align="right">0.02</td>
<td align="right">-0.00</td>
<td align="right">-0.01</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="left">alcohol</td>
<td align="right">0.69</td>
<td align="right">-0.85</td>
<td align="right">-0.10</td>
<td align="right">-0.41</td>
<td align="right">0.71</td>
<td align="right">-0.95</td>
<td align="right">-0.48</td>
<td align="right">0.24</td>
<td align="right">0.37</td>
<td align="right">0.26</td>
</tr>
<tr>
<td align="left">quality</td>
<td align="right">-0.10</td>
<td align="right">-0.33</td>
<td align="right">-0.00</td>
<td align="right">-0.02</td>
<td align="right">0.23</td>
<td align="right">-0.27</td>
<td align="right">-0.22</td>
<td align="right">-0.06</td>
<td align="right">0.37</td>
<td align="right">-0.25</td>
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
<td align="left">fixed acidity</td>
<td align="right">-0.03</td>
<td align="right">0.08</td>
<td align="right">0.06</td>
<td align="right">-0.07</td>
<td align="right">-0.10</td>
<td align="right">0.14</td>
<td align="right">0.24</td>
<td align="right">0.02</td>
<td align="right">-0.17</td>
<td align="right">0.16</td>
</tr>
<tr>
<td align="left">volatile acidity</td>
<td align="right">-0.03</td>
<td align="right">0.06</td>
<td align="right">0.09</td>
<td align="right">-0.20</td>
<td align="right">-0.15</td>
<td align="right">0.27</td>
<td align="right">0.29</td>
<td align="right">0.16</td>
<td align="right">-0.26</td>
<td align="right">1.35</td>
</tr>
<tr>
<td align="left">citric acid</td>
<td align="right">-0.18</td>
<td align="right">0.20</td>
<td align="right">-0.03</td>
<td align="right">0.20</td>
<td align="right">-0.11</td>
<td align="right">0.12</td>
<td align="right">-0.03</td>
<td align="right">-0.07</td>
<td align="right">-0.03</td>
<td align="right">0.53</td>
</tr>
<tr>
<td align="left">residual sugar</td>
<td align="right">-0.64</td>
<td align="right">0.64</td>
<td align="right">0.06</td>
<td align="right">0.40</td>
<td align="right">-0.49</td>
<td align="right">0.68</td>
<td align="right">0.25</td>
<td align="right">-0.35</td>
<td align="right">-0.05</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">chlorides</td>
<td align="right">-0.43</td>
<td align="right">0.29</td>
<td align="right">0.06</td>
<td align="right">0.25</td>
<td align="right">-0.23</td>
<td align="right">0.19</td>
<td align="right">0.31</td>
<td align="right">-0.12</td>
<td align="right">-0.16</td>
<td align="right">1.27</td>
</tr>
<tr>
<td align="left">free sulfur dioxide</td>
<td align="right">-1.26</td>
<td align="right">1.23</td>
<td align="right">-0.25</td>
<td align="right">1.19</td>
<td align="right">-0.60</td>
<td align="right">1.10</td>
<td align="right">-0.26</td>
<td align="right">-0.88</td>
<td align="right">0.31</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">total sulfur dioxide</td>
<td align="right">-1.73</td>
<td align="right">1.26</td>
<td align="right">0.18</td>
<td align="right">0.43</td>
<td align="right">-1.05</td>
<td align="right">2.10</td>
<td align="right">0.90</td>
<td align="right">-0.45</td>
<td align="right">-0.42</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">density</td>
<td align="right">-0.78</td>
<td align="right">0.78</td>
<td align="right">0.12</td>
<td align="right">0.40</td>
<td align="right">-0.68</td>
<td align="right">0.93</td>
<td align="right">0.49</td>
<td align="right">-0.30</td>
<td align="right">-0.26</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">pH</td>
<td align="right">-0.08</td>
<td align="right">-0.09</td>
<td align="right">0.08</td>
<td align="right">0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.05</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
<td align="right">0.04</td>
<td align="right">-0.02</td>
</tr>
<tr>
<td align="left">sulphates</td>
<td align="right">-0.16</td>
<td align="right">0.15</td>
<td align="right">-0.04</td>
<td align="right">0.05</td>
<td align="right">-0.12</td>
<td align="right">0.32</td>
<td align="right">0.16</td>
<td align="right">-0.03</td>
<td align="right">-0.09</td>
<td align="right">0.46</td>
</tr>
<tr>
<td align="left">alcohol</td>
<td align="right">0.58</td>
<td align="right">-0.71</td>
<td align="right">-0.09</td>
<td align="right">-0.34</td>
<td align="right">0.59</td>
<td align="right">-0.79</td>
<td align="right">-0.40</td>
<td align="right">0.20</td>
<td align="right">0.31</td>
<td align="right">0.22</td>
</tr>
<tr>
<td align="left">quality</td>
<td align="right">-0.12</td>
<td align="right">-0.39</td>
<td align="right">-0.00</td>
<td align="right">-0.03</td>
<td align="right">0.28</td>
<td align="right">-0.32</td>
<td align="right">-0.26</td>
<td align="right">-0.07</td>
<td align="right">0.44</td>
<td align="right">-0.30</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-winequality-white/figures/a5374807-4f26-4fa1-92e1-6a81e2b43c27.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-winequality-white/figures/b5f788b7-65b4-4232-a0f9-6e96bcbfc61e.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature total sulfur dioxide e no grupo 5, com valor de 85.98. A maior variação negativa foi na feature total sulfur dioxide e no grupo 0, com o valor registrado de -70.68</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<p><em>Maior proporção de população no grupo.</em></p>
<p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: residual sugar<br>&emsp;Média menor que a população: free sulfur dioxide<br>&emsp;Média menor que a população: total sulfur dioxide<br>&emsp;Média menor que a população: density<br>&emsp;Média maior que a população: alcohol</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: residual sugar<br>&emsp;Média maior que a população: free sulfur dioxide<br>&emsp;Média maior que a população: total sulfur dioxide<br>&emsp;Média maior que a população: density<br>&emsp;Média menor que a população: alcohol</p>
<p>Grupo 3: <br>&emsp;Média maior que a população: free sulfur dioxide</p>
<p>Grupo 4: <br>&emsp;Média menor que a população: free sulfur dioxide<br>&emsp;Média menor que a população: total sulfur dioxide<br>&emsp;Média menor que a população: density<br>&emsp;Média maior que a população: alcohol</p>
<p>Grupo 5: <br>&emsp;Média maior que a população: residual sugar<br>&emsp;Média maior que a população: free sulfur dioxide<br>&emsp;Média maior que a população: total sulfur dioxide<br>&emsp;Média maior que a população: density<br>&emsp;Média menor que a população: alcohol</p>
<p>Grupo 6: <br>&emsp;Média maior que a população: total sulfur dioxide</p>
<p>Grupo 7: <br>&emsp;Média menor que a população: free sulfur dioxide</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: volatile acidity<br>&emsp;Média maior que a população: citric acid<br>&emsp;Média maior que a população: chlorides</p>
