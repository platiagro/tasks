<h1>Relatorio AutoStats CPQD: Clustering - HousingData</h1>
<h2>Análise Geral</h2>
<p>Uma análise geral pode gerar insighs interessantes, no ponto de vista de dados gerais do banco fornecido. Nas tabelas a seguir serão apresentados dados como média, frequencia, maior valor, etc.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">CRIM</th>
<th align="right">ZN</th>
<th align="right">INDUS</th>
<th align="right">CHAS</th>
<th align="right">NOX</th>
<th align="right">RM</th>
<th align="right">AGE</th>
<th align="right">DIS</th>
<th align="right">RAD</th>
<th align="right">TAX</th>
<th align="right">PTRATIO</th>
<th align="right">B</th>
<th align="right">LSTAT</th>
<th align="right">MEDV</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">3.69</td>
<td align="right">11.46</td>
<td align="right">11.00</td>
<td align="right">0.07</td>
<td align="right">0.55</td>
<td align="right">6.28</td>
<td align="right">68.93</td>
<td align="right">3.81</td>
<td align="right">9.40</td>
<td align="right">406.43</td>
<td align="right">18.54</td>
<td align="right">358.49</td>
<td align="right">12.77</td>
<td align="right">22.36</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">9.20</td>
<td align="right">23.95</td>
<td align="right">6.91</td>
<td align="right">0.25</td>
<td align="right">0.11</td>
<td align="right">0.70</td>
<td align="right">27.89</td>
<td align="right">2.10</td>
<td align="right">8.63</td>
<td align="right">168.31</td>
<td align="right">2.17</td>
<td align="right">89.28</td>
<td align="right">7.31</td>
<td align="right">9.14</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.46</td>
<td align="right">0.00</td>
<td align="right">0.39</td>
<td align="right">3.56</td>
<td align="right">2.90</td>
<td align="right">1.13</td>
<td align="right">1.00</td>
<td align="right">187.00</td>
<td align="right">12.60</td>
<td align="right">2.60</td>
<td align="right">1.73</td>
<td align="right">5.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.08</td>
<td align="right">0.00</td>
<td align="right">5.13</td>
<td align="right">0.00</td>
<td align="right">0.45</td>
<td align="right">5.88</td>
<td align="right">45.48</td>
<td align="right">2.11</td>
<td align="right">4.00</td>
<td align="right">280.25</td>
<td align="right">17.40</td>
<td align="right">376.71</td>
<td align="right">7.12</td>
<td align="right">16.80</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">0.27</td>
<td align="right">0.00</td>
<td align="right">8.56</td>
<td align="right">0.00</td>
<td align="right">0.54</td>
<td align="right">6.20</td>
<td align="right">77.70</td>
<td align="right">3.20</td>
<td align="right">5.00</td>
<td align="right">330.00</td>
<td align="right">19.10</td>
<td align="right">392.19</td>
<td align="right">11.30</td>
<td align="right">21.05</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">3.44</td>
<td align="right">12.50</td>
<td align="right">18.10</td>
<td align="right">0.00</td>
<td align="right">0.62</td>
<td align="right">6.61</td>
<td align="right">94.25</td>
<td align="right">5.12</td>
<td align="right">24.00</td>
<td align="right">666.00</td>
<td align="right">20.20</td>
<td align="right">396.90</td>
<td align="right">17.12</td>
<td align="right">25.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">88.98</td>
<td align="right">100.00</td>
<td align="right">27.74</td>
<td align="right">1.00</td>
<td align="right">0.87</td>
<td align="right">8.78</td>
<td align="right">100.00</td>
<td align="right">12.13</td>
<td align="right">24.00</td>
<td align="right">711.00</td>
<td align="right">22.00</td>
<td align="right">396.90</td>
<td align="right">37.97</td>
<td align="right">50.00</td>
</tr>
</tbody>
</table><p><em>Tabela de descrição geral dos dados fornecidos.</em></p>
<p>A análise por agrupamento pode trazer insights interessantes por considerar uma variável alvo como um ponto em comum dos dados. Assim possibilitando a comparação de quais features mais caracterizam cada um dos grupos alvo.</p>
<table>
<thead>
<tr>
<th align="left">MEDV categorizado</th>
<th align="right">RM</th>
<th align="right">TAX</th>
<th align="right">CRIM</th>
<th align="right">CHAS</th>
<th align="right">DIS</th>
<th align="right">ZN</th>
<th align="right">PTRATIO</th>
<th align="right">LSTAT</th>
<th align="right">INDUS</th>
<th align="right">B</th>
<th align="right">MEDV</th>
<th align="right">AGE</th>
<th align="right">RAD</th>
<th align="right">NOX</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(4.955, 14.0]</td>
<td align="right">5.80</td>
<td align="right">612.77</td>
<td align="right">15.10</td>
<td align="right">0.02</td>
<td align="right">1.97</td>
<td align="right">0.00</td>
<td align="right">19.93</td>
<td align="right">23.83</td>
<td align="right">17.76</td>
<td align="right">270.41</td>
<td align="right">10.81</td>
<td align="right">94.45</td>
<td align="right">19.55</td>
<td align="right">0.68</td>
</tr>
<tr>
<td align="left">(14.0, 23.0]</td>
<td align="right">6.03</td>
<td align="right">412.98</td>
<td align="right">2.35</td>
<td align="right">0.07</td>
<td align="right">3.74</td>
<td align="right">5.06</td>
<td align="right">19.16</td>
<td align="right">13.66</td>
<td align="right">12.27</td>
<td align="right">365.63</td>
<td align="right">19.20</td>
<td align="right">73.20</td>
<td align="right">9.03</td>
<td align="right">0.56</td>
</tr>
<tr>
<td align="left">(23.0, 32.0]</td>
<td align="right">6.47</td>
<td align="right">319.90</td>
<td align="right">0.49</td>
<td align="right">0.06</td>
<td align="right">4.84</td>
<td align="right">19.76</td>
<td align="right">17.61</td>
<td align="right">8.06</td>
<td align="right">7.32</td>
<td align="right">384.92</td>
<td align="right">26.17</td>
<td align="right">51.39</td>
<td align="right">5.80</td>
<td align="right">0.49</td>
</tr>
<tr>
<td align="left">(32.0, 41.0]</td>
<td align="right">7.18</td>
<td align="right">264.57</td>
<td align="right">0.12</td>
<td align="right">0.11</td>
<td align="right">4.85</td>
<td align="right">35.48</td>
<td align="right">16.79</td>
<td align="right">5.79</td>
<td align="right">3.23</td>
<td align="right">393.29</td>
<td align="right">35.09</td>
<td align="right">50.60</td>
<td align="right">3.61</td>
<td align="right">0.47</td>
</tr>
<tr>
<td align="left">(41.0, 50.0]</td>
<td align="right">7.74</td>
<td align="right">335.43</td>
<td align="right">1.47</td>
<td align="right">0.22</td>
<td align="right">3.70</td>
<td align="right">29.33</td>
<td align="right">15.82</td>
<td align="right">4.17</td>
<td align="right">7.64</td>
<td align="right">385.00</td>
<td align="right">47.21</td>
<td align="right">62.35</td>
<td align="right">7.30</td>
<td align="right">0.52</td>
</tr>
</tbody>
</table><p><em>Tabela de agrupamento geral dos dados numéricos, por média.</em></p>
<table>
<thead>
<tr>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(4.955, 14.0]</td>
</tr>
<tr>
<td align="left">(14.0, 23.0]</td>
</tr>
<tr>
<td align="left">(23.0, 32.0]</td>
</tr>
<tr>
<td align="left">(32.0, 41.0]</td>
</tr>
<tr>
<td align="left">(41.0, 50.0]</td>
</tr>
</tbody>
</table><p><em>Tabela de agrupamento geral dos dados categóricos, por moda.</em></p>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 394 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">CRIM</th>
<th align="right">ZN</th>
<th align="right">INDUS</th>
<th align="right">CHAS</th>
<th align="right">NOX</th>
<th align="right">RM</th>
<th align="right">AGE</th>
<th align="right">DIS</th>
<th align="right">RAD</th>
<th align="right">TAX</th>
<th align="right">PTRATIO</th>
<th align="right">B</th>
<th align="right">LSTAT</th>
<th align="right">MEDV</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
<td align="right">394.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">3.69</td>
<td align="right">11.46</td>
<td align="right">11.00</td>
<td align="right">0.07</td>
<td align="right">0.55</td>
<td align="right">6.28</td>
<td align="right">68.93</td>
<td align="right">3.81</td>
<td align="right">9.40</td>
<td align="right">406.43</td>
<td align="right">18.54</td>
<td align="right">358.49</td>
<td align="right">12.77</td>
<td align="right">22.36</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">9.20</td>
<td align="right">23.95</td>
<td align="right">6.91</td>
<td align="right">0.25</td>
<td align="right">0.11</td>
<td align="right">0.70</td>
<td align="right">27.89</td>
<td align="right">2.10</td>
<td align="right">8.63</td>
<td align="right">168.31</td>
<td align="right">2.17</td>
<td align="right">89.28</td>
<td align="right">7.31</td>
<td align="right">9.14</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.46</td>
<td align="right">0.00</td>
<td align="right">0.39</td>
<td align="right">3.56</td>
<td align="right">2.90</td>
<td align="right">1.13</td>
<td align="right">1.00</td>
<td align="right">187.00</td>
<td align="right">12.60</td>
<td align="right">2.60</td>
<td align="right">1.73</td>
<td align="right">5.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.08</td>
<td align="right">0.00</td>
<td align="right">5.13</td>
<td align="right">0.00</td>
<td align="right">0.45</td>
<td align="right">5.88</td>
<td align="right">45.48</td>
<td align="right">2.11</td>
<td align="right">4.00</td>
<td align="right">280.25</td>
<td align="right">17.40</td>
<td align="right">376.71</td>
<td align="right">7.12</td>
<td align="right">16.80</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">0.27</td>
<td align="right">0.00</td>
<td align="right">8.56</td>
<td align="right">0.00</td>
<td align="right">0.54</td>
<td align="right">6.20</td>
<td align="right">77.70</td>
<td align="right">3.20</td>
<td align="right">5.00</td>
<td align="right">330.00</td>
<td align="right">19.10</td>
<td align="right">392.19</td>
<td align="right">11.30</td>
<td align="right">21.05</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">3.44</td>
<td align="right">12.50</td>
<td align="right">18.10</td>
<td align="right">0.00</td>
<td align="right">0.62</td>
<td align="right">6.61</td>
<td align="right">94.25</td>
<td align="right">5.12</td>
<td align="right">24.00</td>
<td align="right">666.00</td>
<td align="right">20.20</td>
<td align="right">396.90</td>
<td align="right">17.12</td>
<td align="right">25.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">88.98</td>
<td align="right">100.00</td>
<td align="right">27.74</td>
<td align="right">1.00</td>
<td align="right">0.87</td>
<td align="right">8.78</td>
<td align="right">100.00</td>
<td align="right">12.13</td>
<td align="right">24.00</td>
<td align="right">711.00</td>
<td align="right">22.00</td>
<td align="right">396.90</td>
<td align="right">37.97</td>
<td align="right">50.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">394</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">5</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">(14.0, 23.0]</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">184</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-HousingData/figures/ab72d199-7f04-4a5f-aba0-c42e487d6771.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 20 outliers neste dataset, correspondendo a uma proporção de 5.08% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">CRIM</th>
<th align="right">ZN</th>
<th align="right">INDUS</th>
<th align="right">CHAS</th>
<th align="right">NOX</th>
<th align="right">RM</th>
<th align="right">AGE</th>
<th align="right">DIS</th>
<th align="right">RAD</th>
<th align="right">TAX</th>
<th align="right">PTRATIO</th>
<th align="right">B</th>
<th align="right">LSTAT</th>
<th align="right">MEDV</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
<td align="right">20.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">11.35</td>
<td align="right">11.60</td>
<td align="right">15.39</td>
<td align="right">0.40</td>
<td align="right">0.67</td>
<td align="right">6.35</td>
<td align="right">82.28</td>
<td align="right">2.80</td>
<td align="right">11.45</td>
<td align="right">476.80</td>
<td align="right">17.35</td>
<td align="right">282.69</td>
<td align="right">15.76</td>
<td align="right">26.02</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">20.60</td>
<td align="right">26.25</td>
<td align="right">7.53</td>
<td align="right">0.50</td>
<td align="right">0.16</td>
<td align="right">1.38</td>
<td align="right">29.95</td>
<td align="right">2.70</td>
<td align="right">9.51</td>
<td align="right">174.19</td>
<td align="right">3.05</td>
<td align="right">150.81</td>
<td align="right">12.07</td>
<td align="right">17.27</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.02</td>
<td align="right">0.00</td>
<td align="right">1.21</td>
<td align="right">0.00</td>
<td align="right">0.40</td>
<td align="right">4.52</td>
<td align="right">8.40</td>
<td align="right">1.13</td>
<td align="right">1.00</td>
<td align="right">198.00</td>
<td align="right">13.00</td>
<td align="right">2.60</td>
<td align="right">1.92</td>
<td align="right">7.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">0.55</td>
<td align="right">0.00</td>
<td align="right">15.04</td>
<td align="right">0.00</td>
<td align="right">0.60</td>
<td align="right">5.37</td>
<td align="right">85.90</td>
<td align="right">1.41</td>
<td align="right">5.00</td>
<td align="right">385.75</td>
<td align="right">14.70</td>
<td align="right">151.84</td>
<td align="right">4.72</td>
<td align="right">13.32</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">2.61</td>
<td align="right">0.00</td>
<td align="right">18.10</td>
<td align="right">0.00</td>
<td align="right">0.66</td>
<td align="right">5.92</td>
<td align="right">97.65</td>
<td align="right">1.74</td>
<td align="right">5.00</td>
<td align="right">403.00</td>
<td align="right">17.00</td>
<td align="right">365.81</td>
<td align="right">12.61</td>
<td align="right">17.45</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">6.97</td>
<td align="right">5.00</td>
<td align="right">19.58</td>
<td align="right">1.00</td>
<td align="right">0.87</td>
<td align="right">7.68</td>
<td align="right">100.00</td>
<td align="right">1.94</td>
<td align="right">24.00</td>
<td align="right">666.00</td>
<td align="right">20.20</td>
<td align="right">392.92</td>
<td align="right">27.07</td>
<td align="right">47.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">73.53</td>
<td align="right">90.00</td>
<td align="right">27.74</td>
<td align="right">1.00</td>
<td align="right">0.87</td>
<td align="right">8.78</td>
<td align="right">100.00</td>
<td align="right">10.59</td>
<td align="right">24.00</td>
<td align="right">711.00</td>
<td align="right">22.00</td>
<td align="right">396.90</td>
<td align="right">36.98</td>
<td align="right">50.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">20</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">(4.955, 14.0]</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">7</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-HousingData/figures/929fc3db-ed2a-46f4-8b5c-97e6752d3d4b.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['ZN', 'NOX', 'RM'] com uma quantidade de 10 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">(32.0, 41.0]</td>
<td align="right">0.29</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">0.14</td>
<td align="right">0.00</td>
<td align="right">0.14</td>
<td align="right">0.21</td>
<td align="right">0.00</td>
<td align="right">0.07</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">(14.0, 23.0]</td>
<td align="right">0.85</td>
<td align="right">0.01</td>
<td align="right">0.03</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.03</td>
<td align="right">0.04</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">(41.0, 50.0]</td>
<td align="right">0.44</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.19</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.12</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(23.0, 32.0]</td>
<td align="right">0.57</td>
<td align="right">0.03</td>
<td align="right">0.06</td>
<td align="right">0.04</td>
<td align="right">0.05</td>
<td align="right">0.02</td>
<td align="right">0.11</td>
<td align="right">0.01</td>
<td align="right">0.07</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(4.955, 14.0]</td>
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
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'] com uma quantidade de 5 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(32.0, 41.0]</td>
<td align="right">0.00</td>
<td align="right">0.29</td>
<td align="right">0.00</td>
<td align="right">0.14</td>
<td align="right">0.57</td>
</tr>
<tr>
<td align="left">(14.0, 23.0]</td>
<td align="right">0.20</td>
<td align="right">0.37</td>
<td align="right">0.04</td>
<td align="right">0.26</td>
<td align="right">0.13</td>
</tr>
<tr>
<td align="left">(41.0, 50.0]</td>
<td align="right">0.06</td>
<td align="right">0.44</td>
<td align="right">0.00</td>
<td align="right">0.12</td>
<td align="right">0.38</td>
</tr>
<tr>
<td align="left">(23.0, 32.0]</td>
<td align="right">0.05</td>
<td align="right">0.64</td>
<td align="right">0.00</td>
<td align="right">0.13</td>
<td align="right">0.18</td>
</tr>
<tr>
<td align="left">(4.955, 14.0]</td>
<td align="right">0.60</td>
<td align="right">0.11</td>
<td align="right">0.27</td>
<td align="right">0.02</td>
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
<td align="left">ZN - NOX - RM</td>
<td align="right">0.88</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">CRIM - INDUS - RM</td>
<td align="right">0.65</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">RM - B - LSTAT</td>
<td align="right">0.48</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">CRIM - ZN - INDUS - CHAS - NOX - RM - AGE - DIS - RAD - TAX - PTRATIO - B - LSTAT - MEDV</td>
<td align="right">nan</td>
<td align="right">0.47</td>
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
<td align="left">CRIM</td>
<td align="right">8.21</td>
<td align="right">-2.95</td>
<td align="right">8.45</td>
<td align="right">-2.66</td>
<td align="right">-3.20</td>
<td align="right">8.07</td>
</tr>
<tr>
<td align="left">ZN</td>
<td align="right">-11.45</td>
<td align="right">3.38</td>
<td align="right">-11.45</td>
<td align="right">-2.06</td>
<td align="right">12.23</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">INDUS</td>
<td align="right">7.85</td>
<td align="right">-4.06</td>
<td align="right">6.92</td>
<td align="right">2.13</td>
<td align="right">-4.62</td>
<td align="right">4.62</td>
</tr>
<tr>
<td align="left">CHAS</td>
<td align="right">0.00</td>
<td align="right">0.02</td>
<td align="right">-0.05</td>
<td align="right">-0.04</td>
<td align="right">0.01</td>
<td align="right">0.35</td>
</tr>
<tr>
<td align="left">NOX</td>
<td align="right">0.12</td>
<td align="right">-0.06</td>
<td align="right">0.13</td>
<td align="right">0.02</td>
<td align="right">-0.08</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">RM</td>
<td align="right">-0.39</td>
<td align="right">0.10</td>
<td align="right">-0.02</td>
<td align="right">-0.07</td>
<td align="right">0.31</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">AGE</td>
<td align="right">21.18</td>
<td align="right">-9.15</td>
<td align="right">21.23</td>
<td align="right">6.43</td>
<td align="right">-18.49</td>
<td align="right">14.07</td>
</tr>
<tr>
<td align="left">DIS</td>
<td align="right">-1.72</td>
<td align="right">1.00</td>
<td align="right">-1.78</td>
<td align="right">-0.64</td>
<td align="right">1.05</td>
<td align="right">-1.06</td>
</tr>
<tr>
<td align="left">RAD</td>
<td align="right">13.64</td>
<td align="right">-4.71</td>
<td align="right">13.88</td>
<td align="right">-4.51</td>
<td align="right">-5.62</td>
<td align="right">2.16</td>
</tr>
<tr>
<td align="left">TAX</td>
<td align="right">265.73</td>
<td align="right">-102.69</td>
<td align="right">251.07</td>
<td align="right">6.39</td>
<td align="right">-176.27</td>
<td align="right">74.13</td>
</tr>
<tr>
<td align="left">PTRATIO</td>
<td align="right">1.59</td>
<td align="right">-0.65</td>
<td align="right">1.63</td>
<td align="right">-0.32</td>
<td align="right">-0.65</td>
<td align="right">-1.25</td>
</tr>
<tr>
<td align="left">B</td>
<td align="right">11.15</td>
<td align="right">22.53</td>
<td align="right">-303.42</td>
<td align="right">14.47</td>
<td align="right">29.88</td>
<td align="right">-79.85</td>
</tr>
<tr>
<td align="left">LSTAT</td>
<td align="right">6.14</td>
<td align="right">-2.43</td>
<td align="right">8.30</td>
<td align="right">-0.26</td>
<td align="right">-4.43</td>
<td align="right">3.16</td>
</tr>
<tr>
<td align="left">MEDV</td>
<td align="right">-6.25</td>
<td align="right">1.90</td>
<td align="right">-9.99</td>
<td align="right">0.08</td>
<td align="right">6.64</td>
<td align="right">3.86</td>
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
<td align="left">CRIM</td>
<td align="right">1.03</td>
<td align="right">-0.37</td>
<td align="right">1.06</td>
<td align="right">-0.33</td>
<td align="right">-0.40</td>
<td align="right">1.01</td>
</tr>
<tr>
<td align="left">ZN</td>
<td align="right">-0.48</td>
<td align="right">0.14</td>
<td align="right">-0.48</td>
<td align="right">-0.09</td>
<td align="right">0.51</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">INDUS</td>
<td align="right">1.15</td>
<td align="right">-0.60</td>
<td align="right">1.02</td>
<td align="right">0.31</td>
<td align="right">-0.68</td>
<td align="right">0.68</td>
</tr>
<tr>
<td align="left">CHAS</td>
<td align="right">0.01</td>
<td align="right">0.08</td>
<td align="right">-0.23</td>
<td align="right">-0.16</td>
<td align="right">0.06</td>
<td align="right">1.59</td>
</tr>
<tr>
<td align="left">NOX</td>
<td align="right">1.15</td>
<td align="right">-0.53</td>
<td align="right">1.21</td>
<td align="right">0.16</td>
<td align="right">-0.74</td>
<td align="right">1.13</td>
</tr>
<tr>
<td align="left">RM</td>
<td align="right">-0.60</td>
<td align="right">0.15</td>
<td align="right">-0.03</td>
<td align="right">-0.10</td>
<td align="right">0.48</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">AGE</td>
<td align="right">0.77</td>
<td align="right">-0.33</td>
<td align="right">0.77</td>
<td align="right">0.23</td>
<td align="right">-0.67</td>
<td align="right">0.51</td>
</tr>
<tr>
<td align="left">DIS</td>
<td align="right">-0.84</td>
<td align="right">0.49</td>
<td align="right">-0.87</td>
<td align="right">-0.31</td>
<td align="right">0.51</td>
<td align="right">-0.52</td>
</tr>
<tr>
<td align="left">RAD</td>
<td align="right">1.59</td>
<td align="right">-0.55</td>
<td align="right">1.62</td>
<td align="right">-0.53</td>
<td align="right">-0.66</td>
<td align="right">0.25</td>
</tr>
<tr>
<td align="left">TAX</td>
<td align="right">1.59</td>
<td align="right">-0.61</td>
<td align="right">1.50</td>
<td align="right">0.04</td>
<td align="right">-1.05</td>
<td align="right">0.44</td>
</tr>
<tr>
<td align="left">PTRATIO</td>
<td align="right">0.76</td>
<td align="right">-0.31</td>
<td align="right">0.78</td>
<td align="right">-0.15</td>
<td align="right">-0.31</td>
<td align="right">-0.60</td>
</tr>
<tr>
<td align="left">B</td>
<td align="right">0.13</td>
<td align="right">0.27</td>
<td align="right">-3.65</td>
<td align="right">0.17</td>
<td align="right">0.36</td>
<td align="right">-0.96</td>
</tr>
<tr>
<td align="left">LSTAT</td>
<td align="right">0.88</td>
<td align="right">-0.35</td>
<td align="right">1.20</td>
<td align="right">-0.04</td>
<td align="right">-0.64</td>
<td align="right">0.45</td>
</tr>
<tr>
<td align="left">MEDV</td>
<td align="right">-0.74</td>
<td align="right">0.22</td>
<td align="right">-1.18</td>
<td align="right">0.01</td>
<td align="right">0.78</td>
<td align="right">0.45</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-HousingData/figures/9fb7b22c-e295-455c-9642-ec93106e1e52.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-HousingData/figures/28785e54-b767-4089-959f-484239eae720.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature TAX e no grupo 0, com valor de 265.73. A maior variação negativa foi na feature B e no grupo 2, com o valor registrado de -303.42</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">(4.955, 14.0]</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">15</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.652</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.505</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">(14.0, 23.0]</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">23</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.371</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.105</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">(23.0, 32.0]</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.639</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">MEDV categorizado</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">(14.0, 23.0]</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.258</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: CRIM<br>&emsp;Média maior que a população: INDUS<br>&emsp;Média maior que a população: NOX<br>&emsp;Média menor que a população: RM<br>&emsp;Média maior que a população: AGE<br>&emsp;Média menor que a população: DIS<br>&emsp;Média maior que a população: RAD<br>&emsp;Média maior que a população: TAX<br>&emsp;Média maior que a população: PTRATIO<br>&emsp;Média maior que a população: LSTAT<br>&emsp;Média menor que a população: MEDV</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: INDUS<br>&emsp;Média menor que a população: NOX<br>&emsp;Média menor que a população: RAD<br>&emsp;Média menor que a população: TAX</p>
<p>Grupo 2: <br>&emsp;Média maior que a população: CRIM<br>&emsp;Média maior que a população: INDUS<br>&emsp;Média maior que a população: NOX<br>&emsp;Média maior que a população: AGE<br>&emsp;Média menor que a população: DIS<br>&emsp;Média maior que a população: RAD<br>&emsp;Média maior que a população: TAX<br>&emsp;Média maior que a população: PTRATIO<br>&emsp;Média menor que a população: B<br>&emsp;Média maior que a população: LSTAT<br>&emsp;Média menor que a população: MEDV<br>&emsp;Presença maior de população na feature MEDV categorizado: (4.955, 14.0]</p>
<p>Grupo 3: <br>&emsp;Média menor que a população: RAD<br>&emsp;Presença maior de população na feature MEDV categorizado: (14.0, 23.0]</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: ZN<br>&emsp;Média menor que a população: INDUS<br>&emsp;Média menor que a população: NOX<br>&emsp;Média menor que a população: AGE<br>&emsp;Média maior que a população: DIS<br>&emsp;Média menor que a população: RAD<br>&emsp;Média menor que a população: TAX<br>&emsp;Média menor que a população: LSTAT<br>&emsp;Média maior que a população: MEDV</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: CRIM<br>&emsp;Média maior que a população: INDUS<br>&emsp;Média maior que a população: CHAS<br>&emsp;Média maior que a população: NOX<br>&emsp;Média maior que a população: AGE<br>&emsp;Média menor que a população: DIS<br>&emsp;Média menor que a população: PTRATIO<br>&emsp;Média menor que a população: B</p>
