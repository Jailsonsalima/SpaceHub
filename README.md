# SpaceHub
Este repositório foi criado para o projeto do professor Fabio da disciplina de Desenvolvimento Web
# 📦 Projeto SpaceHub
Este projeto é um sistema web desenvolvido com **Django**, voltado para o projeto do professor Fabio da disciplina de Desenvolvimento Web, o qual facilitará a conexão entre clientes que
buscam salas comerciais e proprietários que desejam disponibilizá-las para aluguel.  
A aplicação oferece funcionalidades completas para:  

- **Administração de anúncios** 
- **Gestão de usuários e salas comerciais**  
- **Gerenciamento de usuários com diferentes níveis de acesso**, incluindo:  
  - cliente(Locatáio)
  - Proprietário(Locador)  
  - Administrador   

Com isso, o sistema centraliza e simplifica os processos de locação, garantindo a conexão entre locador e locatário.

## Desenvolvido com
* Python
* Django

## Estrutura do projeto
### Apps
* usuarios - Gerencia autenticação, cadastro, permisões e perfis de usuários(gerentes, gestores e funcionários).
* fornecedores - Armazena dados de fornecedores de produtos.
* produtos - Controla o catálogo de produtos de cada fornecedor.
* estoque - Monitora a retirada e a quantidade de produtos em estoque e alerta sobre níveis mínimos.
* compras - Registra lista de compras e itens solicitados para reposição do estoque da matriz e das filiais.
* empresas - Gerencia a matriz e as filiais.

### Fluxo de funcionamento
1. Usuários fazem login no sistema (Administrador, cliente ou proprietário).
2. Proprietário podem registar os anúncios de suas salas comerciais.
3. O sistema atualiza automaticamente os anúncios.

### Requisitos para rodar e editar o projeto
* Visual Studio Code;
* Uma conta no git-hub e git instalado;
* 

### Como rodar o projeto no windows
#### No terminal do vs code digite:
1. `git clone https://github.com/Jailsonsalima/SpaceHub.git` (baixa os arquivos do projeto)
2. `cd SpaceHub` (entra na pasta)
3. `python -m venv .venv` (cria um ambiente virtual)
4. `.venv/Scripts/activate` (ativa o ambiente virtual)
5. `pip install django` (instala o Django no ambiente virtual)
6. `python manage.py runserver` (roda o servdor. (Abra o navegador de internet e digite: `http://127.0.0.1:8000/`, para abrir o site do projeto))
7. para acessar o banco de dados do django digite no navegador de internet: `http://127.0.0.1:8000/admin` (usuário: admin; senha: 0123456789)
