# app crud 

App crud é um website open-source que adiciona, visualiza, altera e exclui informações sobre clientes, produtos e pedidos. O seu diferencial é a capacidade de se adaptar em diferentes contextos e ritmos de trabalho.

## Tabela de conteúdos
* [Banco de dados]()
  * [Modelo entidade-relacionamento]()
* [Funcionalidades]()
* [Instalação e execução]()

## Banco de dados 
O banco de dados escolhido para o projeto foi o [MySQL](https://www.mysql.com/): Tradicional, relacional e robusto. Entretanto, fique a vontade para utilizar outras soluções, modificando devidamente o arquivo `settings.py`.

![](docs/db_eer.png)

Não sabe por onde começar? Um [ponto de partida](https://docs.djangoproject.com/en/5.1/ref/databases/) são os serviços com suporte oficial pelo framework Django.

## Funcionalidades 
A regra de negócio do app consiste em operações CRUD (Create, Read, Update and Delete), operações fundamentais em qualquer aplicação web. As entidades que recebem as operações são: Cliente, Produto e Aplicativo

