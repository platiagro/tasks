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
<th align="left">Street</th>
<th align="left">Neighborhood</th>
<th align="left">Functional</th>
<th align="left">LotShape</th>
<th align="left">Utilities</th>
<th align="left">Fence</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior1st</th>
<th align="left">MasVnrType</th>
<th align="left">BsmtFinType1</th>
<th align="left">ExterQual</th>
<th align="left">CentralAir</th>
<th align="left">RoofMatl</th>
<th align="left">BsmtQual</th>
<th align="left">Alley</th>
<th align="left">LandSlope</th>
<th align="left">Electrical</th>
<th align="left">PoolQC</th>
<th align="left">Condition1</th>
<th align="left">Foundation</th>
<th align="left">GarageQual</th>
<th align="left">Exterior2nd</th>
<th align="left">ExterCond</th>
<th align="left">HouseStyle</th>
<th align="left">MSZoning</th>
<th align="left">BldgType</th>
<th align="left">HeatingQC</th>
<th align="left">PavedDrive</th>
<th align="left">BsmtExposure</th>
<th align="left">GarageType</th>
<th align="left">GarageFinish</th>
<th align="left">LandContour</th>
<th align="left">Condition2</th>
<th align="left">BsmtFinType2</th>
<th align="left">RoofStyle</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">Heating</th>
<th align="left">LotConfig</th>
<th align="left">FireplaceQu</th>
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
<td align="left">2</td>
<td align="left">25</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left">3</td>
<td align="left">12</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">15</td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">5</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Pave</td>
<td align="left">NAmes</td>
<td align="left">Typ</td>
<td align="left">Reg</td>
<td align="left">AllPub</td>
<td align="left">-</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">None</td>
<td align="left">GLQ</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">CompShg</td>
<td align="left">Gd</td>
<td align="left">-</td>
<td align="left">Gtl</td>
<td align="left">SBrkr</td>
<td align="left">-</td>
<td align="left">Norm</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">TA</td>
<td align="left">1Story</td>
<td align="left">RL</td>
<td align="left">1Fam</td>
<td align="left">Ex</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Attchd</td>
<td align="left">Fin</td>
<td align="left">Lvl</td>
<td align="left">Norm</td>
<td align="left">Unf</td>
<td align="left">Gable</td>
<td align="left">Gd</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">Inside</td>
<td align="left">Gd</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">582</td>
<td align="left">73</td>
<td align="left">551</td>
<td align="left">351</td>
<td align="left">583</td>
<td align="left">484</td>
<td align="left">534</td>
<td align="left">239</td>
<td align="left">284</td>
<td align="left">205</td>
<td align="left">274</td>
<td align="left">571</td>
<td align="left">569</td>
<td align="left">278</td>
<td align="left">558</td>
<td align="left">552</td>
<td align="left">559</td>
<td align="left">577</td>
<td align="left">509</td>
<td align="left">320</td>
<td align="left">556</td>
<td align="left">236</td>
<td align="left">530</td>
<td align="left">268</td>
<td align="left">508</td>
<td align="left">510</td>
<td align="left">362</td>
<td align="left">556</td>
<td align="left">362</td>
<td align="left">428</td>
<td align="left">218</td>
<td align="left">518</td>
<td align="left">579</td>
<td align="left">521</td>
<td align="left">412</td>
<td align="left">276</td>
<td align="left">572</td>
<td align="left">574</td>
<td align="left">438</td>
<td align="left">315</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/c8cc369d-f86c-4f16-b062-24e7d91d0948.png" alt="Visualização dos outliers: DBscan" /></p>

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
<td align="right">70.67</td>
<td align="right">97.33</td>
<td align="right">27382.27</td>
<td align="right">7.80</td>
<td align="right">5.97</td>
<td align="right">1957.70</td>
<td align="right">1991.20</td>
<td align="right">292.97</td>
<td align="right">1034.90</td>
<td align="right">103.23</td>
<td align="right">646.33</td>
<td align="right">1784.47</td>
<td align="right">1794.30</td>
<td align="right">919.90</td>
<td align="right">32.13</td>
<td align="right">2746.33</td>
<td align="right">0.67</td>
<td align="right">0.17</td>
<td align="right">2.10</td>
<td align="right">0.60</td>
<td align="right">3.37</td>
<td align="right">1.13</td>
<td align="right">9.07</td>
<td align="right">1.50</td>
<td align="right">1975.33</td>
<td align="right">2.43</td>
<td align="right">685.27</td>
<td align="right">171.50</td>
<td align="right">114.70</td>
<td align="right">53.17</td>
<td align="right">0.00</td>
<td align="right">82.93</td>
<td align="right">68.87</td>
<td align="right">5.20</td>
<td align="right">2007.83</td>
<td align="right">339806.67</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">52.88</td>
<td align="right">51.86</td>
<td align="right">38634.49</td>
<td align="right">1.81</td>
<td align="right">1.59</td>
<td align="right">45.65</td>
<td align="right">17.95</td>
<td align="right">435.49</td>
<td align="right">1171.04</td>
<td align="right">267.44</td>
<td align="right">494.84</td>
<td align="right">1037.54</td>
<td align="right">750.70</td>
<td align="right">719.52</td>
<td align="right">124.55</td>
<td align="right">1085.75</td>
<td align="right">0.66</td>
<td align="right">0.46</td>
<td align="right">0.92</td>
<td align="right">0.56</td>
<td align="right">1.13</td>
<td align="right">0.35</td>
<td align="right">2.23</td>
<td align="right">0.57</td>
<td align="right">33.25</td>
<td align="right">0.73</td>
<td align="right">252.99</td>
<td align="right">209.09</td>
<td align="right">162.51</td>
<td align="right">130.19</td>
<td align="right">0.00</td>
<td align="right">147.79</td>
<td align="right">178.85</td>
<td align="right">3.09</td>
<td align="right">1.46</td>
<td align="right">190759.51</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">20.00</td>
<td align="right">47.00</td>
<td align="right">3922.00</td>
<td align="right">5.00</td>
<td align="right">4.00</td>
<td align="right">1880.00</td>
<td align="right">1950.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">32.00</td>
<td align="right">360.00</td>
<td align="right">804.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">804.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">4.00</td>
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
<td align="right">35.00</td>
<td align="right">65.25</td>
<td align="right">11869.00</td>
<td align="right">7.00</td>
<td align="right">5.00</td>
<td align="right">1912.00</td>
<td align="right">1987.75</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">210.75</td>
<td align="right">1237.75</td>
<td align="right">1368.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1935.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">8.00</td>
<td align="right">1.00</td>
<td align="right">1956.00</td>
<td align="right">2.00</td>
<td align="right">517.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.25</td>
<td align="right">2007.00</td>
<td align="right">187112.75</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">60.00</td>
<td align="right">88.50</td>
<td align="right">15527.00</td>
<td align="right">7.00</td>
<td align="right">5.00</td>
<td align="right">1969.00</td>
<td align="right">1996.00</td>
<td align="right">0.00</td>
<td align="right">943.50</td>
<td align="right">0.00</td>
<td align="right">481.00</td>
<td align="right">1580.00</td>
<td align="right">1682.50</td>
<td align="right">1069.50</td>
<td align="right">0.00</td>
<td align="right">2707.50</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">3.50</td>
<td align="right">1.00</td>
<td align="right">9.50</td>
<td align="right">1.00</td>
<td align="right">1989.00</td>
<td align="right">2.50</td>
<td align="right">672.00</td>
<td align="right">112.50</td>
<td align="right">45.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">5.00</td>
<td align="right">2008.00</td>
<td align="right">280489.50</td>
</tr>
<tr>
<td align="left">75%</td>
<td align="right">75.00</td>
<td align="right">104.75</td>
<td align="right">24801.75</td>
<td align="right">10.00</td>
<td align="right">7.00</td>
<td align="right">2001.25</td>
<td align="right">2003.00</td>
<td align="right">558.25</td>
<td align="right">1466.25</td>
<td align="right">0.00</td>
<td align="right">1010.00</td>
<td align="right">2084.50</td>
<td align="right">2002.50</td>
<td align="right">1518.75</td>
<td align="right">0.00</td>
<td align="right">3264.75</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">10.75</td>
<td align="right">2.00</td>
<td align="right">2003.00</td>
<td align="right">3.00</td>
<td align="right">840.75</td>
<td align="right">301.50</td>
<td align="right">155.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">152.25</td>
<td align="right">0.00</td>
<td align="right">7.00</td>
<td align="right">2009.00</td>
<td align="right">465945.00</td>
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
<td align="right">1085.00</td>
<td align="right">1734.00</td>
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
<th align="left">Street</th>
<th align="left">Neighborhood</th>
<th align="left">Functional</th>
<th align="left">LotShape</th>
<th align="left">Utilities</th>
<th align="left">Fence</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior1st</th>
<th align="left">MasVnrType</th>
<th align="left">BsmtFinType1</th>
<th align="left">ExterQual</th>
<th align="left">CentralAir</th>
<th align="left">RoofMatl</th>
<th align="left">BsmtQual</th>
<th align="left">Alley</th>
<th align="left">LandSlope</th>
<th align="left">Electrical</th>
<th align="left">PoolQC</th>
<th align="left">Condition1</th>
<th align="left">Foundation</th>
<th align="left">GarageQual</th>
<th align="left">Exterior2nd</th>
<th align="left">ExterCond</th>
<th align="left">HouseStyle</th>
<th align="left">MSZoning</th>
<th align="left">BldgType</th>
<th align="left">HeatingQC</th>
<th align="left">PavedDrive</th>
<th align="left">BsmtExposure</th>
<th align="left">GarageType</th>
<th align="left">GarageFinish</th>
<th align="left">LandContour</th>
<th align="left">Condition2</th>
<th align="left">BsmtFinType2</th>
<th align="left">RoofStyle</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">Heating</th>
<th align="left">LotConfig</th>
<th align="left">FireplaceQu</th>
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
<td align="left">1</td>
<td align="left">15</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">9</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">10</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">4</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Pave</td>
<td align="left">OldTown</td>
<td align="left">Typ</td>
<td align="left">Reg</td>
<td align="left">AllPub</td>
<td align="left">-</td>
<td align="left">TA</td>
<td align="left">Wd Sdng</td>
<td align="left">None</td>
<td align="left">GLQ</td>
<td align="left">TA</td>
<td align="left">Y</td>
<td align="left">CompShg</td>
<td align="left">TA</td>
<td align="left">-</td>
<td align="left">Gtl</td>
<td align="left">SBrkr</td>
<td align="left">-</td>
<td align="left">Norm</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">Wd Sdng</td>
<td align="left">TA</td>
<td align="left">2Story</td>
<td align="left">RL</td>
<td align="left">1Fam</td>
<td align="left">Ex</td>
<td align="left">Y</td>
<td align="left">Gd</td>
<td align="left">Attchd</td>
<td align="left">Fin</td>
<td align="left">Lvl</td>
<td align="left">Norm</td>
<td align="left">Unf</td>
<td align="left">Gable</td>
<td align="left">Gd</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">Inside</td>
<td align="left">Gd</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">30</td>
<td align="left">9</td>
<td align="left">28</td>
<td align="left">14</td>
<td align="left">30</td>
<td align="left">22</td>
<td align="left">28</td>
<td align="left">7</td>
<td align="left">17</td>
<td align="left">12</td>
<td align="left">11</td>
<td align="left">27</td>
<td align="left">26</td>
<td align="left">11</td>
<td align="left">28</td>
<td align="left">28</td>
<td align="left">29</td>
<td align="left">26</td>
<td align="left">20</td>
<td align="left">14</td>
<td align="left">25</td>
<td align="left">6</td>
<td align="left">21</td>
<td align="left">13</td>
<td align="left">21</td>
<td align="left">25</td>
<td align="left">17</td>
<td align="left">27</td>
<td align="left">12</td>
<td align="left">17</td>
<td align="left">13</td>
<td align="left">22</td>
<td align="left">27</td>
<td align="left">25</td>
<td align="left">15</td>
<td align="left">12</td>
<td align="left">30</td>
<td align="left">26</td>
<td align="left">17</td>
<td align="left">18</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/71e30e6c-ba84-4e1b-8fab-75b6d8a4bf05.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 3 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['FullBath', 'HalfBath', 'WoodDeckSF'] com uma quantidade de 2 grupos. A análise multidimensional em 3 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(61888.802, 161222.6]</td>
<td align="right">0.77</td>
<td align="right">0.23</td>
</tr>
<tr>
<td align="left">(358901.8, 457741.4]</td>
<td align="right">0.31</td>
<td align="right">0.69</td>
</tr>
<tr>
<td align="left">(161222.6, 260062.2]</td>
<td align="right">0.59</td>
<td align="right">0.41</td>
</tr>
<tr>
<td align="left">(260062.2, 358901.8]</td>
<td align="right">0.32</td>
<td align="right">0.68</td>
</tr>
<tr>
<td align="left">(457741.4, 556581.0]</td>
<td align="right">0.33</td>
<td align="right">0.67</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MoSold', 'YrSold', 'SalePrice'] com uma quantidade de 8 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(61888.802, 161222.6]</td>
<td align="right">0.55</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.45</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(358901.8, 457741.4]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.89</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.11</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(161222.6, 260062.2]</td>
<td align="right">0.09</td>
<td align="right">0.00</td>
<td align="right">0.33</td>
<td align="right">0.00</td>
<td align="right">0.48</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">(260062.2, 358901.8]</td>
<td align="right">0.00</td>
<td align="right">0.49</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.51</td>
</tr>
<tr>
<td align="left">(457741.4, 556581.0]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
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
<td align="left">FullBath - HalfBath - WoodDeckSF</td>
<td align="right">0.66</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">GrLivArea - KitchenAbvGr - Fireplaces</td>
<td align="right">0.54</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">1stFlrSF - LowQualFinSF - GarageCars</td>
<td align="right">0.53</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">MSSubClass - LotFrontage - LotArea - OverallQual - OverallCond - YearBuilt - YearRemodAdd - MasVnrArea - BsmtFinSF1 - BsmtFinSF2 - BsmtUnfSF - TotalBsmtSF - 1stFlrSF - 2ndFlrSF - LowQualFinSF - GrLivArea - BsmtFullBath - BsmtHalfBath - FullBath - HalfBath - BedroomAbvGr - KitchenAbvGr - TotRmsAbvGrd - Fireplaces - GarageYrBlt - GarageCars - GarageArea - WoodDeckSF - OpenPorchSF - EnclosedPorch - 3SsnPorch - ScreenPorch - PoolArea - MoSold - YrSold - SalePrice</td>
<td align="right">nan</td>
<td align="right">0.51</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MSSubClass</td>
<td align="right">1.92</td>
<td align="right">-3.72</td>
<td align="right">0.93</td>
<td align="right">-15.17</td>
<td align="right">5.13</td>
<td align="right">-0.71</td>
<td align="right">-5.95</td>
<td align="right">-2.47</td>
<td align="right">16.15</td>
</tr>
<tr>
<td align="left">LotFrontage</td>
<td align="right">-5.33</td>
<td align="right">11.10</td>
<td align="right">2.00</td>
<td align="right">11.62</td>
<td align="right">-3.03</td>
<td align="right">-13.02</td>
<td align="right">8.34</td>
<td align="right">8.53</td>
<td align="right">22.53</td>
</tr>
<tr>
<td align="left">LotArea</td>
<td align="right">-1515.76</td>
<td align="right">1264.30</td>
<td align="right">1116.41</td>
<td align="right">2864.30</td>
<td align="right">-510.72</td>
<td align="right">-2455.82</td>
<td align="right">5142.50</td>
<td align="right">1298.74</td>
<td align="right">16691.76</td>
</tr>
<tr>
<td align="left">OverallQual</td>
<td align="right">-0.93</td>
<td align="right">1.52</td>
<td align="right">0.19</td>
<td align="right">1.85</td>
<td align="right">-0.37</td>
<td align="right">-1.39</td>
<td align="right">2.24</td>
<td align="right">0.91</td>
<td align="right">1.04</td>
</tr>
<tr>
<td align="left">OverallCond</td>
<td align="right">0.23</td>
<td align="right">-0.31</td>
<td align="right">0.00</td>
<td align="right">-0.45</td>
<td align="right">0.12</td>
<td align="right">0.16</td>
<td align="right">-0.49</td>
<td align="right">-0.20</td>
<td align="right">0.48</td>
</tr>
<tr>
<td align="left">YearBuilt</td>
<td align="right">-22.35</td>
<td align="right">20.79</td>
<td align="right">7.35</td>
<td align="right">23.77</td>
<td align="right">2.12</td>
<td align="right">-29.59</td>
<td align="right">27.63</td>
<td align="right">18.20</td>
<td align="right">-21.53</td>
</tr>
<tr>
<td align="left">YearRemodAdd</td>
<td align="right">-14.23</td>
<td align="right">13.69</td>
<td align="right">6.59</td>
<td align="right">16.82</td>
<td align="right">1.72</td>
<td align="right">-23.98</td>
<td align="right">18.46</td>
<td align="right">12.18</td>
<td align="right">2.09</td>
</tr>
<tr>
<td align="left">MasVnrArea</td>
<td align="right">-56.47</td>
<td align="right">153.08</td>
<td align="right">-16.87</td>
<td align="right">221.21</td>
<td align="right">-53.31</td>
<td align="right">-123.68</td>
<td align="right">377.29</td>
<td align="right">68.13</td>
<td align="right">144.83</td>
</tr>
<tr>
<td align="left">BsmtFinSF1</td>
<td align="right">-96.99</td>
<td align="right">362.50</td>
<td align="right">-10.51</td>
<td align="right">479.93</td>
<td align="right">-132.22</td>
<td align="right">-187.43</td>
<td align="right">582.42</td>
<td align="right">43.77</td>
<td align="right">535.60</td>
</tr>
<tr>
<td align="left">BsmtFinSF2</td>
<td align="right">10.10</td>
<td align="right">-13.28</td>
<td align="right">39.77</td>
<td align="right">-36.95</td>
<td align="right">-3.85</td>
<td align="right">-13.20</td>
<td align="right">-42.76</td>
<td align="right">-13.64</td>
<td align="right">60.48</td>
</tr>
<tr>
<td align="left">BsmtUnfSF</td>
<td align="right">-105.96</td>
<td align="right">-19.43</td>
<td align="right">8.05</td>
<td align="right">150.47</td>
<td align="right">-8.63</td>
<td align="right">-90.98</td>
<td align="right">147.34</td>
<td align="right">163.93</td>
<td align="right">-0.61</td>
</tr>
<tr>
<td align="left">TotalBsmtSF</td>
<td align="right">-192.84</td>
<td align="right">329.80</td>
<td align="right">37.31</td>
<td align="right">593.45</td>
<td align="right">-144.70</td>
<td align="right">-291.61</td>
<td align="right">687.00</td>
<td align="right">194.05</td>
<td align="right">595.47</td>
</tr>
<tr>
<td align="left">1stFlrSF</td>
<td align="right">-143.01</td>
<td align="right">258.43</td>
<td align="right">51.31</td>
<td align="right">545.68</td>
<td align="right">-116.43</td>
<td align="right">-291.22</td>
<td align="right">604.44</td>
<td align="right">137.23</td>
<td align="right">510.17</td>
</tr>
<tr>
<td align="left">2ndFlrSF</td>
<td align="right">-110.91</td>
<td align="right">191.11</td>
<td align="right">77.67</td>
<td align="right">-63.02</td>
<td align="right">-14.14</td>
<td align="right">-179.22</td>
<td align="right">263.32</td>
<td align="right">116.31</td>
<td align="right">506.79</td>
</tr>
<tr>
<td align="left">LowQualFinSF</td>
<td align="right">-3.24</td>
<td align="right">-3.24</td>
<td align="right">-3.24</td>
<td align="right">-3.24</td>
<td align="right">6.14</td>
<td align="right">5.59</td>
<td align="right">-3.24</td>
<td align="right">-3.24</td>
<td align="right">28.89</td>
</tr>
<tr>
<td align="left">GrLivArea</td>
<td align="right">-257.16</td>
<td align="right">446.30</td>
<td align="right">125.74</td>
<td align="right">479.42</td>
<td align="right">-124.44</td>
<td align="right">-464.84</td>
<td align="right">864.52</td>
<td align="right">250.30</td>
<td align="right">1045.85</td>
</tr>
<tr>
<td align="left">BsmtFullBath</td>
<td align="right">-0.06</td>
<td align="right">0.36</td>
<td align="right">0.01</td>
<td align="right">0.30</td>
<td align="right">-0.14</td>
<td align="right">-0.16</td>
<td align="right">0.27</td>
<td align="right">0.07</td>
<td align="right">0.22</td>
</tr>
<tr>
<td align="left">BsmtHalfBath</td>
<td align="right">0.03</td>
<td align="right">-0.06</td>
<td align="right">-0.01</td>
<td align="right">-0.03</td>
<td align="right">0.03</td>
<td align="right">0.03</td>
<td align="right">-0.06</td>
<td align="right">-0.05</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">FullBath</td>
<td align="right">-0.36</td>
<td align="right">0.31</td>
<td align="right">0.16</td>
<td align="right">0.22</td>
<td align="right">0.13</td>
<td align="right">-0.56</td>
<td align="right">0.58</td>
<td align="right">0.24</td>
<td align="right">0.39</td>
</tr>
<tr>
<td align="left">HalfBath</td>
<td align="right">-0.06</td>
<td align="right">0.08</td>
<td align="right">0.05</td>
<td align="right">0.07</td>
<td align="right">0.07</td>
<td align="right">-0.32</td>
<td align="right">0.23</td>
<td align="right">0.08</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">BedroomAbvGr</td>
<td align="right">-0.00</td>
<td align="right">0.16</td>
<td align="right">0.11</td>
<td align="right">-0.16</td>
<td align="right">-0.07</td>
<td align="right">-0.12</td>
<td align="right">0.06</td>
<td align="right">0.05</td>
<td align="right">0.43</td>
</tr>
<tr>
<td align="left">KitchenAbvGr</td>
<td align="right">0.02</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">0.13</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd</td>
<td align="right">-0.55</td>
<td align="right">1.12</td>
<td align="right">0.12</td>
<td align="right">1.13</td>
<td align="right">-0.23</td>
<td align="right">-1.22</td>
<td align="right">2.86</td>
<td align="right">0.60</td>
<td align="right">2.07</td>
</tr>
<tr>
<td align="left">Fireplaces</td>
<td align="right">0.08</td>
<td align="right">0.05</td>
<td align="right">0.03</td>
<td align="right">0.07</td>
<td align="right">-0.07</td>
<td align="right">-0.04</td>
<td align="right">0.16</td>
<td align="right">-0.06</td>
<td align="right">0.37</td>
</tr>
<tr>
<td align="left">GarageYrBlt</td>
<td align="right">-19.78</td>
<td align="right">17.99</td>
<td align="right">4.67</td>
<td align="right">20.99</td>
<td align="right">2.31</td>
<td align="right">-23.44</td>
<td align="right">25.12</td>
<td align="right">15.32</td>
<td align="right">-6.84</td>
</tr>
<tr>
<td align="left">GarageCars</td>
<td align="right">-0.40</td>
<td align="right">0.63</td>
<td align="right">0.10</td>
<td align="right">0.85</td>
<td align="right">-0.11</td>
<td align="right">-0.72</td>
<td align="right">0.95</td>
<td align="right">0.40</td>
<td align="right">0.38</td>
</tr>
<tr>
<td align="left">GarageArea</td>
<td align="right">-122.67</td>
<td align="right">193.00</td>
<td align="right">24.92</td>
<td align="right">243.66</td>
<td align="right">-61.99</td>
<td align="right">-169.05</td>
<td align="right">318.35</td>
<td align="right">133.24</td>
<td align="right">144.19</td>
</tr>
<tr>
<td align="left">WoodDeckSF</td>
<td align="right">-36.28</td>
<td align="right">74.19</td>
<td align="right">0.15</td>
<td align="right">78.19</td>
<td align="right">-9.08</td>
<td align="right">-59.04</td>
<td align="right">45.20</td>
<td align="right">31.11</td>
<td align="right">57.27</td>
</tr>
<tr>
<td align="left">OpenPorchSF</td>
<td align="right">-27.19</td>
<td align="right">25.27</td>
<td align="right">19.33</td>
<td align="right">29.55</td>
<td align="right">-6.84</td>
<td align="right">-33.42</td>
<td align="right">37.62</td>
<td align="right">23.06</td>
<td align="right">59.61</td>
</tr>
<tr>
<td align="left">EnclosedPorch</td>
<td align="right">16.20</td>
<td align="right">-13.13</td>
<td align="right">-5.26</td>
<td align="right">-10.94</td>
<td align="right">-3.79</td>
<td align="right">18.70</td>
<td align="right">-17.45</td>
<td align="right">-11.17</td>
<td align="right">35.71</td>
</tr>
<tr>
<td align="left">3SsnPorch</td>
<td align="right">-2.18</td>
<td align="right">-0.38</td>
<td align="right">2.91</td>
<td align="right">11.01</td>
<td align="right">1.69</td>
<td align="right">-3.74</td>
<td align="right">-3.74</td>
<td align="right">-3.74</td>
<td align="right">-3.74</td>
</tr>
<tr>
<td align="left">ScreenPorch</td>
<td align="right">6.18</td>
<td align="right">-5.13</td>
<td align="right">0.72</td>
<td align="right">-4.43</td>
<td align="right">1.69</td>
<td align="right">-10.97</td>
<td align="right">-21.65</td>
<td align="right">4.58</td>
<td align="right">61.28</td>
</tr>
<tr>
<td align="left">PoolArea</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">7.35</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">66.65</td>
</tr>
<tr>
<td align="left">MoSold</td>
<td align="right">-0.21</td>
<td align="right">0.41</td>
<td align="right">0.29</td>
<td align="right">0.19</td>
<td align="right">-0.37</td>
<td align="right">-0.12</td>
<td align="right">0.45</td>
<td align="right">0.29</td>
<td align="right">-1.35</td>
</tr>
<tr>
<td align="left">YrSold</td>
<td align="right">-0.12</td>
<td align="right">0.02</td>
<td align="right">-0.00</td>
<td align="right">0.19</td>
<td align="right">0.00</td>
<td align="right">0.13</td>
<td align="right">-0.00</td>
<td align="right">-0.04</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">SalePrice</td>
<td align="right">-63685.35</td>
<td align="right">106994.63</td>
<td align="right">9078.75</td>
<td align="right">172619.65</td>
<td align="right">-33979.97</td>
<td align="right">-96618.13</td>
<td align="right">257702.19</td>
<td align="right">53106.93</td>
<td align="right">123397.00</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MSSubClass</td>
<td align="right">0.05</td>
<td align="right">-0.10</td>
<td align="right">0.03</td>
<td align="right">-0.42</td>
<td align="right">0.14</td>
<td align="right">-0.02</td>
<td align="right">-0.17</td>
<td align="right">-0.07</td>
<td align="right">0.45</td>
</tr>
<tr>
<td align="left">LotFrontage</td>
<td align="right">-0.22</td>
<td align="right">0.45</td>
<td align="right">0.08</td>
<td align="right">0.47</td>
<td align="right">-0.12</td>
<td align="right">-0.53</td>
<td align="right">0.34</td>
<td align="right">0.34</td>
<td align="right">0.91</td>
</tr>
<tr>
<td align="left">LotArea</td>
<td align="right">-0.30</td>
<td align="right">0.25</td>
<td align="right">0.22</td>
<td align="right">0.56</td>
<td align="right">-0.10</td>
<td align="right">-0.48</td>
<td align="right">1.01</td>
<td align="right">0.26</td>
<td align="right">3.29</td>
</tr>
<tr>
<td align="left">OverallQual</td>
<td align="right">-0.75</td>
<td align="right">1.22</td>
<td align="right">0.15</td>
<td align="right">1.49</td>
<td align="right">-0.30</td>
<td align="right">-1.12</td>
<td align="right">1.80</td>
<td align="right">0.74</td>
<td align="right">0.83</td>
</tr>
<tr>
<td align="left">OverallCond</td>
<td align="right">0.24</td>
<td align="right">-0.32</td>
<td align="right">0.00</td>
<td align="right">-0.48</td>
<td align="right">0.12</td>
<td align="right">0.16</td>
<td align="right">-0.51</td>
<td align="right">-0.21</td>
<td align="right">0.50</td>
</tr>
<tr>
<td align="left">YearBuilt</td>
<td align="right">-0.79</td>
<td align="right">0.73</td>
<td align="right">0.26</td>
<td align="right">0.84</td>
<td align="right">0.07</td>
<td align="right">-1.04</td>
<td align="right">0.98</td>
<td align="right">0.64</td>
<td align="right">-0.76</td>
</tr>
<tr>
<td align="left">YearRemodAdd</td>
<td align="right">-0.72</td>
<td align="right">0.70</td>
<td align="right">0.34</td>
<td align="right">0.86</td>
<td align="right">0.09</td>
<td align="right">-1.22</td>
<td align="right">0.94</td>
<td align="right">0.62</td>
<td align="right">0.11</td>
</tr>
<tr>
<td align="left">MasVnrArea</td>
<td align="right">-0.27</td>
<td align="right">0.73</td>
<td align="right">-0.08</td>
<td align="right">1.05</td>
<td align="right">-0.25</td>
<td align="right">-0.59</td>
<td align="right">1.79</td>
<td align="right">0.32</td>
<td align="right">0.69</td>
</tr>
<tr>
<td align="left">BsmtFinSF1</td>
<td align="right">-0.21</td>
<td align="right">0.77</td>
<td align="right">-0.02</td>
<td align="right">1.02</td>
<td align="right">-0.28</td>
<td align="right">-0.40</td>
<td align="right">1.23</td>
<td align="right">0.09</td>
<td align="right">1.13</td>
</tr>
<tr>
<td align="left">BsmtFinSF2</td>
<td align="right">0.06</td>
<td align="right">-0.08</td>
<td align="right">0.24</td>
<td align="right">-0.23</td>
<td align="right">-0.02</td>
<td align="right">-0.08</td>
<td align="right">-0.26</td>
<td align="right">-0.08</td>
<td align="right">0.37</td>
</tr>
<tr>
<td align="left">BsmtUnfSF</td>
<td align="right">-0.23</td>
<td align="right">-0.04</td>
<td align="right">0.02</td>
<td align="right">0.32</td>
<td align="right">-0.02</td>
<td align="right">-0.20</td>
<td align="right">0.32</td>
<td align="right">0.35</td>
<td align="right">-0.00</td>
</tr>
<tr>
<td align="left">TotalBsmtSF</td>
<td align="right">-0.50</td>
<td align="right">0.85</td>
<td align="right">0.10</td>
<td align="right">1.54</td>
<td align="right">-0.37</td>
<td align="right">-0.76</td>
<td align="right">1.78</td>
<td align="right">0.50</td>
<td align="right">1.54</td>
</tr>
<tr>
<td align="left">1stFlrSF</td>
<td align="right">-0.39</td>
<td align="right">0.70</td>
<td align="right">0.14</td>
<td align="right">1.48</td>
<td align="right">-0.32</td>
<td align="right">-0.79</td>
<td align="right">1.64</td>
<td align="right">0.37</td>
<td align="right">1.39</td>
</tr>
<tr>
<td align="left">2ndFlrSF</td>
<td align="right">-0.24</td>
<td align="right">0.42</td>
<td align="right">0.17</td>
<td align="right">-0.14</td>
<td align="right">-0.03</td>
<td align="right">-0.39</td>
<td align="right">0.58</td>
<td align="right">0.26</td>
<td align="right">1.12</td>
</tr>
<tr>
<td align="left">LowQualFinSF</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">0.18</td>
<td align="right">0.16</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">0.84</td>
</tr>
<tr>
<td align="left">GrLivArea</td>
<td align="right">-0.58</td>
<td align="right">1.00</td>
<td align="right">0.28</td>
<td align="right">1.08</td>
<td align="right">-0.28</td>
<td align="right">-1.05</td>
<td align="right">1.95</td>
<td align="right">0.56</td>
<td align="right">2.35</td>
</tr>
<tr>
<td align="left">BsmtFullBath</td>
<td align="right">-0.12</td>
<td align="right">0.69</td>
<td align="right">0.02</td>
<td align="right">0.58</td>
<td align="right">-0.27</td>
<td align="right">-0.32</td>
<td align="right">0.53</td>
<td align="right">0.13</td>
<td align="right">0.43</td>
</tr>
<tr>
<td align="left">BsmtHalfBath</td>
<td align="right">0.11</td>
<td align="right">-0.25</td>
<td align="right">-0.06</td>
<td align="right">-0.12</td>
<td align="right">0.14</td>
<td align="right">0.13</td>
<td align="right">-0.25</td>
<td align="right">-0.20</td>
<td align="right">0.45</td>
</tr>
<tr>
<td align="left">FullBath</td>
<td align="right">-0.74</td>
<td align="right">0.63</td>
<td align="right">0.33</td>
<td align="right">0.46</td>
<td align="right">0.25</td>
<td align="right">-1.14</td>
<td align="right">1.17</td>
<td align="right">0.48</td>
<td align="right">0.79</td>
</tr>
<tr>
<td align="left">HalfBath</td>
<td align="right">-0.11</td>
<td align="right">0.15</td>
<td align="right">0.10</td>
<td align="right">0.13</td>
<td align="right">0.13</td>
<td align="right">-0.62</td>
<td align="right">0.45</td>
<td align="right">0.16</td>
<td align="right">0.23</td>
</tr>
<tr>
<td align="left">BedroomAbvGr</td>
<td align="right">-0.01</td>
<td align="right">0.22</td>
<td align="right">0.15</td>
<td align="right">-0.22</td>
<td align="right">-0.10</td>
<td align="right">-0.16</td>
<td align="right">0.09</td>
<td align="right">0.07</td>
<td align="right">0.59</td>
</tr>
<tr>
<td align="left">KitchenAbvGr</td>
<td align="right">0.26</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">0.09</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">1.49</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd</td>
<td align="right">-0.38</td>
<td align="right">0.77</td>
<td align="right">0.09</td>
<td align="right">0.78</td>
<td align="right">-0.16</td>
<td align="right">-0.84</td>
<td align="right">1.96</td>
<td align="right">0.41</td>
<td align="right">1.42</td>
</tr>
<tr>
<td align="left">Fireplaces</td>
<td align="right">0.22</td>
<td align="right">0.15</td>
<td align="right">0.09</td>
<td align="right">0.19</td>
<td align="right">-0.21</td>
<td align="right">-0.11</td>
<td align="right">0.46</td>
<td align="right">-0.18</td>
<td align="right">1.07</td>
</tr>
<tr>
<td align="left">GarageYrBlt</td>
<td align="right">-0.79</td>
<td align="right">0.72</td>
<td align="right">0.19</td>
<td align="right">0.84</td>
<td align="right">0.09</td>
<td align="right">-0.93</td>
<td align="right">1.00</td>
<td align="right">0.61</td>
<td align="right">-0.27</td>
</tr>
<tr>
<td align="left">GarageCars</td>
<td align="right">-0.63</td>
<td align="right">0.98</td>
<td align="right">0.15</td>
<td align="right">1.32</td>
<td align="right">-0.17</td>
<td align="right">-1.11</td>
<td align="right">1.47</td>
<td align="right">0.62</td>
<td align="right">0.59</td>
</tr>
<tr>
<td align="left">GarageArea</td>
<td align="right">-0.63</td>
<td align="right">0.98</td>
<td align="right">0.13</td>
<td align="right">1.24</td>
<td align="right">-0.32</td>
<td align="right">-0.86</td>
<td align="right">1.62</td>
<td align="right">0.68</td>
<td align="right">0.74</td>
</tr>
<tr>
<td align="left">WoodDeckSF</td>
<td align="right">-0.29</td>
<td align="right">0.59</td>
<td align="right">0.00</td>
<td align="right">0.62</td>
<td align="right">-0.07</td>
<td align="right">-0.47</td>
<td align="right">0.36</td>
<td align="right">0.25</td>
<td align="right">0.46</td>
</tr>
<tr>
<td align="left">OpenPorchSF</td>
<td align="right">-0.44</td>
<td align="right">0.41</td>
<td align="right">0.32</td>
<td align="right">0.48</td>
<td align="right">-0.11</td>
<td align="right">-0.55</td>
<td align="right">0.61</td>
<td align="right">0.38</td>
<td align="right">0.97</td>
</tr>
<tr>
<td align="left">EnclosedPorch</td>
<td align="right">0.29</td>
<td align="right">-0.24</td>
<td align="right">-0.09</td>
<td align="right">-0.20</td>
<td align="right">-0.07</td>
<td align="right">0.34</td>
<td align="right">-0.31</td>
<td align="right">-0.20</td>
<td align="right">0.64</td>
</tr>
<tr>
<td align="left">3SsnPorch</td>
<td align="right">-0.07</td>
<td align="right">-0.01</td>
<td align="right">0.10</td>
<td align="right">0.37</td>
<td align="right">0.06</td>
<td align="right">-0.13</td>
<td align="right">-0.13</td>
<td align="right">-0.13</td>
<td align="right">-0.13</td>
</tr>
<tr>
<td align="left">ScreenPorch</td>
<td align="right">0.10</td>
<td align="right">-0.08</td>
<td align="right">0.01</td>
<td align="right">-0.07</td>
<td align="right">0.03</td>
<td align="right">-0.17</td>
<td align="right">-0.35</td>
<td align="right">0.07</td>
<td align="right">0.98</td>
</tr>
<tr>
<td align="left">PoolArea</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">0.20</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">1.81</td>
</tr>
<tr>
<td align="left">MoSold</td>
<td align="right">-0.08</td>
<td align="right">0.15</td>
<td align="right">0.10</td>
<td align="right">0.07</td>
<td align="right">-0.14</td>
<td align="right">-0.04</td>
<td align="right">0.16</td>
<td align="right">0.11</td>
<td align="right">-0.49</td>
</tr>
<tr>
<td align="left">YrSold</td>
<td align="right">-0.09</td>
<td align="right">0.02</td>
<td align="right">-0.00</td>
<td align="right">0.14</td>
<td align="right">0.00</td>
<td align="right">0.10</td>
<td align="right">-0.00</td>
<td align="right">-0.03</td>
<td align="right">0.09</td>
</tr>
<tr>
<td align="left">SalePrice</td>
<td align="right">-0.80</td>
<td align="right">1.35</td>
<td align="right">0.11</td>
<td align="right">2.18</td>
<td align="right">-0.43</td>
<td align="right">-1.22</td>
<td align="right">3.25</td>
<td align="right">0.67</td>
<td align="right">1.56</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/71c94f55-38bb-494b-b451-d7774720c641.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-HousePrices/figures/2651e9c5-8e82-49c8-b0a3-7a5d1a744f6f.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature SalePrice e no grupo 6, com valor de 257702.19. A maior variação negativa foi na feature SalePrice e no grupo 5, com o valor registrado de -96618.13</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Street</th>
<th align="left">Neighborhood</th>
<th align="left">Functional</th>
<th align="left">LotShape</th>
<th align="left">Utilities</th>
<th align="left">Fence</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior1st</th>
<th align="left">MasVnrType</th>
<th align="left">BsmtFinType1</th>
<th align="left">ExterQual</th>
<th align="left">CentralAir</th>
<th align="left">RoofMatl</th>
<th align="left">BsmtQual</th>
<th align="left">Alley</th>
<th align="left">LandSlope</th>
<th align="left">Electrical</th>
<th align="left">PoolQC</th>
<th align="left">Condition1</th>
<th align="left">Foundation</th>
<th align="left">GarageQual</th>
<th align="left">Exterior2nd</th>
<th align="left">ExterCond</th>
<th align="left">HouseStyle</th>
<th align="left">MSZoning</th>
<th align="left">BldgType</th>
<th align="left">HeatingQC</th>
<th align="left">PavedDrive</th>
<th align="left">BsmtExposure</th>
<th align="left">GarageType</th>
<th align="left">GarageFinish</th>
<th align="left">LandContour</th>
<th align="left">Condition2</th>
<th align="left">BsmtFinType2</th>
<th align="left">RoofStyle</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">Heating</th>
<th align="left">LotConfig</th>
<th align="left">FireplaceQu</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Pave</td>
<td align="left">NridgHt</td>
<td align="left">Typ</td>
<td align="left">IR1</td>
<td align="left">AllPub</td>
<td align="left">-</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">Stone</td>
<td align="left">GLQ</td>
<td align="left">Ex</td>
<td align="left">Y</td>
<td align="left">CompShg</td>
<td align="left">Ex</td>
<td align="left">-</td>
<td align="left">Gtl</td>
<td align="left">SBrkr</td>
<td align="left">-</td>
<td align="left">Norm</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">TA</td>
<td align="left">2Story</td>
<td align="left">RL</td>
<td align="left">1Fam</td>
<td align="left">Ex</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Detchd</td>
<td align="left">Unf</td>
<td align="left">Lvl</td>
<td align="left">Norm</td>
<td align="left">Unf</td>
<td align="left">Hip</td>
<td align="left">Ex</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">Inside</td>
<td align="left">Gd</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">104</td>
<td align="left">5</td>
<td align="left">31</td>
<td align="left">5</td>
<td align="left">104</td>
<td align="left">31</td>
<td align="left">7</td>
<td align="left">22</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">5</td>
<td align="left">50</td>
<td align="left">50</td>
<td align="left">7</td>
<td align="left">50</td>
<td align="left">7</td>
<td align="left">50</td>
<td align="left">104</td>
<td align="left">7</td>
<td align="left">7</td>
<td align="left">31</td>
<td align="left">22</td>
<td align="left">31</td>
<td align="left">5</td>
<td align="left">7</td>
<td align="left">7</td>
<td align="left">7</td>
<td align="left">50</td>
<td align="left">56</td>
<td align="left">36</td>
<td align="left">54</td>
<td align="left">7</td>
<td align="left">104</td>
<td align="left">7</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">50</td>
<td align="left">50</td>
<td align="left">57</td>
<td align="left">5</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">1.0</td>
<td align="left">0.7142857142857143</td>
<td align="left">1.0</td>
<td align="left">0.7142857142857143</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.7096774193548387</td>
<td align="left">0.7142857142857143</td>
<td align="left">0.8571428571428571</td>
<td align="left">0.7142857142857143</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.7096774193548387</td>
<td align="left">1.0</td>
<td align="left">0.7142857142857143</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.835820895522388</td>
<td align="left">0.5373134328358209</td>
<td align="left">0.8059701492537313</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.7142857142857143</td>
<td align="left">0.8571428571428571</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.8507462686567164</td>
<td align="left">0.7142857142857143</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.001808318264014508</td>
<td align="left">0.5985533453887885</td>
<td align="left">0.054249547920434016</td>
<td align="left">0.352622061482821</td>
<td align="left">0.0</td>
<td align="left">0.16455696202531644</td>
<td align="left">0.08499095840867987</td>
<td align="left">0.28653094557545356</td>
<td align="left">0.5678119349005425</td>
<td align="left">0.5081374321880651</td>
<td align="left">0.6491862567811935</td>
<td align="left">0.016274864376130238</td>
<td align="left">0.018083182640144635</td>
<td align="left">0.8390596745027125</td>
<td align="left">0.04159132007233268</td>
<td align="left">0.05244122965641951</td>
<td align="left">0.04159132007233268</td>
<td align="left">0.003616636528028905</td>
<td align="left">0.11573236889692584</td>
<td align="left">0.44665461121157324</td>
<td align="left">0.039783001808318286</td>
<td align="left">0.29195590036749697</td>
<td align="left">0.07956600361663657</td>
<td align="left">0.3453887884267631</td>
<td align="left">0.11934900542495475</td>
<td align="left">0.12296564195298376</td>
<td align="left">0.3761301989150091</td>
<td align="left">0.04339963833634719</td>
<td align="left">0.2011011848533103</td>
<td align="left">0.3836063803945913</td>
<td align="left">0.5112142722193733</td>
<td align="left">0.10307414104882462</td>
<td align="left">0.001808318264014508</td>
<td align="left">0.10307414104882462</td>
<td align="left">0.4556962025316456</td>
<td align="left">0.725135623869801</td>
<td align="left">0.019891500904159143</td>
<td align="left">0.009041591320072317</td>
<td align="left">0.08944427950662603</td>
<td align="left">0.17721518987341778</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">6</td>
<td align="left">0</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left">6</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Street</th>
<th align="left">Neighborhood</th>
<th align="left">Functional</th>
<th align="left">LotShape</th>
<th align="left">Utilities</th>
<th align="left">Fence</th>
<th align="left">BsmtCond</th>
<th align="left">Exterior1st</th>
<th align="left">MasVnrType</th>
<th align="left">BsmtFinType1</th>
<th align="left">ExterQual</th>
<th align="left">CentralAir</th>
<th align="left">RoofMatl</th>
<th align="left">BsmtQual</th>
<th align="left">Alley</th>
<th align="left">LandSlope</th>
<th align="left">Electrical</th>
<th align="left">PoolQC</th>
<th align="left">Condition1</th>
<th align="left">Foundation</th>
<th align="left">GarageQual</th>
<th align="left">Exterior2nd</th>
<th align="left">ExterCond</th>
<th align="left">HouseStyle</th>
<th align="left">MSZoning</th>
<th align="left">BldgType</th>
<th align="left">HeatingQC</th>
<th align="left">PavedDrive</th>
<th align="left">BsmtExposure</th>
<th align="left">GarageType</th>
<th align="left">GarageFinish</th>
<th align="left">LandContour</th>
<th align="left">Condition2</th>
<th align="left">BsmtFinType2</th>
<th align="left">RoofStyle</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">Heating</th>
<th align="left">LotConfig</th>
<th align="left">FireplaceQu</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Pave</td>
<td align="left">NridgHt</td>
<td align="left">Typ</td>
<td align="left">Reg</td>
<td align="left">AllPub</td>
<td align="left">-</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">None</td>
<td align="left">Unf</td>
<td align="left">Gd</td>
<td align="left">Y</td>
<td align="left">CompShg</td>
<td align="left">Gd</td>
<td align="left">-</td>
<td align="left">Gtl</td>
<td align="left">SBrkr</td>
<td align="left">-</td>
<td align="left">Norm</td>
<td align="left">PConc</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">TA</td>
<td align="left">1Story</td>
<td align="left">RL</td>
<td align="left">1Fam</td>
<td align="left">Ex</td>
<td align="left">Y</td>
<td align="left">No</td>
<td align="left">Attchd</td>
<td align="left">Fin</td>
<td align="left">Lvl</td>
<td align="left">Norm</td>
<td align="left">Unf</td>
<td align="left">Gable</td>
<td align="left">Gd</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">Inside</td>
<td align="left">Gd</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">127</td>
<td align="left">16</td>
<td align="left">93</td>
<td align="left">45</td>
<td align="left">104</td>
<td align="left">42</td>
<td align="left">58</td>
<td align="left">55</td>
<td align="left">38</td>
<td align="left">29</td>
<td align="left">16</td>
<td align="left">62</td>
<td align="left">75</td>
<td align="left">85</td>
<td align="left">61</td>
<td align="left">72</td>
<td align="left">57</td>
<td align="left">126</td>
<td align="left">51</td>
<td align="left">68</td>
<td align="left">59</td>
<td align="left">54</td>
<td align="left">57</td>
<td align="left">53</td>
<td align="left">43</td>
<td align="left">110</td>
<td align="left">41</td>
<td align="left">59</td>
<td align="left">20</td>
<td align="left">4</td>
<td align="left">52</td>
<td align="left">24</td>
<td align="left">30</td>
<td align="left">75</td>
<td align="left">25</td>
<td align="left">67</td>
<td align="left">61</td>
<td align="left">65</td>
<td align="left">59</td>
<td align="left">44</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.9921875</td>
<td align="left">0.20512820512820512</td>
<td align="left">0.8942307692307693</td>
<td align="left">0.5113636363636364</td>
<td align="left">1.0</td>
<td align="left">0.6268656716417911</td>
<td align="left">0.8656716417910447</td>
<td align="left">0.4296875</td>
<td align="left">0.4318181818181818</td>
<td align="left">0.27884615384615385</td>
<td align="left">0.5161290322580645</td>
<td align="left">0.9253731343283582</td>
<td align="left">0.9615384615384616</td>
<td align="left">0.6640625</td>
<td align="left">0.9104477611940298</td>
<td align="left">0.9230769230769231</td>
<td align="left">0.8507462686567164</td>
<td align="left">0.984375</td>
<td align="left">0.7611940298507462</td>
<td align="left">0.53125</td>
<td align="left">0.8805970149253731</td>
<td align="left">0.421875</td>
<td align="left">0.8507462686567164</td>
<td align="left">0.4140625</td>
<td align="left">0.6417910447761194</td>
<td align="left">0.859375</td>
<td align="left">0.3942307692307692</td>
<td align="left">0.8805970149253731</td>
<td align="left">0.4</td>
<td align="left">0.5714285714285714</td>
<td align="left">0.40625</td>
<td align="left">0.7741935483870968</td>
<td align="left">0.967741935483871</td>
<td align="left">0.8522727272727273</td>
<td align="left">0.5</td>
<td align="left">0.5234375</td>
<td align="left">0.9104477611940298</td>
<td align="left">0.9701492537313433</td>
<td align="left">0.6704545454545454</td>
<td align="left">0.5</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.006004181735985492</td>
<td align="left">0.08939583623127927</td>
<td align="left">-0.05151968284879671</td>
<td align="left">-0.09803961860923882</td>
<td align="left">0.0</td>
<td align="left">-0.20857736633289248</td>
<td align="left">-0.049337399800275406</td>
<td align="left">0.0065410262206148095</td>
<td align="left">-0.05100279467368074</td>
<td align="left">-0.01771804145221867</td>
<td align="left">0.056816193198389986</td>
<td align="left">-0.058352001295511546</td>
<td align="left">-0.0203783558213938</td>
<td align="left">0.17581656871609402</td>
<td align="left">-0.0479609187336375</td>
<td align="left">-0.024481847266657364</td>
<td align="left">-0.10766241127095089</td>
<td align="left">-0.012008363471971095</td>
<td align="left">-0.12307360125232791</td>
<td align="left">-0.022095388788426762</td>
<td align="left">-0.07961998326630859</td>
<td align="left">0.004153481012658222</td>
<td align="left">-0.069687727726647</td>
<td align="left">-0.05429193037974683</td>
<td align="left">-0.23885994979892589</td>
<td align="left">-0.017659358047016238</td>
<td align="left">-0.2296390318542217</td>
<td align="left">-0.07600334673827969</td>
<td align="left">-0.2347197106690777</td>
<td align="left">-0.17179023508137437</td>
<td align="left">0.03554475587703437</td>
<td align="left">-0.12273231056407863</td>
<td align="left">-0.030449746252114496</td>
<td align="left">-0.04465313167844809</td>
<td align="left">-0.2179023508137432</td>
<td align="left">0.04604147830018085</td>
<td align="left">-0.06966073790181104</td>
<td align="left">-0.020809154948584374</td>
<td align="left">-0.09084744369554498</td>
<td align="left">-0.037070524412296524</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">4</td>
<td align="left">7</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">7</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">7</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">5</td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">5</td>
<td align="left">2</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: Média menor que a população: OverallQual, Média menor que a população: YearBuilt, Média menor que a população: YearRemodAdd, Média menor que a população: GrLivArea, Média menor que a população: FullBath, Média menor que a população: GarageYrBlt, Média menor que a população: GarageCars, Média menor que a população: GarageArea, Média menor que a população: SalePrice, Presença maior de população na feature Neighborhood: NAmes, Presença maior de população na feature LotShape: Reg, Presença maior de população na feature Exterior1st: Wd Sdng, Presença maior de população na feature MasVnrType: None, Presença maior de população na feature ExterQual: TA, Presença maior de população na feature BsmtQual: TA, Presença maior de população na feature Foundation: CBlock, Presença maior de população na feature Exterior2nd: Wd Sdng, Presença maior de população na feature BsmtExposure: No, Presença maior de população na feature GarageFinish: Unf, Presença maior de população na feature KitchenQual: TA</p>
<p>Grupo 1: Média maior que a população: OverallQual, Média maior que a população: YearBuilt, Média maior que a população: YearRemodAdd, Média maior que a população: MasVnrArea, Média maior que a população: BsmtFinSF1, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: GrLivArea, Média maior que a população: BsmtFullBath, Média maior que a população: FullBath, Média maior que a população: TotRmsAbvGrd, Média maior que a população: GarageYrBlt, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: WoodDeckSF, Média maior que a população: SalePrice, Presença maior de população na feature Neighborhood: NridgHt, Presença maior de população na feature LotShape: IR1, Presença maior de população na feature Fence: -, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature MasVnrType: BrkFace, Presença maior de população na feature BsmtFinType1: GLQ, Presença maior de população na feature ExterQual: Gd, Presença maior de população na feature BsmtQual: Ex, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature HouseStyle: 2Story, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature GarageFinish: Fin, Presença maior de população na feature KitchenQual: Gd, Presença maior de população na feature FireplaceQu: Gd</p>
<p>Grupo 2: Presença maior de população na feature Neighborhood: CollgCr, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature ExterQual: Gd, Presença maior de população na feature BsmtQual: Gd, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature HouseStyle: 2Story, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature KitchenQual: Gd</p>
<p>Grupo 3: Média maior que a população: LotArea, Média maior que a população: OverallQual, Média maior que a população: YearBuilt, Média maior que a população: YearRemodAdd, Média maior que a população: MasVnrArea, Média maior que a população: BsmtFinSF1, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: GrLivArea, Média maior que a população: BsmtFullBath, Média maior que a população: TotRmsAbvGrd, Média maior que a população: GarageYrBlt, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: WoodDeckSF, Média maior que a população: SalePrice, Presença maior de população na feature Neighborhood: NridgHt, Presença maior de população na feature Fence: -, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature MasVnrType: BrkFace, Presença maior de população na feature BsmtFinType1: GLQ, Presença maior de população na feature BsmtQual: Ex, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature HouseStyle: 1Story, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature BsmtExposure: Av, Presença maior de população na feature GarageFinish: Fin, Presença maior de população na feature RoofStyle: Hip, Presença maior de população na feature KitchenQual: Ex, Presença maior de população na feature FireplaceQu: Gd</p>
<p>Grupo 4: Presença maior de população na feature Neighborhood: Gilbert, Presença maior de população na feature BsmtQual: Gd, Presença maior de população na feature FireplaceQu: TA</p>
<p>Grupo 5: Média menor que a população: LotFrontage, Média menor que a população: OverallQual, Média menor que a população: YearBuilt, Média menor que a população: YearRemodAdd, Média menor que a população: MasVnrArea, Média menor que a população: TotalBsmtSF, Média menor que a população: 1stFlrSF, Média menor que a população: GrLivArea, Média menor que a população: FullBath, Média menor que a população: HalfBath, Média menor que a população: TotRmsAbvGrd, Média menor que a população: GarageYrBlt, Média menor que a população: GarageCars, Média menor que a população: GarageArea, Média menor que a população: OpenPorchSF, Média menor que a população: SalePrice, Presença maior de população na feature LotShape: Reg, Presença maior de população na feature Exterior1st: MetalSd, Presença maior de população na feature MasVnrType: None, Presença maior de população na feature ExterQual: TA, Presença maior de população na feature BsmtQual: TA, Presença maior de população na feature Foundation: CBlock, Presença maior de população na feature Exterior2nd: MetalSd, Presença maior de população na feature HeatingQC: TA, Presença maior de população na feature BsmtExposure: No, Presença maior de população na feature GarageType: Detchd, Presença maior de população na feature GarageFinish: Unf, Presença maior de população na feature RoofStyle: Gable, Presença maior de população na feature KitchenQual: TA</p>
<p>Grupo 6: Média maior que a população: LotArea, Média maior que a população: OverallQual, Média menor que a população: OverallCond, Média maior que a população: YearBuilt, Média maior que a população: YearRemodAdd, Média maior que a população: MasVnrArea, Média maior que a população: BsmtFinSF1, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: 2ndFlrSF, Média maior que a população: GrLivArea, Média maior que a população: BsmtFullBath, Média maior que a população: FullBath, Média maior que a população: TotRmsAbvGrd, Média maior que a população: GarageYrBlt, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: OpenPorchSF, Média maior que a população: SalePrice, Presença maior de população na feature Neighborhood: NridgHt, Presença maior de população na feature LotShape: IR1, Presença maior de população na feature Fence: -, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature MasVnrType: Stone, Presença maior de população na feature BsmtFinType1: GLQ, Presença maior de população na feature ExterQual: Ex, Presença maior de população na feature BsmtQual: Ex, Presença maior de população na feature Condition1: Norm, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature HouseStyle: 2Story, Presença maior de população na feature MSZoning: RL, Presença maior de população na feature BldgType: 1Fam, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature GarageFinish: Fin, Presença maior de população na feature LandContour: Lvl, Presença maior de população na feature BsmtFinType2: Unf, Presença maior de população na feature RoofStyle: Hip, Presença maior de população na feature KitchenQual: Ex, Presença maior de população na feature FireplaceQu: Gd</p>
<p>Grupo 7: Média maior que a população: OverallQual, Média maior que a população: YearBuilt, Média maior que a população: YearRemodAdd, Média maior que a população: TotalBsmtSF, Média maior que a população: GrLivArea, Média maior que a população: GarageYrBlt, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: SalePrice, Presença maior de população na feature LotShape: IR1, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature BsmtFinType1: GLQ, Presença maior de população na feature ExterQual: Gd, Presença maior de população na feature BsmtQual: Gd, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature GarageFinish: RFn, Presença maior de população na feature KitchenQual: Gd, Presença maior de população na feature FireplaceQu: Gd</p>
<p>Grupo outlier: Média maior que a população: LotFrontage, Média maior que a população: LotArea, Média maior que a população: OverallQual, Média maior que a população: OverallCond, Média menor que a população: YearBuilt, Média maior que a população: MasVnrArea, Média maior que a população: BsmtFinSF1, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: 2ndFlrSF, Média maior que a população: LowQualFinSF, Média maior que a população: GrLivArea, Média maior que a população: FullBath, Média maior que a população: BedroomAbvGr, Média maior que a população: KitchenAbvGr, Média maior que a população: TotRmsAbvGrd, Média maior que a população: Fireplaces, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: OpenPorchSF, Média maior que a população: EnclosedPorch, Média maior que a população: ScreenPorch, Média maior que a população: PoolArea, Média maior que a população: SalePrice</p>
