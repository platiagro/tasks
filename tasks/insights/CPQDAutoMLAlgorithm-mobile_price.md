<h1>CPQD AutoML Algorithm - mobile_price</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 2000 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">battery_power</th>
<th align="right">blue</th>
<th align="right">clock_speed</th>
<th align="right">dual_sim</th>
<th align="right">fc</th>
<th align="right">four_g</th>
<th align="right">int_memory</th>
<th align="right">m_dep</th>
<th align="right">mobile_wt</th>
<th align="right">n_cores</th>
<th align="right">pc</th>
<th align="right">px_height</th>
<th align="right">px_width</th>
<th align="right">ram</th>
<th align="right">sc_h</th>
<th align="right">sc_w</th>
<th align="right">talk_time</th>
<th align="right">three_g</th>
<th align="right">touch_screen</th>
<th align="right">wifi</th>
<th align="right">price_range</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
<td align="right">2000.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">1238.52</td>
<td align="right">0.49</td>
<td align="right">1.52</td>
<td align="right">0.51</td>
<td align="right">4.31</td>
<td align="right">0.52</td>
<td align="right">32.05</td>
<td align="right">0.50</td>
<td align="right">140.25</td>
<td align="right">4.52</td>
<td align="right">9.92</td>
<td align="right">645.11</td>
<td align="right">1251.52</td>
<td align="right">2124.21</td>
<td align="right">12.31</td>
<td align="right">5.77</td>
<td align="right">11.01</td>
<td align="right">0.76</td>
<td align="right">0.50</td>
<td align="right">0.51</td>
<td align="right">1.50</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">439.42</td>
<td align="right">0.50</td>
<td align="right">0.82</td>
<td align="right">0.50</td>
<td align="right">4.34</td>
<td align="right">0.50</td>
<td align="right">18.15</td>
<td align="right">0.29</td>
<td align="right">35.40</td>
<td align="right">2.29</td>
<td align="right">6.06</td>
<td align="right">443.78</td>
<td align="right">432.20</td>
<td align="right">1084.73</td>
<td align="right">4.21</td>
<td align="right">4.36</td>
<td align="right">5.46</td>
<td align="right">0.43</td>
<td align="right">0.50</td>
<td align="right">0.50</td>
<td align="right">1.12</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">501.00</td>
<td align="right">0.00</td>
<td align="right">0.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.10</td>
<td align="right">80.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">500.00</td>
<td align="right">256.00</td>
<td align="right">5.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">851.75</td>
<td align="right">0.00</td>
<td align="right">0.70</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">16.00</td>
<td align="right">0.20</td>
<td align="right">109.00</td>
<td align="right">3.00</td>
<td align="right">5.00</td>
<td align="right">282.75</td>
<td align="right">874.75</td>
<td align="right">1207.50</td>
<td align="right">9.00</td>
<td align="right">2.00</td>
<td align="right">6.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.75</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">1226.00</td>
<td align="right">0.00</td>
<td align="right">1.50</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">32.00</td>
<td align="right">0.50</td>
<td align="right">141.00</td>
<td align="right">4.00</td>
<td align="right">10.00</td>
<td align="right">564.00</td>
<td align="right">1247.00</td>
<td align="right">2146.50</td>
<td align="right">12.00</td>
<td align="right">5.00</td>
<td align="right">11.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.50</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1615.25</td>
<td align="right">1.00</td>
<td align="right">2.20</td>
<td align="right">1.00</td>
<td align="right">7.00</td>
<td align="right">1.00</td>
<td align="right">48.00</td>
<td align="right">0.80</td>
<td align="right">170.00</td>
<td align="right">7.00</td>
<td align="right">15.00</td>
<td align="right">947.25</td>
<td align="right">1633.00</td>
<td align="right">3064.50</td>
<td align="right">16.00</td>
<td align="right">9.00</td>
<td align="right">16.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">2.25</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1998.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">19.00</td>
<td align="right">1.00</td>
<td align="right">64.00</td>
<td align="right">1.00</td>
<td align="right">200.00</td>
<td align="right">8.00</td>
<td align="right">20.00</td>
<td align="right">1960.00</td>
<td align="right">1998.00</td>
<td align="right">3998.00</td>
<td align="right">19.00</td>
<td align="right">18.00</td>
<td align="right">20.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
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
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-mobile_price/figures/4a4d1cc9-85ce-4ade-9248-8f35c1d2af72.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 100 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">battery_power</th>
<th align="right">blue</th>
<th align="right">clock_speed</th>
<th align="right">dual_sim</th>
<th align="right">fc</th>
<th align="right">four_g</th>
<th align="right">int_memory</th>
<th align="right">m_dep</th>
<th align="right">mobile_wt</th>
<th align="right">n_cores</th>
<th align="right">pc</th>
<th align="right">px_height</th>
<th align="right">px_width</th>
<th align="right">ram</th>
<th align="right">sc_h</th>
<th align="right">sc_w</th>
<th align="right">talk_time</th>
<th align="right">three_g</th>
<th align="right">touch_screen</th>
<th align="right">wifi</th>
<th align="right">price_range</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
<td align="right">100.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">1288.62</td>
<td align="right">0.49</td>
<td align="right">1.80</td>
<td align="right">0.56</td>
<td align="right">7.53</td>
<td align="right">0.26</td>
<td align="right">34.71</td>
<td align="right">0.55</td>
<td align="right">136.37</td>
<td align="right">4.19</td>
<td align="right">12.52</td>
<td align="right">865.48</td>
<td align="right">1427.99</td>
<td align="right">2217.77</td>
<td align="right">13.65</td>
<td align="right">6.53</td>
<td align="right">10.92</td>
<td align="right">0.41</td>
<td align="right">0.51</td>
<td align="right">0.51</td>
<td align="right">1.75</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">470.43</td>
<td align="right">0.50</td>
<td align="right">0.91</td>
<td align="right">0.50</td>
<td align="right">6.49</td>
<td align="right">0.44</td>
<td align="right">21.98</td>
<td align="right">0.35</td>
<td align="right">39.86</td>
<td align="right">2.59</td>
<td align="right">6.95</td>
<td align="right">628.92</td>
<td align="right">498.85</td>
<td align="right">1286.52</td>
<td align="right">4.85</td>
<td align="right">5.96</td>
<td align="right">6.71</td>
<td align="right">0.49</td>
<td align="right">0.50</td>
<td align="right">0.50</td>
<td align="right">1.23</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">512.00</td>
<td align="right">0.00</td>
<td align="right">0.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.10</td>
<td align="right">80.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">512.00</td>
<td align="right">262.00</td>
<td align="right">5.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">866.25</td>
<td align="right">0.00</td>
<td align="right">0.90</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">12.75</td>
<td align="right">0.10</td>
<td align="right">101.25</td>
<td align="right">2.00</td>
<td align="right">6.00</td>
<td align="right">248.75</td>
<td align="right">923.25</td>
<td align="right">1048.75</td>
<td align="right">9.00</td>
<td align="right">1.00</td>
<td align="right">4.75</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">1331.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">6.00</td>
<td align="right">0.00</td>
<td align="right">35.50</td>
<td align="right">0.60</td>
<td align="right">130.50</td>
<td align="right">4.00</td>
<td align="right">15.00</td>
<td align="right">852.00</td>
<td align="right">1643.50</td>
<td align="right">2309.50</td>
<td align="right">16.00</td>
<td align="right">4.00</td>
<td align="right">10.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">2.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1712.25</td>
<td align="right">1.00</td>
<td align="right">2.62</td>
<td align="right">1.00</td>
<td align="right">14.00</td>
<td align="right">1.00</td>
<td align="right">56.00</td>
<td align="right">0.90</td>
<td align="right">179.75</td>
<td align="right">7.00</td>
<td align="right">19.00</td>
<td align="right">1454.75</td>
<td align="right">1849.25</td>
<td align="right">3496.50</td>
<td align="right">18.00</td>
<td align="right">12.25</td>
<td align="right">18.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1989.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">18.00</td>
<td align="right">1.00</td>
<td align="right">64.00</td>
<td align="right">1.00</td>
<td align="right">200.00</td>
<td align="right">8.00</td>
<td align="right">20.00</td>
<td align="right">1878.00</td>
<td align="right">1995.00</td>
<td align="right">3978.00</td>
<td align="right">19.00</td>
<td align="right">18.00</td>
<td align="right">20.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
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
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-mobile_price/figures/b810f148-9ac1-43b7-99ef-c8d1df741597.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['dual<em>sim', 'mobile</em>wt', 'sc_h'] com uma quantidade de 2 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="right"></th>
<th align="right">0</th>
<th align="right">1</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">3</td>
<td align="right">0.47</td>
<td align="right">0.53</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0.55</td>
<td align="right">0.45</td>
</tr>
<tr>
<td align="right">0</td>
<td align="right">0.52</td>
<td align="right">0.48</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0.50</td>
<td align="right">0.50</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['battery<em>power', 'blue', 'clock</em>speed', 'dual<em>sim', 'fc', 'four</em>g', 'int<em>memory', 'm</em>dep', 'mobile<em>wt', 'n</em>cores', 'pc', 'px<em>height', 'px</em>width', 'ram', 'sc<em>h', 'sc</em>w', 'talk<em>time', 'three</em>g', 'touch<em>screen', 'wifi', 'price</em>range'] com uma quantidade de 2 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="right"></th>
<th align="right">0</th>
<th align="right">1</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">3</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0.15</td>
<td align="right">0.85</td>
</tr>
<tr>
<td align="right">0</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0.79</td>
<td align="right">0.21</td>
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
<td align="left">dual_sim - mobile_wt - sc_h</td>
<td align="right">0.61</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">n_cores - px_width - price_range</td>
<td align="right">0.55</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">blue - n_cores - px_height</td>
<td align="right">0.53</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">battery_power - blue - clock_speed - dual_sim - fc - four_g - int_memory - m_dep - mobile_wt - n_cores - pc - px_height - px_width - ram - sc_h - sc_w - talk_time - three_g - touch_screen - wifi - price_range</td>
<td align="right">nan</td>
<td align="right">0.40</td>
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
<td align="left">battery_power</td>
<td align="right">1.75</td>
<td align="right">-1.68</td>
<td align="right">52.74</td>
</tr>
<tr>
<td align="left">blue</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
</tr>
<tr>
<td align="left">clock_speed</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.29</td>
</tr>
<tr>
<td align="left">dual_sim</td>
<td align="right">-0.02</td>
<td align="right">0.01</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="left">fc</td>
<td align="right">-0.08</td>
<td align="right">0.07</td>
<td align="right">3.39</td>
</tr>
<tr>
<td align="left">four_g</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.28</td>
</tr>
<tr>
<td align="left">int_memory</td>
<td align="right">-0.58</td>
<td align="right">0.56</td>
<td align="right">2.80</td>
</tr>
<tr>
<td align="left">m_dep</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="left">mobile_wt</td>
<td align="right">0.08</td>
<td align="right">-0.08</td>
<td align="right">-4.08</td>
</tr>
<tr>
<td align="left">n_cores</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">-0.35</td>
</tr>
<tr>
<td align="left">pc</td>
<td align="right">-0.19</td>
<td align="right">0.19</td>
<td align="right">2.74</td>
</tr>
<tr>
<td align="left">px_height</td>
<td align="right">18.03</td>
<td align="right">-17.28</td>
<td align="right">231.97</td>
</tr>
<tr>
<td align="left">px_width</td>
<td align="right">8.64</td>
<td align="right">-8.28</td>
<td align="right">185.76</td>
</tr>
<tr>
<td align="left">ram</td>
<td align="right">-943.74</td>
<td align="right">904.82</td>
<td align="right">98.48</td>
</tr>
<tr>
<td align="left">sc_h</td>
<td align="right">-0.07</td>
<td align="right">0.07</td>
<td align="right">1.41</td>
</tr>
<tr>
<td align="left">sc_w</td>
<td align="right">-0.16</td>
<td align="right">0.16</td>
<td align="right">0.80</td>
</tr>
<tr>
<td align="left">talk_time</td>
<td align="right">0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.10</td>
</tr>
<tr>
<td align="left">three_g</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.37</td>
</tr>
<tr>
<td align="left">touch_screen</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">wifi</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">price_range</td>
<td align="right">-0.92</td>
<td align="right">0.88</td>
<td align="right">0.26</td>
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
<td align="left">battery_power</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">blue</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">-0.01</td>
</tr>
<tr>
<td align="left">clock_speed</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.36</td>
</tr>
<tr>
<td align="left">dual_sim</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">fc</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">0.82</td>
</tr>
<tr>
<td align="left">four_g</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.55</td>
</tr>
<tr>
<td align="left">int_memory</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">0.16</td>
</tr>
<tr>
<td align="left">m_dep</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.19</td>
</tr>
<tr>
<td align="left">mobile_wt</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">-0.12</td>
</tr>
<tr>
<td align="left">n_cores</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.15</td>
</tr>
<tr>
<td align="left">pc</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">0.46</td>
</tr>
<tr>
<td align="left">px_height</td>
<td align="right">0.04</td>
<td align="right">-0.04</td>
<td align="right">0.54</td>
</tr>
<tr>
<td align="left">px_width</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.44</td>
</tr>
<tr>
<td align="left">ram</td>
<td align="right">-0.88</td>
<td align="right">0.84</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">sc_h</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">0.34</td>
</tr>
<tr>
<td align="left">sc_w</td>
<td align="right">-0.04</td>
<td align="right">0.04</td>
<td align="right">0.19</td>
</tr>
<tr>
<td align="left">talk_time</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.02</td>
</tr>
<tr>
<td align="left">three_g</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">-0.89</td>
</tr>
<tr>
<td align="left">touch_screen</td>
<td align="right">0.03</td>
<td align="right">-0.03</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">wifi</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">price_range</td>
<td align="right">-0.83</td>
<td align="right">0.79</td>
<td align="right">0.24</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-mobile_price/figures/392b2216-a930-4eb3-ac4e-bd1fb0d59104.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-mobile_price/figures/e96c374b-07bd-4cb3-9cb8-061975dd7fe1.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature ram e no grupo 1, com valor de 904.82. A maior variação negativa foi na feature ram e no grupo 0, com o valor registrado de -943.74</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: ram<br>&emsp;Média menor que a população: price_range</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: ram<br>&emsp;Média maior que a população: price_range</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: fc<br>&emsp;Média menor que a população: four<em>g<br>&emsp;Média maior que a população: px</em>height<br>&emsp;Média menor que a população: three_g</p>
