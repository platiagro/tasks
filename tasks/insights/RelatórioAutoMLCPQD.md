<h1>Relatório AutoML CPQD</h1>
<h2>Criação de features Temporais</h2>
<pre><code>        Uma das etapas do componente de insights é a criação de novas featres temporais, e ela se torna
        importante para esse componente, pois, essas novas features melhoram a performace dos modelos
        de Machine Learning.

        Para criar essas novas features foi utilizada médias moveis agrupadas por uma coluna categórica,
        então, se a base de dados possui mais de uma coluna categórica haverá mais de um agrupamento, e
        assim gerando várias features novas.

        A cada agrupamento, quando é calculado as médias moveis, é calculado também o desvio padrão
        da mesma.
</code></pre>
<h3>Análise das novas features</h3>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/4014d055-d121-49a3-bf7f-40fe406819ae.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/83f6f572-17c1-4ce9-9902-b421b91f69f8.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/9cf45f69-3c01-4d6e-a7fa-928c81de0fed.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/42cdbffa-6ee5-4986-8688-ae8acc2b05f2.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/2881519e-f3a1-4430-a009-a282e867791b.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/7b96cc50-32a0-47aa-9e67-93a5bb1cd436.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/961cd7a0-8398-449c-b268-1b3392a46151.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/2d978811-32d7-412a-9ff7-9ae07407ea0f.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/79f6a6c1-d25c-400e-be28-671fceabea31.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/96c1b017-c58e-4940-aff1-1ccb42eadfee.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/06ad678a-c714-4f28-94fc-9b7678f955f0.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/dd0f346d-8698-4158-91f9-719b43921156.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/00a09842-bae2-48f1-9a11-2fa5b8e07385.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/cbc734eb-4c35-4063-bbe8-e52c9c02fa6c.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/1cabba0f-44d7-472e-a0de-b06408bad60c.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/4f83842d-0e22-4339-bbe7-f722a4c54182.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/b5502777-23c1-4d8c-bd88-61df1832c115.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/1bfb2e1f-ff23-4466-81c3-3190a4907351.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/0c83aa56-de65-46e6-b4ed-df200a819e87.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/b8321c52-c213-4f68-a822-abfd7be7c6d2.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/91b59650-1e49-48fd-ae74-95a55ac08499.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/fa97fc0b-e9d5-4ec4-8a98-0ebd5b49dd5f.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/2de1eadb-c8bd-4311-b994-e5a9a3ebda93.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/a944de4e-6381-4039-a1c2-652fbb80ba9b.png" alt="" /></p>
<h3>Análise das features categóricas</h3>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/171df5d8-49cf-40c5-86e4-2a537d5a44dc.png" alt="" /></p>
<h3>Análise de frequência dos dias da semana e meses</h3>
<h3>- Coluna de datatime: Mes</h3>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/fcb55e9c-fb52-48ae-90e9-387c3e117dca.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/4c82fd39-db22-4f29-8dc9-9aad17fe2282.png" alt="" /></p>
<h3>- Coluna de datatime: Data de emissao</h3>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/611f3f17-4d29-4e35-b5e0-29bef9b86599.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/5de72720-de24-4a4a-8ce9-d380c328c7d5.png" alt="" /></p>
<h3>- Coluna de datatime: Data de apresentacao</h3>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/14ebd83b-125f-44b0-b08b-246c5d56d34b.png" alt="" /></p>
<p><img src="insights/markdown_generator/RelatórioAutoMLCPQD/figures/e45a0754-80f7-41ae-b721-bdebad580984.png" alt="" /></p>
