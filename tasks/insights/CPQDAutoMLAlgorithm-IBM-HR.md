<h1>CPQD AutoML Algorithm - IBM-HR</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 1470 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Age</th>
<th align="right">DailyRate</th>
<th align="right">DistanceFromHome</th>
<th align="right">Education</th>
<th align="right">EmployeeCount</th>
<th align="right">EmployeeNumber</th>
<th align="right">EnvironmentSatisfaction</th>
<th align="right">HourlyRate</th>
<th align="right">JobInvolvement</th>
<th align="right">JobLevel</th>
<th align="right">JobSatisfaction</th>
<th align="right">MonthlyIncome</th>
<th align="right">MonthlyRate</th>
<th align="right">NumCompaniesWorked</th>
<th align="right">PercentSalaryHike</th>
<th align="right">PerformanceRating</th>
<th align="right">RelationshipSatisfaction</th>
<th align="right">StandardHours</th>
<th align="right">StockOptionLevel</th>
<th align="right">TotalWorkingYears</th>
<th align="right">TrainingTimesLastYear</th>
<th align="right">WorkLifeBalance</th>
<th align="right">YearsAtCompany</th>
<th align="right">YearsInCurrentRole</th>
<th align="right">YearsSinceLastPromotion</th>
<th align="right">YearsWithCurrManager</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
<td align="right">1470.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">36.92</td>
<td align="right">802.49</td>
<td align="right">9.19</td>
<td align="right">2.91</td>
<td align="right">1.00</td>
<td align="right">1024.87</td>
<td align="right">2.72</td>
<td align="right">65.89</td>
<td align="right">2.73</td>
<td align="right">2.06</td>
<td align="right">2.73</td>
<td align="right">6502.93</td>
<td align="right">14313.10</td>
<td align="right">2.69</td>
<td align="right">15.21</td>
<td align="right">3.15</td>
<td align="right">2.71</td>
<td align="right">80.00</td>
<td align="right">0.79</td>
<td align="right">11.28</td>
<td align="right">2.80</td>
<td align="right">2.76</td>
<td align="right">7.01</td>
<td align="right">4.23</td>
<td align="right">2.19</td>
<td align="right">4.12</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">9.14</td>
<td align="right">403.51</td>
<td align="right">8.11</td>
<td align="right">1.02</td>
<td align="right">0.00</td>
<td align="right">602.02</td>
<td align="right">1.09</td>
<td align="right">20.33</td>
<td align="right">0.71</td>
<td align="right">1.11</td>
<td align="right">1.10</td>
<td align="right">4707.96</td>
<td align="right">7117.79</td>
<td align="right">2.50</td>
<td align="right">3.66</td>
<td align="right">0.36</td>
<td align="right">1.08</td>
<td align="right">0.00</td>
<td align="right">0.85</td>
<td align="right">7.78</td>
<td align="right">1.29</td>
<td align="right">0.71</td>
<td align="right">6.13</td>
<td align="right">3.62</td>
<td align="right">3.22</td>
<td align="right">3.57</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">18.00</td>
<td align="right">102.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">30.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1009.00</td>
<td align="right">2094.00</td>
<td align="right">0.00</td>
<td align="right">11.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">80.00</td>
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
<td align="left">25%</td>
<td align="right">30.00</td>
<td align="right">465.00</td>
<td align="right">2.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">491.25</td>
<td align="right">2.00</td>
<td align="right">48.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">2.00</td>
<td align="right">2911.00</td>
<td align="right">8047.00</td>
<td align="right">1.00</td>
<td align="right">12.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">80.00</td>
<td align="right">0.00</td>
<td align="right">6.00</td>
<td align="right">2.00</td>
<td align="right">2.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">36.00</td>
<td align="right">802.00</td>
<td align="right">7.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">1020.50</td>
<td align="right">3.00</td>
<td align="right">66.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">3.00</td>
<td align="right">4919.00</td>
<td align="right">14235.50</td>
<td align="right">2.00</td>
<td align="right">14.00</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">80.00</td>
<td align="right">1.00</td>
<td align="right">10.00</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">5.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">43.00</td>
<td align="right">1157.00</td>
<td align="right">14.00</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">1555.75</td>
<td align="right">4.00</td>
<td align="right">83.75</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">4.00</td>
<td align="right">8379.00</td>
<td align="right">20461.50</td>
<td align="right">4.00</td>
<td align="right">18.00</td>
<td align="right">3.00</td>
<td align="right">4.00</td>
<td align="right">80.00</td>
<td align="right">1.00</td>
<td align="right">15.00</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">9.00</td>
<td align="right">7.00</td>
<td align="right">3.00</td>
<td align="right">7.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">60.00</td>
<td align="right">1499.00</td>
<td align="right">29.00</td>
<td align="right">5.00</td>
<td align="right">1.00</td>
<td align="right">2068.00</td>
<td align="right">4.00</td>
<td align="right">100.00</td>
<td align="right">4.00</td>
<td align="right">5.00</td>
<td align="right">4.00</td>
<td align="right">19999.00</td>
<td align="right">26999.00</td>
<td align="right">9.00</td>
<td align="right">25.00</td>
<td align="right">4.00</td>
<td align="right">4.00</td>
<td align="right">80.00</td>
<td align="right">3.00</td>
<td align="right">40.00</td>
<td align="right">6.00</td>
<td align="right">4.00</td>
<td align="right">40.00</td>
<td align="right">18.00</td>
<td align="right">15.00</td>
<td align="right">17.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">JobRole</th>
<th align="left">MaritalStatus</th>
<th align="left">Over18</th>
<th align="left">Attrition</th>
<th align="left">Department</th>
<th align="left">BusinessTravel</th>
<th align="left">EducationField</th>
<th align="left">OverTime</th>
<th align="left">Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
<td align="left">1470</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">9</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Sales Executive</td>
<td align="left">Married</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Research &amp; Development</td>
<td align="left">Travel_Rarely</td>
<td align="left">Life Sciences</td>
<td align="left">No</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">326</td>
<td align="left">673</td>
<td align="left">1470</td>
<td align="left">1233</td>
<td align="left">961</td>
<td align="left">1043</td>
<td align="left">606</td>
<td align="left">1054</td>
<td align="left">882</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-IBM-HR/figures/51a77bf1-9a56-4fc3-8353-5adfc3308ba6.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 74 outliers neste dataset, correspondendo a uma proporção de 5.03% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Age</th>
<th align="right">DailyRate</th>
<th align="right">DistanceFromHome</th>
<th align="right">Education</th>
<th align="right">EmployeeCount</th>
<th align="right">EmployeeNumber</th>
<th align="right">EnvironmentSatisfaction</th>
<th align="right">HourlyRate</th>
<th align="right">JobInvolvement</th>
<th align="right">JobLevel</th>
<th align="right">JobSatisfaction</th>
<th align="right">MonthlyIncome</th>
<th align="right">MonthlyRate</th>
<th align="right">NumCompaniesWorked</th>
<th align="right">PercentSalaryHike</th>
<th align="right">PerformanceRating</th>
<th align="right">RelationshipSatisfaction</th>
<th align="right">StandardHours</th>
<th align="right">StockOptionLevel</th>
<th align="right">TotalWorkingYears</th>
<th align="right">TrainingTimesLastYear</th>
<th align="right">WorkLifeBalance</th>
<th align="right">YearsAtCompany</th>
<th align="right">YearsInCurrentRole</th>
<th align="right">YearsSinceLastPromotion</th>
<th align="right">YearsWithCurrManager</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
<td align="right">74.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">48.14</td>
<td align="right">757.89</td>
<td align="right">10.20</td>
<td align="right">2.99</td>
<td align="right">1.00</td>
<td align="right">982.55</td>
<td align="right">2.66</td>
<td align="right">67.89</td>
<td align="right">2.58</td>
<td align="right">3.88</td>
<td align="right">2.55</td>
<td align="right">14478.19</td>
<td align="right">15478.73</td>
<td align="right">3.43</td>
<td align="right">17.55</td>
<td align="right">3.42</td>
<td align="right">2.85</td>
<td align="right">80.00</td>
<td align="right">0.97</td>
<td align="right">26.03</td>
<td align="right">2.77</td>
<td align="right">2.70</td>
<td align="right">18.66</td>
<td align="right">8.49</td>
<td align="right">7.42</td>
<td align="right">8.42</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">8.44</td>
<td align="right">432.96</td>
<td align="right">10.13</td>
<td align="right">1.18</td>
<td align="right">0.00</td>
<td align="right">632.65</td>
<td align="right">1.15</td>
<td align="right">22.04</td>
<td align="right">0.84</td>
<td align="right">1.22</td>
<td align="right">1.09</td>
<td align="right">5519.76</td>
<td align="right">7908.13</td>
<td align="right">2.85</td>
<td align="right">4.74</td>
<td align="right">0.50</td>
<td align="right">1.19</td>
<td align="right">0.00</td>
<td align="right">1.02</td>
<td align="right">8.52</td>
<td align="right">1.53</td>
<td align="right">0.81</td>
<td align="right">10.55</td>
<td align="right">5.03</td>
<td align="right">5.70</td>
<td align="right">4.55</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">19.00</td>
<td align="right">136.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">10.00</td>
<td align="right">1.00</td>
<td align="right">30.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">1.00</td>
<td align="right">2028.00</td>
<td align="right">2125.00</td>
<td align="right">0.00</td>
<td align="right">11.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">80.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">44.00</td>
<td align="right">360.25</td>
<td align="right">2.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">376.75</td>
<td align="right">2.00</td>
<td align="right">52.50</td>
<td align="right">2.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">10673.00</td>
<td align="right">8023.25</td>
<td align="right">1.00</td>
<td align="right">13.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">80.00</td>
<td align="right">0.00</td>
<td align="right">22.00</td>
<td align="right">2.00</td>
<td align="right">2.00</td>
<td align="right">10.00</td>
<td align="right">6.00</td>
<td align="right">1.25</td>
<td align="right">6.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">50.00</td>
<td align="right">671.50</td>
<td align="right">6.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">1036.50</td>
<td align="right">3.00</td>
<td align="right">68.50</td>
<td align="right">3.00</td>
<td align="right">4.00</td>
<td align="right">3.00</td>
<td align="right">16907.50</td>
<td align="right">17394.50</td>
<td align="right">3.00</td>
<td align="right">18.00</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">80.00</td>
<td align="right">1.00</td>
<td align="right">26.00</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">20.00</td>
<td align="right">8.00</td>
<td align="right">7.00</td>
<td align="right">9.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">55.00</td>
<td align="right">1191.25</td>
<td align="right">20.75</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">1535.00</td>
<td align="right">4.00</td>
<td align="right">88.00</td>
<td align="right">3.00</td>
<td align="right">5.00</td>
<td align="right">3.00</td>
<td align="right">19143.25</td>
<td align="right">22249.50</td>
<td align="right">5.00</td>
<td align="right">22.00</td>
<td align="right">4.00</td>
<td align="right">4.00</td>
<td align="right">80.00</td>
<td align="right">1.75</td>
<td align="right">33.00</td>
<td align="right">3.00</td>
<td align="right">3.00</td>
<td align="right">25.75</td>
<td align="right">12.00</td>
<td align="right">13.00</td>
<td align="right">11.75</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">60.00</td>
<td align="right">1499.00</td>
<td align="right">29.00</td>
<td align="right">5.00</td>
<td align="right">1.00</td>
<td align="right">2036.00</td>
<td align="right">4.00</td>
<td align="right">100.00</td>
<td align="right">4.00</td>
<td align="right">5.00</td>
<td align="right">4.00</td>
<td align="right">19999.00</td>
<td align="right">26703.00</td>
<td align="right">9.00</td>
<td align="right">25.00</td>
<td align="right">4.00</td>
<td align="right">4.00</td>
<td align="right">80.00</td>
<td align="right">3.00</td>
<td align="right">40.00</td>
<td align="right">6.00</td>
<td align="right">4.00</td>
<td align="right">40.00</td>
<td align="right">18.00</td>
<td align="right">15.00</td>
<td align="right">17.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">JobRole</th>
<th align="left">MaritalStatus</th>
<th align="left">Over18</th>
<th align="left">Attrition</th>
<th align="left">Department</th>
<th align="left">BusinessTravel</th>
<th align="left">EducationField</th>
<th align="left">OverTime</th>
<th align="left">Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
<td align="left">74</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">8</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Manager</td>
<td align="left">Married</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Research &amp; Development</td>
<td align="left">Travel_Rarely</td>
<td align="left">Medical</td>
<td align="left">No</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">28</td>
<td align="left">36</td>
<td align="left">74</td>
<td align="left">67</td>
<td align="left">45</td>
<td align="left">52</td>
<td align="left">29</td>
<td align="left">57</td>
<td align="left">42</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-IBM-HR/figures/d3024220-feb2-4645-92c4-e8fc5c4b1571.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['EmployeeNumber', 'NumCompaniesWorked', 'TotalWorkingYears'] com uma quantidade de 3 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
<td align="right">3</td>
<td align="right">0.34</td>
<td align="right">0.32</td>
<td align="right">0.34</td>
</tr>
<tr>
<td align="right">4</td>
<td align="right">0.36</td>
<td align="right">0.32</td>
<td align="right">0.32</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EmployeeCount', 'EmployeeNumber', 'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'] com uma quantidade de 2 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
<td align="right">0.50</td>
<td align="right">0.50</td>
</tr>
<tr>
<td align="right">4</td>
<td align="right">0.57</td>
<td align="right">0.43</td>
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
<td align="left">EmployeeNumber - NumCompaniesWorked - TotalWorkingYears</td>
<td align="right">0.60</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">EnvironmentSatisfaction - MonthlyIncome - YearsAtCompany</td>
<td align="right">0.56</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">EmployeeCount - WorkLifeBalance - YearsAtCompany</td>
<td align="right">0.48</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">Age - DailyRate - DistanceFromHome - Education - EmployeeCount - EmployeeNumber - EnvironmentSatisfaction - HourlyRate - JobInvolvement - JobLevel - JobSatisfaction - MonthlyIncome - MonthlyRate - NumCompaniesWorked - PercentSalaryHike - PerformanceRating - RelationshipSatisfaction - StandardHours - StockOptionLevel - TotalWorkingYears - TrainingTimesLastYear - WorkLifeBalance - YearsAtCompany - YearsInCurrentRole - YearsSinceLastPromotion - YearsWithCurrManager</td>
<td align="right">nan</td>
<td align="right">0.48</td>
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
<td align="left">Age</td>
<td align="right">-0.27</td>
<td align="right">0.28</td>
<td align="right">11.81</td>
</tr>
<tr>
<td align="left">DailyRate</td>
<td align="right">7.39</td>
<td align="right">-7.65</td>
<td align="right">-46.96</td>
</tr>
<tr>
<td align="left">DistanceFromHome</td>
<td align="right">-0.05</td>
<td align="right">0.06</td>
<td align="right">1.06</td>
</tr>
<tr>
<td align="left">Education</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.08</td>
</tr>
<tr>
<td align="left">EmployeeCount</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">EmployeeNumber</td>
<td align="right">-0.42</td>
<td align="right">0.43</td>
<td align="right">-44.55</td>
</tr>
<tr>
<td align="left">EnvironmentSatisfaction</td>
<td align="right">-0.05</td>
<td align="right">0.05</td>
<td align="right">-0.06</td>
</tr>
<tr>
<td align="left">HourlyRate</td>
<td align="right">0.44</td>
<td align="right">-0.45</td>
<td align="right">2.11</td>
</tr>
<tr>
<td align="left">JobInvolvement</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.16</td>
</tr>
<tr>
<td align="left">JobLevel</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">1.91</td>
</tr>
<tr>
<td align="left">JobSatisfaction</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">-0.18</td>
</tr>
<tr>
<td align="left">MonthlyIncome</td>
<td align="right">-114.35</td>
<td align="right">118.36</td>
<td align="right">8398.02</td>
</tr>
<tr>
<td align="left">MonthlyRate</td>
<td align="right">-6032.77</td>
<td align="right">6243.83</td>
<td align="right">1227.41</td>
</tr>
<tr>
<td align="left">NumCompaniesWorked</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">0.78</td>
</tr>
<tr>
<td align="left">PercentSalaryHike</td>
<td align="right">0.14</td>
<td align="right">-0.15</td>
<td align="right">2.47</td>
</tr>
<tr>
<td align="left">PerformanceRating</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.28</td>
</tr>
<tr>
<td align="left">RelationshipSatisfaction</td>
<td align="right">0.03</td>
<td align="right">-0.03</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">StandardHours</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">StockOptionLevel</td>
<td align="right">0.04</td>
<td align="right">-0.04</td>
<td align="right">0.19</td>
</tr>
<tr>
<td align="left">TotalWorkingYears</td>
<td align="right">-0.11</td>
<td align="right">0.12</td>
<td align="right">15.53</td>
</tr>
<tr>
<td align="left">TrainingTimesLastYear</td>
<td align="right">-0.05</td>
<td align="right">0.05</td>
<td align="right">-0.03</td>
</tr>
<tr>
<td align="left">WorkLifeBalance</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.06</td>
</tr>
<tr>
<td align="left">YearsAtCompany</td>
<td align="right">0.11</td>
<td align="right">-0.12</td>
<td align="right">12.27</td>
</tr>
<tr>
<td align="left">YearsInCurrentRole</td>
<td align="right">0.11</td>
<td align="right">-0.12</td>
<td align="right">4.48</td>
</tr>
<tr>
<td align="left">YearsSinceLastPromotion</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">5.51</td>
</tr>
<tr>
<td align="left">YearsWithCurrManager</td>
<td align="right">0.16</td>
<td align="right">-0.16</td>
<td align="right">4.52</td>
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
<td align="left">Age</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">1.34</td>
</tr>
<tr>
<td align="left">DailyRate</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">-0.12</td>
</tr>
<tr>
<td align="left">DistanceFromHome</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">0.13</td>
</tr>
<tr>
<td align="left">Education</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.08</td>
</tr>
<tr>
<td align="left">EmployeeCount</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">EmployeeNumber</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">-0.07</td>
</tr>
<tr>
<td align="left">EnvironmentSatisfaction</td>
<td align="right">-0.04</td>
<td align="right">0.05</td>
<td align="right">-0.06</td>
</tr>
<tr>
<td align="left">HourlyRate</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">0.10</td>
</tr>
<tr>
<td align="left">JobInvolvement</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.22</td>
</tr>
<tr>
<td align="left">JobLevel</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">1.88</td>
</tr>
<tr>
<td align="left">JobSatisfaction</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">-0.17</td>
</tr>
<tr>
<td align="left">MonthlyIncome</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">1.97</td>
</tr>
<tr>
<td align="left">MonthlyRate</td>
<td align="right">-0.85</td>
<td align="right">0.88</td>
<td align="right">0.17</td>
</tr>
<tr>
<td align="left">NumCompaniesWorked</td>
<td align="right">0.00</td>
<td align="right">-0.00</td>
<td align="right">0.31</td>
</tr>
<tr>
<td align="left">PercentSalaryHike</td>
<td align="right">0.04</td>
<td align="right">-0.04</td>
<td align="right">0.70</td>
</tr>
<tr>
<td align="left">PerformanceRating</td>
<td align="right">0.05</td>
<td align="right">-0.05</td>
<td align="right">0.81</td>
</tr>
<tr>
<td align="left">RelationshipSatisfaction</td>
<td align="right">0.03</td>
<td align="right">-0.03</td>
<td align="right">0.14</td>
</tr>
<tr>
<td align="left">StandardHours</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">StockOptionLevel</td>
<td align="right">0.04</td>
<td align="right">-0.04</td>
<td align="right">0.22</td>
</tr>
<tr>
<td align="left">TotalWorkingYears</td>
<td align="right">-0.02</td>
<td align="right">0.02</td>
<td align="right">2.25</td>
</tr>
<tr>
<td align="left">TrainingTimesLastYear</td>
<td align="right">-0.04</td>
<td align="right">0.04</td>
<td align="right">-0.02</td>
</tr>
<tr>
<td align="left">WorkLifeBalance</td>
<td align="right">0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.09</td>
</tr>
<tr>
<td align="left">YearsAtCompany</td>
<td align="right">0.02</td>
<td align="right">-0.02</td>
<td align="right">2.40</td>
</tr>
<tr>
<td align="left">YearsInCurrentRole</td>
<td align="right">0.03</td>
<td align="right">-0.03</td>
<td align="right">1.32</td>
</tr>
<tr>
<td align="left">YearsSinceLastPromotion</td>
<td align="right">-0.00</td>
<td align="right">0.00</td>
<td align="right">1.99</td>
</tr>
<tr>
<td align="left">YearsWithCurrManager</td>
<td align="right">0.05</td>
<td align="right">-0.05</td>
<td align="right">1.35</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-IBM-HR/figures/767d7304-c44f-4881-9f70-572529141df3.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-IBM-HR/figures/21644223-2a73-47e5-83d7-6d5f8fd31d13.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature MonthlyIncome e no grupo outlier, com valor de 8398.02. A maior variação negativa foi na feature MonthlyRate e no grupo 0, com o valor registrado de -6032.77</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">JobRole</th>
<th align="left">MaritalStatus</th>
<th align="left">Over18</th>
<th align="left">Attrition</th>
<th align="left">Department</th>
<th align="left">BusinessTravel</th>
<th align="left">EducationField</th>
<th align="left">OverTime</th>
<th align="left">Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Sales Executive</td>
<td align="left">Married</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Research &amp; Development</td>
<td align="left">Travel_Rarely</td>
<td align="left">Life Sciences</td>
<td align="left">No</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">156</td>
<td align="left">338</td>
<td align="left">710</td>
<td align="left">597</td>
<td align="left">451</td>
<td align="left">490</td>
<td align="left">295</td>
<td align="left">513</td>
<td align="left">443</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.227</td>
<td align="left">0.476</td>
<td align="left">1.0</td>
<td align="left">0.841</td>
<td align="left">0.657</td>
<td align="left">0.714</td>
<td align="left">0.43</td>
<td align="left">0.723</td>
<td align="left">0.624</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.002</td>
<td align="left">0.02</td>
<td align="left">0.0</td>
<td align="left">0.006</td>
<td align="left">0.001</td>
<td align="left">0.004</td>
<td align="left">0.016</td>
<td align="left">0.008</td>
<td align="left">0.022</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">JobRole</th>
<th align="left">MaritalStatus</th>
<th align="left">Over18</th>
<th align="left">Attrition</th>
<th align="left">Department</th>
<th align="left">BusinessTravel</th>
<th align="left">EducationField</th>
<th align="left">OverTime</th>
<th align="left">Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Sales Executive</td>
<td align="left">Married</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Research &amp; Development</td>
<td align="left">Travel_Rarely</td>
<td align="left">Life Sciences</td>
<td align="left">No</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">159</td>
<td align="left">299</td>
<td align="left">710</td>
<td align="left">569</td>
<td align="left">465</td>
<td align="left">501</td>
<td align="left">283</td>
<td align="left">484</td>
<td align="left">397</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.224</td>
<td align="left">0.436</td>
<td align="left">1.0</td>
<td align="left">0.829</td>
<td align="left">0.655</td>
<td align="left">0.706</td>
<td align="left">0.399</td>
<td align="left">0.706</td>
<td align="left">0.579</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.002</td>
<td align="left">-0.02</td>
<td align="left">0.0</td>
<td align="left">-0.006</td>
<td align="left">-0.001</td>
<td align="left">-0.004</td>
<td align="left">-0.015</td>
<td align="left">-0.009</td>
<td align="left">-0.023</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">JobRole</th>
<th align="left">MaritalStatus</th>
<th align="left">Over18</th>
<th align="left">Attrition</th>
<th align="left">Department</th>
<th align="left">BusinessTravel</th>
<th align="left">EducationField</th>
<th align="left">OverTime</th>
<th align="left">Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Human Resources</td>
<td align="left">Married</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Human Resources</td>
<td align="left">Travel_Frequently</td>
<td align="left">Other</td>
<td align="left">No</td>
<td align="left">Male</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.577</td>
<td align="left">0.531</td>
<td align="left">0.509</td>
<td align="left">0.512</td>
<td align="left">0.559</td>
<td align="left">0.525</td>
<td align="left">0.6</td>
<td align="left">0.515</td>
<td align="left">0.527</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">JobRole</th>
<th align="left">MaritalStatus</th>
<th align="left">Over18</th>
<th align="left">Attrition</th>
<th align="left">Department</th>
<th align="left">BusinessTravel</th>
<th align="left">EducationField</th>
<th align="left">OverTime</th>
<th align="left">Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Manager</td>
<td align="left">Single</td>
<td align="left">Y</td>
<td align="left">Yes</td>
<td align="left">Sales</td>
<td align="left">Non-Travel</td>
<td align="left">Life Sciences</td>
<td align="left">Yes</td>
<td align="left">Female</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.568</td>
<td align="left">0.526</td>
<td align="left">0.491</td>
<td align="left">0.509</td>
<td align="left">0.496</td>
<td align="left">0.5</td>
<td align="left">0.51</td>
<td align="left">0.506</td>
<td align="left">0.52</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média menor que a população: MonthlyRate</p>
<p>Grupo 1: <br>&emsp;Média maior que a população: MonthlyRate</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: Age<br>&emsp;Média maior que a população: JobLevel<br>&emsp;Média maior que a população: MonthlyIncome<br>&emsp;Média maior que a população: PercentSalaryHike<br>&emsp;Média maior que a população: PerformanceRating<br>&emsp;Média maior que a população: TotalWorkingYears<br>&emsp;Média maior que a população: YearsAtCompany<br>&emsp;Média maior que a população: YearsInCurrentRole<br>&emsp;Média maior que a população: YearsSinceLastPromotion<br>&emsp;Média maior que a população: YearsWithCurrManager</p>
