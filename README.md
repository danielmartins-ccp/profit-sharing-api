# profit-sharing-api
API para calculo de Participação de lucros


Este repositório contém o código fontedo projeto de API para cálculo de participação de lucro. 


## Estrutura

O repositório está distribuído em diferentes pastas para melhor organização, segue abaixo descrição das pastas:

  * [profit_calc](./profit_calc/README.rst): contém um pacote reutilizavél do motor de regras e o calculo de distribuição; 
  * [dj_stone_profit_sharing_api](./dj_stone_profit_sharing_api/README.rst): contém uma aplicação completa de API Rest + Persistência feita principalmente com Django + DRF. 

Cada pasta possui internamente maiores detalhes de funcionamento. 


## Para executar a aplicação (para os apressados)

![GIF demonstrating base installation](https://gist.githubusercontent.com/danielmartins/51252360eaec89fa366940129f635195/raw/58656d080ee3dcda219b6daa24f3893094640faa/base_start.gif)

### Start

  1. Instalar docker
  2. Instalar docker-compose
  3. Entrar na pasta dj_stone_profit_sharing_api
  4. Levantar serviços
     1. docker-compose -f local.yml up -d
  5. Criar usuário
     1. docker-compose -f local.yml run django python manage.py createsuperuser
     2. Preencher as informações do usuário
  6. Acessar a documentação da API em http://localhost:8000/swagger
  