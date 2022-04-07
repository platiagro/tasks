<h1>Relatorio AutoStats CPQD: Clustering - insurance</h1>
<h2>Análise Geral</h2>
<p>Uma análise geral pode gerar insighs interessantes, no ponto de vista de dados gerais do banco fornecido. Nas tabelas a seguir serão apresentados dados como média, frequencia, maior valor, etc.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">age</th>
<th align="right">bmi</th>
<th align="right">children</th>
<th align="right">charges</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">39.21</td>
<td align="right">30.66</td>
<td align="right">1.09</td>
<td align="right">13270.42</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">14.05</td>
<td align="right">6.10</td>
<td align="right">1.21</td>
<td align="right">12110.01</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">15.96</td>
<td align="right">0.00</td>
<td align="right">1121.87</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">27.00</td>
<td align="right">26.30</td>
<td align="right">0.00</td>
<td align="right">4740.29</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">39.00</td>
<td align="right">30.40</td>
<td align="right">1.00</td>
<td align="right">9382.03</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">51.00</td>
<td align="right">34.69</td>
<td align="right">2.00</td>
<td align="right">16639.91</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">64.00</td>
<td align="right">53.13</td>
<td align="right">5.00</td>
<td align="right">63770.43</td>
</tr>
</tbody>
</table><p><em>Tabela de descrição geral dos dados fornecidos.</em></p>
<p>A análise por agrupamento pode trazer insights interessantes por considerar uma variável alvo como um ponto em comum dos dados. Assim possibilitando a comparação de quais features mais caracterizam cada um dos grupos alvo.</p>
<table>
<thead>
<tr>
<th align="left">charges categorizado</th>
<th align="right">charges</th>
<th align="right">age</th>
<th align="right">bmi</th>
<th align="right">children</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(1059.225, 13651.585]</td>
<td align="right">6762.13</td>
<td align="right">38.12</td>
<td align="right">30.51</td>
<td align="right">1.06</td>
</tr>
<tr>
<td align="left">(13651.585, 26181.296]</td>
<td align="right">18993.56</td>
<td align="right">41.15</td>
<td align="right">28.26</td>
<td align="right">1.22</td>
</tr>
<tr>
<td align="left">(26181.296, 38711.006]</td>
<td align="right">33151.30</td>
<td align="right">38.16</td>
<td align="right">31.78</td>
<td align="right">0.91</td>
</tr>
<tr>
<td align="left">(38711.006, 51240.717]</td>
<td align="right">43679.52</td>
<td align="right">46.57</td>
<td align="right">36.48</td>
<td align="right">1.35</td>
</tr>
<tr>
<td align="left">(51240.717, 63770.428]</td>
<td align="right">58780.33</td>
<td align="right">45.83</td>
<td align="right">36.45</td>
<td align="right">0.67</td>
</tr>
</tbody>
</table><p><em>Tabela de agrupamento geral dos dados numéricos, por média.</em></p>
<table>
<thead>
<tr>
<th align="left">charges categorizado</th>
<th align="right">sex</th>
<th align="right">region</th>
<th align="right">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(1059.225, 13651.585]</td>
<td align="right">0.70</td>
<td align="right">0.70</td>
<td align="right">0.70</td>
</tr>
<tr>
<td align="left">(13651.585, 26181.296]</td>
<td align="right">0.16</td>
<td align="right">0.16</td>
<td align="right">0.16</td>
</tr>
<tr>
<td align="left">(26181.296, 38711.006]</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">(38711.006, 51240.717]</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">(51240.717, 63770.428]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
</tbody>
</table><p><em>Tabela de agrupamento geral dos dados categóricos, por moda.</em></p>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 1338 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">age</th>
<th align="right">bmi</th>
<th align="right">children</th>
<th align="right">charges</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
<td align="right">1338.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">39.21</td>
<td align="right">30.66</td>
<td align="right">1.09</td>
<td align="right">13270.42</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">14.05</td>
<td align="right">6.10</td>
<td align="right">1.21</td>
<td align="right">12110.01</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">15.96</td>
<td align="right">0.00</td>
<td align="right">1121.87</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">27.00</td>
<td align="right">26.30</td>
<td align="right">0.00</td>
<td align="right">4740.29</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">39.00</td>
<td align="right">30.40</td>
<td align="right">1.00</td>
<td align="right">9382.03</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">51.00</td>
<td align="right">34.69</td>
<td align="right">2.00</td>
<td align="right">16639.91</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">64.00</td>
<td align="right">53.13</td>
<td align="right">5.00</td>
<td align="right">63770.43</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">sex</th>
<th align="left">charges categorizado</th>
<th align="left">region</th>
<th align="left">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">1338</td>
<td align="left">1338</td>
<td align="left">1338</td>
<td align="left">1338</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">male</td>
<td align="left">(1059.225, 13651.585]</td>
<td align="left">southeast</td>
<td align="left">no</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">676</td>
<td align="left">934</td>
<td align="left">364</td>
<td align="left">1064</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-insurance/figures/85ffd537-1a14-4a99-8815-1eeefb911f01.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 67 outliers neste dataset, correspondendo a uma proporção de 5.01% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">age</th>
<th align="right">bmi</th>
<th align="right">children</th>
<th align="right">charges</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">67.00</td>
<td align="right">67.00</td>
<td align="right">67.00</td>
<td align="right">67.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">41.97</td>
<td align="right">35.72</td>
<td align="right">2.64</td>
<td align="right">31415.68</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">15.60</td>
<td align="right">8.21</td>
<td align="right">1.90</td>
<td align="right">19624.40</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">17.29</td>
<td align="right">0.00</td>
<td align="right">1163.46</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">28.00</td>
<td align="right">30.62</td>
<td align="right">1.00</td>
<td align="right">10537.09</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">43.00</td>
<td align="right">35.53</td>
<td align="right">3.00</td>
<td align="right">40182.25</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">58.00</td>
<td align="right">41.85</td>
<td align="right">5.00</td>
<td align="right">47433.39</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">64.00</td>
<td align="right">53.13</td>
<td align="right">5.00</td>
<td align="right">63770.43</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">sex</th>
<th align="left">charges categorizado</th>
<th align="left">region</th>
<th align="left">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">67</td>
<td align="left">67</td>
<td align="left">67</td>
<td align="left">67</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">2</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">male</td>
<td align="left">(38711.006, 51240.717]</td>
<td align="left">southeast</td>
<td align="left">yes</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">40</td>
<td align="left">30</td>
<td align="left">27</td>
<td align="left">40</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-insurance/figures/1161070e-41d3-4ad7-be9c-21f1019351f5.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['age', 'children', 'charges'] com uma quantidade de 9 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(29779.831, 39332.483]</td>
<td align="right">0.09</td>
<td align="right">0.00</td>
<td align="right">0.91</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(39332.483, 48885.136]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(20227.179, 29779.831]</td>
<td align="right">0.63</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.37</td>
</tr>
<tr>
<td align="left">(1074.111, 10674.526]</td>
<td align="right">0.00</td>
<td align="right">0.30</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.28</td>
<td align="right">0.34</td>
<td align="right">0.00</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(10674.526, 20227.179]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.37</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.44</td>
<td align="right">0.19</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['age', 'bmi', 'children', 'charges'] com uma quantidade de 10 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="left">(29779.831, 39332.483]</td>
<td align="right">0.00</td>
<td align="right">0.10</td>
<td align="right">0.90</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(39332.483, 48885.136]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(20227.179, 29779.831]</td>
<td align="right">0.00</td>
<td align="right">0.36</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.60</td>
</tr>
<tr>
<td align="left">(1074.111, 10674.526]</td>
<td align="right">0.27</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.13</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.28</td>
<td align="right">0.00</td>
<td align="right">0.31</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(10674.526, 20227.179]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.30</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.46</td>
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
<td align="left">age - children - charges</td>
<td align="right">0.56</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">age - bmi - charges</td>
<td align="right">0.56</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">bmi - children - charges</td>
<td align="right">0.55</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">age - bmi - children - charges</td>
<td align="right">nan</td>
<td align="right">0.55</td>
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
<td align="left">age</td>
<td align="right">-7.19</td>
<td align="right">14.03</td>
<td align="right">-10.51</td>
<td align="right">12.72</td>
<td align="right">-7.84</td>
<td align="right">7.29</td>
<td align="right">3.55</td>
<td align="right">16.50</td>
<td align="right">-17.52</td>
<td align="right">4.49</td>
<td align="right">2.91</td>
</tr>
<tr>
<td align="left">bmi</td>
<td align="right">-0.05</td>
<td align="right">-1.02</td>
<td align="right">2.69</td>
<td align="right">0.97</td>
<td align="right">-2.95</td>
<td align="right">4.64</td>
<td align="right">0.01</td>
<td align="right">0.31</td>
<td align="right">-0.78</td>
<td align="right">-2.79</td>
<td align="right">5.32</td>
</tr>
<tr>
<td align="left">children</td>
<td align="right">0.29</td>
<td align="right">0.10</td>
<td align="right">-0.14</td>
<td align="right">0.04</td>
<td align="right">0.10</td>
<td align="right">0.25</td>
<td align="right">0.43</td>
<td align="right">-0.16</td>
<td align="right">-0.69</td>
<td align="right">0.16</td>
<td align="right">1.63</td>
</tr>
<tr>
<td align="left">charges</td>
<td align="right">-7539.36</td>
<td align="right">15460.24</td>
<td align="right">23805.06</td>
<td align="right">-1729.32</td>
<td align="right">5916.54</td>
<td align="right">30378.88</td>
<td align="right">-4746.73</td>
<td align="right">1067.54</td>
<td align="right">-10043.12</td>
<td align="right">10371.76</td>
<td align="right">19101.77</td>
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
<td align="left">age</td>
<td align="right">-0.52</td>
<td align="right">1.01</td>
<td align="right">-0.75</td>
<td align="right">0.91</td>
<td align="right">-0.56</td>
<td align="right">0.52</td>
<td align="right">0.25</td>
<td align="right">1.18</td>
<td align="right">-1.26</td>
<td align="right">0.32</td>
<td align="right">0.21</td>
</tr>
<tr>
<td align="left">bmi</td>
<td align="right">-0.01</td>
<td align="right">-0.17</td>
<td align="right">0.46</td>
<td align="right">0.17</td>
<td align="right">-0.50</td>
<td align="right">0.79</td>
<td align="right">0.00</td>
<td align="right">0.05</td>
<td align="right">-0.13</td>
<td align="right">-0.48</td>
<td align="right">0.91</td>
</tr>
<tr>
<td align="left">children</td>
<td align="right">0.26</td>
<td align="right">0.09</td>
<td align="right">-0.13</td>
<td align="right">0.04</td>
<td align="right">0.09</td>
<td align="right">0.22</td>
<td align="right">0.39</td>
<td align="right">-0.15</td>
<td align="right">-0.63</td>
<td align="right">0.14</td>
<td align="right">1.48</td>
</tr>
<tr>
<td align="left">charges</td>
<td align="right">-0.70</td>
<td align="right">1.44</td>
<td align="right">2.21</td>
<td align="right">-0.16</td>
<td align="right">0.55</td>
<td align="right">2.82</td>
<td align="right">-0.44</td>
<td align="right">0.10</td>
<td align="right">-0.93</td>
<td align="right">0.96</td>
<td align="right">1.77</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-insurance/figures/df8e3094-e459-4457-9383-d84fc772fa4e.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-insurance/figures/45007631-3c83-4444-af6d-4c750e176c37.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature charges e no grupo 5, com valor de 30378.88. A maior variação negativa foi na feature charges e no grupo 8, com o valor registrado de -10043.12</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">sex</th>
<th align="left">charges categorizado</th>
<th align="left">region</th>
<th align="left">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">male</td>
<td align="left">(38711.006, 51240.717]</td>
<td align="left">southeast</td>
<td align="left">yes</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">44</td>
<td align="left">54</td>
<td align="left">23</td>
<td align="left">54</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.698</td>
<td align="left">1.0</td>
<td align="left">0.426</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.198</td>
<td align="left">0.954</td>
<td align="left">0.161</td>
<td align="left">0.816</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">5</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">sex</th>
<th align="left">charges categorizado</th>
<th align="left">region</th>
<th align="left">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">female</td>
<td align="left">(1059.225, 13651.585]</td>
<td align="left">southeast</td>
<td align="left">no</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">95</td>
<td align="left">87</td>
<td align="left">56</td>
<td align="left">27</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.503</td>
<td align="left">0.621</td>
<td align="left">0.28</td>
<td align="left">0.6</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.003</td>
<td align="left">-0.096</td>
<td align="left">0.015</td>
<td align="left">-0.216</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">3</td>
<td align="left">7</td>
<td align="left">0</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">sex</th>
<th align="left">charges categorizado</th>
<th align="left">region</th>
<th align="left">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">male</td>
<td align="left">(38711.006, 51240.717]</td>
<td align="left">southeast</td>
<td align="left">yes</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.193</td>
<td align="left">0.915</td>
<td align="left">0.202</td>
<td align="left">0.252</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">8</td>
<td align="left">5</td>
<td align="left">8</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">sex</th>
<th align="left">charges categorizado</th>
<th align="left">region</th>
<th align="left">smoker</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">female</td>
<td align="left">(1059.225, 13651.585]</td>
<td align="left">northwest</td>
<td align="left">yes</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.036</td>
<td align="left">0.207</td>
<td align="left">0.047</td>
<td align="left">0.077</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: age<br>&emsp;Média menor que a população: charges<br>&emsp;Presença maior de população na feature charges categorizado: (1059.225, 13651.585]<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: age<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature charges categorizado: (26181.296, 38711.006]</p>
<p>Grupo 2: <br>&emsp;Média menor que a população: age<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature sex: male<br>&emsp;Presença maior de população na feature charges categorizado: (26181.296, 38711.006]<br>&emsp;Presença maior de população na feature smoker: yes</p>
<p>Grupo 3: <br>&emsp;Média maior que a população: age<br>&emsp;Presença maior de população na feature charges categorizado: (1059.225, 13651.585]<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 4: <br>&emsp;Média menor que a população: age<br>&emsp;Média menor que a população: bmi<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature charges categorizado: (13651.585, 26181.296]<br>&emsp;Presença maior de população na feature smoker: yes</p>
<p>Grupo 5: <br>&emsp;Média maior que a população: age<br>&emsp;Média maior que a população: bmi<br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature charges categorizado: (38711.006, 51240.717]<br>&emsp;Presença maior de população na feature region: southeast<br>&emsp;Presença maior de população na feature smoker: yes</p>
<p>Grupo 6: <br>&emsp;Presença maior de população na feature charges categorizado: (1059.225, 13651.585]<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 7: <br>&emsp;Média maior que a população: age<br>&emsp;Presença maior de população na feature sex: female<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 8: <br>&emsp;Média menor que a população: age<br>&emsp;Média menor que a população: children<br>&emsp;Média menor que a população: charges<br>&emsp;Presença maior de população na feature charges categorizado: (1059.225, 13651.585]<br>&emsp;Presença maior de população na feature smoker: no</p>
<p>Grupo 9: <br>&emsp;Média maior que a população: charges<br>&emsp;Presença maior de população na feature charges categorizado: (13651.585, 26181.296]<br>&emsp;Presença maior de população na feature smoker: yes</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: bmi<br>&emsp;Média maior que a população: children<br>&emsp;Média maior que a população: charges</p>
