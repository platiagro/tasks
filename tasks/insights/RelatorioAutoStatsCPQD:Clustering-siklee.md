<h1>Relatorio AutoStats CPQD: Clustering - siklee</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 173 outliers neste dataset, correspondendo a uma proporção de 21.12% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Tempo de dispensa</th>
<th align="right">Sexo [Funcionario]</th>
<th align="right">Tempo de Dispensa (dias)</th>
<th align="right">Tempo de Entrega</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">173.00</td>
<td align="right">173.00</td>
<td align="right">173.00</td>
<td align="right">173.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">72.74</td>
<td align="right">0.00</td>
<td align="right">12.39</td>
<td align="right">12.47</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">115.37</td>
<td align="right">0.00</td>
<td align="right">19.66</td>
<td align="right">23.01</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">-14.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">23.61</td>
<td align="right">0.00</td>
<td align="right">4.00</td>
<td align="right">2.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">49.00</td>
<td align="right">0.00</td>
<td align="right">8.40</td>
<td align="right">7.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">81.07</td>
<td align="right">0.00</td>
<td align="right">13.80</td>
<td align="right">13.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">973.53</td>
<td align="right">0.00</td>
<td align="right">165.90</td>
<td align="right">194.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Instituicao de saude</th>
<th align="left">Area de atuacao [Funcionario]</th>
<th align="left">Cid</th>
<th align="left">Especialidade medica</th>
<th align="left">Empresa [Funcionario]</th>
<th align="left">Tipo de registro</th>
<th align="left">Cfm</th>
<th align="left">Dia da Semana</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">9</td>
<td align="left">26</td>
<td align="left">74</td>
<td align="left">24</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">7</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">HOSPITAL SANTA FILOMENA</td>
<td align="left">Operador Manufatura I</td>
<td align="left">J110</td>
<td align="left">Clinico Geral</td>
<td align="left">E-LifeTech</td>
<td align="left">CRM0085318</td>
<td align="left">Não</td>
<td align="left">ter.</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">108</td>
<td align="left">66</td>
<td align="left">23</td>
<td align="left">59</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">173</td>
<td align="left">39</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-siklee/figures/c5f35c15-894c-44b5-9d06-4f826f433bfc.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 41 outliers neste dataset, correspondendo a uma proporção de 5.01% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Tempo de dispensa</th>
<th align="right">Sexo [Funcionario]</th>
<th align="right">Tempo de Dispensa (dias)</th>
<th align="right">Tempo de Entrega</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">41.00</td>
<td align="right">41.00</td>
<td align="right">41.00</td>
<td align="right">41.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">173.93</td>
<td align="right">0.00</td>
<td align="right">29.63</td>
<td align="right">28.49</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">203.25</td>
<td align="right">0.00</td>
<td align="right">34.64</td>
<td align="right">42.64</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">-14.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">76.50</td>
<td align="right">0.00</td>
<td align="right">13.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">93.50</td>
<td align="right">0.00</td>
<td align="right">15.90</td>
<td align="right">12.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">237.08</td>
<td align="right">0.00</td>
<td align="right">40.40</td>
<td align="right">49.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">973.53</td>
<td align="right">0.00</td>
<td align="right">165.90</td>
<td align="right">194.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Instituicao de saude</th>
<th align="left">Area de atuacao [Funcionario]</th>
<th align="left">Cid</th>
<th align="left">Especialidade medica</th>
<th align="left">Empresa [Funcionario]</th>
<th align="left">Tipo de registro</th>
<th align="left">Cfm</th>
<th align="left">Dia da Semana</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">4</td>
<td align="left">15</td>
<td align="left">23</td>
<td align="left">13</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">7</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">HOSPITAL SANTA FILOMENA</td>
<td align="left">Operador Manufatura I</td>
<td align="left">M659</td>
<td align="left">ORTOPEDIA E TRA.</td>
<td align="left">E-LifeTech</td>
<td align="left">CRM0085318</td>
<td align="left">Não</td>
<td align="left">ter.</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">21</td>
<td align="left">16</td>
<td align="left">6</td>
<td align="left">12</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">41</td>
<td align="left">10</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-siklee/figures/705d2845-1a8e-426e-8e3b-b9020c1bf1a6.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Tempo de dispensa', 'Sexo [Funcionario]', 'Tempo de Dispensa (dias)'] com uma quantidade de 10 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="left">sáb.</td>
<td align="right">0.06</td>
<td align="right">0.06</td>
<td align="right">0.15</td>
<td align="right">0.26</td>
<td align="right">0.00</td>
<td align="right">0.09</td>
<td align="right">0.17</td>
<td align="right">0.17</td>
<td align="right">0.00</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">qui.</td>
<td align="right">0.06</td>
<td align="right">0.15</td>
<td align="right">0.08</td>
<td align="right">0.29</td>
<td align="right">0.07</td>
<td align="right">0.05</td>
<td align="right">0.13</td>
<td align="right">0.08</td>
<td align="right">0.03</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="left">qua.</td>
<td align="right">0.01</td>
<td align="right">0.05</td>
<td align="right">0.24</td>
<td align="right">0.32</td>
<td align="right">0.02</td>
<td align="right">0.05</td>
<td align="right">0.11</td>
<td align="right">0.10</td>
<td align="right">0.04</td>
<td align="right">0.06</td>
</tr>
<tr>
<td align="left">seg.</td>
<td align="right">0.01</td>
<td align="right">0.05</td>
<td align="right">0.09</td>
<td align="right">0.41</td>
<td align="right">0.00</td>
<td align="right">0.07</td>
<td align="right">0.15</td>
<td align="right">0.10</td>
<td align="right">0.01</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">ter.</td>
<td align="right">0.03</td>
<td align="right">0.10</td>
<td align="right">0.12</td>
<td align="right">0.35</td>
<td align="right">0.04</td>
<td align="right">0.11</td>
<td align="right">0.10</td>
<td align="right">0.10</td>
<td align="right">0.01</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">dom.</td>
<td align="right">0.05</td>
<td align="right">0.07</td>
<td align="right">0.12</td>
<td align="right">0.22</td>
<td align="right">0.03</td>
<td align="right">0.21</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
<td align="right">0.02</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">sex.</td>
<td align="right">0.03</td>
<td align="right">0.12</td>
<td align="right">0.11</td>
<td align="right">0.46</td>
<td align="right">0.01</td>
<td align="right">0.05</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
<td align="right">0.07</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Tempo de dispensa', 'Sexo [Funcionario]', 'Tempo de Dispensa (dias)', 'Tempo de Entrega'] com uma quantidade de 10 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="left">sáb.</td>
<td align="right">0.08</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.15</td>
<td align="right">0.02</td>
<td align="right">0.17</td>
<td align="right">0.08</td>
<td align="right">0.17</td>
<td align="right">0.06</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">qui.</td>
<td align="right">0.08</td>
<td align="right">0.28</td>
<td align="right">0.07</td>
<td align="right">0.12</td>
<td align="right">0.06</td>
<td align="right">0.24</td>
<td align="right">0.05</td>
<td align="right">0.08</td>
<td align="right">0.02</td>
<td align="right">0.01</td>
</tr>
<tr>
<td align="left">qua.</td>
<td align="right">0.03</td>
<td align="right">0.30</td>
<td align="right">0.03</td>
<td align="right">0.27</td>
<td align="right">0.04</td>
<td align="right">0.09</td>
<td align="right">0.08</td>
<td align="right">0.10</td>
<td align="right">0.03</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">seg.</td>
<td align="right">0.10</td>
<td align="right">0.37</td>
<td align="right">0.00</td>
<td align="right">0.14</td>
<td align="right">0.02</td>
<td align="right">0.14</td>
<td align="right">0.06</td>
<td align="right">0.09</td>
<td align="right">0.03</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">ter.</td>
<td align="right">0.03</td>
<td align="right">0.31</td>
<td align="right">0.04</td>
<td align="right">0.14</td>
<td align="right">0.03</td>
<td align="right">0.15</td>
<td align="right">0.12</td>
<td align="right">0.09</td>
<td align="right">0.02</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">dom.</td>
<td align="right">0.16</td>
<td align="right">0.21</td>
<td align="right">0.03</td>
<td align="right">0.10</td>
<td align="right">0.02</td>
<td align="right">0.14</td>
<td align="right">0.24</td>
<td align="right">0.05</td>
<td align="right">0.02</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">sex.</td>
<td align="right">0.09</td>
<td align="right">0.47</td>
<td align="right">0.01</td>
<td align="right">0.13</td>
<td align="right">0.01</td>
<td align="right">0.17</td>
<td align="right">0.04</td>
<td align="right">0.06</td>
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
<td align="left">Tempo de dispensa - Sexo [Funcionario] - Tempo de Dispensa (dias)</td>
<td align="right">0.66</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Tempo de dispensa - Sexo [Funcionario] - Tempo de Entrega</td>
<td align="right">0.51</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Tempo de dispensa - Tempo de Dispensa (dias) - Tempo de Entrega</td>
<td align="right">0.44</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Tempo de dispensa - Sexo [Funcionario] - Tempo de Dispensa (dias) - Tempo de Entrega</td>
<td align="right">nan</td>
<td align="right">0.45</td>
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
<td align="left">Tempo de dispensa</td>
<td align="right">23.37</td>
<td align="right">-12.75</td>
<td align="right">62.38</td>
<td align="right">4.38</td>
<td align="right">41.32</td>
<td align="right">-3.71</td>
<td align="right">13.71</td>
<td align="right">-17.27</td>
<td align="right">8.43</td>
<td align="right">-11.76</td>
<td align="right">154.16</td>
</tr>
<tr>
<td align="left">Sexo [Funcionario]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
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
<td align="left">Tempo de Dispensa (dias)</td>
<td align="right">3.99</td>
<td align="right">-2.19</td>
<td align="right">10.63</td>
<td align="right">0.75</td>
<td align="right">7.03</td>
<td align="right">-0.62</td>
<td align="right">2.35</td>
<td align="right">-2.93</td>
<td align="right">1.44</td>
<td align="right">-2.01</td>
<td align="right">26.27</td>
</tr>
<tr>
<td align="left">Tempo de Entrega</td>
<td align="right">-0.06</td>
<td align="right">-0.53</td>
<td align="right">-0.22</td>
<td align="right">-1.09</td>
<td align="right">-1.31</td>
<td align="right">-0.52</td>
<td align="right">-0.92</td>
<td align="right">-0.86</td>
<td align="right">9.89</td>
<td align="right">10.40</td>
<td align="right">25.17</td>
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
<td align="left">Tempo de dispensa</td>
<td align="right">1.33</td>
<td align="right">-0.73</td>
<td align="right">3.56</td>
<td align="right">0.25</td>
<td align="right">2.35</td>
<td align="right">-0.21</td>
<td align="right">0.78</td>
<td align="right">-0.98</td>
<td align="right">0.48</td>
<td align="right">-0.67</td>
<td align="right">8.79</td>
</tr>
<tr>
<td align="left">Sexo [Funcionario]</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Tempo de Dispensa (dias)</td>
<td align="right">1.33</td>
<td align="right">-0.73</td>
<td align="right">3.55</td>
<td align="right">0.25</td>
<td align="right">2.35</td>
<td align="right">-0.21</td>
<td align="right">0.79</td>
<td align="right">-0.98</td>
<td align="right">0.48</td>
<td align="right">-0.67</td>
<td align="right">8.77</td>
</tr>
<tr>
<td align="left">Tempo de Entrega</td>
<td align="right">-0.02</td>
<td align="right">-0.15</td>
<td align="right">-0.06</td>
<td align="right">-0.31</td>
<td align="right">-0.37</td>
<td align="right">-0.15</td>
<td align="right">-0.26</td>
<td align="right">-0.24</td>
<td align="right">2.80</td>
<td align="right">2.94</td>
<td align="right">7.12</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-siklee/figures/b8451263-6b82-4f10-a14f-4fbb6111036f.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/RelatorioAutoStatsCPQD:Clustering-siklee/figures/de14071a-a2f4-45c4-8cd1-aac03d4b58ce.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature Tempo de dispensa e no grupo outlier, com valor de 154.16. A maior variação negativa foi na feature Tempo de dispensa e no grupo 7, com o valor registrado de -17.27</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Instituicao de saude</th>
<th align="left">Area de atuacao [Funcionario]</th>
<th align="left">Cid</th>
<th align="left">Especialidade medica</th>
<th align="left">Empresa [Funcionario]</th>
<th align="left">Tipo de registro</th>
<th align="left">Cfm</th>
<th align="left">Dia da Semana</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">CONSULTÓRIO MÉDICO</td>
<td align="left">Operador Manufatura I</td>
<td align="left">M659</td>
<td align="left">ORTOPEDIA E TRA.</td>
<td align="left">E-LifeTech</td>
<td align="left">CRM0085318</td>
<td align="left">Não</td>
<td align="left">qui.</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">13</td>
<td align="left">13</td>
<td align="left">5</td>
<td align="left">10</td>
<td align="left">55</td>
<td align="left">55</td>
<td align="left">55</td>
<td align="left">8</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.619</td>
<td align="left">0.565</td>
<td align="left">0.238</td>
<td align="left">0.476</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.381</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.485</td>
<td align="left">0.182</td>
<td align="left">0.227</td>
<td align="left">0.413</td>
<td align="left">0.0</td>
<td align="left">0.0</td>
<td align="left">0.0</td>
<td align="left">0.228</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Instituicao de saude</th>
<th align="left">Area de atuacao [Funcionario]</th>
<th align="left">Cid</th>
<th align="left">Especialidade medica</th>
<th align="left">Empresa [Funcionario]</th>
<th align="left">Tipo de registro</th>
<th align="left">Cfm</th>
<th align="left">Dia da Semana</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">HOSPITAL SANTA FILOMENA</td>
<td align="left">Operador Manufatura I</td>
<td align="left">J110</td>
<td align="left">Médico do Trabalho</td>
<td align="left">E-LifeTech</td>
<td align="left">CRM0085318</td>
<td align="left">Não</td>
<td align="left">qua.</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">10</td>
<td align="left">20</td>
<td align="left">4</td>
<td align="left">83</td>
<td align="left">55</td>
<td align="left">55</td>
<td align="left">55</td>
<td align="left">16</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.435</td>
<td align="left">0.282</td>
<td align="left">0.143</td>
<td align="left">0.332</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.225</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.236</td>
<td align="left">-0.101</td>
<td align="left">-0.058</td>
<td align="left">0.002</td>
<td align="left">0.0</td>
<td align="left">0.0</td>
<td align="left">0.0</td>
<td align="left">0.022</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">4</td>
<td align="left">7</td>
<td align="left">9</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">7</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Instituicao de saude</th>
<th align="left">Area de atuacao [Funcionario]</th>
<th align="left">Cid</th>
<th align="left">Especialidade medica</th>
<th align="left">Empresa [Funcionario]</th>
<th align="left">Tipo de registro</th>
<th align="left">Cfm</th>
<th align="left">Dia da Semana</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">HOSPITAL SANTA CASA</td>
<td align="left">Controlador Produção</td>
<td align="left">B029</td>
<td align="left">MEDICINA DO TRABALHO</td>
<td align="left">E-LifeTech</td>
<td align="left">CRM0085318</td>
<td align="left">Não</td>
<td align="left">sex.</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.321</td>
<td align="left">0.321</td>
<td align="left">0.321</td>
<td align="left">0.468</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Instituicao de saude</th>
<th align="left">Area de atuacao [Funcionario]</th>
<th align="left">Cid</th>
<th align="left">Especialidade medica</th>
<th align="left">Empresa [Funcionario]</th>
<th align="left">Tipo de registro</th>
<th align="left">Cfm</th>
<th align="left">Dia da Semana</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">CONSULTÓRIO MÉDICO</td>
<td align="left">Inspetor Qualidade I</td>
<td align="left">B029</td>
<td align="left">UROLOGIA</td>
<td align="left">E-LifeTech</td>
<td align="left">CRM0085318</td>
<td align="left">Não</td>
<td align="left">sáb.</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.048</td>
<td align="left">0.167</td>
<td align="left">1.0</td>
<td align="left">0.375</td>
<td align="left">0.026</td>
<td align="left">0.026</td>
<td align="left">0.026</td>
<td align="left">0.057</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">9</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">9</td>
<td align="left">8</td>
<td align="left">8</td>
<td align="left">8</td>
<td align="left">8</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: Tempo de dispensa<br>&emsp;Média maior que a população: Tempo de Dispensa (dias)</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: Tempo de dispensa<br>&emsp;Média menor que a população: Tempo de Dispensa (dias)</p>
<p>Grupo 2: <br>&emsp;Média maior que a população: Tempo de dispensa<br>&emsp;Média maior que a população: Tempo de Dispensa (dias)<br>&emsp;Presença maior de população na feature Instituicao de saude: CONSULTÓRIO MÉDICO<br>&emsp;Presença maior de população na feature Cid: M659<br>&emsp;Presença maior de população na feature Especialidade medica: ORTOPEDIA E TRA.<br>&emsp;Presença maior de população na feature Dia da Semana: qui.</p>
<p>Grupo 3: <br>&emsp;Presença maior de população na feature Instituicao de saude: HOSPITAL SANTA FILOMENA<br>&emsp;Presença maior de população na feature Cid: J110<br>&emsp;Presença maior de população na feature Especialidade medica: Médico do Trabalho<br>&emsp;Presença maior de população na feature Dia da Semana: qua.</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: Tempo de dispensa<br>&emsp;Média maior que a população: Tempo de Dispensa (dias)<br>&emsp;Presença maior de população na feature Area de atuacao [Funcionario]: Operador Manufatura I<br>&emsp;Presença maior de população na feature Cid: Z290<br>&emsp;Presença maior de população na feature Dia da Semana: qui.</p>
<p>Grupo 5: <br>&emsp;Presença maior de população na feature Cid: J110<br>&emsp;Presença maior de população na feature Especialidade medica: Clinico Geral</p>
<p>Grupo 6: <br>&emsp;Média maior que a população: Tempo de dispensa<br>&emsp;Média maior que a população: Tempo de Dispensa (dias)<br>&emsp;Presença maior de população na feature Instituicao de saude: HOSPITAL SANTA FILOMENA<br>&emsp;Presença maior de população na feature Especialidade medica: Clinico Geral</p>
<p>Grupo 7: <br>&emsp;Média menor que a população: Tempo de dispensa<br>&emsp;Média menor que a população: Tempo de Dispensa (dias)<br>&emsp;Presença maior de população na feature Cid: Z000</p>
<p>Grupo 8: <br>&emsp;Média maior que a população: Tempo de Entrega<br>&emsp;Presença maior de população na feature Instituicao de saude: HOSPITAL SANTA FILOMENA</p>
<p>Grupo 9: <br>&emsp;Média menor que a população: Tempo de dispensa<br>&emsp;Média menor que a população: Tempo de Dispensa (dias)<br>&emsp;Média maior que a população: Tempo de Entrega<br>&emsp;Presença maior de população na feature Instituicao de saude: HOSPITAL SANTA FILOMENA<br>&emsp;Presença maior de população na feature Dia da Semana: ter.</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: Tempo de dispensa<br>&emsp;Média maior que a população: Tempo de Dispensa (dias)<br>&emsp;Média maior que a população: Tempo de Entrega</p>
