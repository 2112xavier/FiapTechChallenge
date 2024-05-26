# Tech Challenge 2024 - Entrega 1

**API para Informações sobre Produção, Processamento, Comercialização, Importação e Exportação de Uvas**

## Descrição

Esta API fornece informações relacionadas às abas de Produção, Processamento, Comercialização, Importação e Exportação do website "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01". Ela foi desenvolvida utilizando a linguagem de programação Python e o framework FastAPI.

![Alt text](/Documentation/Pos_TechChallenge_v1-Intro.png?raw=true "Optional Title")

## Tecnologias Utilizadas

-   **Linguagem de Programação**: Python
-   **Framework para a API**: FastAPI

![Alt text](/Documentation/Pos_TechChallenge_v1-ArqSolucao.png?raw=true "Optional Title")

## Endpoints da API

A seguir, são detalhados os endpoints disponíveis na API, onde é possível realizar o seu consumo através do método GET.

- https://api-emb.azurewebsites.net/docs#/ : Documentação da API criada pela FastAPI, sendo possível testar o seu consumo.
- https://api-emb.azurewebsites.net/producao : Endpoint sobre uva, vinho e derivados. Produção de vinhos, sucos e derivados do Rio Grande do Sul
- https://api-emb.azurewebsites.net/processamento : Endpoint sobre uva, vinho e derivados. Quantidade de uvas processadas no Rio Grande do Sul
- https://api-emb.azurewebsites.net/comercializacao : Endpoint sobre uva, vinho e derivados. Comercialização de vinhos e derivados no Rio Grande do Sul
- https://api-emb.azurewebsites.net/importacao : Endpoint sobre uva, vinho e derivados. Importação de derivados de uva
- https://api-emb.azurewebsites.net/exportacao : Endpoint sobre uva, vinho e derivados. Exportação de derivados de uva


## Código e Deploy da API

A API foi criada em Python, utilizando o framework FastAPI. Para realizar o scrapping da página da Embrapa, empregamos a biblioteca Pandas, realizando solicitações GET às URLs fornecidas pela Embrapa. Em seguida, os dados foram transformados em um dataframe e convertidos para JSON. O Código fonte está armazenado em um repositório no GiHub, e utilizando o GitHub Actions para automatizar o deploy do código no serviço de aplicativos da Azure. 

Para mais informações de como o App Service funciona, consultar a documentação oficial da Microsoft:
https://learn.microsoft.com/en-us/training/modules/deploy-run-container-app-service/

![Alt text](/Documentation/Pos_TechChallenge_v1-Deploy.png?raw=true "Optional Title")

Após o acesso à AWS for viabilizado e os devidos conteúdos serem apresentados, vamos migrar a solução para o ambiente, dando continuidade nos próximos desenvolvimentos do curso. 

## Considerações Finais

Esta API foi desenvolvida para facilitar o acesso a dados específicos disponíveis no website da Embrapa. Para manter a API funcionando corretamente, é importante verificar periodicamente a estrutura do site de origem para garantir que o scraping continue a funcionar conforme esperado.
