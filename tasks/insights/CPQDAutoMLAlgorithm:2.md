<h1>CPQD AutoML Algorithm: 2</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 465 outliers neste dataset, correspondendo a uma proporção de 65.31% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Survived</th>
<th align="right">Pclass</th>
<th align="right">Age</th>
<th align="right">SibSp</th>
<th align="right">Parch</th>
<th align="right">Fare</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">465.00</td>
<td align="right">465.00</td>
<td align="right">465.00</td>
<td align="right">465.00</td>
<td align="right">465.00</td>
<td align="right">465.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">0.49</td>
<td align="right">1.93</td>
<td align="right">31.97</td>
<td align="right">0.73</td>
<td align="right">0.65</td>
<td align="right">48.24</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.50</td>
<td align="right">0.85</td>
<td align="right">16.93</td>
<td align="right">1.06</td>
<td align="right">0.99</td>
<td align="right">61.25</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.42</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">19.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">15.90</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">33.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">26.55</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">44.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">55.90</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">80.00</td>
<td align="right">5.00</td>
<td align="right">6.00</td>
<td align="right">512.33</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Sex</th>
<th align="left">Embarked</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">465</td>
<td align="left">465</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">male</td>
<td align="left">S</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">261</td>
<td align="left">344</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:2/figures/f49ae0ef-5e9d-4a4d-b939-42a426eb0f85.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 36 outliers neste dataset, correspondendo a uma proporção de 5.06% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Survived</th>
<th align="right">Pclass</th>
<th align="right">Age</th>
<th align="right">SibSp</th>
<th align="right">Parch</th>
<th align="right">Fare</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">36.00</td>
<td align="right">36.00</td>
<td align="right">36.00</td>
<td align="right">36.00</td>
<td align="right">36.00</td>
<td align="right">36.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">0.47</td>
<td align="right">2.06</td>
<td align="right">26.16</td>
<td align="right">1.89</td>
<td align="right">2.44</td>
<td align="right">140.02</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.51</td>
<td align="right">0.98</td>
<td align="right">16.68</td>
<td align="right">1.83</td>
<td align="right">1.52</td>
<td align="right">148.24</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.92</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">7.92</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">15.50</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">31.36</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">0.00</td>
<td align="right">2.50</td>
<td align="right">24.00</td>
<td align="right">1.00</td>
<td align="right">2.00</td>
<td align="right">46.90</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">38.25</td>
<td align="right">3.25</td>
<td align="right">3.00</td>
<td align="right">251.23</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">64.00</td>
<td align="right">5.00</td>
<td align="right">6.00</td>
<td align="right">512.33</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Sex</th>
<th align="left">Embarked</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">36</td>
<td align="left">36</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">female</td>
<td align="left">S</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">21</td>
<td align="left">25</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:2/figures/38928ec7-83b0-439b-8d4a-304f843f46c7.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 2 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['SibSp', 'Parch'] com uma quantidade de 9 grupos. A análise multidimensional em 2 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="right"></th>
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
<td align="right">0</td>
<td align="right">0.68</td>
<td align="right">0.06</td>
<td align="right">0.05</td>
<td align="right">0.12</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0.46</td>
<td align="right">0.14</td>
<td align="right">0.00</td>
<td align="right">0.19</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.08</td>
<td align="right">0.04</td>
<td align="right">0.01</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'] com uma quantidade de 11 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="right"></th>
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
<td align="right">0</td>
<td align="right">0.03</td>
<td align="right">0.43</td>
<td align="right">0.01</td>
<td align="right">0.12</td>
<td align="right">0.00</td>
<td align="right">0.21</td>
<td align="right">0.04</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.08</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0.07</td>
<td align="right">0.23</td>
<td align="right">0.08</td>
<td align="right">0.15</td>
<td align="right">0.02</td>
<td align="right">0.09</td>
<td align="right">0.11</td>
<td align="right">0.15</td>
<td align="right">0.04</td>
<td align="right">0.04</td>
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
<td align="left">SibSp - Parch</td>
<td align="right">0.96</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Survived - Parch</td>
<td align="right">0.84</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Pclass - Fare</td>
<td align="right">0.67</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Survived - Pclass - Age - SibSp - Parch - Fare</td>
<td align="right">nan</td>
<td align="right">0.44</td>
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
<td align="left">Survived</td>
<td align="right">-0.02</td>
<td align="right">-0.08</td>
<td align="right">0.20</td>
<td align="right">-0.10</td>
<td align="right">0.03</td>
<td align="right">-0.00</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">Pclass</td>
<td align="right">-0.22</td>
<td align="right">0.22</td>
<td align="right">0.40</td>
<td align="right">-0.68</td>
<td align="right">-0.14</td>
<td align="right">0.09</td>
<td align="right">0.30</td>
<td align="right">-0.65</td>
<td align="right">-0.19</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="right">12.31</td>
<td align="right">-6.86</td>
<td align="right">-25.09</td>
<td align="right">34.06</td>
<td align="right">4.77</td>
<td align="right">-1.24</td>
<td align="right">-12.25</td>
<td align="right">21.01</td>
<td align="right">-3.66</td>
</tr>
<tr>
<td align="left">SibSp</td>
<td align="right">-0.10</td>
<td align="right">-0.16</td>
<td align="right">1.21</td>
<td align="right">-0.27</td>
<td align="right">-0.10</td>
<td align="right">-0.13</td>
<td align="right">-0.07</td>
<td align="right">-0.06</td>
<td align="right">1.45</td>
</tr>
<tr>
<td align="left">Parch</td>
<td align="right">0.04</td>
<td align="right">-0.13</td>
<td align="right">1.04</td>
<td align="right">-0.16</td>
<td align="right">-0.09</td>
<td align="right">-0.18</td>
<td align="right">-0.05</td>
<td align="right">-0.12</td>
<td align="right">2.12</td>
</tr>
<tr>
<td align="left">Fare</td>
<td align="right">8.46</td>
<td align="right">-5.77</td>
<td align="right">-1.98</td>
<td align="right">9.85</td>
<td align="right">2.91</td>
<td align="right">-4.70</td>
<td align="right">-4.88</td>
<td align="right">10.56</td>
<td align="right">111.07</td>
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
<td align="left">Survived</td>
<td align="right">-0.05</td>
<td align="right">-0.16</td>
<td align="right">0.41</td>
<td align="right">-0.21</td>
<td align="right">0.05</td>
<td align="right">-0.00</td>
<td align="right">-0.03</td>
<td align="right">0.02</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">Pclass</td>
<td align="right">-0.27</td>
<td align="right">0.27</td>
<td align="right">0.48</td>
<td align="right">-0.83</td>
<td align="right">-0.17</td>
<td align="right">0.11</td>
<td align="right">0.36</td>
<td align="right">-0.78</td>
<td align="right">-0.24</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="right">0.86</td>
<td align="right">-0.48</td>
<td align="right">-1.75</td>
<td align="right">2.37</td>
<td align="right">0.33</td>
<td align="right">-0.09</td>
<td align="right">-0.85</td>
<td align="right">1.46</td>
<td align="right">-0.26</td>
</tr>
<tr>
<td align="left">SibSp</td>
<td align="right">-0.13</td>
<td align="right">-0.20</td>
<td align="right">1.52</td>
<td align="right">-0.35</td>
<td align="right">-0.13</td>
<td align="right">-0.16</td>
<td align="right">-0.09</td>
<td align="right">-0.08</td>
<td align="right">1.82</td>
</tr>
<tr>
<td align="left">Parch</td>
<td align="right">0.06</td>
<td align="right">-0.21</td>
<td align="right">1.61</td>
<td align="right">-0.24</td>
<td align="right">-0.14</td>
<td align="right">-0.28</td>
<td align="right">-0.08</td>
<td align="right">-0.18</td>
<td align="right">3.27</td>
</tr>
<tr>
<td align="left">Fare</td>
<td align="right">0.25</td>
<td align="right">-0.17</td>
<td align="right">-0.06</td>
<td align="right">0.29</td>
<td align="right">0.08</td>
<td align="right">-0.14</td>
<td align="right">-0.14</td>
<td align="right">0.31</td>
<td align="right">3.22</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:2/figures/8a75ef7b-4229-4051-a7bc-bbfb1eba5b14.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm:2/figures/9b3c3884-8122-450b-8172-46fcd0c3dd7d.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Fare e no grupo outlier, com valor de 111.07. A maior variação negativa foi na feature Age e no grupo 2, com o valor registrado de -25.09</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Sex</th>
<th align="left">Embarked</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">male</td>
<td align="left">S</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">24</td>
<td align="left">86</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.8</td>
<td align="left">0.8349514563106796</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.15207100591715983</td>
<td align="left">0.05240707761245467</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">3</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Sex</th>
<th align="left">Embarked</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">male</td>
<td align="left">S</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">64</td>
<td align="left">21</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.6037735849056604</td>
<td align="left">0.7</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.04415540917717986</td>
<td align="left">-0.08254437869822495</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">6</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: Média maior que a população: Age</p>
<p>Grupo 2: Média menor que a população: Age, Média maior que a população: SibSp, Média maior que a população: Parch, Presença maior de população na feature Sex: female</p>
<p>Grupo 3: Média menor que a população: Pclass, Média maior que a população: Age, Presença maior de população na feature Sex: male</p>
<p>Grupo 6: Média menor que a população: Age</p>
<p>Grupo 7: Média menor que a população: Pclass, Média maior que a população: Age</p>
<p>Grupo outlier: Média maior que a população: SibSp, Média maior que a população: Parch, Média maior que a população: Fare</p>
