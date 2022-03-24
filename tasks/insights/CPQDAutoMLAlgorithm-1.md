<h1>CPQD AutoML Algorithm - 1</h1>
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
<th align="left">CentralAir</th>
<th align="left">Exterior2nd</th>
<th align="left">RoofMatl</th>
<th align="left">RoofStyle</th>
<th align="left">Utilities</th>
<th align="left">Foundation</th>
<th align="left">Condition2</th>
<th align="left">FireplaceQu</th>
<th align="left">Exterior1st</th>
<th align="left">GarageFinish</th>
<th align="left">PavedDrive</th>
<th align="left">Alley</th>
<th align="left">Fence</th>
<th align="left">BsmtExposure</th>
<th align="left">BldgType</th>
<th align="left">BsmtQual</th>
<th align="left">MasVnrType</th>
<th align="left">Electrical</th>
<th align="left">Condition1</th>
<th align="left">HeatingQC</th>
<th align="left">MSZoning</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtFinType2</th>
<th align="left">Street</th>
<th align="left">LandContour</th>
<th align="left">LotConfig</th>
<th align="left">GarageQual</th>
<th align="left">Neighborhood</th>
<th align="left">PoolQC</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">LandSlope</th>
<th align="left">ExterCond</th>
<th align="left">BsmtCond</th>
<th align="left">ExterQual</th>
<th align="left">Heating</th>
<th align="left">BsmtFinType1</th>
<th align="left">GarageType</th>
<th align="left">LotShape</th>
<th align="left">Functional</th>
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
<td align="left">15</td>
<td align="left">6</td>
<td align="left">5</td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">12</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">8</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left">6</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">25</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">5</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">6</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Y</td>
<td align="left">VinylSd</td>
<td align="left">CompShg</td>
<td align="left">Gable</td>
<td align="left">AllPub</td>
<td align="left">PConc</td>
<td align="left">Norm</td>
<td align="left">Gd</td>
<td align="left">VinylSd</td>
<td align="left">Fin</td>
<td align="left">Y</td>
<td align="left">-</td>
<td align="left">-</td>
<td align="left">No</td>
<td align="left">1Fam</td>
<td align="left">Gd</td>
<td align="left">None</td>
<td align="left">SBrkr</td>
<td align="left">Norm</td>
<td align="left">Ex</td>
<td align="left">RL</td>
<td align="left">1Story</td>
<td align="left">Unf</td>
<td align="left">Pave</td>
<td align="left">Lvl</td>
<td align="left">Inside</td>
<td align="left">TA</td>
<td align="left">NAmes</td>
<td align="left">-</td>
<td align="left">Gd</td>
<td align="left">TA</td>
<td align="left">Gtl</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">GLQ</td>
<td align="left">Attchd</td>
<td align="left">Reg</td>
<td align="left">Typ</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">571</td>
<td align="left">236</td>
<td align="left">569</td>
<td align="left">412</td>
<td align="left">583</td>
<td align="left">320</td>
<td align="left">579</td>
<td align="left">315</td>
<td align="left">239</td>
<td align="left">218</td>
<td align="left">556</td>
<td align="left">558</td>
<td align="left">484</td>
<td align="left">362</td>
<td align="left">510</td>
<td align="left">278</td>
<td align="left">284</td>
<td align="left">559</td>
<td align="left">509</td>
<td align="left">362</td>
<td align="left">508</td>
<td align="left">268</td>
<td align="left">521</td>
<td align="left">582</td>
<td align="left">518</td>
<td align="left">438</td>
<td align="left">556</td>
<td align="left">73</td>
<td align="left">577</td>
<td align="left">276</td>
<td align="left">572</td>
<td align="left">552</td>
<td align="left">530</td>
<td align="left">534</td>
<td align="left">274</td>
<td align="left">574</td>
<td align="left">205</td>
<td align="left">428</td>
<td align="left">351</td>
<td align="left">551</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: DBscan</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-1/figures/85795a71-c6db-4404-8a0f-a36a44c37443.png" alt="Visualização dos outliers: DBscan" /></p>

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
<td align="right">79.83</td>
<td align="right">96.40</td>
<td align="right">28259.03</td>
<td align="right">7.63</td>
<td align="right">5.77</td>
<td align="right">1948.97</td>
<td align="right">1987.60</td>
<td align="right">245.43</td>
<td align="right">943.17</td>
<td align="right">121.43</td>
<td align="right">627.13</td>
<td align="right">1691.73</td>
<td align="right">1808.30</td>
<td align="right">964.27</td>
<td align="right">45.37</td>
<td align="right">2817.93</td>
<td align="right">0.60</td>
<td align="right">0.10</td>
<td align="right">2.13</td>
<td align="right">0.60</td>
<td align="right">3.53</td>
<td align="right">1.20</td>
<td align="right">9.33</td>
<td align="right">1.47</td>
<td align="right">1973.90</td>
<td align="right">2.40</td>
<td align="right">708.23</td>
<td align="right">155.87</td>
<td align="right">122.07</td>
<td align="right">48.47</td>
<td align="right">0.00</td>
<td align="right">91.70</td>
<td align="right">68.87</td>
<td align="right">5.57</td>
<td align="right">2007.70</td>
<td align="right">329030.63</td>
</tr>
<tr>
<td align="left">std</td>
<td align="right">58.93</td>
<td align="right">52.54</td>
<td align="right">38460.44</td>
<td align="right">1.88</td>
<td align="right">1.70</td>
<td align="right">46.87</td>
<td align="right">20.19</td>
<td align="right">400.88</td>
<td align="right">1165.10</td>
<td align="right">278.52</td>
<td align="right">527.49</td>
<td align="right">1080.40</td>
<td align="right">726.33</td>
<td align="right">640.41</td>
<td align="right">141.02</td>
<td align="right">1012.03</td>
<td align="right">0.67</td>
<td align="right">0.31</td>
<td align="right">0.82</td>
<td align="right">0.50</td>
<td align="right">1.11</td>
<td align="right">0.41</td>
<td align="right">2.17</td>
<td align="right">0.57</td>
<td align="right">34.25</td>
<td align="right">0.72</td>
<td align="right">259.29</td>
<td align="right">204.48</td>
<td align="right">160.87</td>
<td align="right">131.24</td>
<td align="right">0.00</td>
<td align="right">150.47</td>
<td align="right">178.85</td>
<td align="right">2.87</td>
<td align="right">1.32</td>
<td align="right">197615.17</td>
</tr>
<tr>
<td align="left">min</td>
<td align="right">20.00</td>
<td align="right">47.00</td>
<td align="right">7200.00</td>
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
<td align="right">50.00</td>
<td align="right">60.00</td>
<td align="right">11025.00</td>
<td align="right">6.00</td>
<td align="right">5.00</td>
<td align="right">1908.50</td>
<td align="right">1971.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">184.50</td>
<td align="right">1020.00</td>
<td align="right">1368.00</td>
<td align="right">658.75</td>
<td align="right">0.00</td>
<td align="right">2099.75</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">2.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">8.00</td>
<td align="right">1.00</td>
<td align="right">1956.25</td>
<td align="right">2.00</td>
<td align="right">520.00</td>
<td align="right">0.00</td>
<td align="right">6.75</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">4.00</td>
<td align="right">2007.00</td>
<td align="right">164750.00</td>
</tr>
<tr>
<td align="left">50%</td>
<td align="right">60.00</td>
<td align="right">83.50</td>
<td align="right">15743.00</td>
<td align="right">7.00</td>
<td align="right">5.00</td>
<td align="right">1947.00</td>
<td align="right">1996.00</td>
<td align="right">0.00</td>
<td align="right">727.00</td>
<td align="right">0.00</td>
<td align="right">439.50</td>
<td align="right">1490.00</td>
<td align="right">1681.00</td>
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
<td align="right">1.00</td>
<td align="right">1984.50</td>
<td align="right">2.00</td>
<td align="right">801.00</td>
<td align="right">96.50</td>
<td align="right">65.00</td>
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
<td align="right">9.75</td>
<td align="right">7.00</td>
<td align="right">1995.75</td>
<td align="right">2002.75</td>
<td align="right">374.50</td>
<td align="right">1408.75</td>
<td align="right">0.00</td>
<td align="right">973.00</td>
<td align="right">1929.00</td>
<td align="right">1935.00</td>
<td align="right">1384.00</td>
<td align="right">0.00</td>
<td align="right">3244.25</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
<td align="right">4.00</td>
<td align="right">1.00</td>
<td align="right">11.00</td>
<td align="right">2.00</td>
<td align="right">2003.00</td>
<td align="right">3.00</td>
<td align="right">858.25</td>
<td align="right">212.50</td>
<td align="right">155.50</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">173.75</td>
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
<td align="right">1085.00</td>
<td align="right">1926.00</td>
<td align="right">6110.00</td>
<td align="right">4692.00</td>
<td align="right">2065.00</td>
<td align="right">572.00</td>
<td align="right">5642.00</td>
<td align="right">2.00</td>
<td align="right">1.00</td>
<td align="right">3.00</td>
<td align="right">1.00</td>
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
<th align="left">CentralAir</th>
<th align="left">Exterior2nd</th>
<th align="left">RoofMatl</th>
<th align="left">RoofStyle</th>
<th align="left">Utilities</th>
<th align="left">Foundation</th>
<th align="left">Condition2</th>
<th align="left">FireplaceQu</th>
<th align="left">Exterior1st</th>
<th align="left">GarageFinish</th>
<th align="left">PavedDrive</th>
<th align="left">Alley</th>
<th align="left">Fence</th>
<th align="left">BsmtExposure</th>
<th align="left">BldgType</th>
<th align="left">BsmtQual</th>
<th align="left">MasVnrType</th>
<th align="left">Electrical</th>
<th align="left">Condition1</th>
<th align="left">HeatingQC</th>
<th align="left">MSZoning</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtFinType2</th>
<th align="left">Street</th>
<th align="left">LandContour</th>
<th align="left">LotConfig</th>
<th align="left">GarageQual</th>
<th align="left">Neighborhood</th>
<th align="left">PoolQC</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">LandSlope</th>
<th align="left">ExterCond</th>
<th align="left">BsmtCond</th>
<th align="left">ExterQual</th>
<th align="left">Heating</th>
<th align="left">BsmtFinType1</th>
<th align="left">GarageType</th>
<th align="left">LotShape</th>
<th align="left">Functional</th>
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
<td align="left">2</td>
<td align="left">10</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">9</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">5</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">6</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">13</td>
<td align="left">4</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left">2</td>
<td align="left">6</td>
<td align="left">5</td>
<td align="left">4</td>
<td align="left">2</td>
</tr>
<tr>
<td align="left">top</td>
<td align="left">Y</td>
<td align="left">Wd Sdng</td>
<td align="left">CompShg</td>
<td align="left">Gable</td>
<td align="left">AllPub</td>
<td align="left">BrkTil</td>
<td align="left">Norm</td>
<td align="left">Gd</td>
<td align="left">Wd Sdng</td>
<td align="left">Unf</td>
<td align="left">Y</td>
<td align="left">-</td>
<td align="left">-</td>
<td align="left">No</td>
<td align="left">1Fam</td>
<td align="left">TA</td>
<td align="left">None</td>
<td align="left">SBrkr</td>
<td align="left">Norm</td>
<td align="left">Ex</td>
<td align="left">RL</td>
<td align="left">2Story</td>
<td align="left">Unf</td>
<td align="left">Pave</td>
<td align="left">Lvl</td>
<td align="left">Inside</td>
<td align="left">TA</td>
<td align="left">OldTown</td>
<td align="left">-</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">Gtl</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">GLQ</td>
<td align="left">Attchd</td>
<td align="left">Reg</td>
<td align="left">Typ</td>
</tr>
<tr>
<td align="left">freq</td>
<td align="left">24</td>
<td align="left">8</td>
<td align="left">26</td>
<td align="left">15</td>
<td align="left">30</td>
<td align="left">11</td>
<td align="left">27</td>
<td align="left">17</td>
<td align="left">10</td>
<td align="left">14</td>
<td align="left">26</td>
<td align="left">26</td>
<td align="left">22</td>
<td align="left">15</td>
<td align="left">24</td>
<td align="left">14</td>
<td align="left">19</td>
<td align="left">28</td>
<td align="left">20</td>
<td align="left">17</td>
<td align="left">20</td>
<td align="left">12</td>
<td align="left">24</td>
<td align="left">29</td>
<td align="left">23</td>
<td align="left">18</td>
<td align="left">24</td>
<td align="left">11</td>
<td align="left">26</td>
<td align="left">11</td>
<td align="left">29</td>
<td align="left">27</td>
<td align="left">22</td>
<td align="left">27</td>
<td align="left">13</td>
<td align="left">25</td>
<td align="left">11</td>
<td align="left">13</td>
<td align="left">16</td>
<td align="left">27</td>
</tr>
</tbody>
</table><p><em>Descrição Features Categóricas dos Outliers: Isolation Forest</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-1/figures/7034321d-ad60-4054-9ef9-b017855b4a55.png" alt="Visualização dos outliers: Isolation Forest" /></p>

<p><em>Visualização dos outliers: Isolation Forest</em></p>
<h2>Análise de Cluster</h2>
<p>O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. </p>
<h3>Feature Permutation 2 dim.</h3>
<p>A melhor separação de grupos ocorreu nas features: ['TotRmsAbvGrd', 'PoolArea'] com uma quantidade de 7 grupos. A análise multidimensional em 2 dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.</p>
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
</tr>
</thead>
<tbody>
<tr>
<td align="left">(61888.802, 161222.6]</td>
<td align="right">0.22</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.01</td>
<td align="right">0.31</td>
<td align="right">0.39</td>
<td align="right">0.07</td>
</tr>
<tr>
<td align="left">(457741.4, 556581.0]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(161222.6, 260062.2]</td>
<td align="right">0.33</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.09</td>
<td align="right">0.07</td>
<td align="right">0.29</td>
<td align="right">0.22</td>
</tr>
<tr>
<td align="left">(260062.2, 358901.8]</td>
<td align="right">0.22</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.32</td>
<td align="right">0.08</td>
<td align="right">0.11</td>
<td align="right">0.27</td>
</tr>
<tr>
<td align="left">(358901.8, 457741.4]</td>
<td align="right">0.25</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.44</td>
<td align="right">0.03</td>
<td align="right">0.06</td>
<td align="right">0.22</td>
</tr>
</tbody>
</table><p><em>Matriz de separação do melhor agrupamento</em></p>
<h3>Multidimensional</h3>
<p>A melhor separação de grupos ocorreu nas features: ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MoSold', 'YrSold', 'SalePrice'] com uma quantidade de 4 grupos. A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.</p>
<p>A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">0</th>
<th align="right">1</th>
<th align="right">2</th>
<th align="right">3</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">(61888.802, 161222.6]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(457741.4, 556581.0]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
</tr>
<tr>
<td align="left">(161222.6, 260062.2]</td>
<td align="right">0.72</td>
<td align="right">0.21</td>
<td align="right">0.07</td>
<td align="right">0.00</td>
</tr>
<tr>
<td align="left">(260062.2, 358901.8]</td>
<td align="right">0.00</td>
<td align="right">0.85</td>
<td align="right">0.00</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">(358901.8, 457741.4]</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">0.00</td>
<td align="right">1.00</td>
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
<td align="left">TotRmsAbvGrd - PoolArea</td>
<td align="right">0.90</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd - 3SsnPorch</td>
<td align="right">0.63</td>
<td align="right">nan</td>
</tr>
<tr>
<td align="left">YearBuilt - YearRemodAdd</td>
<td align="right">0.62</td>
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
<th align="right">outlier</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MSSubClass</td>
<td align="right">3.56</td>
<td align="right">-1.58</td>
<td align="right">0.28</td>
<td align="right">-9.21</td>
<td align="right">25.81</td>
</tr>
<tr>
<td align="left">LotFrontage</td>
<td align="right">-1.99</td>
<td align="right">8.43</td>
<td align="right">-8.55</td>
<td align="right">10.96</td>
<td align="right">21.55</td>
</tr>
<tr>
<td align="left">LotArea</td>
<td align="right">-256.62</td>
<td align="right">1416.94</td>
<td align="right">-1887.22</td>
<td align="right">2952.14</td>
<td align="right">17616.09</td>
</tr>
<tr>
<td align="left">OverallQual</td>
<td align="right">-0.23</td>
<td align="right">0.94</td>
<td align="right">-1.13</td>
<td align="right">1.78</td>
<td align="right">0.86</td>
</tr>
<tr>
<td align="left">OverallCond</td>
<td align="right">0.05</td>
<td align="right">-0.16</td>
<td align="right">0.20</td>
<td align="right">-0.37</td>
<td align="right">0.27</td>
</tr>
<tr>
<td align="left">YearBuilt</td>
<td align="right">3.91</td>
<td align="right">15.63</td>
<td align="right">-25.02</td>
<td align="right">21.74</td>
<td align="right">-30.73</td>
</tr>
<tr>
<td align="left">YearRemodAdd</td>
<td align="right">2.99</td>
<td align="right">11.13</td>
<td align="right">-17.98</td>
<td align="right">15.29</td>
<td align="right">-1.71</td>
</tr>
<tr>
<td align="left">MasVnrArea</td>
<td align="right">-45.94</td>
<td align="right">73.20</td>
<td align="right">-85.03</td>
<td align="right">229.15</td>
<td align="right">94.71</td>
</tr>
<tr>
<td align="left">BsmtFinSF1</td>
<td align="right">-111.32</td>
<td align="right">131.01</td>
<td align="right">-144.92</td>
<td align="right">490.25</td>
<td align="right">438.89</td>
</tr>
<tr>
<td align="left">BsmtFinSF2</td>
<td align="right">11.64</td>
<td align="right">-0.94</td>
<td align="right">-0.02</td>
<td align="right">-38.44</td>
<td align="right">79.66</td>
</tr>
<tr>
<td align="left">BsmtUnfSF</td>
<td align="right">0.52</td>
<td align="right">95.89</td>
<td align="right">-94.87</td>
<td align="right">35.88</td>
<td align="right">-20.85</td>
</tr>
<tr>
<td align="left">TotalBsmtSF</td>
<td align="right">-99.16</td>
<td align="right">225.96</td>
<td align="right">-239.80</td>
<td align="right">487.69</td>
<td align="right">497.70</td>
</tr>
<tr>
<td align="left">1stFlrSF</td>
<td align="right">-79.31</td>
<td align="right">193.20</td>
<td align="right">-216.08</td>
<td align="right">431.68</td>
<td align="right">524.93</td>
</tr>
<tr>
<td align="left">2ndFlrSF</td>
<td align="right">9.64</td>
<td align="right">96.61</td>
<td align="right">-140.23</td>
<td align="right">141.33</td>
<td align="right">553.56</td>
</tr>
<tr>
<td align="left">LowQualFinSF</td>
<td align="right">1.71</td>
<td align="right">-2.52</td>
<td align="right">1.04</td>
<td align="right">-2.52</td>
<td align="right">42.84</td>
</tr>
<tr>
<td align="left">GrLivArea</td>
<td align="right">-67.96</td>
<td align="right">287.28</td>
<td align="right">-355.27</td>
<td align="right">570.49</td>
<td align="right">1121.33</td>
</tr>
<tr>
<td align="left">BsmtFullBath</td>
<td align="right">-0.11</td>
<td align="right">0.14</td>
<td align="right">-0.11</td>
<td align="right">0.33</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">BsmtHalfBath</td>
<td align="right">0.02</td>
<td align="right">-0.04</td>
<td align="right">0.03</td>
<td align="right">-0.04</td>
<td align="right">0.04</td>
</tr>
<tr>
<td align="left">FullBath</td>
<td align="right">0.12</td>
<td align="right">0.24</td>
<td align="right">-0.45</td>
<td align="right">0.33</td>
<td align="right">0.42</td>
</tr>
<tr>
<td align="left">HalfBath</td>
<td align="right">0.06</td>
<td align="right">0.04</td>
<td align="right">-0.15</td>
<td align="right">0.15</td>
<td align="right">0.12</td>
</tr>
<tr>
<td align="left">BedroomAbvGr</td>
<td align="right">-0.02</td>
<td align="right">0.07</td>
<td align="right">-0.05</td>
<td align="right">0.05</td>
<td align="right">0.61</td>
</tr>
<tr>
<td align="left">KitchenAbvGr</td>
<td align="right">-0.00</td>
<td align="right">-0.00</td>
<td align="right">0.01</td>
<td align="right">-0.00</td>
<td align="right">0.20</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd</td>
<td align="right">-0.13</td>
<td align="right">0.61</td>
<td align="right">-0.86</td>
<td align="right">1.50</td>
<td align="right">2.35</td>
</tr>
<tr>
<td align="left">Fireplaces</td>
<td align="right">-0.04</td>
<td align="right">-0.02</td>
<td align="right">0.03</td>
<td align="right">0.09</td>
<td align="right">0.34</td>
</tr>
<tr>
<td align="left">GarageYrBlt</td>
<td align="right">3.37</td>
<td align="right">13.11</td>
<td align="right">-21.45</td>
<td align="right">19.38</td>
<td align="right">-8.35</td>
</tr>
<tr>
<td align="left">GarageCars</td>
<td align="right">-0.07</td>
<td align="right">0.41</td>
<td align="right">-0.54</td>
<td align="right">0.82</td>
<td align="right">0.35</td>
</tr>
<tr>
<td align="left">GarageArea</td>
<td align="right">-42.91</td>
<td align="right">131.01</td>
<td align="right">-143.04</td>
<td align="right">243.76</td>
<td align="right">168.40</td>
</tr>
<tr>
<td align="left">WoodDeckSF</td>
<td align="right">-6.15</td>
<td align="right">35.03</td>
<td align="right">-46.01</td>
<td align="right">70.33</td>
<td align="right">40.79</td>
</tr>
<tr>
<td align="left">OpenPorchSF</td>
<td align="right">1.96</td>
<td align="right">19.14</td>
<td align="right">-28.71</td>
<td align="right">30.66</td>
<td align="right">67.37</td>
</tr>
<tr>
<td align="left">EnclosedPorch</td>
<td align="right">-4.24</td>
<td align="right">-12.44</td>
<td align="right">17.62</td>
<td align="right">-6.28</td>
<td align="right">30.76</td>
</tr>
<tr>
<td align="left">3SsnPorch</td>
<td align="right">3.00</td>
<td align="right">-2.56</td>
<td align="right">-2.76</td>
<td align="right">4.73</td>
<td align="right">-3.74</td>
</tr>
<tr>
<td align="left">ScreenPorch</td>
<td align="right">-0.28</td>
<td align="right">4.94</td>
<td align="right">-1.35</td>
<td align="right">-7.95</td>
<td align="right">70.52</td>
</tr>
<tr>
<td align="left">PoolArea</td>
<td align="right">4.23</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">-2.21</td>
<td align="right">66.65</td>
</tr>
<tr>
<td align="left">MoSold</td>
<td align="right">-0.29</td>
<td align="right">0.47</td>
<td align="right">-0.16</td>
<td align="right">0.26</td>
<td align="right">-0.97</td>
</tr>
<tr>
<td align="left">YrSold</td>
<td align="right">-0.01</td>
<td align="right">-0.02</td>
<td align="right">-0.02</td>
<td align="right">0.16</td>
<td align="right">-0.03</td>
</tr>
<tr>
<td align="left">SalePrice</td>
<td align="right">-23422.05</td>
<td align="right">58232.00</td>
<td align="right">-78031.24</td>
<td align="right">168077.77</td>
<td align="right">112036.37</td>
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
<td align="left">MSSubClass</td>
<td align="right">0.10</td>
<td align="right">-0.05</td>
<td align="right">0.01</td>
<td align="right">-0.26</td>
<td align="right">0.74</td>
</tr>
<tr>
<td align="left">LotFrontage</td>
<td align="right">-0.08</td>
<td align="right">0.34</td>
<td align="right">-0.35</td>
<td align="right">0.44</td>
<td align="right">0.87</td>
</tr>
<tr>
<td align="left">LotArea</td>
<td align="right">-0.05</td>
<td align="right">0.28</td>
<td align="right">-0.38</td>
<td align="right">0.59</td>
<td align="right">3.54</td>
</tr>
<tr>
<td align="left">OverallQual</td>
<td align="right">-0.18</td>
<td align="right">0.76</td>
<td align="right">-0.91</td>
<td align="right">1.43</td>
<td align="right">0.69</td>
</tr>
<tr>
<td align="left">OverallCond</td>
<td align="right">0.05</td>
<td align="right">-0.17</td>
<td align="right">0.21</td>
<td align="right">-0.39</td>
<td align="right">0.28</td>
</tr>
<tr>
<td align="left">YearBuilt</td>
<td align="right">0.14</td>
<td align="right">0.56</td>
<td align="right">-0.90</td>
<td align="right">0.78</td>
<td align="right">-1.11</td>
</tr>
<tr>
<td align="left">YearRemodAdd</td>
<td align="right">0.15</td>
<td align="right">0.57</td>
<td align="right">-0.92</td>
<td align="right">0.78</td>
<td align="right">-0.09</td>
</tr>
<tr>
<td align="left">MasVnrArea</td>
<td align="right">-0.21</td>
<td align="right">0.34</td>
<td align="right">-0.39</td>
<td align="right">1.06</td>
<td align="right">0.44</td>
</tr>
<tr>
<td align="left">BsmtFinSF1</td>
<td align="right">-0.23</td>
<td align="right">0.27</td>
<td align="right">-0.30</td>
<td align="right">1.03</td>
<td align="right">0.92</td>
</tr>
<tr>
<td align="left">BsmtFinSF2</td>
<td align="right">0.07</td>
<td align="right">-0.01</td>
<td align="right">-0.00</td>
<td align="right">-0.24</td>
<td align="right">0.49</td>
</tr>
<tr>
<td align="left">BsmtUnfSF</td>
<td align="right">0.00</td>
<td align="right">0.21</td>
<td align="right">-0.20</td>
<td align="right">0.08</td>
<td align="right">-0.04</td>
</tr>
<tr>
<td align="left">TotalBsmtSF</td>
<td align="right">-0.26</td>
<td align="right">0.58</td>
<td align="right">-0.62</td>
<td align="right">1.26</td>
<td align="right">1.29</td>
</tr>
<tr>
<td align="left">1stFlrSF</td>
<td align="right">-0.21</td>
<td align="right">0.52</td>
<td align="right">-0.59</td>
<td align="right">1.17</td>
<td align="right">1.42</td>
</tr>
<tr>
<td align="left">2ndFlrSF</td>
<td align="right">0.02</td>
<td align="right">0.21</td>
<td align="right">-0.31</td>
<td align="right">0.31</td>
<td align="right">1.21</td>
</tr>
<tr>
<td align="left">LowQualFinSF</td>
<td align="right">0.06</td>
<td align="right">-0.08</td>
<td align="right">0.03</td>
<td align="right">-0.08</td>
<td align="right">1.42</td>
</tr>
<tr>
<td align="left">GrLivArea</td>
<td align="right">-0.15</td>
<td align="right">0.65</td>
<td align="right">-0.80</td>
<td align="right">1.29</td>
<td align="right">2.53</td>
</tr>
<tr>
<td align="left">BsmtFullBath</td>
<td align="right">-0.21</td>
<td align="right">0.27</td>
<td align="right">-0.21</td>
<td align="right">0.64</td>
<td align="right">0.30</td>
</tr>
<tr>
<td align="left">BsmtHalfBath</td>
<td align="right">0.08</td>
<td align="right">-0.17</td>
<td align="right">0.11</td>
<td align="right">-0.18</td>
<td align="right">0.15</td>
</tr>
<tr>
<td align="left">FullBath</td>
<td align="right">0.24</td>
<td align="right">0.48</td>
<td align="right">-0.90</td>
<td align="right">0.66</td>
<td align="right">0.85</td>
</tr>
<tr>
<td align="left">HalfBath</td>
<td align="right">0.12</td>
<td align="right">0.07</td>
<td align="right">-0.29</td>
<td align="right">0.29</td>
<td align="right">0.23</td>
</tr>
<tr>
<td align="left">BedroomAbvGr</td>
<td align="right">-0.02</td>
<td align="right">0.09</td>
<td align="right">-0.07</td>
<td align="right">0.07</td>
<td align="right">0.83</td>
</tr>
<tr>
<td align="left">KitchenAbvGr</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">0.14</td>
<td align="right">-0.06</td>
<td align="right">3.27</td>
</tr>
<tr>
<td align="left">TotRmsAbvGrd</td>
<td align="right">-0.09</td>
<td align="right">0.42</td>
<td align="right">-0.60</td>
<td align="right">1.04</td>
<td align="right">1.63</td>
</tr>
<tr>
<td align="left">Fireplaces</td>
<td align="right">-0.11</td>
<td align="right">-0.05</td>
<td align="right">0.08</td>
<td align="right">0.27</td>
<td align="right">0.97</td>
</tr>
<tr>
<td align="left">GarageYrBlt</td>
<td align="right">0.13</td>
<td align="right">0.52</td>
<td align="right">-0.86</td>
<td align="right">0.77</td>
<td align="right">-0.33</td>
</tr>
<tr>
<td align="left">GarageCars</td>
<td align="right">-0.10</td>
<td align="right">0.63</td>
<td align="right">-0.84</td>
<td align="right">1.26</td>
<td align="right">0.54</td>
</tr>
<tr>
<td align="left">GarageArea</td>
<td align="right">-0.22</td>
<td align="right">0.67</td>
<td align="right">-0.73</td>
<td align="right">1.25</td>
<td align="right">0.87</td>
</tr>
<tr>
<td align="left">WoodDeckSF</td>
<td align="right">-0.05</td>
<td align="right">0.28</td>
<td align="right">-0.37</td>
<td align="right">0.56</td>
<td align="right">0.32</td>
</tr>
<tr>
<td align="left">OpenPorchSF</td>
<td align="right">0.03</td>
<td align="right">0.31</td>
<td align="right">-0.47</td>
<td align="right">0.50</td>
<td align="right">1.10</td>
</tr>
<tr>
<td align="left">EnclosedPorch</td>
<td align="right">-0.08</td>
<td align="right">-0.22</td>
<td align="right">0.32</td>
<td align="right">-0.11</td>
<td align="right">0.55</td>
</tr>
<tr>
<td align="left">3SsnPorch</td>
<td align="right">0.10</td>
<td align="right">-0.09</td>
<td align="right">-0.09</td>
<td align="right">0.16</td>
<td align="right">-0.13</td>
</tr>
<tr>
<td align="left">ScreenPorch</td>
<td align="right">-0.00</td>
<td align="right">0.08</td>
<td align="right">-0.02</td>
<td align="right">-0.13</td>
<td align="right">1.14</td>
</tr>
<tr>
<td align="left">PoolArea</td>
<td align="right">0.11</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">-0.06</td>
<td align="right">1.81</td>
</tr>
<tr>
<td align="left">MoSold</td>
<td align="right">-0.10</td>
<td align="right">0.17</td>
<td align="right">-0.06</td>
<td align="right">0.09</td>
<td align="right">-0.35</td>
</tr>
<tr>
<td align="left">YrSold</td>
<td align="right">-0.01</td>
<td align="right">-0.01</td>
<td align="right">-0.02</td>
<td align="right">0.12</td>
<td align="right">-0.02</td>
</tr>
<tr>
<td align="left">SalePrice</td>
<td align="right">-0.30</td>
<td align="right">0.73</td>
<td align="right">-0.98</td>
<td align="right">2.12</td>
<td align="right">1.41</td>
</tr>
</tbody>
</table><p><em>Diferença de Variância entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-1/figures/7b0546ef-48f1-40bd-b690-d1861200a51d.png" alt="Diferença de Média entre População - Grupos" /></p>

<p><em>Diferença de Média entre População - Grupos</em></p>
<p><img src="insights/markdown_generator/CPQDAutoMLAlgorithm-1/figures/93fdc0ca-c904-489b-a64e-a64c08905a18.png" alt="Diferença de Variância entre População - Grupos" /></p>

<p><em>Diferença de Variância entre População - Grupos</em></p>
<p>A maior diferença populacional positiva foi detectada na feature SalePrice e no grupo 3, com valor de 168077.77. A maior variação negativa foi na feature SalePrice e no grupo 2, com o valor registrado de -78031.24</p>
<h3>Insights - Variáveis Categóricas</h3>
<p>É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">CentralAir</th>
<th align="left">Exterior2nd</th>
<th align="left">RoofMatl</th>
<th align="left">RoofStyle</th>
<th align="left">Utilities</th>
<th align="left">Foundation</th>
<th align="left">Condition2</th>
<th align="left">FireplaceQu</th>
<th align="left">Exterior1st</th>
<th align="left">GarageFinish</th>
<th align="left">PavedDrive</th>
<th align="left">Alley</th>
<th align="left">Fence</th>
<th align="left">BsmtExposure</th>
<th align="left">BldgType</th>
<th align="left">BsmtQual</th>
<th align="left">MasVnrType</th>
<th align="left">Electrical</th>
<th align="left">Condition1</th>
<th align="left">HeatingQC</th>
<th align="left">MSZoning</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtFinType2</th>
<th align="left">Street</th>
<th align="left">LandContour</th>
<th align="left">LotConfig</th>
<th align="left">GarageQual</th>
<th align="left">Neighborhood</th>
<th align="left">PoolQC</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">LandSlope</th>
<th align="left">ExterCond</th>
<th align="left">BsmtCond</th>
<th align="left">ExterQual</th>
<th align="left">Heating</th>
<th align="left">BsmtFinType1</th>
<th align="left">GarageType</th>
<th align="left">LotShape</th>
<th align="left">Functional</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Y</td>
<td align="left">VinylSd</td>
<td align="left">CompShg</td>
<td align="left">Hip</td>
<td align="left">AllPub</td>
<td align="left">PConc</td>
<td align="left">Norm</td>
<td align="left">TA</td>
<td align="left">VinylSd</td>
<td align="left">Fin</td>
<td align="left">Y</td>
<td align="left">-</td>
<td align="left">-</td>
<td align="left">Gd</td>
<td align="left">1Fam</td>
<td align="left">Ex</td>
<td align="left">None</td>
<td align="left">SBrkr</td>
<td align="left">Norm</td>
<td align="left">Ex</td>
<td align="left">RL</td>
<td align="left">1Story</td>
<td align="left">Unf</td>
<td align="left">Pave</td>
<td align="left">Lvl</td>
<td align="left">Inside</td>
<td align="left">TA</td>
<td align="left">NridgHt</td>
<td align="left">-</td>
<td align="left">Ex</td>
<td align="left">TA</td>
<td align="left">Gtl</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">GasA</td>
<td align="left">GLQ</td>
<td align="left">Attchd</td>
<td align="left">Reg</td>
<td align="left">Typ</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">190</td>
<td align="left">34</td>
<td align="left">54</td>
<td align="left">32</td>
<td align="left">190</td>
<td align="left">52</td>
<td align="left">190</td>
<td align="left">93</td>
<td align="left">34</td>
<td align="left">42</td>
<td align="left">54</td>
<td align="left">54</td>
<td align="left">53</td>
<td align="left">19</td>
<td align="left">52</td>
<td align="left">37</td>
<td align="left">119</td>
<td align="left">54</td>
<td align="left">136</td>
<td align="left">50</td>
<td align="left">181</td>
<td align="left">73</td>
<td align="left">53</td>
<td align="left">190</td>
<td align="left">177</td>
<td align="left">137</td>
<td align="left">54</td>
<td align="left">23</td>
<td align="left">143</td>
<td align="left">32</td>
<td align="left">143</td>
<td align="left">184</td>
<td align="left">52</td>
<td align="left">52</td>
<td align="left">152</td>
<td align="left">54</td>
<td align="left">44</td>
<td align="left">161</td>
<td align="left">137</td>
<td align="left">54</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">1.0</td>
<td align="left">0.6296296296296297</td>
<td align="left">1.0</td>
<td align="left">0.5925925925925926</td>
<td align="left">1.0</td>
<td align="left">0.9629629629629629</td>
<td align="left">1.0</td>
<td align="left">0.48947368421052634</td>
<td align="left">0.6296296296296297</td>
<td align="left">0.7777777777777778</td>
<td align="left">1.0</td>
<td align="left">1.0</td>
<td align="left">0.9814814814814815</td>
<td align="left">0.35185185185185186</td>
<td align="left">0.9629629629629629</td>
<td align="left">0.6851851851851852</td>
<td align="left">0.7168674698795181</td>
<td align="left">1.0</td>
<td align="left">0.951048951048951</td>
<td align="left">0.9259259259259259</td>
<td align="left">0.9526315789473684</td>
<td align="left">0.5104895104895105</td>
<td align="left">0.9814814814814815</td>
<td align="left">1.0</td>
<td align="left">0.9315789473684211</td>
<td align="left">0.8253012048192772</td>
<td align="left">1.0</td>
<td align="left">0.42592592592592593</td>
<td align="left">1.0</td>
<td align="left">0.5925925925925926</td>
<td align="left">1.0</td>
<td align="left">0.968421052631579</td>
<td align="left">0.9629629629629629</td>
<td align="left">0.9629629629629629</td>
<td align="left">0.9156626506024096</td>
<td align="left">1.0</td>
<td align="left">0.8148148148148148</td>
<td align="left">0.8473684210526315</td>
<td align="left">0.8253012048192772</td>
<td align="left">1.0</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">0.010849909584086825</td>
<td align="left">0.21009979237827342</td>
<td align="left">0.018083182640144635</td>
<td align="left">0.33400308083852387</td>
<td align="left">0.0</td>
<td align="left">0.40419261938249273</td>
<td align="left">0.001808318264014508</td>
<td align="left">0.12238507661558962</td>
<td align="left">0.20467483758623</td>
<td align="left">0.4034558971267832</td>
<td align="left">0.04159132007233268</td>
<td align="left">0.03797468354430378</td>
<td align="left">0.14603844350679795</td>
<td align="left">0.23973611948295492</td>
<td align="left">0.08412028665193216</td>
<td align="left">0.5224365414238832</td>
<td align="left">0.23766312991568445</td>
<td align="left">0.039783001808318286</td>
<td align="left">0.06678131994587688</td>
<td align="left">0.302056124840935</td>
<td align="left">0.07017226610830873</td>
<td align="left">0.03671012531772028</td>
<td align="left">0.08274730426629162</td>
<td align="left">0.0</td>
<td align="left">0.03646140668126008</td>
<td align="left">0.06580753393320116</td>
<td align="left">0.03797468354430378</td>
<td align="left">0.31200187529301454</td>
<td align="left">0.003616636528028905</td>
<td align="left">0.4605853593195365</td>
<td align="left">0.018083182640144635</td>
<td align="left">0.01905396402398407</td>
<td align="left">0.04433728484361388</td>
<td align="left">0.046145603107628386</td>
<td align="left">0.4436915836946338</td>
<td align="left">0.007233273056057921</td>
<td align="left">0.4640010715960083</td>
<td align="left">0.09691634148662798</td>
<td align="left">0.2195145863744309</td>
<td align="left">0.05244122965641951</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
</tbody>
</table><p><em>Diferença Máxima de População entre Grupos e Dataset</em></p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">CentralAir</th>
<th align="left">Exterior2nd</th>
<th align="left">RoofMatl</th>
<th align="left">RoofStyle</th>
<th align="left">Utilities</th>
<th align="left">Foundation</th>
<th align="left">Condition2</th>
<th align="left">FireplaceQu</th>
<th align="left">Exterior1st</th>
<th align="left">GarageFinish</th>
<th align="left">PavedDrive</th>
<th align="left">Alley</th>
<th align="left">Fence</th>
<th align="left">BsmtExposure</th>
<th align="left">BldgType</th>
<th align="left">BsmtQual</th>
<th align="left">MasVnrType</th>
<th align="left">Electrical</th>
<th align="left">Condition1</th>
<th align="left">HeatingQC</th>
<th align="left">MSZoning</th>
<th align="left">HouseStyle</th>
<th align="left">BsmtFinType2</th>
<th align="left">Street</th>
<th align="left">LandContour</th>
<th align="left">LotConfig</th>
<th align="left">GarageQual</th>
<th align="left">Neighborhood</th>
<th align="left">PoolQC</th>
<th align="left">KitchenQual</th>
<th align="left">GarageCond</th>
<th align="left">LandSlope</th>
<th align="left">ExterCond</th>
<th align="left">BsmtCond</th>
<th align="left">ExterQual</th>
<th align="left">Heating</th>
<th align="left">BsmtFinType1</th>
<th align="left">GarageType</th>
<th align="left">LotShape</th>
<th align="left">Functional</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">maior ocorrencia</td>
<td align="left">Y</td>
<td align="left">VinylSd</td>
<td align="left">CompShg</td>
<td align="left">Gable</td>
<td align="left">AllPub</td>
<td align="left">PConc</td>
<td align="left">Norm</td>
<td align="left">Gd</td>
<td align="left">VinylSd</td>
<td align="left">Fin</td>
<td align="left">Y</td>
<td align="left">-</td>
<td align="left">-</td>
<td align="left">No</td>
<td align="left">1Fam</td>
<td align="left">Gd</td>
<td align="left">None</td>
<td align="left">SBrkr</td>
<td align="left">Norm</td>
<td align="left">Ex</td>
<td align="left">RL</td>
<td align="left">1Story</td>
<td align="left">Unf</td>
<td align="left">Pave</td>
<td align="left">Lvl</td>
<td align="left">Inside</td>
<td align="left">TA</td>
<td align="left">NridgHt</td>
<td align="left">-</td>
<td align="left">Gd</td>
<td align="left">TA</td>
<td align="left">Gtl</td>
<td align="left">TA</td>
<td align="left">TA</td>
<td align="left">Gd</td>
<td align="left">GasA</td>
<td align="left">Unf</td>
<td align="left">Attchd</td>
<td align="left">Reg</td>
<td align="left">Typ</td>
</tr>
<tr>
<td align="left">contagem</td>
<td align="left">161</td>
<td align="left">92</td>
<td align="left">137</td>
<td align="left">84</td>
<td align="left">190</td>
<td align="left">110</td>
<td align="left">53</td>
<td align="left">88</td>
<td align="left">93</td>
<td align="left">75</td>
<td align="left">150</td>
<td align="left">156</td>
<td align="left">115</td>
<td align="left">73</td>
<td align="left">164</td>
<td align="left">89</td>
<td align="left">94</td>
<td align="left">148</td>
<td align="left">135</td>
<td align="left">113</td>
<td align="left">128</td>
<td align="left">83</td>
<td align="left">145</td>
<td align="left">190</td>
<td align="left">46</td>
<td align="left">98</td>
<td align="left">154</td>
<td align="left">28</td>
<td align="left">188</td>
<td align="left">115</td>
<td align="left">158</td>
<td align="left">132</td>
<td align="left">143</td>
<td align="left">172</td>
<td align="left">99</td>
<td align="left">164</td>
<td align="left">53</td>
<td align="left">95</td>
<td align="left">107</td>
<td align="left">150</td>
</tr>
<tr>
<td align="left">proporção</td>
<td align="left">0.9698795180722891</td>
<td align="left">0.4842105263157895</td>
<td align="left">0.958041958041958</td>
<td align="left">0.5874125874125874</td>
<td align="left">1.0</td>
<td align="left">0.5789473684210527</td>
<td align="left">0.9814814814814815</td>
<td align="left">0.5301204819277109</td>
<td align="left">0.48947368421052634</td>
<td align="left">0.39473684210526316</td>
<td align="left">0.9036144578313253</td>
<td align="left">0.9397590361445783</td>
<td align="left">0.6927710843373494</td>
<td align="left">0.5104895104895105</td>
<td align="left">0.8631578947368421</td>
<td align="left">0.6223776223776224</td>
<td align="left">0.49473684210526314</td>
<td align="left">0.891566265060241</td>
<td align="left">0.8132530120481928</td>
<td align="left">0.5947368421052631</td>
<td align="left">0.7710843373493976</td>
<td align="left">0.4368421052631579</td>
<td align="left">0.8734939759036144</td>
<td align="left">1.0</td>
<td align="left">0.8518518518518519</td>
<td align="left">0.6853146853146853</td>
<td align="left">0.927710843373494</td>
<td align="left">0.1958041958041958</td>
<td align="left">0.9894736842105263</td>
<td align="left">0.6052631578947368</td>
<td align="left">0.9518072289156626</td>
<td align="left">0.9230769230769231</td>
<td align="left">0.8614457831325302</td>
<td align="left">0.9052631578947369</td>
<td align="left">0.5210526315789473</td>
<td align="left">0.9879518072289156</td>
<td align="left">0.3192771084337349</td>
<td align="left">0.572289156626506</td>
<td align="left">0.5631578947368421</td>
<td align="left">0.9036144578313253</td>
</tr>
<tr>
<td align="left">diferença da população</td>
<td align="left">-0.01927057234362406</td>
<td align="left">0.06468068906443325</td>
<td align="left">-0.023874859317897346</td>
<td align="left">-0.1304897634011558</td>
<td align="left">0.0</td>
<td align="left">0.02017702484058248</td>
<td align="left">-0.016710200254503982</td>
<td align="left">-0.008758360748600147</td>
<td align="left">0.0645188921671267</td>
<td align="left">0.020414961454268576</td>
<td align="left">-0.054794222096341993</td>
<td align="left">-0.02226628031111788</td>
<td align="left">-0.1426719536373342</td>
<td align="left">-0.1169969271235094</td>
<td align="left">-0.015684781574188622</td>
<td align="left">0.128706736301673</td>
<td align="left">0.015532502141429483</td>
<td align="left">-0.06865073313144077</td>
<td align="left">-0.07101461905488138</td>
<td align="left">-0.029132958979727785</td>
<td align="left">-0.11137497548966202</td>
<td align="left">-0.036937279908632326</td>
<td align="left">-0.02524020131157545</td>
<td align="left">0.0</td>
<td align="left">-0.043265688835309124</td>
<td align="left">-0.07417898557139069</td>
<td align="left">-0.03431447308220226</td>
<td align="left">0.08188014517128442</td>
<td align="left">-0.006909679261444812</td>
<td align="left">0.12244218140287427</td>
<td align="left">-0.03010958844419276</td>
<td align="left">-0.02629016553067176</td>
<td align="left">-0.05717989498681886</td>
<td align="left">-0.011554201960597643</td>
<td align="left">0.0581231559912439</td>
<td align="left">-0.0048149197150264555</td>
<td align="left">0.02271291313536239</td>
<td align="left">-0.17816292293949754</td>
<td align="left">-0.04262872370800419</td>
<td align="left">-0.04394431251225517</td>
</tr>
<tr>
<td align="left">grupo</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">2</td>
</tr>
</tbody>
</table><p><em>Diferença Mínima de População entre Grupos e Dataset</em></p>
<h3>Insights - Resumo Clustering</h3>
<p>Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:</p>
<p>Grupo 0: Presença maior de população na feature FireplaceQu: TA, Presença maior de população na feature BsmtQual: Gd, Presença maior de população na feature Neighborhood: Gilbert, Presença maior de população na feature KitchenQual: Gd</p>
<p>Grupo 1: Média maior que a população: OverallQual, Média maior que a população: YearBuilt, Média maior que a população: YearRemodAdd, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: GrLivArea, Média maior que a população: GarageYrBlt, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: SalePrice, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature GarageFinish: Fin, Presença maior de população na feature BsmtQual: Gd, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature KitchenQual: Gd, Presença maior de população na feature ExterQual: Gd, Presença maior de população na feature BsmtFinType1: GLQ, Presença maior de população na feature LotShape: IR1</p>
<p>Grupo 2: Média menor que a população: OverallQual, Média menor que a população: YearBuilt, Média menor que a população: YearRemodAdd, Média menor que a população: TotalBsmtSF, Média menor que a população: 1stFlrSF, Média menor que a população: GrLivArea, Média menor que a população: FullBath, Média menor que a população: TotRmsAbvGrd, Média menor que a população: GarageYrBlt, Média menor que a população: GarageCars, Média menor que a população: GarageArea, Média menor que a população: SalePrice, Presença maior de população na feature Exterior2nd: MetalSd, Presença maior de população na feature RoofStyle: Gable, Presença maior de população na feature Foundation: CBlock, Presença maior de população na feature Exterior1st: Wd Sdng, Presença maior de população na feature GarageFinish: Unf, Presença maior de população na feature BsmtExposure: No, Presença maior de população na feature BsmtQual: TA, Presença maior de população na feature MasVnrType: None, Presença maior de população na feature HeatingQC: TA, Presença maior de população na feature Neighborhood: NAmes, Presença maior de população na feature KitchenQual: TA, Presença maior de população na feature ExterQual: TA, Presença maior de população na feature LotShape: Reg</p>
<p>Grupo 3: Média maior que a população: LotArea, Média maior que a população: OverallQual, Média maior que a população: YearBuilt, Média maior que a população: YearRemodAdd, Média maior que a população: MasVnrArea, Média maior que a população: BsmtFinSF1, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: GrLivArea, Média maior que a população: BsmtFullBath, Média maior que a população: FullBath, Média maior que a população: TotRmsAbvGrd, Média maior que a população: GarageYrBlt, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: WoodDeckSF, Média maior que a população: OpenPorchSF, Média maior que a população: SalePrice, Presença maior de população na feature Exterior2nd: VinylSd, Presença maior de população na feature RoofStyle: Hip, Presença maior de população na feature Foundation: PConc, Presença maior de população na feature FireplaceQu: Gd, Presença maior de população na feature Exterior1st: VinylSd, Presença maior de população na feature GarageFinish: Fin, Presença maior de população na feature Fence: -, Presença maior de população na feature BsmtExposure: Gd, Presença maior de população na feature BsmtQual: Ex, Presença maior de população na feature MasVnrType: BrkFace, Presença maior de população na feature HeatingQC: Ex, Presença maior de população na feature Neighborhood: NridgHt, Presença maior de população na feature KitchenQual: Ex, Presença maior de população na feature ExterQual: Gd, Presença maior de população na feature BsmtFinType1: GLQ</p>
<p>Grupo outlier: Média maior que a população: MSSubClass, Média maior que a população: LotFrontage, Média maior que a população: LotArea, Média maior que a população: OverallQual, Média menor que a população: YearBuilt, Média maior que a população: BsmtFinSF1, Média maior que a população: TotalBsmtSF, Média maior que a população: 1stFlrSF, Média maior que a população: 2ndFlrSF, Média maior que a população: LowQualFinSF, Média maior que a população: GrLivArea, Média maior que a população: FullBath, Média maior que a população: BedroomAbvGr, Média maior que a população: KitchenAbvGr, Média maior que a população: TotRmsAbvGrd, Média maior que a população: Fireplaces, Média maior que a população: GarageCars, Média maior que a população: GarageArea, Média maior que a população: OpenPorchSF, Média maior que a população: EnclosedPorch, Média maior que a população: ScreenPorch, Média maior que a população: PoolArea, Média maior que a população: SalePrice</p>
