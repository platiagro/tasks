<h1>CPQD AutoML Algorithm - avocado</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 18249 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">AveragePrice</th>
<th align="right">Total Volume</th>
<th align="right">4046</th>
<th align="right">4225</th>
<th align="right">4770</th>
<th align="right">Total Bags</th>
<th align="right">Small Bags</th>
<th align="right">Large Bags</th>
<th align="right">XLarge Bags</th>
<th align="right">year</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
<td align="right">18249.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">1.41</td>
<td align="right">850644.01</td>
<td align="right">293008.42</td>
<td align="right">295154.57</td>
<td align="right">22839.74</td>
<td align="right">239639.20</td>
<td align="right">182194.69</td>
<td align="right">54338.09</td>
<td align="right">3106.43</td>
<td align="right">2016.15</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.40</td>
<td align="right">3453545.36</td>
<td align="right">1264989.08</td>
<td align="right">1204120.40</td>
<td align="right">107464.07</td>
<td align="right">986242.40</td>
<td align="right">746178.51</td>
<td align="right">243965.96</td>
<td align="right">17692.89</td>
<td align="right">0.94</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.44</td>
<td align="right">84.56</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2015.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">1.10</td>
<td align="right">10838.58</td>
<td align="right">854.07</td>
<td align="right">3008.78</td>
<td align="right">0.00</td>
<td align="right">5088.64</td>
<td align="right">2849.42</td>
<td align="right">127.47</td>
<td align="right">0.00</td>
<td align="right">2015.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">1.37</td>
<td align="right">107376.76</td>
<td align="right">8645.30</td>
<td align="right">29061.02</td>
<td align="right">184.99</td>
<td align="right">39743.83</td>
<td align="right">26362.82</td>
<td align="right">2647.71</td>
<td align="right">0.00</td>
<td align="right">2016.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1.66</td>
<td align="right">432962.29</td>
<td align="right">111020.20</td>
<td align="right">150206.86</td>
<td align="right">6243.42</td>
<td align="right">110783.37</td>
<td align="right">83337.67</td>
<td align="right">22029.25</td>
<td align="right">132.50</td>
<td align="right">2017.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">3.25</td>
<td align="right">62505646.52</td>
<td align="right">22743616.17</td>
<td align="right">20470572.61</td>
<td align="right">2546439.11</td>
<td align="right">19373134.37</td>
<td align="right">13384586.80</td>
<td align="right">5719096.61</td>
<td align="right">551693.65</td>
<td align="right">2018.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">region</th>
<th align="left">type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">18249</td>
<td align="left">18249</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">54</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Albany</td>
<td align="left">conventional</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">338</td>
<td align="left">9126</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/c601a226-6d24-4acd-ae81-800cda7917cb.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 913 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">AveragePrice</th>
<th align="right">Total Volume</th>
<th align="right">4046</th>
<th align="right">4225</th>
<th align="right">4770</th>
<th align="right">Total Bags</th>
<th align="right">Small Bags</th>
<th align="right">Large Bags</th>
<th align="right">XLarge Bags</th>
<th align="right">year</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
<td align="right">913.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">1.06</td>
<td align="right">10530076.78</td>
<td align="right">3798700.73</td>
<td align="right">3500013.68</td>
<td align="right">304647.21</td>
<td align="right">2926715.14</td>
<td align="right">2217103.94</td>
<td align="right">664493.70</td>
<td align="right">45117.51</td>
<td align="right">2016.31</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.23</td>
<td align="right">11454410.18</td>
<td align="right">4179759.81</td>
<td align="right">4058744.98</td>
<td align="right">368844.55</td>
<td align="right">3340381.33</td>
<td align="right">2513768.97</td>
<td align="right">859416.04</td>
<td align="right">64635.19</td>
<td align="right">0.97</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.53</td>
<td align="right">2063573.51</td>
<td align="right">93569.28</td>
<td align="right">315802.19</td>
<td align="right">3377.63</td>
<td align="right">472090.38</td>
<td align="right">325850.00</td>
<td align="right">300.84</td>
<td align="right">0.00</td>
<td align="right">2015.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.91</td>
<td align="right">4250394.01</td>
<td align="right">1275098.12</td>
<td align="right">1265510.82</td>
<td align="right">87250.83</td>
<td align="right">1078418.77</td>
<td align="right">756322.54</td>
<td align="right">109448.15</td>
<td align="right">5126.49</td>
<td align="right">2016.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">1.03</td>
<td align="right">5791508.96</td>
<td align="right">2324813.13</td>
<td align="right">1762047.32</td>
<td align="right">161251.98</td>
<td align="right">1552503.62</td>
<td align="right">1226901.91</td>
<td align="right">314632.79</td>
<td align="right">25383.34</td>
<td align="right">2016.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1.18</td>
<td align="right">7158300.84</td>
<td align="right">3495036.65</td>
<td align="right">2718513.23</td>
<td align="right">382295.13</td>
<td align="right">2668036.20</td>
<td align="right">1924479.53</td>
<td align="right">888237.91</td>
<td align="right">56719.10</td>
<td align="right">2017.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1.98</td>
<td align="right">62505646.52</td>
<td align="right">22743616.17</td>
<td align="right">20470572.61</td>
<td align="right">2546439.11</td>
<td align="right">19373134.37</td>
<td align="right">13384586.80</td>
<td align="right">5719096.61</td>
<td align="right">551693.65</td>
<td align="right">2018.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">region</th>
<th align="left">type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">913</td>
<td align="left">913</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">9</td>
<td align="left">1</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">TotalUS</td>
<td align="left">conventional</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">169</td>
<td align="left">913</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/805e97dc-9808-4ff4-b50c-73ef7d2d0988.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['4770', 'Total Bags', 'year'] com uma quantidade de 10 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(1.002, 1.564]</td>
<td align="right">0.43</td>
<td align="right">0.02</td>
<td align="right">0.11</td>
<td align="right">0.03</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
<td align="right">0.32</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">(1.564, 2.126]</td>
<td align="right">0.78</td>
<td align="right">0.01</td>
<td align="right">0.05</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.13</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">(2.126, 2.688]</td>
<td align="right">0.93</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.05</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(2.688, 3.25]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(0.437, 1.002]</td>
<td align="right">0.15</td>
<td align="right">0.01</td>
<td align="right">0.19</td>
<td align="right">0.09</td>
<td align="right">0.01</td>
<td align="right">0.15</td>
<td align="right">0.31</td>
<td align="right">0.04</td>
<td align="right">0.01</td>
<td align="right">0.03</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['AveragePrice', 'Total Volume', '4046', '4225', '4770', 'Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags', 'year'] com uma quantidade de 10 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="left">(1.002, 1.564]</td>
<td align="right">0.53</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
<td align="right">0.11</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.27</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">(1.564, 2.126]</td>
<td align="right">0.86</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">0.02</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.08</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(2.126, 2.688]</td>
<td align="right">0.98</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(2.688, 3.25]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(0.437, 1.002]</td>
<td align="right">0.21</td>
<td align="right">0.01</td>
<td align="right">0.21</td>
<td align="right">0.18</td>
<td align="right">0.03</td>
<td align="right">0.02</td>
<td align="right">0.02</td>
<td align="right">0.00</td>
<td align="right">0.31</td>
<td align="right">0.02</td>
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
<td align="left">4770 - Total Bags - year</td>
<td align="right">0.64</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Total Volume - 4046 - Large Bags</td>
<td align="right">0.63</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Total Volume - Total Bags - year</td>
<td align="right">0.62</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">AveragePrice - Total Volume - 4046 - 4225 - 4770 - Total Bags - Small Bags - Large Bags - XLarge Bags - year</td>
<td align="right">nan</td>
<td align="right">0.59</td>
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
<th align="right">9</th>
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">AveragePrice</td>
<td align="right">0.16</td>
<td align="right">-0.24</td>
<td align="right">-0.59</td>
<td align="right">-0.23</td>
<td align="right">-0.34</td>
<td align="right">-0.07</td>
<td align="right">-0.45</td>
<td align="right">-0.11</td>
<td align="right">-0.20</td>
<td align="right">-0.31</td>
<td align="right">-0.36</td>
</tr>
<tr>
<td align="left">Total Volume</td>
<td align="right">-303684.87</td>
<td align="right">2545822.33</td>
<td align="right">808368.80</td>
<td align="right">331931.57</td>
<td align="right">2784376.11</td>
<td align="right">903075.13</td>
<td align="right">4592222.09</td>
<td align="right">3507665.61</td>
<td align="right">-50163.13</td>
<td align="right">1668302.67</td>
<td align="right">10189199.84</td>
</tr>
<tr>
<td align="left">4046</td>
<td align="right">-101230.04</td>
<td align="right">502210.32</td>
<td align="right">518654.14</td>
<td align="right">46644.97</td>
<td align="right">1636816.84</td>
<td align="right">-17410.08</td>
<td align="right">2527439.74</td>
<td align="right">105293.65</td>
<td align="right">-16094.61</td>
<td align="right">764204.08</td>
<td align="right">3690319.50</td>
</tr>
<tr>
<td align="left">4225</td>
<td align="right">-113002.38</td>
<td align="right">1166155.06</td>
<td align="right">125467.06</td>
<td align="right">181475.78</td>
<td align="right">376276.17</td>
<td align="right">544039.32</td>
<td align="right">1243257.63</td>
<td align="right">2499535.35</td>
<td align="right">-28259.21</td>
<td align="right">418200.60</td>
<td align="right">3373642.94</td>
</tr>
<tr>
<td align="left">4770</td>
<td align="right">-7217.89</td>
<td align="right">100095.52</td>
<td align="right">13761.34</td>
<td align="right">15971.37</td>
<td align="right">34673.56</td>
<td align="right">3771.52</td>
<td align="right">57381.07</td>
<td align="right">23748.33</td>
<td align="right">-162.67</td>
<td align="right">32326.11</td>
<td align="right">296648.86</td>
</tr>
<tr>
<td align="left">Total Bags</td>
<td align="right">-82233.16</td>
<td align="right">777363.58</td>
<td align="right">150488.46</td>
<td align="right">87841.64</td>
<td align="right">736611.73</td>
<td align="right">372623.88</td>
<td align="right">764145.86</td>
<td align="right">879090.47</td>
<td align="right">-5648.11</td>
<td align="right">453573.03</td>
<td align="right">2828590.73</td>
</tr>
<tr>
<td align="left">Small Bags</td>
<td align="right">-63232.26</td>
<td align="right">676895.36</td>
<td align="right">95490.65</td>
<td align="right">62308.53</td>
<td align="right">523934.94</td>
<td align="right">286233.13</td>
<td align="right">604858.89</td>
<td align="right">782094.36</td>
<td align="right">-7058.55</td>
<td align="right">390698.90</td>
<td align="right">2142077.69</td>
</tr>
<tr>
<td align="left">Large Bags</td>
<td align="right">-18215.01</td>
<td align="right">92617.24</td>
<td align="right">54025.51</td>
<td align="right">25229.68</td>
<td align="right">205257.48</td>
<td align="right">85966.41</td>
<td align="right">156550.55</td>
<td align="right">94500.32</td>
<td align="right">894.81</td>
<td align="right">54868.94</td>
<td align="right">642289.44</td>
</tr>
<tr>
<td align="left">XLarge Bags</td>
<td align="right">-785.89</td>
<td align="right">7850.98</td>
<td align="right">972.30</td>
<td align="right">303.42</td>
<td align="right">7419.30</td>
<td align="right">424.34</td>
<td align="right">2736.41</td>
<td align="right">2495.82</td>
<td align="right">515.63</td>
<td align="right">8005.20</td>
<td align="right">44223.60</td>
</tr>
<tr>
<td align="left">year</td>
<td align="right">-0.03</td>
<td align="right">-0.05</td>
<td align="right">-0.01</td>
<td align="right">0.03</td>
<td align="right">-0.33</td>
<td align="right">0.30</td>
<td align="right">-0.64</td>
<td align="right">0.02</td>
<td align="right">0.07</td>
<td align="right">0.12</td>
<td align="right">0.17</td>
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
<th align="right">9</th>
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">AveragePrice</td>
<td align="right">0.41</td>
<td align="right">-0.60</td>
<td align="right">-1.46</td>
<td align="right">-0.58</td>
<td align="right">-0.85</td>
<td align="right">-0.18</td>
<td align="right">-1.13</td>
<td align="right">-0.27</td>
<td align="right">-0.51</td>
<td align="right">-0.77</td>
<td align="right">-0.91</td>
</tr>
<tr>
<td align="left">Total Volume</td>
<td align="right">-0.45</td>
<td align="right">3.76</td>
<td align="right">1.19</td>
<td align="right">0.49</td>
<td align="right">4.11</td>
<td align="right">1.33</td>
<td align="right">6.79</td>
<td align="right">5.18</td>
<td align="right">-0.07</td>
<td align="right">2.47</td>
<td align="right">15.06</td>
</tr>
<tr>
<td align="left">4046</td>
<td align="right">-0.35</td>
<td align="right">1.73</td>
<td align="right">1.79</td>
<td align="right">0.16</td>
<td align="right">5.65</td>
<td align="right">-0.06</td>
<td align="right">8.72</td>
<td align="right">0.36</td>
<td align="right">-0.06</td>
<td align="right">2.64</td>
<td align="right">12.73</td>
</tr>
<tr>
<td align="left">4225</td>
<td align="right">-0.38</td>
<td align="right">3.88</td>
<td align="right">0.42</td>
<td align="right">0.60</td>
<td align="right">1.25</td>
<td align="right">1.81</td>
<td align="right">4.14</td>
<td align="right">8.33</td>
<td align="right">-0.09</td>
<td align="right">1.39</td>
<td align="right">11.24</td>
</tr>
<tr>
<td align="left">4770</td>
<td align="right">-0.30</td>
<td align="right">4.10</td>
<td align="right">0.56</td>
<td align="right">0.65</td>
<td align="right">1.42</td>
<td align="right">0.15</td>
<td align="right">2.35</td>
<td align="right">0.97</td>
<td align="right">-0.01</td>
<td align="right">1.32</td>
<td align="right">12.15</td>
</tr>
<tr>
<td align="left">Total Bags</td>
<td align="right">-0.43</td>
<td align="right">4.07</td>
<td align="right">0.79</td>
<td align="right">0.46</td>
<td align="right">3.85</td>
<td align="right">1.95</td>
<td align="right">4.00</td>
<td align="right">4.60</td>
<td align="right">-0.03</td>
<td align="right">2.37</td>
<td align="right">14.79</td>
</tr>
<tr>
<td align="left">Small Bags</td>
<td align="right">-0.41</td>
<td align="right">4.36</td>
<td align="right">0.62</td>
<td align="right">0.40</td>
<td align="right">3.38</td>
<td align="right">1.84</td>
<td align="right">3.90</td>
<td align="right">5.04</td>
<td align="right">-0.05</td>
<td align="right">2.52</td>
<td align="right">13.80</td>
</tr>
<tr>
<td align="left">Large Bags</td>
<td align="right">-0.32</td>
<td align="right">1.65</td>
<td align="right">0.96</td>
<td align="right">0.45</td>
<td align="right">3.65</td>
<td align="right">1.53</td>
<td align="right">2.79</td>
<td align="right">1.68</td>
<td align="right">0.02</td>
<td align="right">0.98</td>
<td align="right">11.43</td>
</tr>
<tr>
<td align="left">XLarge Bags</td>
<td align="right">-0.23</td>
<td align="right">2.28</td>
<td align="right">0.28</td>
<td align="right">0.09</td>
<td align="right">2.15</td>
<td align="right">0.12</td>
<td align="right">0.79</td>
<td align="right">0.72</td>
<td align="right">0.15</td>
<td align="right">2.32</td>
<td align="right">12.83</td>
</tr>
<tr>
<td align="left">year</td>
<td align="right">-0.03</td>
<td align="right">-0.05</td>
<td align="right">-0.01</td>
<td align="right">0.04</td>
<td align="right">-0.35</td>
<td align="right">0.32</td>
<td align="right">-0.68</td>
<td align="right">0.02</td>
<td align="right">0.07</td>
<td align="right">0.13</td>
<td align="right">0.18</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/852f0356-6fff-45a9-b7e1-ac2b8d398927.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/222fd571-798a-4fb2-afef-422e8566e707.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Total Volume e no grupo outlier, com valor de 10189199.84. A maior variação negativa foi na feature Total Volume e no grupo 0, com o valor registrado de -303684.87</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">region</th>
<th align="left">type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Northeast</td>
<td align="left">conventional</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">97</td>
<td align="left">209</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.941747572815534</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.9257115783531435</td>
<td align="left">0.5262459621596678</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">7</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">region</th>
<th align="left">type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Boise</td>
<td align="left">conventional</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">338</td>
<td align="left">220</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.03251563251563252</td>
<td align="left">0.7166123778501629</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.013018632054165053</td>
<td align="left">0.2428583400098306</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">5</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: Presença maior de população na feature type: organic</p>
<p>Grupo 1: Média menor que a população: AveragePrice, Média maior que a população: Total Volume, Média maior que a população: 4046, Média maior que a população: 4225, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Média maior que a população: XLarge Bags, Presença maior de população na feature region: Midsouth, Presença maior de população na feature type: conventional</p>
<p>Grupo 2: Média menor que a população: AveragePrice, Média maior que a população: Total Volume, Média maior que a população: 4046, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Presença maior de população na feature region: DallasFtWorth, Presença maior de população na feature type: conventional</p>
<p>Grupo 3: Média menor que a população: AveragePrice, Média maior que a população: 4225, Média maior que a população: 4770, Presença maior de população na feature type: conventional</p>
<p>Grupo 4: Média menor que a população: AveragePrice, Média maior que a população: Total Volume, Média maior que a população: 4046, Média maior que a população: 4225, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Média maior que a população: XLarge Bags, Presença maior de população na feature region: Southeast, Presença maior de população na feature type: conventional</p>
<p>Grupo 5: Média maior que a população: Total Volume, Média maior que a população: 4225, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Presença maior de população na feature region: NewYork, Presença maior de população na feature type: conventional</p>
<p>Grupo 6: Média menor que a população: AveragePrice, Média maior que a população: Total Volume, Média maior que a população: 4046, Média maior que a população: 4225, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Média maior que a população: XLarge Bags, Média menor que a população: year, Presença maior de população na feature region: SouthCentral, Presença maior de população na feature type: conventional</p>
<p>Grupo 7: Média maior que a população: Total Volume, Média maior que a população: 4225, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Média maior que a população: XLarge Bags, Presença maior de população na feature region: Northeast, Presença maior de população na feature type: conventional</p>
<p>Grupo 8: Média menor que a população: AveragePrice, Presença maior de população na feature type: conventional</p>
<p>Grupo 9: Média menor que a população: AveragePrice, Média maior que a população: Total Volume, Média maior que a população: 4046, Média maior que a população: 4225, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Média maior que a população: XLarge Bags, Presença maior de população na feature region: Plains, Presença maior de população na feature type: conventional</p>
<p>Grupo outlier: Média menor que a população: AveragePrice, Média maior que a população: Total Volume, Média maior que a população: 4046, Média maior que a população: 4225, Média maior que a população: 4770, Média maior que a população: Total Bags, Média maior que a população: Small Bags, Média maior que a população: Large Bags, Média maior que a população: XLarge Bags</p>
