<h1>CPQD AutoML Algorithm - titanic</h1>
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
<th align="left">Embarked</th>
<th align="left">Sex</th>
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
<td align="left">3</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">S</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">344</td>
<td align="left">261</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-titanic/figures/6b80141a-3254-4f20-bdad-0028470a52a0.png" alt="Visualização dos outliers: DBscan" /></p>

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
<td align="right">0.44</td>
<td align="right">2.00</td>
<td align="right">28.41</td>
<td align="right">1.75</td>
<td align="right">2.56</td>
<td align="right">141.22</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">0.50</td>
<td align="right">0.99</td>
<td align="right">17.85</td>
<td align="right">1.79</td>
<td align="right">1.48</td>
<td align="right">147.45</td>
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
<td align="right">16.75</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">31.36</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">24.50</td>
<td align="right">1.00</td>
<td align="right">2.00</td>
<td align="right">46.90</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">39.00</td>
<td align="right">3.00</td>
<td align="right">3.25</td>
<td align="right">251.23</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">70.00</td>
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
<th align="left">Embarked</th>
<th align="left">Sex</th>
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
<td align="left">3</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">S</td>
<td align="left">female</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">25</td>
<td align="left">21</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-titanic/figures/b727bd54-a623-41f6-a605-77d22dae8ac5.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Pclass', 'SibSp', 'Fare'] com uma quantidade de 9 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="right">1</td>
<td align="right">0.22</td>
<td align="right">0.04</td>
<td align="right">0.10</td>
<td align="right">0.02</td>
<td align="right">0.12</td>
<td align="right">0.20</td>
<td align="right">0.04</td>
<td align="right">0.21</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="right">0</td>
<td align="right">0.52</td>
<td align="right">0.01</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">0.03</td>
<td align="right">0.15</td>
<td align="right">0.00</td>
<td align="right">0.19</td>
<td align="right">0.05</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'] com uma quantidade de 9 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="right">1</td>
<td align="right">0.12</td>
<td align="right">0.12</td>
<td align="right">0.02</td>
<td align="right">0.20</td>
<td align="right">0.11</td>
<td align="right">0.07</td>
<td align="right">0.05</td>
<td align="right">0.15</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="right">0</td>
<td align="right">0.25</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">0.38</td>
<td align="right">0.03</td>
<td align="right">0.01</td>
<td align="right">0.10</td>
<td align="right">0.08</td>
<td align="right">0.11</td>
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
<td align="left">Pclass - SibSp - Fare</td>
<td align="right">0.65</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Survived - Pclass - Fare</td>
<td align="right">0.65</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Survived - Age - Parch</td>
<td align="right">0.52</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Survived - Pclass - Age - SibSp - Parch - Fare</td>
<td align="right">nan</td>
<td align="right">0.42</td>
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
<td align="left">Survived</td>
<td align="right">-0.16</td>
<td align="right">0.29</td>
<td align="right">0.60</td>
<td align="right">-0.14</td>
<td align="right">0.28</td>
<td align="right">0.43</td>
<td align="right">-0.15</td>
<td align="right">0.17</td>
<td align="right">0.07</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">Pclass</td>
<td align="right">0.43</td>
<td align="right">-1.15</td>
<td align="right">-1.25</td>
<td align="right">0.56</td>
<td align="right">-1.03</td>
<td align="right">-1.25</td>
<td align="right">-0.45</td>
<td align="right">0.34</td>
<td align="right">-0.40</td>
<td align="right">-0.25</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="right">5.75</td>
<td align="right">6.50</td>
<td align="right">1.13</td>
<td align="right">-7.87</td>
<td align="right">5.36</td>
<td align="right">3.92</td>
<td align="right">27.33</td>
<td align="right">-22.80</td>
<td align="right">4.39</td>
<td align="right">-1.29</td>
</tr>
<tr>
<td align="left">SibSp</td>
<td align="right">-0.31</td>
<td align="right">0.22</td>
<td align="right">-0.28</td>
<td align="right">-0.25</td>
<td align="right">0.14</td>
<td align="right">0.14</td>
<td align="right">-0.39</td>
<td align="right">1.13</td>
<td align="right">0.16</td>
<td align="right">1.30</td>
</tr>
<tr>
<td align="left">Parch</td>
<td align="right">-0.24</td>
<td align="right">-0.03</td>
<td align="right">0.01</td>
<td align="right">-0.23</td>
<td align="right">-0.00</td>
<td align="right">0.43</td>
<td align="right">-0.28</td>
<td align="right">0.93</td>
<td align="right">0.21</td>
<td align="right">2.24</td>
</tr>
<tr>
<td align="left">Fare</td>
<td align="right">-19.24</td>
<td align="right">53.23</td>
<td align="right">190.54</td>
<td align="right">-19.27</td>
<td align="right">27.57</td>
<td align="right">102.56</td>
<td align="right">-8.94</td>
<td align="right">-3.23</td>
<td align="right">-1.35</td>
<td align="right">112.34</td>
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
<td align="left">Survived</td>
<td align="right">-0.33</td>
<td align="right">0.58</td>
<td align="right">1.22</td>
<td align="right">-0.29</td>
<td align="right">0.57</td>
<td align="right">0.88</td>
<td align="right">-0.30</td>
<td align="right">0.35</td>
<td align="right">0.14</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">Pclass</td>
<td align="right">0.52</td>
<td align="right">-1.39</td>
<td align="right">-1.52</td>
<td align="right">0.68</td>
<td align="right">-1.24</td>
<td align="right">-1.52</td>
<td align="right">-0.55</td>
<td align="right">0.41</td>
<td align="right">-0.49</td>
<td align="right">-0.31</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="right">0.40</td>
<td align="right">0.45</td>
<td align="right">0.08</td>
<td align="right">-0.55</td>
<td align="right">0.38</td>
<td align="right">0.27</td>
<td align="right">1.91</td>
<td align="right">-1.60</td>
<td align="right">0.31</td>
<td align="right">-0.09</td>
</tr>
<tr>
<td align="left">SibSp</td>
<td align="right">-0.38</td>
<td align="right">0.27</td>
<td align="right">-0.35</td>
<td align="right">-0.31</td>
<td align="right">0.18</td>
<td align="right">0.17</td>
<td align="right">-0.49</td>
<td align="right">1.39</td>
<td align="right">0.20</td>
<td align="right">1.60</td>
</tr>
<tr>
<td align="left">Parch</td>
<td align="right">-0.37</td>
<td align="right">-0.04</td>
<td align="right">0.02</td>
<td align="right">-0.37</td>
<td align="right">-0.00</td>
<td align="right">0.68</td>
<td align="right">-0.45</td>
<td align="right">1.46</td>
<td align="right">0.33</td>
<td align="right">3.53</td>
</tr>
<tr>
<td align="left">Fare</td>
<td align="right">-0.56</td>
<td align="right">1.55</td>
<td align="right">5.54</td>
<td align="right">-0.56</td>
<td align="right">0.80</td>
<td align="right">2.98</td>
<td align="right">-0.26</td>
<td align="right">-0.09</td>
<td align="right">-0.04</td>
<td align="right">3.26</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-titanic/figures/ef02dbed-3740-4ee6-b91c-228be2eb1acc.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-titanic/figures/de3fdcd6-a8ab-4da7-bf45-ca4ea04b99e4.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Fare e no grupo 2, com valor de 190.54. A maior variação negativa foi na feature Age e no grupo 7, com o valor registrado de -22.80</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Embarked</th>
<th align="left">Sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">C</td>
<td align="left">female</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">3</td>
<td align="left">6</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.5</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.322</td>
<td align="left">0.648</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Embarked</th>
<th align="left">Sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">S</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">26</td>
<td align="left">25</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.542</td>
<td align="left">0.568</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.241</td>
<td align="left">-0.08</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">4</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Embarked</th>
<th align="left">Sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Q</td>
<td align="left">male</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.37</td>
<td align="left">0.338</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">3</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Embarked</th>
<th align="left">Sex</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">C</td>
<td align="left">female</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.025</td>
<td align="left">0.025</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: Pclass<br>&emsp;Média menor que a população: Fare<br>&emsp;Presença maior de população na feature Sex: male</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: Survived<br>&emsp;Média menor que a população: Pclass<br>&emsp;Média maior que a população: Fare<br>&emsp;Presença maior de população na feature Sex: female</p>
<p>Grupo 2: <br>&emsp;Média maior que a população: Survived<br>&emsp;Média menor que a população: Pclass<br>&emsp;Média maior que a população: Fare<br>&emsp;Presença maior de população na feature Embarked: C<br>&emsp;Presença maior de população na feature Sex: female</p>
<p>Grupo 3: <br>&emsp;Média maior que a população: Pclass<br>&emsp;Média menor que a população: Age<br>&emsp;Média menor que a população: Fare</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: Survived<br>&emsp;Média menor que a população: Pclass<br>&emsp;Média maior que a população: Fare</p>
<p>Grupo 5: <br>&emsp;Média maior que a população: Survived<br>&emsp;Média menor que a população: Pclass<br>&emsp;Média maior que a população: Parch<br>&emsp;Média maior que a população: Fare<br>&emsp;Presença maior de população na feature Embarked: C<br>&emsp;Presença maior de população na feature Sex: female</p>
<p>Grupo 6: <br>&emsp;Média menor que a população: Pclass<br>&emsp;Média maior que a população: Age<br>&emsp;Presença maior de população na feature Sex: male</p>
<p>Grupo 7: <br>&emsp;Média menor que a população: Age<br>&emsp;Média maior que a população: SibSp<br>&emsp;Média maior que a população: Parch<br>&emsp;Presença maior de população na feature Sex: female</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: SibSp<br>&emsp;Média maior que a população: Parch<br>&emsp;Média maior que a população: Fare</p>
