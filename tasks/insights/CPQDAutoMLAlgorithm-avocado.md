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
<th align="left">type</th>
<th align="left">region</th>
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
<td align="left">2</td>
<td align="left">54</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">conventional</td>
<td align="left">Albany</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">9126</td>
<td align="left">338</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/6a231078-4964-40ec-ba29-07d35bc0ef81.png" alt="Visualização dos outliers: DBscan" /></p>

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
<td align="right">1.04</td>
<td align="right">10582780.09</td>
<td align="right">3873553.77</td>
<td align="right">3478724.72</td>
<td align="right">303804.49</td>
<td align="right">2926697.09</td>
<td align="right">2213219.39</td>
<td align="right">669264.29</td>
<td align="right">44213.41</td>
<td align="right">2016.30</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.21</td>
<td align="right">11425636.33</td>
<td align="right">4139263.80</td>
<td align="right">4063686.09</td>
<td align="right">369050.28</td>
<td align="right">3341501.37</td>
<td align="right">2516499.27</td>
<td align="right">857674.71</td>
<td align="right">64925.94</td>
<td align="right">0.98</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.53</td>
<td align="right">2289168.77</td>
<td align="right">100735.10</td>
<td align="right">315802.19</td>
<td align="right">3465.07</td>
<td align="right">472090.38</td>
<td align="right">325850.00</td>
<td align="right">300.84</td>
<td align="right">0.00</td>
<td align="right">2015.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.90</td>
<td align="right">4506892.62</td>
<td align="right">1497227.27</td>
<td align="right">1248422.73</td>
<td align="right">86789.70</td>
<td align="right">1085392.69</td>
<td align="right">738082.97</td>
<td align="right">110035.17</td>
<td align="right">4247.78</td>
<td align="right">2015.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">1.02</td>
<td align="right">5794410.58</td>
<td align="right">2392258.48</td>
<td align="right">1755106.40</td>
<td align="right">157620.26</td>
<td align="right">1565930.06</td>
<td align="right">1233354.94</td>
<td align="right">330575.32</td>
<td align="right">22539.94</td>
<td align="right">2016.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1.15</td>
<td align="right">7158300.84</td>
<td align="right">3495036.65</td>
<td align="right">2628579.48</td>
<td align="right">382295.13</td>
<td align="right">2668036.20</td>
<td align="right">1924479.53</td>
<td align="right">888237.91</td>
<td align="right">56560.73</td>
<td align="right">2017.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1.89</td>
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
<th align="left">type</th>
<th align="left">region</th>
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
<td align="left">1</td>
<td align="left">9</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">conventional</td>
<td align="left">TotalUS</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">913</td>
<td align="left">169</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/379c1df4-3f0c-4202-aae0-2e44368d4019.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['AveragePrice', '4770', 'year'] com uma quantidade de 10 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(2.688, 3.25]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(1.564, 2.126]</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.93</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">(0.437, 1.002]</td>
<td align="right">0.20</td>
<td align="right">0.00</td>
<td align="right">0.40</td>
<td align="right">0.03</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
<td align="right">0.22</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">(1.002, 1.564]</td>
<td align="right">0.08</td>
<td align="right">0.01</td>
<td align="right">0.70</td>
<td align="right">0.01</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.12</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(2.126, 2.688]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.99</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
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
<td align="left">(1.564, 2.126]</td>
<td align="right">0.86</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.02</td>
<td align="right">0.08</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(0.437, 1.002]</td>
<td align="right">0.22</td>
<td align="right">0.01</td>
<td align="right">0.18</td>
<td align="right">0.21</td>
<td align="right">0.03</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.31</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">(1.002, 1.564]</td>
<td align="right">0.53</td>
<td align="right">0.02</td>
<td align="right">0.11</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
<td align="right">0.27</td>
<td align="right">0.00</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">(2.126, 2.688]</td>
<td align="right">0.98</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
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
<td align="left">AveragePrice - 4770 - year</td>
<td align="right">0.80</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Total Volume - XLarge Bags - year</td>
<td align="right">0.67</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">AveragePrice - Small Bags - year</td>
<td align="right">0.66</td>
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
<td align="right">-0.20</td>
<td align="right">-0.24</td>
<td align="right">-0.59</td>
<td align="right">-0.33</td>
<td align="right">-0.14</td>
<td align="right">-0.06</td>
<td align="right">-0.20</td>
<td align="right">-0.38</td>
<td align="right">-0.29</td>
<td align="right">-0.38</td>
</tr>
<tr>
<td align="left">Total Volume</td>
<td align="right">-300299.00</td>
<td align="right">2610215.79</td>
<td align="right">343270.45</td>
<td align="right">820992.59</td>
<td align="right">2680846.40</td>
<td align="right">3707935.53</td>
<td align="right">918958.75</td>
<td align="right">-42923.99</td>
<td align="right">4081905.47</td>
<td align="right">1693548.03</td>
<td align="right">10244678.77</td>
</tr>
<tr>
<td align="left">4046</td>
<td align="right">-97090.49</td>
<td align="right">454111.31</td>
<td align="right">50369.56</td>
<td align="right">527991.51</td>
<td align="right">1520855.44</td>
<td align="right">90199.04</td>
<td align="right">-15839.12</td>
<td align="right">-10295.07</td>
<td align="right">2369947.84</td>
<td align="right">758898.44</td>
<td align="right">3769114.68</td>
</tr>
<tr>
<td align="left">4225</td>
<td align="right">-113959.03</td>
<td align="right">1284530.96</td>
<td align="right">184725.02</td>
<td align="right">125317.59</td>
<td align="right">384936.27</td>
<td align="right">2696023.80</td>
<td align="right">557591.02</td>
<td align="right">-27656.01</td>
<td align="right">899048.11</td>
<td align="right">436614.78</td>
<td align="right">3351232.80</td>
</tr>
<tr>
<td align="left">4770</td>
<td align="right">-7233.70</td>
<td align="right">99603.67</td>
<td align="right">16252.36</td>
<td align="right">13569.55</td>
<td align="right">35640.15</td>
<td align="right">27266.04</td>
<td align="right">3679.22</td>
<td align="right">-175.28</td>
<td align="right">42749.06</td>
<td align="right">35321.38</td>
<td align="right">295761.76</td>
</tr>
<tr>
<td align="left">Total Bags</td>
<td align="right">-82014.42</td>
<td align="right">771971.99</td>
<td align="right">91925.69</td>
<td align="right">154116.14</td>
<td align="right">739416.73</td>
<td align="right">894448.84</td>
<td align="right">373474.61</td>
<td align="right">-4798.99</td>
<td align="right">770162.67</td>
<td align="right">462714.54</td>
<td align="right">2828571.72</td>
</tr>
<tr>
<td align="left">Small Bags</td>
<td align="right">-63274.69</td>
<td align="right">668131.25</td>
<td align="right">64458.91</td>
<td align="right">98842.67</td>
<td align="right">553117.27</td>
<td align="right">802518.83</td>
<td align="right">290551.00</td>
<td align="right">-6654.23</td>
<td align="right">577583.75</td>
<td align="right">400374.14</td>
<td align="right">2137988.57</td>
</tr>
<tr>
<td align="left">Large Bags</td>
<td align="right">-17911.65</td>
<td align="right">96204.35</td>
<td align="right">27215.88</td>
<td align="right">54377.91</td>
<td align="right">175317.37</td>
<td align="right">89193.22</td>
<td align="right">82499.58</td>
<td align="right">1379.37</td>
<td align="right">188376.49</td>
<td align="right">53848.97</td>
<td align="right">647311.27</td>
</tr>
<tr>
<td align="left">XLarge Bags</td>
<td align="right">-828.08</td>
<td align="right">7636.40</td>
<td align="right">250.90</td>
<td align="right">895.55</td>
<td align="right">10982.08</td>
<td align="right">2736.82</td>
<td align="right">424.04</td>
<td align="right">475.87</td>
<td align="right">4202.42</td>
<td align="right">8491.43</td>
<td align="right">43271.88</td>
</tr>
<tr>
<td align="left">year</td>
<td align="right">-0.03</td>
<td align="right">-0.09</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
<td align="right">-0.25</td>
<td align="right">-0.15</td>
<td align="right">0.29</td>
<td align="right">0.07</td>
<td align="right">-0.45</td>
<td align="right">0.12</td>
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
<td align="right">0.40</td>
<td align="right">-0.49</td>
<td align="right">-0.59</td>
<td align="right">-1.46</td>
<td align="right">-0.83</td>
<td align="right">-0.35</td>
<td align="right">-0.15</td>
<td align="right">-0.51</td>
<td align="right">-0.95</td>
<td align="right">-0.72</td>
<td align="right">-0.95</td>
</tr>
<tr>
<td align="left">Total Volume</td>
<td align="right">-0.45</td>
<td align="right">3.95</td>
<td align="right">0.52</td>
<td align="right">1.24</td>
<td align="right">4.06</td>
<td align="right">5.62</td>
<td align="right">1.39</td>
<td align="right">-0.07</td>
<td align="right">6.18</td>
<td align="right">2.56</td>
<td align="right">15.52</td>
</tr>
<tr>
<td align="left">4046</td>
<td align="right">-0.36</td>
<td align="right">1.69</td>
<td align="right">0.19</td>
<td align="right">1.96</td>
<td align="right">5.66</td>
<td align="right">0.34</td>
<td align="right">-0.06</td>
<td align="right">-0.04</td>
<td align="right">8.81</td>
<td align="right">2.82</td>
<td align="right">14.02</td>
</tr>
<tr>
<td align="left">4225</td>
<td align="right">-0.37</td>
<td align="right">4.16</td>
<td align="right">0.60</td>
<td align="right">0.41</td>
<td align="right">1.25</td>
<td align="right">8.72</td>
<td align="right">1.80</td>
<td align="right">-0.09</td>
<td align="right">2.91</td>
<td align="right">1.41</td>
<td align="right">10.84</td>
</tr>
<tr>
<td align="left">4770</td>
<td align="right">-0.29</td>
<td align="right">4.02</td>
<td align="right">0.66</td>
<td align="right">0.55</td>
<td align="right">1.44</td>
<td align="right">1.10</td>
<td align="right">0.15</td>
<td align="right">-0.01</td>
<td align="right">1.72</td>
<td align="right">1.42</td>
<td align="right">11.93</td>
</tr>
<tr>
<td align="left">Total Bags</td>
<td align="right">-0.43</td>
<td align="right">4.06</td>
<td align="right">0.48</td>
<td align="right">0.81</td>
<td align="right">3.89</td>
<td align="right">4.70</td>
<td align="right">1.96</td>
<td align="right">-0.03</td>
<td align="right">4.05</td>
<td align="right">2.43</td>
<td align="right">14.87</td>
</tr>
<tr>
<td align="left">Small Bags</td>
<td align="right">-0.41</td>
<td align="right">4.29</td>
<td align="right">0.41</td>
<td align="right">0.63</td>
<td align="right">3.55</td>
<td align="right">5.15</td>
<td align="right">1.87</td>
<td align="right">-0.04</td>
<td align="right">3.71</td>
<td align="right">2.57</td>
<td align="right">13.73</td>
</tr>
<tr>
<td align="left">Large Bags</td>
<td align="right">-0.33</td>
<td align="right">1.76</td>
<td align="right">0.50</td>
<td align="right">0.99</td>
<td align="right">3.21</td>
<td align="right">1.63</td>
<td align="right">1.51</td>
<td align="right">0.03</td>
<td align="right">3.45</td>
<td align="right">0.98</td>
<td align="right">11.84</td>
</tr>
<tr>
<td align="left">XLarge Bags</td>
<td align="right">-0.22</td>
<td align="right">2.04</td>
<td align="right">0.07</td>
<td align="right">0.24</td>
<td align="right">2.93</td>
<td align="right">0.73</td>
<td align="right">0.11</td>
<td align="right">0.13</td>
<td align="right">1.12</td>
<td align="right">2.26</td>
<td align="right">11.54</td>
</tr>
<tr>
<td align="left">year</td>
<td align="right">-0.03</td>
<td align="right">-0.09</td>
<td align="right">0.04</td>
<td align="right">0.01</td>
<td align="right">-0.26</td>
<td align="right">-0.16</td>
<td align="right">0.31</td>
<td align="right">0.07</td>
<td align="right">-0.48</td>
<td align="right">0.13</td>
<td align="right">0.17</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/983c6bf2-86e2-4165-a14b-072c94c49357.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-avocado/figures/d4323c4e-4d2e-4ffd-b8e3-141a538cd625.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Total Volume e no grupo outlier, com valor de 10244678.77. A maior variação negativa foi na feature Total Volume e no grupo 0, com o valor registrado de -300299.00</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">type</th>
<th align="left">region</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">conventional</td>
<td align="left">Northeast</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">225</td>
<td align="left">94</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">1.0</td>
<td align="left">0.969</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.526</td>
<td align="left">0.952</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">5</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">type</th>
<th align="left">region</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">conventional</td>
<td align="left">Boise</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">209</td>
<td align="left">338</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.713</td>
<td align="left">0.032</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.24</td>
<td align="left">0.013</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">6</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">type</th>
<th align="left">region</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">organic</td>
<td align="left">Boise</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.944</td>
<td align="left">1.0</td>
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
<th align="left">type</th>
<th align="left">region</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">conventional</td>
<td align="left">SouthCentral</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.006</td>
<td align="left">0.124</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">8</td>
<td align="left">8</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Presença maior de população na feature type: organic</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4046<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Média maior que a população: XLarge Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: Midsouth</p>
<p>Grupo 2: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Presença maior de população na feature type: conventional</p>
<p>Grupo 3: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4046<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: DallasFtWorth</p>
<p>Grupo 4: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4046<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Média maior que a população: XLarge Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: Southeast</p>
<p>Grupo 5: <br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Média maior que a população: XLarge Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: Northeast</p>
<p>Grupo 6: <br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: NewYork</p>
<p>Grupo 7: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Presença maior de população na feature type: conventional</p>
<p>Grupo 8: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4046<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Média maior que a população: XLarge Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: SouthCentral</p>
<p>Grupo 9: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4046<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Média maior que a população: XLarge Bags<br>&emsp;Presença maior de população na feature type: conventional<br>&emsp;Presença maior de população na feature region: Plains</p>
<p>Grupo outlier: <br>&emsp;Média menor que a população: AveragePrice<br>&emsp;Média maior que a população: Total Volume<br>&emsp;Média maior que a população: 4046<br>&emsp;Média maior que a população: 4225<br>&emsp;Média maior que a população: 4770<br>&emsp;Média maior que a população: Total Bags<br>&emsp;Média maior que a população: Small Bags<br>&emsp;Média maior que a população: Large Bags<br>&emsp;Média maior que a população: XLarge Bags</p>
