Profit Sharing API
==================
:License: GPLv3


Distribuição dos Lucros
-----------------------

Este projeto visa ser uma API REST para o cálculo de participação de lucros de acordo com regras específicas.

Regras
^^^^^^

* Foi estabelecido um peso por área de atuação:

  * Peso 1: Diretoria;
  * Peso 2: Contabilidade, Financeiro, Tecnologia;
  * Peso 3: Serviços Gerais;
  * Peso 5: Relacionamento com o Cliente;

* Foi estabelecido um peso por faixa salarial e uma exceção para estagiários:

  * Peso 5: Acima de 8 salários mínimos;
  * Peso 3: Acima de 5 salários mínimos e menor que 8 salários mínimos;
  * Peso 2: Acima de 3 salários mínimos e menor que 5 salários mínimos;
  * Peso 1: Todos os estagiários e funcionários que ganham até 3 salários mínimos;

* Foi estabelecido um peso por tempo de admissão:

  * Peso 1: Até 1 ano de casa;
  * Peso 2: Mais de 1 ano e menos de 3 anos;
  * Peso 3: Acima de 3 anos e menos de 8 anos;
  * Peso 5: Mais de 8 anos



Decisões
--------
Para o desenvolvimento deste projeto algumas divisões foram realizadas.

Decisão 1
^^^^^^^^^
Separação em 2 pacotes principais
  * API REST
  * Pacote de cálculo de distribuição e motor de especificação de regras.

Decisão 2
^^^^^^^^^
Arredondamento de valores para BAIXO: Diante da necessidade de arredondamento dos valores calculos, é realizada o arredondamento para BAIXO, para evitar extrapolar o valor alvo.

Decisão 3
^^^^^^^^^
A API calcula somente em RUNTIME, não faz persistência do cálculo. 


Organização do código
---------------------

Esta aplicação tradicional Django +  DRF

Aplicação principal se encontra dentro da pasta profit_sharing/:

  * `specifications.py <https://github.com/danielmartins-ccp/profit-sharing-api/blob/master/dj_stone_profit_sharing_api/profit_sharing/specifications.py>`_: Contém todas as especificações das regras (essas especificações usam o pacote `profit_calc <https://github.com/danielmartins-ccp/profit-sharing-api/blob/master/profit_calc/profit_calc/specifications.py>`_  * `views.py <https://github.com/danielmartins-ccp/profit-sharing-api/blob/master/dj_stone_profit_sharing_api/profit_sharing/views.py>`_ : Contém os controladores dos endpoints
  * `models.py <https://github.com/danielmartins-ccp/profit-sharing-api/blob/master/dj_stone_profit_sharing_api/profit_sharing/models.py>`_: Persistência + Integração com profit_calc


Testes
^^^^^^

Cobertura
~~~~~~~~~

Para executar os testes, gere o report HTML::

    $ docker-compose -f local.yml run django coverage run -m pytest
    $ docker-compose -f local.yml run django coverage html
    $ google-chrome htmlcov/index.html

Executando testes com  py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose -f local.yml run django pytest


Possível Roadmap
----------------

  * Dinamizar motor de regras (Talvez uma DSL ?)
  * Persistência do cálculo em 2 etapas (dry-run & persist)
  * Expor mecanismo de arredondamento
  * Criar endpoint para composição de regras

