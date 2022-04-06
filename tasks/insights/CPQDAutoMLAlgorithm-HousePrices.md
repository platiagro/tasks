<h1>CPQD AutoML Algorithm - HousePrices</h1>
<h2>Análise de Outliers</h2>
<p>Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.</p>
<h3>DBscan</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método DBscan foram detectados 583 outliers neste dataset, correspondendo a uma proporção de 100.00% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">MSSubClass</th>
<th align="right">LotFrontage</th>
<th align="right">LotArea</th>
<th align="right">OverallQual</th>
<th align="right">OverallCond</th>
<th align="right">YearBuilt</th>
<th align="right">YearRemodAdd</th>
<th align="right">MasVnrArea</th>
<th align="right">BsmtFinSF1</th>
<th align="right">BsmtFinSF2</th>
<th align="right">BsmtUnfSF</th>
<th align="right">TotalBsmtSF</th>
<th align="right">1stFlrSF</th>
<th align="right">2ndFlrSF</th>
<th align="right">LowQualFinSF</th>
<th align="right">GrLivArea</th>
<th align="right">BsmtFullBath</th>
<th align="right">BsmtHalfBath</th>
<th align="right">FullBath</th>
<th align="right">HalfBath</th>
<th align="right">BedroomAbvGr</th>
<th align="right">KitchenAbvGr</th>
<th align="right">TotRmsAbvGrd</th>
<th align="right">Fireplaces</th>
<th align="right">GarageYrBlt</th>
<th align="right">GarageCars</th>
<th align="right">GarageArea</th>
<th align="right">WoodDeckSF</th>
<th align="right">OpenPorchSF</th>
<th align="right">EnclosedPorch</th>
<th align="right">3SsnPorch</th>
<th align="right">ScreenPorch</th>
<th align="right">PoolArea</th>
<th align="right">MoSold</th>
<th align="right">YrSold</th>
<th align="right">SalePrice</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
<td align="right">583.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">55.35</td>
<td align="right">75.96</td>
<td align="right">11549.43</td>
<td align="right">6.82</td>
<td align="right">5.51</td>
<td align="right">1978.12</td>
<td align="right">1989.22</td>
<td align="right">155.59</td>
<td align="right">526.86</td>
<td align="right">45.87</td>
<td align="right">646.91</td>
<td align="right">1219.64</td>
<td align="right">1310.38</td>
<td align="right">439.19</td>
<td align="right">4.73</td>
<td align="right">1754.30</td>
<td align="right">0.46</td>
<td align="right">0.07</td>
<td align="right">1.73</td>
<td align="right">0.49</td>
<td align="right">2.96</td>
<td align="right">1.01</td>
<td align="right">7.11</td>
<td align="right">1.15</td>
<td align="right">1981.82</td>
<td align="right">2.07</td>
<td align="right">548.50</td>
<td align="right">117.18</td>
<td align="right">58.16</td>
<td align="right">19.29</td>
<td align="right">3.54</td>
<td align="right">24.81</td>
<td align="right">5.64</td>
<td align="right">6.48</td>
<td align="right">2007.72</td>
<td align="right">222759.43</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">36.94</td>
<td align="right">27.21</td>
<td align="right">10602.91</td>
<td align="right">1.30</td>
<td align="right">1.00</td>
<td align="right">29.81</td>
<td align="right">19.58</td>
<td align="right">229.15</td>
<td align="right">542.35</td>
<td align="right">171.25</td>
<td align="right">467.57</td>
<td align="right">460.94</td>
<td align="right">411.38</td>
<td align="right">484.12</td>
<td align="right">44.12</td>
<td align="right">547.40</td>
<td align="right">0.52</td>
<td align="right">0.25</td>
<td align="right">0.53</td>
<td align="right">0.52</td>
<td align="right">0.76</td>
<td align="right">0.12</td>
<td align="right">1.57</td>
<td align="right">0.37</td>
<td align="right">25.65</td>
<td align="right">0.66</td>
<td align="right">201.84</td>
<td align="right">131.31</td>
<td align="right">71.15</td>
<td align="right">61.94</td>
<td align="right">28.89</td>
<td align="right">70.77</td>
<td align="right">55.66</td>
<td align="right">2.79</td>
<td align="right">1.32</td>
<td align="right">92364.18</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">20.00</td>
<td align="right">21.00</td>
<td align="right">1300.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">1880.00</td>
<td align="right">1950.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">360.00</td>
<td align="right">483.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">694.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">1900.00</td>
<td align="right">1.00</td>
<td align="right">164.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">2006.00</td>
<td align="right">62383.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">20.00</td>
<td align="right">60.00</td>
<td align="right">8425.00</td>
<td align="right">6.00</td>
<td align="right">5.00</td>
<td align="right">1959.00</td>
<td align="right">1976.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">289.50</td>
<td align="right">893.50</td>
<td align="right">1005.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1406.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">6.00</td>
<td align="right">1.00</td>
<td align="right">1964.50</td>
<td align="right">2.00</td>
<td align="right">430.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">5.00</td>
<td align="right">2007.00</td>
<td align="right">159975.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">60.00</td>
<td align="right">75.00</td>
<td align="right">10261.00</td>
<td align="right">7.00</td>
<td align="right">5.00</td>
<td align="right">1990.00</td>
<td align="right">1997.00</td>
<td align="right">16.00</td>
<td align="right">442.00</td>
<td align="right">0.00</td>
<td align="right">548.00</td>
<td align="right">1145.00</td>
<td align="right">1264.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1664.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">7.00</td>
<td align="right">1.00</td>
<td align="right">1992.00</td>
<td align="right">2.00</td>
<td align="right">516.00</td>
<td align="right">100.00</td>
<td align="right">40.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">6.00</td>
<td align="right">2008.00</td>
<td align="right">193500.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">60.00</td>
<td align="right">86.00</td>
<td align="right">12436.50</td>
<td align="right">8.00</td>
<td align="right">6.00</td>
<td align="right">2005.00</td>
<td align="right">2005.00</td>
<td align="right">256.00</td>
<td align="right">872.50</td>
<td align="right">0.00</td>
<td align="right">909.50</td>
<td align="right">1480.00</td>
<td align="right">1572.00</td>
<td align="right">839.00</td>
<td align="right">0.00</td>
<td align="right">1980.50</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">8.00</td>
<td align="right">1.00</td>
<td align="right">2005.00</td>
<td align="right">2.00</td>
<td align="right">672.00</td>
<td align="right">192.00</td>
<td align="right">82.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">8.00</td>
<td align="right">2009.00</td>
<td align="right">266250.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">190.00</td>
<td align="right">313.00</td>
<td align="right">215245.00</td>
<td align="right">10.00</td>
<td align="right">9.00</td>
<td align="right">2010.00</td>
<td align="right">2010.00</td>
<td align="right">1600.00</td>
<td align="right">5644.00</td>
<td align="right">1474.00</td>
<td align="right">2336.00</td>
<td align="right">6110.00</td>
<td align="right">4692.00</td>
<td align="right">2065.00</td>
<td align="right">572.00</td>
<td align="right">5642.00</td>
<td align="right">2.00</td>
<td align="right">2.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">5.00</td>
<td align="right">2.00</td>
<td align="right">12.00</td>
<td align="right">3.00</td>
<td align="right">2010.00</td>
<td align="right">4.00</td>
<td align="right">1418.00</td>
<td align="right">857.00</td>
<td align="right">547.00</td>
<td align="right">552.00</td>
<td align="right">407.00</td>
<td align="right">480.00</td>
<td align="right">648.00</td>
<td align="right">12.00</td>
<td align="right">2010.00</td>
<td align="right">755000.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: DBscan</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">LandSlope</th>
<th align="left">Neighborhood</th>
<th align="left">Fence</th>
<th align="left">GarageType</th>
<th align="left">BsmtFinType1</th>
<th align="left">LotConfig</th>
<th align="left">HeatingQC</th>
<th align="left">GarageFinish</th>
<th align="left">MSZoning</th>
<th align="left">RoofStyle</th>
<th align="left">FireplaceQu</th>
<th align="left">Condition2</th>
<th align="left">ExterCond</th>
<th align="left">Street</th>
<th align="left">MasVnrType</th>
<th align="left">GarageCond</th>
<th align="left">BldgType</th>
<th align="left">ExterQual</th>
<th align="left">LotShape</th>
<th align="left">Condition1</th>
<th align="left">GarageQual</th>
<th align="left">CentralAir</th>
<th align="left">BsmtQual</th>
<th align="left">RoofMatl</th>
<th align="left">Exterior1st</th>
<th align="left">KitchenQual</th>
<th align="left">Functional</th>
<th align="left">Alley</th>
<th align="left">Heating</th>
<th align="left">PavedDrive</th>
<th align="left">LandContour</th>
<th align="left">Foundation</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior2nd</th>
<th align="left">Electrical</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtExposure</th>
<th align="left">BsmtFinType2</th>
<th align="left">PoolQC</th>
<th align="left">Utilities</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
<td align="left">583</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">3</td>
<td align="left">25</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">12</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">15</td>
<td align="left">3</td>
<td align="left">8</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">1</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Gtl</td>
<td align="left">NAmes</td>
<td align="left">-</td>
<td align="left">Attchd</td>
<td align="left">GLQ</td>
<td align="left">Inside</td>
<td align="left">Ex</td>
<td align="left">Fin</td>
<td align="left">RL</td>
<td align="left">Gable</td>
<td align="left">Gd</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Pave</td>
<td align="left">None</td>
<td align="left">TA</td>
<td align="left">1Fam</td>
<td align="left">TA</td>
<td align="left">Reg</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">Gd</td>
<td align="left">CompShg</td>
<td align="left">VinylSd</td>
<td align="left">Gd</td>
<td align="left">Typ</td>
<td align="left">-</td>
<td align="left">GasA</td>
<td align="left">Y</td>
<td align="left">Lvl</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">SBrkr</td>
<td align="left">1Story</td>
<td align="left">No</td>
<td align="left">Unf</td>
<td align="left">-</td>
<td align="left">AllPub</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">552</td>
<td align="left">73</td>
<td align="left">484</td>
<td align="left">428</td>
<td align="left">205</td>
<td align="left">438</td>
<td align="left">362</td>
<td align="left">218</td>
<td align="left">508</td>
<td align="left">412</td>
<td align="left">315</td>
<td align="left">579</td>
<td align="left">530</td>
<td align="left">582</td>
<td align="left">284</td>
<td align="left">572</td>
<td align="left">510</td>
<td align="left">274</td>
<td align="left">351</td>
<td align="left">509</td>
<td align="left">556</td>
<td align="left">571</td>
<td align="left">278</td>
<td align="left">569</td>
<td align="left">239</td>
<td align="left">276</td>
<td align="left">551</td>
<td align="left">558</td>
<td align="left">574</td>
<td align="left">556</td>
<td align="left">518</td>
<td align="left">320</td>
<td align="left">534</td>
<td align="left">236</td>
<td align="left">559</td>
<td align="left">268</td>
<td align="left">362</td>
<td align="left">521</td>
<td align="left">577</td>
<td align="left">583</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/80d077b7-ddef-45f5-acb0-403d9c4eeac5.png" alt="Visualização dos outliers: DBscan" /></p>

<p><em>Visualização dos outliers: DBscan</em></p>
<h3>Isolation Forest</h3>
<p>Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.</p>
<p>Utilizando o método Isolation Forest foram detectados 30 outliers neste dataset, correspondendo a uma proporção de 5.15% do conjunto de amostras.</p>
<p>A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">MSSubClass</th>
<th align="right">LotFrontage</th>
<th align="right">LotArea</th>
<th align="right">OverallQual</th>
<th align="right">OverallCond</th>
<th align="right">YearBuilt</th>
<th align="right">YearRemodAdd</th>
<th align="right">MasVnrArea</th>
<th align="right">BsmtFinSF1</th>
<th align="right">BsmtFinSF2</th>
<th align="right">BsmtUnfSF</th>
<th align="right">TotalBsmtSF</th>
<th align="right">1stFlrSF</th>
<th align="right">2ndFlrSF</th>
<th align="right">LowQualFinSF</th>
<th align="right">GrLivArea</th>
<th align="right">BsmtFullBath</th>
<th align="right">BsmtHalfBath</th>
<th align="right">FullBath</th>
<th align="right">HalfBath</th>
<th align="right">BedroomAbvGr</th>
<th align="right">KitchenAbvGr</th>
<th align="right">TotRmsAbvGrd</th>
<th align="right">Fireplaces</th>
<th align="right">GarageYrBlt</th>
<th align="right">GarageCars</th>
<th align="right">GarageArea</th>
<th align="right">WoodDeckSF</th>
<th align="right">OpenPorchSF</th>
<th align="right">EnclosedPorch</th>
<th align="right">3SsnPorch</th>
<th align="right">ScreenPorch</th>
<th align="right">PoolArea</th>
<th align="right">MoSold</th>
<th align="right">YrSold</th>
<th align="right">SalePrice</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
<td align="right">30.00</td>
</tr>
<tr>
<td align="left">mean</td>
<td align="right">81.67</td>
<td align="right">94.13</td>
<td align="right">27658.83</td>
<td align="right">7.77</td>
<td align="right">5.60</td>
<td align="right">1954.47</td>
<td align="right">1987.90</td>
<td align="right">288.97</td>
<td align="right">963.57</td>
<td align="right">67.07</td>
<td align="right">644.47</td>
<td align="right">1675.10</td>
<td align="right">1760.10</td>
<td align="right">950.63</td>
<td align="right">45.37</td>
<td align="right">2756.10</td>
<td align="right">0.63</td>
<td align="right">0.10</td>
<td align="right">2.10</td>
<td align="right">0.67</td>
<td align="right">3.40</td>
<td align="right">1.27</td>
<td align="right">9.27</td>
<td align="right">1.53</td>
<td align="right">1975.30</td>
<td align="right">2.43</td>
<td align="right">711.47</td>
<td align="right">156.27</td>
<td align="right">107.63</td>
<td align="right">56.53</td>
<td align="right">0.00</td>
<td align="right">81.30</td>
<td align="right">68.87</td>
<td align="right">5.57</td>
<td align="right">2007.77</td>
<td align="right">333064.53</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">57.99</td>
<td align="right">53.33</td>
<td align="right">38705.76</td>
<td align="right">1.91</td>
<td align="right">1.54</td>
<td align="right">46.01</td>
<td align="right">20.20</td>
<td align="right">419.40</td>
<td align="right">1163.48</td>
<td align="right">193.14</td>
<td align="right">525.32</td>
<td align="right">1080.00</td>
<td align="right">749.62</td>
<td align="right">629.77</td>
<td align="right">141.02</td>
<td align="right">1044.09</td>
<td align="right">0.72</td>
<td align="right">0.31</td>
<td align="right">0.88</td>
<td align="right">0.55</td>
<td align="right">1.13</td>
<td align="right">0.45</td>
<td align="right">2.18</td>
<td align="right">0.57</td>
<td align="right">33.37</td>
<td align="right">0.68</td>
<td align="right">242.90</td>
<td align="right">200.79</td>
<td align="right">152.57</td>
<td align="right">133.58</td>
<td align="right">0.00</td>
<td align="right">145.42</td>
<td align="right">178.85</td>
<td align="right">2.96</td>
<td align="right">1.33</td>
<td align="right">199211.31</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">20.00</td>
<td align="right">47.00</td>
<td align="right">6120.00</td>
<td align="right">5.00</td>
<td align="right">3.00</td>
<td align="right">1880.00</td>
<td align="right">1950.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">360.00</td>
<td align="right">964.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1077.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">5.00</td>
<td align="right">1.00</td>
<td align="right">1900.00</td>
<td align="right">1.00</td>
<td align="right">205.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">2006.00</td>
<td align="right">118000.00</td>
</tr>
<tr>
<td align="left">25%</td>
<td align="right">52.50</td>
<td align="right">60.00</td>
<td align="right">10800.00</td>
<td align="right">6.00</td>
<td align="right">5.00</td>
<td align="right">1910.00</td>
<td align="right">1972.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">184.50</td>
<td align="right">1014.75</td>
<td align="right">1310.25</td>
<td align="right">658.75</td>
<td align="right">0.00</td>
<td align="right">1943.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">8.00</td>
<td align="right">1.00</td>
<td align="right">1960.75</td>
<td align="right">2.00</td>
<td align="right">522.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">4.00</td>
<td align="right">2007.00</td>
<td align="right">160750.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">60.00</td>
<td align="right">75.50</td>
<td align="right">14661.00</td>
<td align="right">7.50</td>
<td align="right">5.00</td>
<td align="right">1964.00</td>
<td align="right">1996.00</td>
<td align="right">0.00</td>
<td align="right">820.50</td>
<td align="right">0.00</td>
<td align="right">474.00</td>
<td align="right">1401.00</td>
<td align="right">1578.00</td>
<td align="right">1041.00</td>
<td align="right">0.00</td>
<td align="right">2707.50</td>
<td align="right">0.50</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">10.00</td>
<td align="right">1.50</td>
<td align="right">1984.50</td>
<td align="right">2.00</td>
<td align="right">733.50</td>
<td align="right">112.50</td>
<td align="right">56.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">6.00</td>
<td align="right">2008.00</td>
<td align="right">253000.00</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">75.00</td>
<td align="right">104.75</td>
<td align="right">32704.50</td>
<td align="right">10.00</td>
<td align="right">6.00</td>
<td align="right">2001.25</td>
<td align="right">2003.00</td>
<td align="right">558.25</td>
<td align="right">1408.75</td>
<td align="right">0.00</td>
<td align="right">979.75</td>
<td align="right">1929.00</td>
<td align="right">1935.00</td>
<td align="right">1384.00</td>
<td align="right">0.00</td>
<td align="right">3133.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">4.00</td>
<td align="right">1.75</td>
<td align="right">11.00</td>
<td align="right">2.00</td>
<td align="right">2003.00</td>
<td align="right">3.00</td>
<td align="right">840.75</td>
<td align="right">204.00</td>
<td align="right">103.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">152.25</td>
<td align="right">0.00</td>
<td align="right">7.00</td>
<td align="right">2009.00</td>
<td align="right">482500.00</td>
</tr>
<tr>
<td align="left">max</td>
<td align="right">190.00</td>
<td align="right">313.00</td>
<td align="right">215245.00</td>
<td align="right">10.00</td>
<td align="right">9.00</td>
<td align="right">2009.00</td>
<td align="right">2010.00</td>
<td align="right">1378.00</td>
<td align="right">5644.00</td>
<td align="right">820.00</td>
<td align="right">1926.00</td>
<td align="right">6110.00</td>
<td align="right">4692.00</td>
<td align="right">2065.00</td>
<td align="right">572.00</td>
<td align="right">5642.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">2.00</td>
<td align="right">5.00</td>
<td align="right">2.00</td>
<td align="right">12.00</td>
<td align="right">3.00</td>
<td align="right">2009.00</td>
<td align="right">4.00</td>
<td align="right">1418.00</td>
<td align="right">857.00</td>
<td align="right">547.00</td>
<td align="right">552.00</td>
<td align="right">0.00</td>
<td align="right">480.00</td>
<td align="right">555.00</td>
<td align="right">11.00</td>
<td align="right">2010.00</td>
<td align="right">755000.00</td>
</tr>
</tbody>
</table><p><em>Descrição Features Numéricas dos Outliers: Isolation Forest</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">LandSlope</th>
<th align="left">Neighborhood</th>
<th align="left">Fence</th>
<th align="left">GarageType</th>
<th align="left">BsmtFinType1</th>
<th align="left">LotConfig</th>
<th align="left">HeatingQC</th>
<th align="left">GarageFinish</th>
<th align="left">MSZoning</th>
<th align="left">RoofStyle</th>
<th align="left">FireplaceQu</th>
<th align="left">Condition2</th>
<th align="left">ExterCond</th>
<th align="left">Street</th>
<th align="left">MasVnrType</th>
<th align="left">GarageCond</th>
<th align="left">BldgType</th>
<th align="left">ExterQual</th>
<th align="left">LotShape</th>
<th align="left">Condition1</th>
<th align="left">GarageQual</th>
<th align="left">CentralAir</th>
<th align="left">BsmtQual</th>
<th align="left">RoofMatl</th>
<th align="left">Exterior1st</th>
<th align="left">KitchenQual</th>
<th align="left">Functional</th>
<th align="left">Alley</th>
<th align="left">Heating</th>
<th align="left">PavedDrive</th>
<th align="left">LandContour</th>
<th align="left">Foundation</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior2nd</th>
<th align="left">Electrical</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtExposure</th>
<th align="left">BsmtFinType2</th>
<th align="left">PoolQC</th>
<th align="left">Utilities</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">count</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
<td align="left">30</td>
</tr>
<tr>
<td align="left">unique</td>
<td align="left">3</td>
<td align="left">13</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">9</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">10</td>
<td align="left">3</td>
<td align="left">7</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">1</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Gtl</td>
<td align="left">OldTown</td>
<td align="left">-</td>
<td align="left">Detchd</td>
<td align="left">GLQ</td>
<td align="left">Inside</td>
<td align="left">Ex</td>
<td align="left">Unf</td>
<td align="left">RL</td>
<td align="left">Gable</td>
<td align="left">Gd</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Pave</td>
<td align="left">None</td>
<td align="left">TA</td>
<td align="left">1Fam</td>
<td align="left">TA</td>
<td align="left">Reg</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">TA</td>
<td align="left">CompShg</td>
<td align="left">Wd Sdng</td>
<td align="left">TA</td>
<td align="left">Typ</td>
<td align="left">-</td>
<td align="left">GasA</td>
<td align="left">Y</td>
<td align="left">Lvl</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">Wd Sdng</td>
<td align="left">SBrkr</td>
<td align="left">2Story</td>
<td align="left">No</td>
<td align="left">Unf</td>
<td align="left">-</td>
<td align="left">AllPub</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">27</td>
<td align="left">10</td>
<td align="left">23</td>
<td align="left">12</td>
<td align="left">12</td>
<td align="left">17</td>
<td align="left">17</td>
<td align="left">13</td>
<td align="left">21</td>
<td align="left">15</td>
<td align="left">16</td>
<td align="left">27</td>
<td align="left">23</td>
<td align="left">29</td>
<td align="left">17</td>
<td align="left">29</td>
<td align="left">23</td>
<td align="left">12</td>
<td align="left">15</td>
<td align="left">19</td>
<td align="left">23</td>
<td align="left">25</td>
<td align="left">12</td>
<td align="left">26</td>
<td align="left">9</td>
<td align="left">12</td>
<td align="left">26</td>
<td align="left">27</td>
<td align="left">26</td>
<td align="left">26</td>
<td align="left">21</td>
<td align="left">12</td>
<td align="left">27</td>
<td align="left">8</td>
<td align="left">27</td>
<td align="left">13</td>
<td align="left">14</td>
<td align="left">26</td>
<td align="left">26</td>
<td align="left">30</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/0cb2b2cc-2fbd-42a7-a908-4252bbacefcb.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['MSSubClass', 'OverallCond', 'FullBath'] com uma quantidade de 6 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(260062.2, 358901.8]</td>
<td align="right">0.36</td>
<td align="right">0.47</td>
<td align="right">0.00</td>
<td align="right">0.11</td>
<td align="right">0.04</td>
<td align="right">0.02</td>
</tr>
<tr>
<td align="left">(457741.4, 556581.0]</td>
<td align="right">0.50</td>
<td align="right">0.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(358901.8, 457741.4]</td>
<td align="right">0.57</td>
<td align="right">0.31</td>
<td align="right">0.00</td>
<td align="right">0.06</td>
<td align="right">0.03</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">(161222.6, 260062.2]</td>
<td align="right">0.33</td>
<td align="right">0.37</td>
<td align="right">0.01</td>
<td align="right">0.11</td>
<td align="right">0.13</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="left">(61888.802, 161222.6]</td>
<td align="right">0.44</td>
<td align="right">0.05</td>
<td align="right">0.09</td>
<td align="right">0.05</td>
<td align="right">0.12</td>
<td align="right">0.25</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MoSold', 'YrSold', 'SalePrice'] com uma quantidade de 6 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(260062.2, 358901.8]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.52</td>
<td align="right">0.00</td>
<td align="right">0.48</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(457741.4, 556581.0]</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(358901.8, 457741.4]</td>
<td align="right">0.91</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.09</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(161222.6, 260062.2]</td>
<td align="right">0.00</td>
<td align="right">0.55</td>
<td align="right">0.09</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.36</td>
</tr>
<tr>
<td align="left">(61888.802, 161222.6]</td>
<td align="right">0.00</td>
<td align="right">0.21</td>
<td align="right">0.00</td>
<td align="right">0.79</td>
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
<td align="left">MSSubClass - OverallCond - FullBath</td>
<td align="right">0.89</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">MasVnrArea - TotRmsAbvGrd - OpenPorchSF</td>
<td align="right">0.51</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">YearBuilt - BsmtUnfSF - PoolArea</td>
<td align="right">0.49</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">MSSubClass - LotFrontage - LotArea - OverallQual - OverallCond - YearBuilt - YearRemodAdd - MasVnrArea - BsmtFinSF1 - BsmtFinSF2 - BsmtUnfSF - TotalBsmtSF - 1stFlrSF - 2ndFlrSF - LowQualFinSF - GrLivArea - BsmtFullBath - BsmtHalfBath - FullBath - HalfBath - BedroomAbvGr - KitchenAbvGr - TotRmsAbvGrd - Fireplaces - GarageYrBlt - GarageCars - GarageArea - WoodDeckSF - OpenPorchSF - EnclosedPorch - 3SsnPorch - ScreenPorch - PoolArea - MoSold - YrSold - SalePrice</td>
<td align="right">nan</td>
<td align="right">0.54</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MSSubClass</td>
<td align="right">-14.22</td>
<td align="right">2.82</td>
<td align="right">-1.99</td>
<td align="right">0.55</td>
<td align="right">-3.00</td>
<td align="right">2.60</td>
<td align="right">27.74</td>
</tr>
<tr>
<td align="left">LotFrontage</td>
<td align="right">10.53</td>
<td align="right">-2.40</td>
<td align="right">8.35</td>
<td align="right">-11.36</td>
<td align="right">11.25</td>
<td align="right">0.97</td>
<td align="right">19.16</td>
</tr>
<tr>
<td align="left">LotArea</td>
<td align="right">3457.68</td>
<td align="right">-843.42</td>
<td align="right">1376.80</td>
<td align="right">-2147.08</td>
<td align="right">1434.93</td>
<td align="right">940.23</td>
<td align="right">16983.33</td>
</tr>
<tr>
<td align="left">OverallQual</td>
<td align="right">1.94</td>
<td align="right">-0.54</td>
<td align="right">0.91</td>
<td align="right">-1.24</td>
<td align="right">1.47</td>
<td align="right">0.20</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">OverallCond</td>
<td align="right">-0.51</td>
<td align="right">0.16</td>
<td align="right">-0.18</td>
<td align="right">0.18</td>
<td align="right">-0.27</td>
<td align="right">-0.03</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">YearBuilt</td>
<td align="right">26.18</td>
<td align="right">-3.98</td>
<td align="right">16.67</td>
<td align="right">-27.94</td>
<td align="right">18.49</td>
<td align="right">7.24</td>
<td align="right">-24.94</td>
</tr>
<tr>
<td align="left">YearRemodAdd</td>
<td align="right">17.18</td>
<td align="right">-2.45</td>
<td align="right">12.10</td>
<td align="right">-21.02</td>
<td align="right">13.15</td>
<td align="right">6.14</td>
<td align="right">-1.39</td>
</tr>
<tr>
<td align="left">MasVnrArea</td>
<td align="right">257.58</td>
<td align="right">-46.04</td>
<td align="right">66.70</td>
<td align="right">-107.41</td>
<td align="right">132.96</td>
<td align="right">-9.11</td>
<td align="right">140.61</td>
</tr>
<tr>
<td align="left">BsmtFinSF1</td>
<td align="right">562.30</td>
<td align="right">-121.36</td>
<td align="right">42.42</td>
<td align="right">-162.10</td>
<td align="right">355.72</td>
<td align="right">-19.39</td>
<td align="right">460.40</td>
</tr>
<tr>
<td align="left">BsmtFinSF2</td>
<td align="right">-39.42</td>
<td align="right">8.45</td>
<td align="right">-16.33</td>
<td align="right">-7.87</td>
<td align="right">-17.42</td>
<td align="right">31.72</td>
<td align="right">22.35</td>
</tr>
<tr>
<td align="left">BsmtUnfSF</td>
<td align="right">116.51</td>
<td align="right">-50.49</td>
<td align="right">167.14</td>
<td align="right">-93.68</td>
<td align="right">-16.47</td>
<td align="right">33.33</td>
<td align="right">-2.58</td>
</tr>
<tr>
<td align="left">TotalBsmtSF</td>
<td align="right">639.39</td>
<td align="right">-163.40</td>
<td align="right">193.23</td>
<td align="right">-263.65</td>
<td align="right">321.83</td>
<td align="right">45.67</td>
<td align="right">480.17</td>
</tr>
<tr>
<td align="left">1stFlrSF</td>
<td align="right">561.96</td>
<td align="right">-129.81</td>
<td align="right">142.25</td>
<td align="right">-242.49</td>
<td align="right">272.51</td>
<td align="right">56.85</td>
<td align="right">474.11</td>
</tr>
<tr>
<td align="left">2ndFlrSF</td>
<td align="right">-62.97</td>
<td align="right">-42.62</td>
<td align="right">127.47</td>
<td align="right">-153.76</td>
<td align="right">223.74</td>
<td align="right">52.66</td>
<td align="right">539.19</td>
</tr>
<tr>
<td align="left">LowQualFinSF</td>
<td align="right">-2.52</td>
<td align="right">2.07</td>
<td align="right">-2.52</td>
<td align="right">2.62</td>
<td align="right">-2.52</td>
<td align="right">-2.52</td>
<td align="right">42.84</td>
</tr>
<tr>
<td align="left">GrLivArea</td>
<td align="right">496.46</td>
<td align="right">-170.36</td>
<td align="right">267.20</td>
<td align="right">-393.62</td>
<td align="right">493.73</td>
<td align="right">106.98</td>
<td align="right">1056.15</td>
</tr>
<tr>
<td align="left">BsmtFullBath</td>
<td align="right">0.35</td>
<td align="right">-0.12</td>
<td align="right">0.07</td>
<td align="right">-0.12</td>
<td align="right">0.33</td>
<td align="right">-0.00</td>
<td align="right">0.19</td>
</tr>
<tr>
<td align="left">BsmtHalfBath</td>
<td align="right">-0.03</td>
<td align="right">0.06</td>
<td align="right">-0.05</td>
<td align="right">0.01</td>
<td align="right">-0.06</td>
<td align="right">-0.02</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">FullBath</td>
<td align="right">0.26</td>
<td align="right">-0.03</td>
<td align="right">0.25</td>
<td align="right">-0.49</td>
<td align="right">0.33</td>
<td align="right">0.16</td>
<td align="right">0.39</td>
</tr>
<tr>
<td align="left">HalfBath</td>
<td align="right">0.08</td>
<td align="right">0.06</td>
<td align="right">0.07</td>
<td align="right">-0.23</td>
<td align="right">0.08</td>
<td align="right">0.03</td>
<td align="right">0.19</td>
</tr>
<tr>
<td align="left">BedroomAbvGr</td>
<td align="right">-0.23</td>
<td align="right">-0.04</td>
<td align="right">0.05</td>
<td align="right">-0.08</td>
<td align="right">0.23</td>
<td align="right">0.09</td>
<td align="right">0.47</td>
</tr>
<tr>
<td align="left">KitchenAbvGr</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.27</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd</td>
<td align="right">1.30</td>
<td align="right">-0.33</td>
<td align="right">0.64</td>
<td align="right">-1.01</td>
<td align="right">1.25</td>
<td align="right">0.11</td>
<td align="right">2.28</td>
</tr>
<tr>
<td align="left">Fireplaces</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.06</td>
<td align="right">-0.03</td>
<td align="right">0.13</td>
<td align="right">0.03</td>
<td align="right">0.41</td>
</tr>
<tr>
<td align="left">GarageYrBlt</td>
<td align="right">23.62</td>
<td align="right">-4.08</td>
<td align="right">15.50</td>
<td align="right">-22.89</td>
<td align="right">15.85</td>
<td align="right">4.71</td>
<td align="right">-6.87</td>
</tr>
<tr>
<td align="left">GarageCars</td>
<td align="right">0.89</td>
<td align="right">-0.16</td>
<td align="right">0.41</td>
<td align="right">-0.67</td>
<td align="right">0.62</td>
<td align="right">0.08</td>
<td align="right">0.38</td>
</tr>
<tr>
<td align="left">GarageArea</td>
<td align="right">277.08</td>
<td align="right">-79.56</td>
<td align="right">139.00</td>
<td align="right">-155.58</td>
<td align="right">178.73</td>
<td align="right">17.08</td>
<td align="right">171.81</td>
</tr>
<tr>
<td align="left">WoodDeckSF</td>
<td align="right">73.32</td>
<td align="right">-24.12</td>
<td align="right">33.03</td>
<td align="right">-41.28</td>
<td align="right">72.20</td>
<td align="right">-0.69</td>
<td align="right">41.21</td>
</tr>
<tr>
<td align="left">OpenPorchSF</td>
<td align="right">30.40</td>
<td align="right">-11.12</td>
<td align="right">21.27</td>
<td align="right">-32.46</td>
<td align="right">27.04</td>
<td align="right">15.62</td>
<td align="right">52.16</td>
</tr>
<tr>
<td align="left">EnclosedPorch</td>
<td align="right">-11.33</td>
<td align="right">0.87</td>
<td align="right">-11.15</td>
<td align="right">19.20</td>
<td align="right">-10.27</td>
<td align="right">-5.56</td>
<td align="right">39.26</td>
</tr>
<tr>
<td align="left">3SsnPorch</td>
<td align="right">9.71</td>
<td align="right">0.23</td>
<td align="right">-3.74</td>
<td align="right">-2.33</td>
<td align="right">-0.62</td>
<td align="right">2.42</td>
<td align="right">-3.74</td>
</tr>
<tr>
<td align="left">ScreenPorch</td>
<td align="right">-6.04</td>
<td align="right">9.10</td>
<td align="right">3.83</td>
<td align="right">-10.87</td>
<td align="right">-6.45</td>
<td align="right">-1.02</td>
<td align="right">59.56</td>
</tr>
<tr>
<td align="left">PoolArea</td>
<td align="right">-2.21</td>
<td align="right">4.78</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">66.65</td>
</tr>
<tr>
<td align="left">MoSold</td>
<td align="right">0.05</td>
<td align="right">-0.25</td>
<td align="right">0.32</td>
<td align="right">-0.30</td>
<td align="right">0.43</td>
<td align="right">0.30</td>
<td align="right">-0.97</td>
</tr>
<tr>
<td align="left">YrSold</td>
<td align="right">0.25</td>
<td align="right">-0.03</td>
<td align="right">-0.02</td>
<td align="right">0.04</td>
<td align="right">0.00</td>
<td align="right">-0.07</td>
<td align="right">0.05</td>
</tr>
<tr>
<td align="left">SalePrice</td>
<td align="right">189479.66</td>
<td align="right">-41819.20</td>
<td align="right">53403.26</td>
<td align="right">-86989.49</td>
<td align="right">109321.50</td>
<td align="right">7412.86</td>
<td align="right">116289.11</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MSSubClass</td>
<td align="right">-0.41</td>
<td align="right">0.08</td>
<td align="right">-0.06</td>
<td align="right">0.02</td>
<td align="right">-0.09</td>
<td align="right">0.07</td>
<td align="right">0.79</td>
</tr>
<tr>
<td align="left">LotFrontage</td>
<td align="right">0.43</td>
<td align="right">-0.10</td>
<td align="right">0.34</td>
<td align="right">-0.46</td>
<td align="right">0.45</td>
<td align="right">0.04</td>
<td align="right">0.77</td>
</tr>
<tr>
<td align="left">LotArea</td>
<td align="right">0.69</td>
<td align="right">-0.17</td>
<td align="right">0.28</td>
<td align="right">-0.43</td>
<td align="right">0.29</td>
<td align="right">0.19</td>
<td align="right">3.40</td>
</tr>
<tr>
<td align="left">OverallQual</td>
<td align="right">1.57</td>
<td align="right">-0.44</td>
<td align="right">0.73</td>
<td align="right">-1.01</td>
<td align="right">1.19</td>
<td align="right">0.16</td>
<td align="right">0.81</td>
</tr>
<tr>
<td align="left">OverallCond</td>
<td align="right">-0.53</td>
<td align="right">0.17</td>
<td align="right">-0.19</td>
<td align="right">0.19</td>
<td align="right">-0.28</td>
<td align="right">-0.03</td>
<td align="right">0.10</td>
</tr>
<tr>
<td align="left">YearBuilt</td>
<td align="right">0.93</td>
<td align="right">-0.14</td>
<td align="right">0.59</td>
<td align="right">-0.99</td>
<td align="right">0.66</td>
<td align="right">0.26</td>
<td align="right">-0.89</td>
</tr>
<tr>
<td align="left">YearRemodAdd</td>
<td align="right">0.88</td>
<td align="right">-0.13</td>
<td align="right">0.62</td>
<td align="right">-1.08</td>
<td align="right">0.67</td>
<td align="right">0.31</td>
<td align="right">-0.07</td>
</tr>
<tr>
<td align="left">MasVnrArea</td>
<td align="right">1.21</td>
<td align="right">-0.22</td>
<td align="right">0.31</td>
<td align="right">-0.51</td>
<td align="right">0.63</td>
<td align="right">-0.04</td>
<td align="right">0.66</td>
</tr>
<tr>
<td align="left">BsmtFinSF1</td>
<td align="right">1.18</td>
<td align="right">-0.25</td>
<td align="right">0.09</td>
<td align="right">-0.34</td>
<td align="right">0.75</td>
<td align="right">-0.04</td>
<td align="right">0.96</td>
</tr>
<tr>
<td align="left">BsmtFinSF2</td>
<td align="right">-0.23</td>
<td align="right">0.05</td>
<td align="right">-0.10</td>
<td align="right">-0.05</td>
<td align="right">-0.10</td>
<td align="right">0.19</td>
<td align="right">0.13</td>
</tr>
<tr>
<td align="left">BsmtUnfSF</td>
<td align="right">0.25</td>
<td align="right">-0.11</td>
<td align="right">0.36</td>
<td align="right">-0.20</td>
<td align="right">-0.04</td>
<td align="right">0.07</td>
<td align="right">-0.01</td>
</tr>
<tr>
<td align="left">TotalBsmtSF</td>
<td align="right">1.65</td>
<td align="right">-0.42</td>
<td align="right">0.50</td>
<td align="right">-0.68</td>
<td align="right">0.83</td>
<td align="right">0.12</td>
<td align="right">1.24</td>
</tr>
<tr>
<td align="left">1stFlrSF</td>
<td align="right">1.52</td>
<td align="right">-0.35</td>
<td align="right">0.38</td>
<td align="right">-0.65</td>
<td align="right">0.74</td>
<td align="right">0.15</td>
<td align="right">1.28</td>
</tr>
<tr>
<td align="left">2ndFlrSF</td>
<td align="right">-0.14</td>
<td align="right">-0.09</td>
<td align="right">0.28</td>
<td align="right">-0.33</td>
<td align="right">0.49</td>
<td align="right">0.11</td>
<td align="right">1.17</td>
</tr>
<tr>
<td align="left">LowQualFinSF</td>
<td align="right">-0.08</td>
<td align="right">0.07</td>
<td align="right">-0.08</td>
<td align="right">0.09</td>
<td align="right">-0.08</td>
<td align="right">-0.08</td>
<td align="right">1.42</td>
</tr>
<tr>
<td align="left">GrLivArea</td>
<td align="right">1.11</td>
<td align="right">-0.38</td>
<td align="right">0.60</td>
<td align="right">-0.88</td>
<td align="right">1.10</td>
<td align="right">0.24</td>
<td align="right">2.36</td>
</tr>
<tr>
<td align="left">BsmtFullBath</td>
<td align="right">0.68</td>
<td align="right">-0.23</td>
<td align="right">0.13</td>
<td align="right">-0.25</td>
<td align="right">0.65</td>
<td align="right">-0.01</td>
<td align="right">0.37</td>
</tr>
<tr>
<td align="left">BsmtHalfBath</td>
<td align="right">-0.14</td>
<td align="right">0.23</td>
<td align="right">-0.20</td>
<td align="right">0.03</td>
<td align="right">-0.25</td>
<td align="right">-0.08</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">FullBath</td>
<td align="right">0.52</td>
<td align="right">-0.06</td>
<td align="right">0.51</td>
<td align="right">-1.00</td>
<td align="right">0.66</td>
<td align="right">0.33</td>
<td align="right">0.79</td>
</tr>
<tr>
<td align="left">HalfBath</td>
<td align="right">0.16</td>
<td align="right">0.12</td>
<td align="right">0.14</td>
<td align="right">-0.44</td>
<td align="right">0.15</td>
<td align="right">0.05</td>
<td align="right">0.37</td>
</tr>
<tr>
<td align="left">BedroomAbvGr</td>
<td align="right">-0.31</td>
<td align="right">-0.06</td>
<td align="right">0.07</td>
<td align="right">-0.11</td>
<td align="right">0.32</td>
<td align="right">0.12</td>
<td align="right">0.64</td>
</tr>
<tr>
<td align="left">KitchenAbvGr</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">nan</td>
<td align="right">inf</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd</td>
<td align="right">0.90</td>
<td align="right">-0.23</td>
<td align="right">0.44</td>
<td align="right">-0.70</td>
<td align="right">0.87</td>
<td align="right">0.07</td>
<td align="right">1.58</td>
</tr>
<tr>
<td align="left">Fireplaces</td>
<td align="right">-0.02</td>
<td align="right">-0.03</td>
<td align="right">-0.18</td>
<td align="right">-0.08</td>
<td align="right">0.39</td>
<td align="right">0.10</td>
<td align="right">1.18</td>
</tr>
<tr>
<td align="left">GarageYrBlt</td>
<td align="right">0.94</td>
<td align="right">-0.16</td>
<td align="right">0.62</td>
<td align="right">-0.91</td>
<td align="right">0.63</td>
<td align="right">0.19</td>
<td align="right">-0.27</td>
</tr>
<tr>
<td align="left">GarageCars</td>
<td align="right">1.37</td>
<td align="right">-0.24</td>
<td align="right">0.64</td>
<td align="right">-1.02</td>
<td align="right">0.95</td>
<td align="right">0.12</td>
<td align="right">0.59</td>
</tr>
<tr>
<td align="left">GarageArea</td>
<td align="right">1.42</td>
<td align="right">-0.41</td>
<td align="right">0.71</td>
<td align="right">-0.80</td>
<td align="right">0.91</td>
<td align="right">0.09</td>
<td align="right">0.88</td>
</tr>
<tr>
<td align="left">WoodDeckSF</td>
<td align="right">0.58</td>
<td align="right">-0.19</td>
<td align="right">0.26</td>
<td align="right">-0.33</td>
<td align="right">0.57</td>
<td align="right">-0.01</td>
<td align="right">0.33</td>
</tr>
<tr>
<td align="left">OpenPorchSF</td>
<td align="right">0.48</td>
<td align="right">-0.18</td>
<td align="right">0.34</td>
<td align="right">-0.52</td>
<td align="right">0.43</td>
<td align="right">0.25</td>
<td align="right">0.83</td>
</tr>
<tr>
<td align="left">EnclosedPorch</td>
<td align="right">-0.21</td>
<td align="right">0.02</td>
<td align="right">-0.20</td>
<td align="right">0.35</td>
<td align="right">-0.19</td>
<td align="right">-0.10</td>
<td align="right">0.71</td>
</tr>
<tr>
<td align="left">3SsnPorch</td>
<td align="right">0.33</td>
<td align="right">0.01</td>
<td align="right">-0.13</td>
<td align="right">-0.08</td>
<td align="right">-0.02</td>
<td align="right">0.08</td>
<td align="right">-0.13</td>
</tr>
<tr>
<td align="left">ScreenPorch</td>
<td align="right">-0.10</td>
<td align="right">0.14</td>
<td align="right">0.06</td>
<td align="right">-0.17</td>
<td align="right">-0.10</td>
<td align="right">-0.02</td>
<td align="right">0.94</td>
</tr>
<tr>
<td align="left">PoolArea</td>
<td align="right">-0.06</td>
<td align="right">0.13</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">1.81</td>
</tr>
<tr>
<td align="left">MoSold</td>
<td align="right">0.02</td>
<td align="right">-0.09</td>
<td align="right">0.11</td>
<td align="right">-0.11</td>
<td align="right">0.15</td>
<td align="right">0.11</td>
<td align="right">-0.35</td>
</tr>
<tr>
<td align="left">YrSold</td>
<td align="right">0.19</td>
<td align="right">-0.02</td>
<td align="right">-0.02</td>
<td align="right">0.03</td>
<td align="right">0.00</td>
<td align="right">-0.05</td>
<td align="right">0.03</td>
</tr>
<tr>
<td align="left">SalePrice</td>
<td align="right">2.41</td>
<td align="right">-0.53</td>
<td align="right">0.68</td>
<td align="right">-1.10</td>
<td align="right">1.39</td>
<td align="right">0.09</td>
<td align="right">1.48</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/feb9f9b2-05be-4544-9710-2ae6ae566848.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/6c7b9945-a368-40eb-bdfc-07ed0fd84d1e.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature SalePrice e no grupo 0, com valor de 189479.66. A maior variação negativa foi na feature SalePrice e no grupo 3, com o valor registrado de -86989.49</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">LandSlope</th>
<th align="left">Neighborhood</th>
<th align="left">Fence</th>
<th align="left">GarageType</th>
<th align="left">BsmtFinType1</th>
<th align="left">LotConfig</th>
<th align="left">HeatingQC</th>
<th align="left">GarageFinish</th>
<th align="left">MSZoning</th>
<th align="left">RoofStyle</th>
<th align="left">FireplaceQu</th>
<th align="left">Condition2</th>
<th align="left">ExterCond</th>
<th align="left">Street</th>
<th align="left">MasVnrType</th>
<th align="left">GarageCond</th>
<th align="left">BldgType</th>
<th align="left">ExterQual</th>
<th align="left">LotShape</th>
<th align="left">Condition1</th>
<th align="left">GarageQual</th>
<th align="left">CentralAir</th>
<th align="left">BsmtQual</th>
<th align="left">RoofMatl</th>
<th align="left">Exterior1st</th>
<th align="left">KitchenQual</th>
<th align="left">Functional</th>
<th align="left">Alley</th>
<th align="left">Heating</th>
<th align="left">PavedDrive</th>
<th align="left">LandContour</th>
<th align="left">Foundation</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior2nd</th>
<th align="left">Electrical</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtExposure</th>
<th align="left">BsmtFinType2</th>
<th align="left">PoolQC</th>
<th align="left">Utilities</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Gtl</td>
<td align="left">NridgHt</td>
<td align="left">-</td>
<td align="left">Attchd</td>
<td align="left">GLQ</td>
<td align="left">Inside</td>
<td align="left">Ex</td>
<td align="left">Unf</td>
<td align="left">RL</td>
<td align="left">Hip</td>
<td align="left">Gd</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Pave</td>
<td align="left">None</td>
<td align="left">TA</td>
<td align="left">1Fam</td>
<td align="left">TA</td>
<td align="left">Reg</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">Ex</td>
<td align="left">CompShg</td>
<td align="left">VinylSd</td>
<td align="left">Ex</td>
<td align="left">Typ</td>
<td align="left">-</td>
<td align="left">GasA</td>
<td align="left">Y</td>
<td align="left">Lvl</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">SBrkr</td>
<td align="left">1Story</td>
<td align="left">No</td>
<td align="left">Unf</td>
<td align="left">-</td>
<td align="left">AllPub</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">33</td>
<td align="left">17</td>
<td align="left">34</td>
<td align="left">67</td>
<td align="left">29</td>
<td align="left">97</td>
<td align="left">33</td>
<td align="left">85</td>
<td align="left">90</td>
<td align="left">23</td>
<td align="left">23</td>
<td align="left">175</td>
<td align="left">34</td>
<td align="left">34</td>
<td align="left">91</td>
<td align="left">34</td>
<td align="left">32</td>
<td align="left">111</td>
<td align="left">100</td>
<td align="left">78</td>
<td align="left">34</td>
<td align="left">34</td>
<td align="left">28</td>
<td align="left">34</td>
<td align="left">23</td>
<td align="left">23</td>
<td align="left">34</td>
<td align="left">34</td>
<td align="left">34</td>
<td align="left">34</td>
<td align="left">162</td>
<td align="left">33</td>
<td align="left">33</td>
<td align="left">23</td>
<td align="left">34</td>
<td align="left">22</td>
<td align="left">98</td>
<td align="left">53</td>
<td align="left">34</td>
<td align="left">34</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.971</td>
<td align="left">0.5</td>
<td align="left">1.0</td>
<td align="left">0.838</td>
<td align="left">0.853</td>
<td align="left">0.843</td>
<td align="left">0.971</td>
<td align="left">0.739</td>
<td align="left">0.947</td>
<td align="left">0.676</td>
<td align="left">0.676</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.791</td>
<td align="left">1.0</td>
<td align="left">0.941</td>
<td align="left">0.965</td>
<td align="left">0.87</td>
<td align="left">0.975</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.824</td>
<td align="left">1.0</td>
<td align="left">0.676</td>
<td align="left">0.676</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.926</td>
<td align="left">0.971</td>
<td align="left">0.971</td>
<td align="left">0.676</td>
<td align="left">1.0</td>
<td align="left">0.647</td>
<td align="left">0.852</td>
<td align="left">0.981</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.021</td>
<td align="left">0.386</td>
<td align="left">0.166</td>
<td align="left">0.083</td>
<td align="left">0.504</td>
<td align="left">0.082</td>
<td align="left">0.347</td>
<td align="left">0.444</td>
<td align="left">0.067</td>
<td align="left">0.418</td>
<td align="left">0.136</td>
<td align="left">0.002</td>
<td align="left">0.083</td>
<td align="left">0.0</td>
<td align="left">0.308</td>
<td align="left">0.018</td>
<td align="left">0.061</td>
<td align="left">0.491</td>
<td align="left">0.262</td>
<td align="left">0.089</td>
<td align="left">0.036</td>
<td align="left">0.013</td>
<td align="left">0.663</td>
<td align="left">0.018</td>
<td align="left">0.253</td>
<td align="left">0.544</td>
<td align="left">0.051</td>
<td align="left">0.04</td>
<td align="left">0.009</td>
<td align="left">0.042</td>
<td align="left">0.027</td>
<td align="left">0.414</td>
<td align="left">0.054</td>
<td align="left">0.259</td>
<td align="left">0.038</td>
<td align="left">0.171</td>
<td align="left">0.223</td>
<td align="left">0.086</td>
<td align="left">0.004</td>
<td align="left">0.0</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">LandSlope</th>
<th align="left">Neighborhood</th>
<th align="left">Fence</th>
<th align="left">GarageType</th>
<th align="left">BsmtFinType1</th>
<th align="left">LotConfig</th>
<th align="left">HeatingQC</th>
<th align="left">GarageFinish</th>
<th align="left">MSZoning</th>
<th align="left">RoofStyle</th>
<th align="left">FireplaceQu</th>
<th align="left">Condition2</th>
<th align="left">ExterCond</th>
<th align="left">Street</th>
<th align="left">MasVnrType</th>
<th align="left">GarageCond</th>
<th align="left">BldgType</th>
<th align="left">ExterQual</th>
<th align="left">LotShape</th>
<th align="left">Condition1</th>
<th align="left">GarageQual</th>
<th align="left">CentralAir</th>
<th align="left">BsmtQual</th>
<th align="left">RoofMatl</th>
<th align="left">Exterior1st</th>
<th align="left">KitchenQual</th>
<th align="left">Functional</th>
<th align="left">Alley</th>
<th align="left">Heating</th>
<th align="left">PavedDrive</th>
<th align="left">LandContour</th>
<th align="left">Foundation</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior2nd</th>
<th align="left">Electrical</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtExposure</th>
<th align="left">BsmtFinType2</th>
<th align="left">PoolQC</th>
<th align="left">Utilities</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Gtl</td>
<td align="left">NAmes</td>
<td align="left">-</td>
<td align="left">Attchd</td>
<td align="left">Unf</td>
<td align="left">Inside</td>
<td align="left">Ex</td>
<td align="left">RFn</td>
<td align="left">RL</td>
<td align="left">Gable</td>
<td align="left">Gd</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Pave</td>
<td align="left">None</td>
<td align="left">TA</td>
<td align="left">1Fam</td>
<td align="left">TA</td>
<td align="left">Reg</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">Gd</td>
<td align="left">CompShg</td>
<td align="left">VinylSd</td>
<td align="left">Gd</td>
<td align="left">Typ</td>
<td align="left">-</td>
<td align="left">GasA</td>
<td align="left">Y</td>
<td align="left">Lvl</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">SBrkr</td>
<td align="left">1Story</td>
<td align="left">No</td>
<td align="left">Unf</td>
<td align="left">-</td>
<td align="left">AllPub</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">74</td>
<td align="left">32</td>
<td align="left">75</td>
<td align="left">64</td>
<td align="left">58</td>
<td align="left">23</td>
<td align="left">85</td>
<td align="left">67</td>
<td align="left">85</td>
<td align="left">28</td>
<td align="left">50</td>
<td align="left">33</td>
<td align="left">97</td>
<td align="left">34</td>
<td align="left">40</td>
<td align="left">108</td>
<td align="left">80</td>
<td align="left">113</td>
<td align="left">16</td>
<td align="left">91</td>
<td align="left">107</td>
<td align="left">110</td>
<td align="left">95</td>
<td align="left">77</td>
<td align="left">64</td>
<td align="left">30</td>
<td align="left">105</td>
<td align="left">107</td>
<td align="left">93</td>
<td align="left">104</td>
<td align="left">28</td>
<td align="left">64</td>
<td align="left">72</td>
<td align="left">63</td>
<td align="left">100</td>
<td align="left">75</td>
<td align="left">21</td>
<td align="left">151</td>
<td align="left">173</td>
<td align="left">34</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.925</td>
<td align="left">0.183</td>
<td align="left">0.652</td>
<td align="left">0.557</td>
<td align="left">0.331</td>
<td align="left">0.676</td>
<td align="left">0.486</td>
<td align="left">0.383</td>
<td align="left">0.739</td>
<td align="left">0.519</td>
<td align="left">0.526</td>
<td align="left">0.971</td>
<td align="left">0.843</td>
<td align="left">1.0</td>
<td align="left">0.421</td>
<td align="left">0.939</td>
<td align="left">0.842</td>
<td align="left">0.646</td>
<td align="left">0.471</td>
<td align="left">0.791</td>
<td align="left">0.93</td>
<td align="left">0.957</td>
<td align="left">0.543</td>
<td align="left">0.962</td>
<td align="left">0.366</td>
<td align="left">0.556</td>
<td align="left">0.913</td>
<td align="left">0.93</td>
<td align="left">0.979</td>
<td align="left">0.904</td>
<td align="left">0.824</td>
<td align="left">0.674</td>
<td align="left">0.9</td>
<td align="left">0.36</td>
<td align="left">0.87</td>
<td align="left">0.429</td>
<td align="left">0.389</td>
<td align="left">0.863</td>
<td align="left">0.989</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.024</td>
<td align="left">0.053</td>
<td align="left">-0.181</td>
<td align="left">-0.198</td>
<td align="left">0.037</td>
<td align="left">-0.085</td>
<td align="left">-0.138</td>
<td align="left">0.05</td>
<td align="left">-0.142</td>
<td align="left">-0.199</td>
<td align="left">-0.014</td>
<td align="left">-0.028</td>
<td align="left">-0.073</td>
<td align="left">0.0</td>
<td align="left">-0.062</td>
<td align="left">-0.043</td>
<td align="left">-0.039</td>
<td align="left">0.172</td>
<td align="left">-0.137</td>
<td align="left">-0.095</td>
<td align="left">-0.033</td>
<td align="left">-0.031</td>
<td align="left">0.051</td>
<td align="left">-0.019</td>
<td align="left">-0.057</td>
<td align="left">0.071</td>
<td align="left">-0.036</td>
<td align="left">-0.03</td>
<td align="left">-0.012</td>
<td align="left">-0.054</td>
<td align="left">-0.075</td>
<td align="left">0.117</td>
<td align="left">-0.017</td>
<td align="left">-0.058</td>
<td align="left">-0.092</td>
<td align="left">-0.047</td>
<td align="left">-0.24</td>
<td align="left">-0.032</td>
<td align="left">-0.008</td>
<td align="left">0.0</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">5</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">5</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">LandSlope</th>
<th align="left">Neighborhood</th>
<th align="left">Fence</th>
<th align="left">GarageType</th>
<th align="left">BsmtFinType1</th>
<th align="left">LotConfig</th>
<th align="left">HeatingQC</th>
<th align="left">GarageFinish</th>
<th align="left">MSZoning</th>
<th align="left">RoofStyle</th>
<th align="left">FireplaceQu</th>
<th align="left">Condition2</th>
<th align="left">ExterCond</th>
<th align="left">Street</th>
<th align="left">MasVnrType</th>
<th align="left">GarageCond</th>
<th align="left">BldgType</th>
<th align="left">ExterQual</th>
<th align="left">LotShape</th>
<th align="left">Condition1</th>
<th align="left">GarageQual</th>
<th align="left">CentralAir</th>
<th align="left">BsmtQual</th>
<th align="left">RoofMatl</th>
<th align="left">Exterior1st</th>
<th align="left">KitchenQual</th>
<th align="left">Functional</th>
<th align="left">Alley</th>
<th align="left">Heating</th>
<th align="left">PavedDrive</th>
<th align="left">LandContour</th>
<th align="left">Foundation</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior2nd</th>
<th align="left">Electrical</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtExposure</th>
<th align="left">BsmtFinType2</th>
<th align="left">PoolQC</th>
<th align="left">Utilities</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Sev</td>
<td align="left">Blueste</td>
<td align="left">MnWw</td>
<td align="left">CarPort</td>
<td align="left">Rec</td>
<td align="left">FR3</td>
<td align="left">Gd</td>
<td align="left">Unf</td>
<td align="left">RM</td>
<td align="left">Mansard</td>
<td align="left">Po</td>
<td align="left">PosN</td>
<td align="left">Ex</td>
<td align="left">Pave</td>
<td align="left">BrkCmn</td>
<td align="left">Gd</td>
<td align="left">Twnhs</td>
<td align="left">Ex</td>
<td align="left">IR3</td>
<td align="left">RRAe</td>
<td align="left">Ex</td>
<td align="left">N</td>
<td align="left">Fa</td>
<td align="left">WdShngl</td>
<td align="left">ImStucc</td>
<td align="left">Fa</td>
<td align="left">Maj2</td>
<td align="left">Pave</td>
<td align="left">OthW</td>
<td align="left">P</td>
<td align="left">Bnk</td>
<td align="left">Stone</td>
<td align="left">Fa</td>
<td align="left">AsphShn</td>
<td align="left">FuseF</td>
<td align="left">1.5Unf</td>
<td align="left">No</td>
<td align="left">GLQ</td>
<td align="left">Fa</td>
<td align="left">AllPub</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.667</td>
<td align="left">1.0</td>
<td align="left">0.667</td>
<td align="left">1.0</td>
<td align="left">0.452</td>
<td align="left">0.5</td>
<td align="left">0.56</td>
<td align="left">0.521</td>
<td align="left">0.667</td>
<td align="left">0.667</td>
<td align="left">0.727</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.316</td>
<td align="left">0.8</td>
<td align="left">1.0</td>
<td align="left">0.556</td>
<td align="left">0.486</td>
<td align="left">0.75</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.714</td>
<td align="left">0.571</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.875</td>
<td align="left">1.0</td>
<td align="left">0.6</td>
<td align="left">1.0</td>
<td align="left">0.571</td>
<td align="left">0.526</td>
<td align="left">1.0</td>
<td align="left">0.667</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.356</td>
<td align="left">0.667</td>
<td align="left">1.0</td>
<td align="left">0.316</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
</tbody>
</table><p><em>Maior proporção de população no grupo.</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">LandSlope</th>
<th align="left">Neighborhood</th>
<th align="left">Fence</th>
<th align="left">GarageType</th>
<th align="left">BsmtFinType1</th>
<th align="left">LotConfig</th>
<th align="left">HeatingQC</th>
<th align="left">GarageFinish</th>
<th align="left">MSZoning</th>
<th align="left">RoofStyle</th>
<th align="left">FireplaceQu</th>
<th align="left">Condition2</th>
<th align="left">ExterCond</th>
<th align="left">Street</th>
<th align="left">MasVnrType</th>
<th align="left">GarageCond</th>
<th align="left">BldgType</th>
<th align="left">ExterQual</th>
<th align="left">LotShape</th>
<th align="left">Condition1</th>
<th align="left">GarageQual</th>
<th align="left">CentralAir</th>
<th align="left">BsmtQual</th>
<th align="left">RoofMatl</th>
<th align="left">Exterior1st</th>
<th align="left">KitchenQual</th>
<th align="left">Functional</th>
<th align="left">Alley</th>
<th align="left">Heating</th>
<th align="left">PavedDrive</th>
<th align="left">LandContour</th>
<th align="left">Foundation</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior2nd</th>
<th align="left">Electrical</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtExposure</th>
<th align="left">BsmtFinType2</th>
<th align="left">PoolQC</th>
<th align="left">Utilities</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior classe proporcional</td>
<td align="left">Gtl</td>
<td align="left">NoRidge</td>
<td align="left">-</td>
<td align="left">BuiltIn</td>
<td align="left">GLQ</td>
<td align="left">CulDSac</td>
<td align="left">Ex</td>
<td align="left">Fin</td>
<td align="left">RL</td>
<td align="left">Hip</td>
<td align="left">TA</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">Pave</td>
<td align="left">Stone</td>
<td align="left">TA</td>
<td align="left">1Fam</td>
<td align="left">Gd</td>
<td align="left">IR1</td>
<td align="left">PosN</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">Ex</td>
<td align="left">CompShg</td>
<td align="left">CemntBd</td>
<td align="left">Gd</td>
<td align="left">Typ</td>
<td align="left">-</td>
<td align="left">GasA</td>
<td align="left">Y</td>
<td align="left">Low</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">CmentBd</td>
<td align="left">SBrkr</td>
<td align="left">1Story</td>
<td align="left">Av</td>
<td align="left">Unf</td>
<td align="left">-</td>
<td align="left">AllPub</td>
</tr>
<tr>
<td align="left">proporção da classe</td>
<td align="left">0.063</td>
<td align="left">0.345</td>
<td align="left">0.074</td>
<td align="left">0.152</td>
<td align="left">0.15</td>
<td align="left">0.161</td>
<td align="left">0.096</td>
<td align="left">0.131</td>
<td align="left">0.066</td>
<td align="left">0.161</td>
<td align="left">0.209</td>
<td align="left">0.098</td>
<td align="left">0.067</td>
<td align="left">0.061</td>
<td align="left">0.2</td>
<td align="left">0.063</td>
<td align="left">0.066</td>
<td align="left">0.262</td>
<td align="left">0.134</td>
<td align="left">0.143</td>
<td align="left">0.064</td>
<td align="left">0.062</td>
<td align="left">0.213</td>
<td align="left">0.063</td>
<td align="left">0.2</td>
<td align="left">0.272</td>
<td align="left">0.065</td>
<td align="left">0.064</td>
<td align="left">0.062</td>
<td align="left">0.064</td>
<td align="left">0.143</td>
<td align="left">0.107</td>
<td align="left">0.065</td>
<td align="left">0.29</td>
<td align="left">0.064</td>
<td align="left">0.084</td>
<td align="left">0.196</td>
<td align="left">0.067</td>
<td align="left">0.062</td>
<td align="left">0.061</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
</tr>
</tbody>
</table><p><em>Menor proporção de população no grupo.</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: <br>&emsp;Média maior que a população: LotArea<br>&emsp;Média maior que a população: OverallQual<br>&emsp;Média menor que a população: OverallCond<br>&emsp;Média maior que a população: YearBuilt<br>&emsp;Média maior que a população: YearRemodAdd<br>&emsp;Média maior que a população: MasVnrArea<br>&emsp;Média maior que a população: BsmtFinSF1<br>&emsp;Média maior que a população: TotalBsmtSF<br>&emsp;Média maior que a população: 1stFlrSF<br>&emsp;Média maior que a população: GrLivArea<br>&emsp;Média maior que a população: BsmtFullBath<br>&emsp;Média maior que a população: FullBath<br>&emsp;Média maior que a população: TotRmsAbvGrd<br>&emsp;Média maior que a população: GarageYrBlt<br>&emsp;Média maior que a população: GarageCars<br>&emsp;Média maior que a população: GarageArea<br>&emsp;Média maior que a população: WoodDeckSF<br>&emsp;Média maior que a população: SalePrice<br>&emsp;Presença maior de população na feature Neighborhood: NridgHt<br>&emsp;Presença maior de população na feature Fence: -<br>&emsp;Presença maior de população na feature BsmtFinType1: GLQ<br>&emsp;Presença maior de população na feature HeatingQC: Ex<br>&emsp;Presença maior de população na feature GarageFinish: Fin<br>&emsp;Presença maior de população na feature RoofStyle: Hip<br>&emsp;Presença maior de população na feature FireplaceQu: Gd<br>&emsp;Presença maior de população na feature MasVnrType: BrkFace<br>&emsp;Presença maior de população na feature ExterQual: Ex<br>&emsp;Presença maior de população na feature BsmtQual: Ex<br>&emsp;Presença maior de população na feature Exterior1st: VinylSd<br>&emsp;Presença maior de população na feature KitchenQual: Ex<br>&emsp;Presença maior de população na feature Foundation: PConc<br>&emsp;Presença maior de população na feature Exterior2nd: VinylSd<br>&emsp;Presença maior de população na feature HouseStyle: 1Story<br>&emsp;Presença maior de população na feature BsmtExposure: Av</p>
<p>Grupo 1: <br>&emsp;Média menor que a população: SalePrice<br>&emsp;Presença maior de população na feature FireplaceQu: TA<br>&emsp;Presença maior de população na feature ExterQual: TA<br>&emsp;Presença maior de população na feature KitchenQual: TA<br>&emsp;Presença maior de população na feature Foundation: CBlock</p>
<p>Grupo 2: <br>&emsp;Média maior que a população: OverallQual<br>&emsp;Média maior que a população: YearBuilt<br>&emsp;Média maior que a população: YearRemodAdd<br>&emsp;Média maior que a população: GrLivArea<br>&emsp;Média maior que a população: FullBath<br>&emsp;Média maior que a população: GarageYrBlt<br>&emsp;Média maior que a população: GarageCars<br>&emsp;Média maior que a população: GarageArea<br>&emsp;Média maior que a população: SalePrice<br>&emsp;Presença maior de população na feature BsmtFinType1: GLQ<br>&emsp;Presença maior de população na feature HeatingQC: Ex<br>&emsp;Presença maior de população na feature GarageFinish: RFn<br>&emsp;Presença maior de população na feature ExterQual: Gd<br>&emsp;Presença maior de população na feature LotShape: IR1<br>&emsp;Presença maior de população na feature BsmtQual: Gd<br>&emsp;Presença maior de população na feature Exterior1st: VinylSd<br>&emsp;Presença maior de população na feature KitchenQual: Gd<br>&emsp;Presença maior de população na feature Foundation: PConc<br>&emsp;Presença maior de população na feature Exterior2nd: VinylSd</p>
<p>Grupo 3: <br>&emsp;Média menor que a população: OverallQual<br>&emsp;Média menor que a população: YearBuilt<br>&emsp;Média menor que a população: YearRemodAdd<br>&emsp;Média menor que a população: MasVnrArea<br>&emsp;Média menor que a população: TotalBsmtSF<br>&emsp;Média menor que a população: 1stFlrSF<br>&emsp;Média menor que a população: GrLivArea<br>&emsp;Média menor que a população: FullBath<br>&emsp;Média menor que a população: TotRmsAbvGrd<br>&emsp;Média menor que a população: GarageYrBlt<br>&emsp;Média menor que a população: GarageCars<br>&emsp;Média menor que a população: GarageArea<br>&emsp;Média menor que a população: OpenPorchSF<br>&emsp;Média menor que a população: SalePrice<br>&emsp;Presença maior de população na feature Neighborhood: NAmes<br>&emsp;Presença maior de população na feature HeatingQC: TA<br>&emsp;Presença maior de população na feature GarageFinish: Unf<br>&emsp;Presença maior de população na feature RoofStyle: Gable<br>&emsp;Presença maior de população na feature MasVnrType: None<br>&emsp;Presença maior de população na feature ExterQual: TA<br>&emsp;Presença maior de população na feature LotShape: Reg<br>&emsp;Presença maior de população na feature BsmtQual: TA<br>&emsp;Presença maior de população na feature Exterior1st: MetalSd<br>&emsp;Presença maior de população na feature KitchenQual: TA<br>&emsp;Presença maior de população na feature Foundation: CBlock<br>&emsp;Presença maior de população na feature Exterior2nd: MetalSd<br>&emsp;Presença maior de população na feature BsmtExposure: No</p>
<p>Grupo 4: <br>&emsp;Média maior que a população: OverallQual<br>&emsp;Média maior que a população: YearBuilt<br>&emsp;Média maior que a população: YearRemodAdd<br>&emsp;Média maior que a população: MasVnrArea<br>&emsp;Média maior que a população: BsmtFinSF1<br>&emsp;Média maior que a população: TotalBsmtSF<br>&emsp;Média maior que a população: 1stFlrSF<br>&emsp;Média maior que a população: GrLivArea<br>&emsp;Média maior que a população: BsmtFullBath<br>&emsp;Média maior que a população: FullBath<br>&emsp;Média maior que a população: TotRmsAbvGrd<br>&emsp;Média maior que a população: GarageYrBlt<br>&emsp;Média maior que a população: GarageCars<br>&emsp;Média maior que a população: GarageArea<br>&emsp;Média maior que a população: WoodDeckSF<br>&emsp;Média maior que a população: SalePrice<br>&emsp;Presença maior de população na feature Neighborhood: NridgHt<br>&emsp;Presença maior de população na feature Fence: -<br>&emsp;Presença maior de população na feature BsmtFinType1: GLQ<br>&emsp;Presença maior de população na feature HeatingQC: Ex<br>&emsp;Presença maior de população na feature GarageFinish: Fin<br>&emsp;Presença maior de população na feature MasVnrType: BrkFace<br>&emsp;Presença maior de população na feature ExterQual: Gd<br>&emsp;Presença maior de população na feature LotShape: IR1<br>&emsp;Presença maior de população na feature BsmtQual: Ex<br>&emsp;Presença maior de população na feature Exterior1st: VinylSd<br>&emsp;Presença maior de população na feature Foundation: PConc<br>&emsp;Presença maior de população na feature Exterior2nd: VinylSd<br>&emsp;Presença maior de população na feature HouseStyle: 2Story</p>
<p>Grupo 5: <br>&emsp;Presença maior de população na feature Neighborhood: CollgCr<br>&emsp;Presença maior de população na feature HeatingQC: Ex<br>&emsp;Presença maior de população na feature ExterQual: Gd<br>&emsp;Presença maior de população na feature BsmtQual: Gd<br>&emsp;Presença maior de população na feature Exterior1st: VinylSd<br>&emsp;Presença maior de população na feature KitchenQual: Gd<br>&emsp;Presença maior de população na feature Foundation: PConc<br>&emsp;Presença maior de população na feature Exterior2nd: VinylSd</p>
<p>Grupo outlier: <br>&emsp;Média maior que a população: MSSubClass<br>&emsp;Média maior que a população: LotFrontage<br>&emsp;Média maior que a população: LotArea<br>&emsp;Média maior que a população: OverallQual<br>&emsp;Média menor que a população: YearBuilt<br>&emsp;Média maior que a população: MasVnrArea<br>&emsp;Média maior que a população: BsmtFinSF1<br>&emsp;Média maior que a população: TotalBsmtSF<br>&emsp;Média maior que a população: 1stFlrSF<br>&emsp;Média maior que a população: 2ndFlrSF<br>&emsp;Média maior que a população: LowQualFinSF<br>&emsp;Média maior que a população: GrLivArea<br>&emsp;Média maior que a população: FullBath<br>&emsp;Média maior que a população: BedroomAbvGr<br>&emsp;Média maior que a população: KitchenAbvGr<br>&emsp;Média maior que a população: TotRmsAbvGrd<br>&emsp;Média maior que a população: Fireplaces<br>&emsp;Média maior que a população: GarageCars<br>&emsp;Média maior que a população: GarageArea<br>&emsp;Média maior que a população: OpenPorchSF<br>&emsp;Média maior que a população: EnclosedPorch<br>&emsp;Média maior que a população: ScreenPorch<br>&emsp;Média maior que a população: PoolArea<br>&emsp;Média maior que a população: SalePrice</p>