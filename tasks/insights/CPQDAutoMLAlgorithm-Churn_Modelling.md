<h1>CPQD AutoML Algorithm - Churn_Modelling</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 10000 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">CreditScore</th>
<th align="right">Age</th>
<th align="right">Tenure</th>
<th align="right">Balance</th>
<th align="right">NumOfProducts</th>
<th align="right">HasCrCard</th>
<th align="right">IsActiveMember</th>
<th align="right">EstimatedSalary</th>
<th align="right">Exited</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
<td align="right">10000.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">650.53</td>
<td align="right">38.92</td>
<td align="right">5.01</td>
<td align="right">76485.89</td>
<td align="right">1.53</td>
<td align="right">0.71</td>
<td align="right">0.52</td>
<td align="right">100090.24</td>
<td align="right">0.20</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">96.65</td>
<td align="right">10.49</td>
<td align="right">2.89</td>
<td align="right">62397.41</td>
<td align="right">0.58</td>
<td align="right">0.46</td>
<td align="right">0.50</td>
<td align="right">57510.49</td>
<td align="right">0.40</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">350.00</td>
<td align="right">18.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">11.58</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">584.00</td>
<td align="right">32.00</td>
<td align="right">3.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">51002.11</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">652.00</td>
<td align="right">37.00</td>
<td align="right">5.00</td>
<td align="right">97198.54</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">100193.91</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">718.00</td>
<td align="right">44.00</td>
<td align="right">7.00</td>
<td align="right">127644.24</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">149388.25</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">850.00</td>
<td align="right">92.00</td>
<td align="right">10.00</td>
<td align="right">250898.09</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">199992.48</td>
<td align="right">1.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Gender</th>
<th align="left">Geography</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">10000</td>
<td align="left">10000</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Male</td>
<td align="left">France</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">5457</td>
<td align="left">5014</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Churn_Modelling/figures/35204b76-b99a-4127-928e-282a6f3bec30.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 500 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">CreditScore</th>
<th align="right">Age</th>
<th align="right">Tenure</th>
<th align="right">Balance</th>
<th align="right">NumOfProducts</th>
<th align="right">HasCrCard</th>
<th align="right">IsActiveMember</th>
<th align="right">EstimatedSalary</th>
<th align="right">Exited</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
<td align="right">500.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">644.55</td>
<td align="right">47.55</td>
<td align="right">5.40</td>
<td align="right">82414.15</td>
<td align="right">2.08</td>
<td align="right">0.41</td>
<td align="right">0.49</td>
<td align="right">96130.37</td>
<td align="right">0.91</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">137.30</td>
<td align="right">12.81</td>
<td align="right">3.44</td>
<td align="right">66306.29</td>
<td align="right">1.08</td>
<td align="right">0.49</td>
<td align="right">0.50</td>
<td align="right">67294.28</td>
<td align="right">0.28</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">350.00</td>
<td align="right">18.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">91.75</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">534.75</td>
<td align="right">39.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">28229.93</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">645.00</td>
<td align="right">47.50</td>
<td align="right">6.00</td>
<td align="right">103957.14</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">92200.37</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">766.75</td>
<td align="right">56.00</td>
<td align="right">9.00</td>
<td align="right">131589.51</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">164837.78</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">850.00</td>
<td align="right">92.00</td>
<td align="right">10.00</td>
<td align="right">250898.09</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">199693.84</td>
<td align="right">1.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Gender</th>
<th align="left">Geography</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">500</td>
<td align="left">500</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Female</td>
<td align="left">France</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">277</td>
<td align="left">233</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Churn_Modelling/figures/5c776ffa-9e1e-4c42-ace0-2fa2252d2aa4.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Balance', 'NumOfProducts', 'IsActiveMember'] com uma quantidade de 3 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="right"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">1</td>
<td align="right">0.39</td>
<td align="right">0.38</td>
<td align="right">0.23</td>
</tr>
<tr>
<td align="right">0</td>
<td align="right">0.30</td>
<td align="right">0.30</td>
<td align="right">0.40</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited'] com uma quantidade de 5 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="right">1</td>
<td align="right">0.24</td>
<td align="right">0.11</td>
<td align="right">0.26</td>
<td align="right">0.13</td>
<td align="right">0.26</td>
</tr>
<tr>
<td align="right">0</td>
<td align="right">0.20</td>
<td align="right">0.21</td>
<td align="right">0.19</td>
<td align="right">0.20</td>
<td align="right">0.20</td>
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
<td align="left">Balance - NumOfProducts - IsActiveMember</td>
<td align="right">0.71</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Tenure - Balance - Exited</td>
<td align="right">0.71</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Tenure - HasCrCard - Exited</td>
<td align="right">0.53</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">CreditScore - Age - Tenure - Balance - NumOfProducts - HasCrCard - IsActiveMember - EstimatedSalary - Exited</td>
<td align="right">nan</td>
<td align="right">0.46</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CreditScore</td>
<td align="right">1.19</td>
<td align="right">-1.29</td>
<td align="right">0.12</td>
<td align="right">-0.26</td>
<td align="right">0.11</td>
<td align="right">-6.29</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="right">0.21</td>
<td align="right">-0.43</td>
<td align="right">0.02</td>
<td align="right">-0.47</td>
<td align="right">0.58</td>
<td align="right">9.09</td>
</tr>
<tr>
<td align="left">Tenure</td>
<td align="right">-0.06</td>
<td align="right">0.03</td>
<td align="right">-0.00</td>
<td align="right">0.07</td>
<td align="right">-0.03</td>
<td align="right">0.41</td>
</tr>
<tr>
<td align="left">Balance</td>
<td align="right">45240.82</td>
<td align="right">-74088.54</td>
<td align="right">45217.13</td>
<td align="right">-74211.51</td>
<td align="right">44916.24</td>
<td align="right">6240.27</td>
</tr>
<tr>
<td align="left">NumOfProducts</td>
<td align="right">-0.17</td>
<td align="right">0.26</td>
<td align="right">-0.15</td>
<td align="right">0.25</td>
<td align="right">-0.16</td>
<td align="right">0.58</td>
</tr>
<tr>
<td align="left">HasCrCard</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
<td align="right">-0.01</td>
<td align="right">0.00</td>
<td align="right">-0.01</td>
<td align="right">-0.31</td>
</tr>
<tr>
<td align="left">IsActiveMember</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.00</td>
<td align="right">-0.01</td>
<td align="right">-0.03</td>
</tr>
<tr>
<td align="left">EstimatedSalary</td>
<td align="right">-64838.13</td>
<td align="right">-50175.66</td>
<td align="right">66779.88</td>
<td align="right">48346.18</td>
<td align="right">833.25</td>
<td align="right">-4168.28</td>
</tr>
<tr>
<td align="left">Exited</td>
<td align="right">0.03</td>
<td align="right">-0.07</td>
<td align="right">0.04</td>
<td align="right">-0.05</td>
<td align="right">0.04</td>
<td align="right">0.75</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CreditScore</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">-0.07</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="right">0.02</td>
<td align="right">-0.04</td>
<td align="right">0.00</td>
<td align="right">-0.05</td>
<td align="right">0.06</td>
<td align="right">0.90</td>
</tr>
<tr>
<td align="left">Tenure</td>
<td align="right">-0.02</td>
<td align="right">0.01</td>
<td align="right">-0.00</td>
<td align="right">0.02</td>
<td align="right">-0.01</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">Balance</td>
<td align="right">0.73</td>
<td align="right">-1.19</td>
<td align="right">0.73</td>
<td align="right">-1.19</td>
<td align="right">0.72</td>
<td align="right">0.10</td>
</tr>
<tr>
<td align="left">NumOfProducts</td>
<td align="right">-0.32</td>
<td align="right">0.50</td>
<td align="right">-0.28</td>
<td align="right">0.48</td>
<td align="right">-0.30</td>
<td align="right">1.10</td>
</tr>
<tr>
<td align="left">HasCrCard</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
<td align="right">-0.03</td>
<td align="right">0.01</td>
<td align="right">-0.03</td>
<td align="right">-0.69</td>
</tr>
<tr>
<td align="left">IsActiveMember</td>
<td align="right">0.03</td>
<td align="right">0.02</td>
<td align="right">-0.03</td>
<td align="right">-0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.06</td>
</tr>
<tr>
<td align="left">EstimatedSalary</td>
<td align="right">-1.14</td>
<td align="right">-0.88</td>
<td align="right">1.17</td>
<td align="right">0.85</td>
<td align="right">0.01</td>
<td align="right">-0.07</td>
</tr>
<tr>
<td align="left">Exited</td>
<td align="right">0.08</td>
<td align="right">-0.19</td>
<td align="right">0.12</td>
<td align="right">-0.14</td>
<td align="right">0.11</td>
<td align="right">2.00</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Churn_Modelling/figures/71d3e5f6-3907-437d-868e-dacc360cd615.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-Churn_Modelling/figures/ac118869-71cd-4af1-938a-a5cce7b3ca75.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature EstimatedSalary e no grupo 2, com valor de 66779.88. A maior variação negativa foi na feature Balance e no grupo 3, com o valor registrado de -74211.51</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Gender</th>
<th align="left">Geography</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Male</td>
<td align="left">France</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">1099</td>
<td align="left">1200</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.562</td>
<td align="left">0.664</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.011</td>
<td align="left">0.161</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Gender</th>
<th align="left">Geography</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Male</td>
<td align="left">France</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">966</td>
<td align="left">776</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.541</td>
<td align="left">0.4</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.01</td>
<td align="left">-0.103</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">3</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Gender</th>
<th align="left">Geography</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Female</td>
<td align="left">Germany</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.214</td>
<td align="left">0.328</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">4</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Gender</th>
<th align="left">Geography</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Male</td>
<td align="left">Spain</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.191</td>
<td align="left">0.249</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: Balance<br>&emsp;Média menor que a população: EstimatedSalary</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: Balance<br>&emsp;Média maior que a população: NumOfProducts<br>&emsp;Média menor que a população: EstimatedSalary<br>&emsp;Presença maior de população na feature Geography: France</p>
<p>Grupo 2: <br>&emsp;Média maior que a população: Balance<br>&emsp;Média maior que a população: EstimatedSalary</p>
<p>Grupo 3: <br>&emsp;Média menor que a população: Balance<br>&emsp;Média maior que a população: EstimatedSalary<br>&emsp;Presença maior de população na feature Geography: France</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: Balance</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: Age<br>&emsp;Média maior que a população: NumOfProducts<br>&emsp;Média menor que a população: HasCrCard<br>&emsp;Média maior que a população: Exited</p>