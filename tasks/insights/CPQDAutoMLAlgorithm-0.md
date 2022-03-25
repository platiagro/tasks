<h1>CPQD AutoML Algorithm - 0</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 5000 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Time</th>
<th align="right">V1</th>
<th align="right">V2</th>
<th align="right">V3</th>
<th align="right">V4</th>
<th align="right">V5</th>
<th align="right">V6</th>
<th align="right">V7</th>
<th align="right">V8</th>
<th align="right">V9</th>
<th align="right">V10</th>
<th align="right">V11</th>
<th align="right">V12</th>
<th align="right">V13</th>
<th align="right">V14</th>
<th align="right">V15</th>
<th align="right">V16</th>
<th align="right">V17</th>
<th align="right">V18</th>
<th align="right">V19</th>
<th align="right">V20</th>
<th align="right">V21</th>
<th align="right">V22</th>
<th align="right">V23</th>
<th align="right">V24</th>
<th align="right">V25</th>
<th align="right">V26</th>
<th align="right">V27</th>
<th align="right">V28</th>
<th align="right">Amount</th>
<th align="right">Class</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
<td align="right">5000.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">2115.71</td>
<td align="right">-0.23</td>
<td align="right">0.26</td>
<td align="right">0.82</td>
<td align="right">0.02</td>
<td align="right">-0.00</td>
<td align="right">0.18</td>
<td align="right">0.04</td>
<td align="right">-0.03</td>
<td align="right">0.24</td>
<td align="right">-0.07</td>
<td align="right">0.35</td>
<td align="right">-0.29</td>
<td align="right">0.19</td>
<td align="right">0.20</td>
<td align="right">0.18</td>
<td align="right">-0.04</td>
<td align="right">0.07</td>
<td align="right">-0.17</td>
<td align="right">0.03</td>
<td align="right">0.06</td>
<td align="right">-0.02</td>
<td align="right">-0.15</td>
<td align="right">-0.04</td>
<td align="right">0.04</td>
<td align="right">0.10</td>
<td align="right">-0.05</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">63.80</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">1310.43</td>
<td align="right">1.37</td>
<td align="right">1.16</td>
<td align="right">1.01</td>
<td align="right">1.42</td>
<td align="right">1.19</td>
<td align="right">1.37</td>
<td align="right">1.06</td>
<td align="right">1.20</td>
<td align="right">0.98</td>
<td align="right">0.97</td>
<td align="right">1.07</td>
<td align="right">1.32</td>
<td align="right">1.13</td>
<td align="right">0.93</td>
<td align="right">0.90</td>
<td align="right">0.85</td>
<td align="right">0.76</td>
<td align="right">0.79</td>
<td align="right">0.79</td>
<td align="right">0.56</td>
<td align="right">0.80</td>
<td align="right">0.63</td>
<td align="right">0.37</td>
<td align="right">0.62</td>
<td align="right">0.40</td>
<td align="right">0.49</td>
<td align="right">0.33</td>
<td align="right">0.24</td>
<td align="right">197.47</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">-12.17</td>
<td align="right">-15.73</td>
<td align="right">-12.39</td>
<td align="right">-4.66</td>
<td align="right">-32.09</td>
<td align="right">-7.47</td>
<td align="right">-11.16</td>
<td align="right">-23.63</td>
<td align="right">-3.34</td>
<td align="right">-6.04</td>
<td align="right">-2.60</td>
<td align="right">-6.56</td>
<td align="right">-3.39</td>
<td align="right">-6.58</td>
<td align="right">-4.15</td>
<td align="right">-4.17</td>
<td align="right">-5.40</td>
<td align="right">-3.89</td>
<td align="right">-4.58</td>
<td align="right">-11.75</td>
<td align="right">-11.27</td>
<td align="right">-5.71</td>
<td align="right">-8.00</td>
<td align="right">-2.51</td>
<td align="right">-2.32</td>
<td align="right">-1.34</td>
<td align="right">-5.34</td>
<td align="right">-2.91</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">965.75</td>
<td align="right">-0.98</td>
<td align="right">-0.33</td>
<td align="right">0.28</td>
<td align="right">-0.92</td>
<td align="right">-0.60</td>
<td align="right">-0.70</td>
<td align="right">-0.47</td>
<td align="right">-0.19</td>
<td align="right">-0.36</td>
<td align="right">-0.57</td>
<td align="right">-0.46</td>
<td align="right">-0.76</td>
<td align="right">-0.57</td>
<td align="right">-0.26</td>
<td align="right">-0.37</td>
<td align="right">-0.59</td>
<td align="right">-0.44</td>
<td align="right">-0.62</td>
<td align="right">-0.44</td>
<td align="right">-0.13</td>
<td align="right">-0.24</td>
<td align="right">-0.59</td>
<td align="right">-0.19</td>
<td align="right">-0.34</td>
<td align="right">-0.14</td>
<td align="right">-0.42</td>
<td align="right">-0.04</td>
<td align="right">-0.02</td>
<td align="right">3.80</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">2072.50</td>
<td align="right">-0.41</td>
<td align="right">0.33</td>
<td align="right">0.85</td>
<td align="right">0.06</td>
<td align="right">-0.08</td>
<td align="right">-0.17</td>
<td align="right">0.06</td>
<td align="right">0.04</td>
<td align="right">0.23</td>
<td align="right">-0.13</td>
<td align="right">0.32</td>
<td align="right">0.08</td>
<td align="right">0.11</td>
<td align="right">0.17</td>
<td align="right">0.26</td>
<td align="right">0.00</td>
<td align="right">-0.01</td>
<td align="right">-0.13</td>
<td align="right">0.05</td>
<td align="right">0.01</td>
<td align="right">-0.09</td>
<td align="right">-0.17</td>
<td align="right">-0.05</td>
<td align="right">0.10</td>
<td align="right">0.12</td>
<td align="right">-0.09</td>
<td align="right">0.02</td>
<td align="right">0.02</td>
<td align="right">15.16</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">3243.50</td>
<td align="right">1.13</td>
<td align="right">0.90</td>
<td align="right">1.46</td>
<td align="right">0.99</td>
<td align="right">0.43</td>
<td align="right">0.58</td>
<td align="right">0.58</td>
<td align="right">0.34</td>
<td align="right">0.76</td>
<td align="right">0.29</td>
<td align="right">1.11</td>
<td align="right">0.61</td>
<td align="right">0.94</td>
<td align="right">0.67</td>
<td align="right">0.82</td>
<td align="right">0.52</td>
<td align="right">0.47</td>
<td align="right">0.30</td>
<td align="right">0.57</td>
<td align="right">0.18</td>
<td align="right">0.07</td>
<td align="right">0.28</td>
<td align="right">0.09</td>
<td align="right">0.45</td>
<td align="right">0.36</td>
<td align="right">0.25</td>
<td align="right">0.17</td>
<td align="right">0.08</td>
<td align="right">57.16</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">4563.00</td>
<td align="right">1.69</td>
<td align="right">6.22</td>
<td align="right">4.10</td>
<td align="right">6.01</td>
<td align="right">10.66</td>
<td align="right">21.39</td>
<td align="right">34.30</td>
<td align="right">3.88</td>
<td align="right">9.27</td>
<td align="right">11.94</td>
<td align="right">4.35</td>
<td align="right">3.77</td>
<td align="right">3.75</td>
<td align="right">4.20</td>
<td align="right">3.64</td>
<td align="right">4.09</td>
<td align="right">4.07</td>
<td align="right">2.95</td>
<td align="right">3.10</td>
<td align="right">7.74</td>
<td align="right">15.63</td>
<td align="right">4.39</td>
<td align="right">4.10</td>
<td align="right">3.20</td>
<td align="right">1.97</td>
<td align="right">3.46</td>
<td align="right">3.85</td>
<td align="right">4.16</td>
<td align="right">7712.43</td>
<td align="right">1.00</td>
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
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-0/figures/4817c67d-a086-4b86-8d96-649d04f4b52f.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 250 outliers neste dataset, correspondendo a uma proporção de 5.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Time</th>
<th align="right">V1</th>
<th align="right">V2</th>
<th align="right">V3</th>
<th align="right">V4</th>
<th align="right">V5</th>
<th align="right">V6</th>
<th align="right">V7</th>
<th align="right">V8</th>
<th align="right">V9</th>
<th align="right">V10</th>
<th align="right">V11</th>
<th align="right">V12</th>
<th align="right">V13</th>
<th align="right">V14</th>
<th align="right">V15</th>
<th align="right">V16</th>
<th align="right">V17</th>
<th align="right">V18</th>
<th align="right">V19</th>
<th align="right">V20</th>
<th align="right">V21</th>
<th align="right">V22</th>
<th align="right">V23</th>
<th align="right">V24</th>
<th align="right">V25</th>
<th align="right">V26</th>
<th align="right">V27</th>
<th align="right">V28</th>
<th align="right">Amount</th>
<th align="right">Class</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
<td align="right">250.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">2020.77</td>
<td align="right">-2.86</td>
<td align="right">-0.16</td>
<td align="right">0.09</td>
<td align="right">0.13</td>
<td align="right">-0.05</td>
<td align="right">0.72</td>
<td align="right">-0.11</td>
<td align="right">-1.89</td>
<td align="right">1.04</td>
<td align="right">0.84</td>
<td align="right">0.61</td>
<td align="right">-0.30</td>
<td align="right">0.26</td>
<td align="right">-0.62</td>
<td align="right">0.29</td>
<td align="right">-0.15</td>
<td align="right">0.27</td>
<td align="right">0.11</td>
<td align="right">-0.19</td>
<td align="right">0.55</td>
<td align="right">0.44</td>
<td align="right">-0.33</td>
<td align="right">0.10</td>
<td align="right">0.04</td>
<td align="right">0.08</td>
<td align="right">0.03</td>
<td align="right">0.08</td>
<td align="right">-0.11</td>
<td align="right">336.59</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">1408.43</td>
<td align="right">2.07</td>
<td align="right">3.54</td>
<td align="right">1.92</td>
<td align="right">1.98</td>
<td align="right">3.38</td>
<td align="right">2.56</td>
<td align="right">3.57</td>
<td align="right">4.24</td>
<td align="right">1.92</td>
<td align="right">2.87</td>
<td align="right">1.25</td>
<td align="right">1.53</td>
<td align="right">1.00</td>
<td align="right">1.93</td>
<td align="right">1.12</td>
<td align="right">1.11</td>
<td align="right">1.42</td>
<td align="right">1.00</td>
<td align="right">1.01</td>
<td align="right">2.09</td>
<td align="right">3.07</td>
<td align="right">1.26</td>
<td align="right">1.27</td>
<td align="right">0.70</td>
<td align="right">0.59</td>
<td align="right">0.52</td>
<td align="right">1.01</td>
<td align="right">0.82</td>
<td align="right">741.55</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">14.00</td>
<td align="right">-12.17</td>
<td align="right">-15.73</td>
<td align="right">-12.39</td>
<td align="right">-4.52</td>
<td align="right">-32.09</td>
<td align="right">-7.47</td>
<td align="right">-11.16</td>
<td align="right">-23.63</td>
<td align="right">-3.24</td>
<td align="right">-6.04</td>
<td align="right">-1.79</td>
<td align="right">-6.56</td>
<td align="right">-2.15</td>
<td align="right">-6.58</td>
<td align="right">-3.35</td>
<td align="right">-4.17</td>
<td align="right">-5.40</td>
<td align="right">-3.18</td>
<td align="right">-3.10</td>
<td align="right">-11.75</td>
<td align="right">-11.27</td>
<td align="right">-5.71</td>
<td align="right">-8.00</td>
<td align="right">-2.04</td>
<td align="right">-2.32</td>
<td align="right">-1.24</td>
<td align="right">-5.34</td>
<td align="right">-2.91</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">771.25</td>
<td align="right">-4.12</td>
<td align="right">-2.72</td>
<td align="right">-0.95</td>
<td align="right">-1.35</td>
<td align="right">-1.42</td>
<td align="right">-0.78</td>
<td align="right">-1.82</td>
<td align="right">-2.27</td>
<td align="right">-0.29</td>
<td align="right">-0.85</td>
<td align="right">-0.40</td>
<td align="right">-1.11</td>
<td align="right">-0.34</td>
<td align="right">-1.68</td>
<td align="right">-0.47</td>
<td align="right">-0.85</td>
<td align="right">-0.50</td>
<td align="right">-0.44</td>
<td align="right">-0.92</td>
<td align="right">-0.74</td>
<td align="right">-0.75</td>
<td align="right">-1.00</td>
<td align="right">-0.37</td>
<td align="right">-0.38</td>
<td align="right">-0.27</td>
<td align="right">-0.36</td>
<td align="right">-0.25</td>
<td align="right">-0.54</td>
<td align="right">3.99</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">1823.50</td>
<td align="right">-2.85</td>
<td align="right">0.92</td>
<td align="right">0.15</td>
<td align="right">-0.03</td>
<td align="right">-0.04</td>
<td align="right">0.50</td>
<td align="right">0.05</td>
<td align="right">-0.48</td>
<td align="right">0.85</td>
<td align="right">0.18</td>
<td align="right">0.65</td>
<td align="right">-0.03</td>
<td align="right">0.09</td>
<td align="right">-0.36</td>
<td align="right">0.38</td>
<td align="right">-0.07</td>
<td align="right">0.23</td>
<td align="right">0.08</td>
<td align="right">-0.25</td>
<td align="right">0.45</td>
<td align="right">-0.14</td>
<td align="right">-0.25</td>
<td align="right">0.08</td>
<td align="right">0.10</td>
<td align="right">0.10</td>
<td align="right">-0.04</td>
<td align="right">0.05</td>
<td align="right">0.01</td>
<td align="right">46.87</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">3111.00</td>
<td align="right">-1.51</td>
<td align="right">2.30</td>
<td align="right">1.43</td>
<td align="right">1.51</td>
<td align="right">1.33</td>
<td align="right">2.04</td>
<td align="right">1.40</td>
<td align="right">0.23</td>
<td align="right">2.13</td>
<td align="right">1.51</td>
<td align="right">1.47</td>
<td align="right">0.70</td>
<td align="right">0.84</td>
<td align="right">0.54</td>
<td align="right">1.03</td>
<td align="right">0.61</td>
<td align="right">1.16</td>
<td align="right">0.63</td>
<td align="right">0.50</td>
<td align="right">1.66</td>
<td align="right">0.65</td>
<td align="right">0.30</td>
<td align="right">0.67</td>
<td align="right">0.51</td>
<td align="right">0.47</td>
<td align="right">0.43</td>
<td align="right">0.46</td>
<td align="right">0.24</td>
<td align="right">354.86</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">4526.00</td>
<td align="right">1.51</td>
<td align="right">6.22</td>
<td align="right">3.77</td>
<td align="right">6.01</td>
<td align="right">10.66</td>
<td align="right">21.39</td>
<td align="right">34.30</td>
<td align="right">3.88</td>
<td align="right">9.27</td>
<td align="right">11.94</td>
<td align="right">4.35</td>
<td align="right">3.77</td>
<td align="right">3.70</td>
<td align="right">4.20</td>
<td align="right">3.64</td>
<td align="right">4.09</td>
<td align="right">4.07</td>
<td align="right">2.41</td>
<td align="right">2.86</td>
<td align="right">7.74</td>
<td align="right">15.63</td>
<td align="right">4.39</td>
<td align="right">4.10</td>
<td align="right">1.22</td>
<td align="right">1.63</td>
<td align="right">1.32</td>
<td align="right">3.85</td>
<td align="right">4.16</td>
<td align="right">7712.43</td>
<td align="right">1.00</td>
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
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-0/figures/f6624056-49ed-4f72-80a0-310c8c652f7f.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 2 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['V26', 'V28'] com uma quantidade de 2 grupos. A análise multidimensional em 2 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="right">0</td>
<td align="right">0.46</td>
<td align="right">0.54</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0.33</td>
<td align="right">0.67</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Class'] com uma quantidade de 4 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="right"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
<th align="right">3</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">0.26</td>
<td align="right">0.24</td>
<td align="right">0.26</td>
<td align="right">0.24</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0.00</td>
<td align="right">0.33</td>
<td align="right">0.67</td>
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
<th align="right">Feature Permutation 2 dim.</th>
<th align="right">Multidimensional</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">V26 - V28</td>
<td align="right">0.49</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">V18 - V23</td>
<td align="right">0.45</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">V25 - V28</td>
<td align="right">0.44</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Time - V1 - V2 - V3 - V4 - V5 - V6 - V7 - V8 - V9 - V10 - V11 - V12 - V13 - V14 - V15 - V16 - V17 - V18 - V19 - V20 - V21 - V22 - V23 - V24 - V25 - V26 - V27 - V28 - Amount - Class</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Time</td>
<td align="right">-572.49</td>
<td align="right">1773.68</td>
<td align="right">-1626.33</td>
<td align="right">621.43</td>
<td align="right">-94.94</td>
</tr>
<tr>
<td align="left">V1</td>
<td align="right">-0.24</td>
<td align="right">0.35</td>
<td align="right">0.03</td>
<td align="right">-0.12</td>
<td align="right">-2.63</td>
</tr>
<tr>
<td align="left">V2</td>
<td align="right">0.08</td>
<td align="right">-0.16</td>
<td align="right">-0.02</td>
<td align="right">0.10</td>
<td align="right">-0.42</td>
</tr>
<tr>
<td align="left">V3</td>
<td align="right">-0.01</td>
<td align="right">-0.05</td>
<td align="right">0.06</td>
<td align="right">0.00</td>
<td align="right">-0.73</td>
</tr>
<tr>
<td align="left">V4</td>
<td align="right">-0.03</td>
<td align="right">0.02</td>
<td align="right">0.24</td>
<td align="right">-0.25</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">V5</td>
<td align="right">-0.14</td>
<td align="right">0.09</td>
<td align="right">-0.03</td>
<td align="right">0.10</td>
<td align="right">-0.05</td>
</tr>
<tr>
<td align="left">V6</td>
<td align="right">-0.18</td>
<td align="right">0.38</td>
<td align="right">-0.06</td>
<td align="right">-0.11</td>
<td align="right">0.54</td>
</tr>
<tr>
<td align="left">V7</td>
<td align="right">0.10</td>
<td align="right">-0.32</td>
<td align="right">0.07</td>
<td align="right">0.14</td>
<td align="right">-0.15</td>
</tr>
<tr>
<td align="left">V8</td>
<td align="right">-0.06</td>
<td align="right">0.14</td>
<td align="right">-0.03</td>
<td align="right">-0.05</td>
<td align="right">-1.86</td>
</tr>
<tr>
<td align="left">V9</td>
<td align="right">-0.18</td>
<td align="right">0.57</td>
<td align="right">-0.24</td>
<td align="right">-0.11</td>
<td align="right">0.80</td>
</tr>
<tr>
<td align="left">V10</td>
<td align="right">0.05</td>
<td align="right">-0.05</td>
<td align="right">0.12</td>
<td align="right">-0.13</td>
<td align="right">0.90</td>
</tr>
<tr>
<td align="left">V11</td>
<td align="right">-0.25</td>
<td align="right">0.71</td>
<td align="right">-0.23</td>
<td align="right">-0.18</td>
<td align="right">0.26</td>
</tr>
<tr>
<td align="left">V12</td>
<td align="right">0.60</td>
<td align="right">-1.85</td>
<td align="right">0.54</td>
<td align="right">0.61</td>
<td align="right">-0.00</td>
</tr>
<tr>
<td align="left">V13</td>
<td align="right">-0.36</td>
<td align="right">1.10</td>
<td align="right">-0.32</td>
<td align="right">-0.37</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">V14</td>
<td align="right">-0.27</td>
<td align="right">0.97</td>
<td align="right">-0.39</td>
<td align="right">-0.25</td>
<td align="right">-0.82</td>
</tr>
<tr>
<td align="left">V15</td>
<td align="right">-0.00</td>
<td align="right">-0.32</td>
<td align="right">0.06</td>
<td align="right">0.26</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">V16</td>
<td align="right">-0.06</td>
<td align="right">0.34</td>
<td align="right">-0.09</td>
<td align="right">-0.17</td>
<td align="right">-0.12</td>
</tr>
<tr>
<td align="left">V17</td>
<td align="right">-0.18</td>
<td align="right">0.55</td>
<td align="right">-0.14</td>
<td align="right">-0.20</td>
<td align="right">0.20</td>
</tr>
<tr>
<td align="left">V18</td>
<td align="right">0.06</td>
<td align="right">-0.15</td>
<td align="right">-0.00</td>
<td align="right">0.08</td>
<td align="right">0.28</td>
</tr>
<tr>
<td align="left">V19</td>
<td align="right">0.04</td>
<td align="right">-0.00</td>
<td align="right">-0.00</td>
<td align="right">-0.04</td>
<td align="right">-0.22</td>
</tr>
<tr>
<td align="left">V20</td>
<td align="right">-0.01</td>
<td align="right">-0.00</td>
<td align="right">0.01</td>
<td align="right">0.00</td>
<td align="right">0.49</td>
</tr>
<tr>
<td align="left">V21</td>
<td align="right">0.07</td>
<td align="right">-0.11</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
<td align="right">0.46</td>
</tr>
<tr>
<td align="left">V22</td>
<td align="right">-0.02</td>
<td align="right">-0.20</td>
<td align="right">0.03</td>
<td align="right">0.19</td>
<td align="right">-0.18</td>
</tr>
<tr>
<td align="left">V23</td>
<td align="right">0.00</td>
<td align="right">0.05</td>
<td align="right">-0.00</td>
<td align="right">-0.05</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">V24</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
<td align="right">-0.04</td>
<td align="right">0.02</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">V25</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.01</td>
</tr>
<tr>
<td align="left">V26</td>
<td align="right">0.11</td>
<td align="right">-0.13</td>
<td align="right">0.08</td>
<td align="right">-0.08</td>
<td align="right">0.08</td>
</tr>
<tr>
<td align="left">V27</td>
<td align="right">0.03</td>
<td align="right">-0.02</td>
<td align="right">-0.02</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">V28</td>
<td align="right">0.01</td>
<td align="right">0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.00</td>
<td align="right">-0.12</td>
</tr>
<tr>
<td align="left">Amount</td>
<td align="right">10.38</td>
<td align="right">-4.72</td>
<td align="right">2.31</td>
<td align="right">-9.21</td>
<td align="right">272.79</td>
</tr>
<tr>
<td align="left">Class</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.01</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Time</td>
<td align="right">-0.44</td>
<td align="right">1.35</td>
<td align="right">-1.24</td>
<td align="right">0.47</td>
<td align="right">-0.07</td>
</tr>
<tr>
<td align="left">V1</td>
<td align="right">-0.17</td>
<td align="right">0.25</td>
<td align="right">0.02</td>
<td align="right">-0.09</td>
<td align="right">-1.91</td>
</tr>
<tr>
<td align="left">V2</td>
<td align="right">0.07</td>
<td align="right">-0.14</td>
<td align="right">-0.02</td>
<td align="right">0.08</td>
<td align="right">-0.36</td>
</tr>
<tr>
<td align="left">V3</td>
<td align="right">-0.01</td>
<td align="right">-0.05</td>
<td align="right">0.06</td>
<td align="right">0.00</td>
<td align="right">-0.73</td>
</tr>
<tr>
<td align="left">V4</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">0.17</td>
<td align="right">-0.18</td>
<td align="right">0.08</td>
</tr>
<tr>
<td align="left">V5</td>
<td align="right">-0.12</td>
<td align="right">0.08</td>
<td align="right">-0.02</td>
<td align="right">0.08</td>
<td align="right">-0.04</td>
</tr>
<tr>
<td align="left">V6</td>
<td align="right">-0.13</td>
<td align="right">0.28</td>
<td align="right">-0.05</td>
<td align="right">-0.08</td>
<td align="right">0.40</td>
</tr>
<tr>
<td align="left">V7</td>
<td align="right">0.10</td>
<td align="right">-0.31</td>
<td align="right">0.06</td>
<td align="right">0.13</td>
<td align="right">-0.14</td>
</tr>
<tr>
<td align="left">V8</td>
<td align="right">-0.05</td>
<td align="right">0.12</td>
<td align="right">-0.02</td>
<td align="right">-0.04</td>
<td align="right">-1.55</td>
</tr>
<tr>
<td align="left">V9</td>
<td align="right">-0.18</td>
<td align="right">0.58</td>
<td align="right">-0.25</td>
<td align="right">-0.11</td>
<td align="right">0.82</td>
</tr>
<tr>
<td align="left">V10</td>
<td align="right">0.05</td>
<td align="right">-0.05</td>
<td align="right">0.12</td>
<td align="right">-0.14</td>
<td align="right">0.93</td>
</tr>
<tr>
<td align="left">V11</td>
<td align="right">-0.23</td>
<td align="right">0.66</td>
<td align="right">-0.22</td>
<td align="right">-0.17</td>
<td align="right">0.25</td>
</tr>
<tr>
<td align="left">V12</td>
<td align="right">0.45</td>
<td align="right">-1.40</td>
<td align="right">0.41</td>
<td align="right">0.46</td>
<td align="right">-0.00</td>
</tr>
<tr>
<td align="left">V13</td>
<td align="right">-0.32</td>
<td align="right">0.98</td>
<td align="right">-0.28</td>
<td align="right">-0.32</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">V14</td>
<td align="right">-0.29</td>
<td align="right">1.04</td>
<td align="right">-0.42</td>
<td align="right">-0.27</td>
<td align="right">-0.88</td>
</tr>
<tr>
<td align="left">V15</td>
<td align="right">-0.00</td>
<td align="right">-0.35</td>
<td align="right">0.06</td>
<td align="right">0.29</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">V16</td>
<td align="right">-0.08</td>
<td align="right">0.40</td>
<td align="right">-0.10</td>
<td align="right">-0.20</td>
<td align="right">-0.14</td>
</tr>
<tr>
<td align="left">V17</td>
<td align="right">-0.24</td>
<td align="right">0.72</td>
<td align="right">-0.18</td>
<td align="right">-0.26</td>
<td align="right">0.27</td>
</tr>
<tr>
<td align="left">V18</td>
<td align="right">0.08</td>
<td align="right">-0.18</td>
<td align="right">-0.00</td>
<td align="right">0.10</td>
<td align="right">0.35</td>
</tr>
<tr>
<td align="left">V19</td>
<td align="right">0.05</td>
<td align="right">-0.00</td>
<td align="right">-0.01</td>
<td align="right">-0.05</td>
<td align="right">-0.28</td>
</tr>
<tr>
<td align="left">V20</td>
<td align="right">-0.02</td>
<td align="right">-0.00</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
<td align="right">0.88</td>
</tr>
<tr>
<td align="left">V21</td>
<td align="right">0.09</td>
<td align="right">-0.14</td>
<td align="right">0.01</td>
<td align="right">0.02</td>
<td align="right">0.58</td>
</tr>
<tr>
<td align="left">V22</td>
<td align="right">-0.03</td>
<td align="right">-0.31</td>
<td align="right">0.05</td>
<td align="right">0.30</td>
<td align="right">-0.28</td>
</tr>
<tr>
<td align="left">V23</td>
<td align="right">0.01</td>
<td align="right">0.14</td>
<td align="right">-0.01</td>
<td align="right">-0.15</td>
<td align="right">0.37</td>
</tr>
<tr>
<td align="left">V24</td>
<td align="right">0.02</td>
<td align="right">0.02</td>
<td align="right">-0.07</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">V25</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
<td align="right">-0.04</td>
<td align="right">-0.03</td>
</tr>
<tr>
<td align="left">V26</td>
<td align="right">0.22</td>
<td align="right">-0.26</td>
<td align="right">0.17</td>
<td align="right">-0.16</td>
<td align="right">0.16</td>
</tr>
<tr>
<td align="left">V27</td>
<td align="right">0.09</td>
<td align="right">-0.07</td>
<td align="right">-0.07</td>
<td align="right">0.04</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">V28</td>
<td align="right">0.04</td>
<td align="right">0.04</td>
<td align="right">-0.06</td>
<td align="right">-0.01</td>
<td align="right">-0.49</td>
</tr>
<tr>
<td align="left">Amount</td>
<td align="right">0.05</td>
<td align="right">-0.02</td>
<td align="right">0.01</td>
<td align="right">-0.05</td>
<td align="right">1.38</td>
</tr>
<tr>
<td align="left">Class</td>
<td align="right">-0.02</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
<td align="right">-0.02</td>
<td align="right">0.47</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-0/figures/0183664b-0a78-4fd5-85ef-96cdc0c77647.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-0/figures/e2a05964-baa1-47d7-9272-aee27976cefc.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Time e no grupo 1, com valor de 1773.68. A maior variação negativa foi na feature Time e no grupo 2, com o valor registrado de -1626.33</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 1: Média maior que a população: Time, Média maior que a população: V9, Média maior que a população: V11, Média menor que a população: V12, Média maior que a população: V13, Média maior que a população: V14, Média maior que a população: V17</p>
<p>Grupo 2: Média menor que a população: Time</p>
<p>Grupo outlier: Média menor que a população: V1, Média menor que a população: V3, Média menor que a população: V8, Média maior que a população: V9, Média maior que a população: V10, Média menor que a população: V14, Média maior que a população: V20, Média maior que a população: V21, Média maior que a população: Amount</p>
