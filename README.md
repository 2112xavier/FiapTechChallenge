# Tech Challenge 2024 - Entrega 1

**API para Informações sobre Produção, Processamento, Comercialização, Importação e Exportação de Uvas**

## Descrição

Esta API fornece informações relacionadas às abas de Produção, Processamento, Comercialização, Importação e Exportação do website "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01". Ela foi desenvolvida utilizando a linguagem de programação Python e o framework FastAPI.

![Alt text](/Documentation/Pos_TechChallenge_v1-Intro.png?raw=true "Optional Title")

## Tecnologias Utilizadas

-   **Linguagem de Programação**: Python
-   **Framework para a API**: FastAPI

![Alt text](/Documentation/Pos_TechChallenge_v1-Arq Solução.png?raw=true "Optional Title")

## Endpoints da API

A seguir, são detalhados os endpoints disponíveis na API:



## Deploy e disponibilização da API

Para viabilizar a execução da API, uma imagem Docker foi construída com o código Python, incluindo suas devidas bibliotecas. Esta imagem pode ser disponibilizada de N maneiras, mas como o conteúdo de AWS ainda não foi abordado no curso, seguimos com o conhecimento atual do time, sendo mais focado em Azure. Para realizar o deploy, criamos um Web App, utilizando o serviço da Azure chamado "App Service". 

![Alt text](/Documentation/Pos_TechChallenge_v1-Deploy.png?raw=true "Optional Title")

Para mais informações de como o App Service funciona, consultar a documentação oficial da Microsoft:
https://learn.microsoft.com/en-us/training/modules/deploy-run-container-app-service/

Após o acesso à AWS for viabilizado e os devidos conteúdos serem apresentados, vamos migrar a solução para o ambiente, dando continuidade nos próximos desenvolvimentos do curso. 

## Considerações Finais

Esta API foi desenvolvida para facilitar o acesso a dados específicos disponíveis no website da Embrapa. Para manter a API funcionando corretamente, é importante verificar periodicamente a estrutura do site de origem para garantir que o scraping continue a funcionar conforme esperado.
