# Projeto - Formulário para envio de currículo
 Projeto para criação de formulário web com Python, Django e HTML. O formulário possui validações para campos obrigatórios, tipo do arquivo(doc, docx, pdf) e tamanho do arquivo(1MB).

 ## Intruções para executar o projeto:
 
Será necessário estar instalado na máquina o Python. Versão utilizada para desenvolvimento Python 3.13.1.

Acesse a pasta do projeto via PowerShel e crie o ambiente virtual: 

- cd caminho/do/projeto

- python -m venv venv

Ative o ambiente virtual (Windows):

- .\venv\Scripts\activate

OBS.: Caso tenha problemas de segurança no Windows para executar esse comando no PowerShel, será necessário abrir o PowerShel como administrador e executar o comando:

- Set-ExecutionPolicy RemoteSigned

Requirements (pip freeze):

- asgiref==3.8.1
- Django==5.1.5
- python-dotenv==1.0.1
- sqlparse==0.5.3
- tzdata==2025.1

Instale as dependências(Django e dotenv): 

- pip install django
- pip install python-dotenv

Na pasta raiz do projeto, crie um arquivo '.env'. Nela configure as seguintes variáveis:
- EMAIL_USER=seu_email@gmail.com
- EMAIL_APP_PASSWORD=senha do app gmail

Email_app_password deve ser uma senha de app criada pelo gmail(myaccount.google > procure por Senha de App > crie uma nova senha de app). Essa senha não será compartilhada com o sistema.

Rodar o servidor na máquina(Windows):

- python manage.py runserver

Acesse o formulário pelo navegador: http://127.0.0.1:8000/

Ao preencher o formulário corretamente, as informações ficaram salvas no banco de dados. Uma cópia das respostas do formulário serão enviadas para o email informado no formulário.

## Testes

Foram feitos testes iniciais para Views, Models e Forms.

Para executar os testes, certifique-se que existe o arquivo "Test.pdf" na pasta '/curriculos'. Esse arquivo será necessário para o teste do Model.

O comando para executar os testes é: 

- python manage.py test resume_form

Serão executados 5 testes(1 na view, 2 no model e 2 no form).
 

