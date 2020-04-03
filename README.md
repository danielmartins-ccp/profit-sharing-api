# profit-sharing-api
API para calculo de Participação de lucros


Este repositório contém o código fontedo projeto de API para cálculo de participação de lucro. 


## Estrutura

O repositório está distribuído em diferentes pastas para melhor organização, segue abaixo descrição das pastas:

  * [profit_calc](./profict_calc/README.md): contém um pacote reutilizavél que contém o motor de regras e o calculo de distribuição; 
  * [dj_stone_profit_sharing_api](./dj_stone_profit_sharing_api/README.md): contém uma aplicação completa de API Rest + Persistência feita principalmente com Django + DRF



## Para executar a aplicação (para os apressados)

![GIF demonstrating base installation](https://gist.githubusercontent.com/danielmartins-ccp/bd014cf5781bfb7e67b3076c01bbffa5/raw/dcfd5bb2e758b52869708e3dceb5953aad9b973f/base_start.gif)

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
  