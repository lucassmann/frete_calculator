# frete_calculator
(PT) Projeto de faculdade: um website simples para oferecer e encontrar serviços de frete.

(ENG) College project: a simple website to offer and find shipping services.

# Instruções:
## Python3 (linguagem de programação utilizada)
https://www.python.org/downloads/

## Git
Ferramenta de versionamento para acesso e contribuição ao projeto: https://git-scm.com/downloads

Guia para instalação -> https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 

Guia para uso -> https://www.git-tower.com/learn/git/commands

## IDE
Escolha um: 

Recomentado: VSCode. Existem diversas outras opções, essas são duas mais populares e "fáceis" de usar.
### VSCode
https://code.visualstudio.com/
- Mais versátil e customizável
- Um ambiente para praticamente qualquer projeto de programação
- Depende de extensões para ter várias funcionalidades
### Pycharm
https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
- Mais completo por padrão
- Tem versão paga e versão gratis


## VSCode Config
### Extensões:
- Python Extention Pack (extensões essenciais e/ou bastante úteis para Python)

*Opcional: Python Indent

- Git Extention Pack (extensões essenciais e/ou bastante úteis para Git)



## Rodando no Windows
### 1. Ajustando a política de execução
####    1.1. pesquisar no windows por PowerShell
####    1.2. executar como administrador
####    1.3. colar esse comando: Set-ExecutionPolicy AllSigned
####    1.4. se pedir confirmação, digite S e pressione Enter.
### 2. Rodando o projeto
####    2.1. Abra o VSCode na pasta do projeto
####    2.2. Abra o terminal no VSCode
####    2.3. Digite os seguintes comandos:
##### py -m venv venv
##### venv\Scripts\activate
##### Confirme a execução digitando R ou A (Erros nessa etapa podem indicar falha no item 1)
##### pip install flask
##### pip install flask-sqlalchemy
##### set FLASK_APP=app.py
##### flask run
####    2.4 entre no link para ver o projeto no navegador (copie e cole ou ALT+Click)

## Rodando no Linux
python3 -m venv venv
. venv/bin/activate

pip install Flask
pip install Flask-SQLAlchemy

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

### Opcional (potencialmente "complicado" mas bem mais prático quando pega o jeito)

Pra quem usa Windows, existe uma ferramenta chamada WSL2 (Windows Subsystem for Linux) que permite usar Linux dentro do Windows de forma bem integrada.

Porque é bom? Fácil(subjetivo) de instalar, atualizar e utilizar ferramentas para desenvolvimento de forma mais confiável e estável

Porque complicado? Tem q saber basição de terminal de Linux, pode ser difícil/impossível de instalar em Windows 10 dependendo da versão(Em Windows 11 é mais tranquilo).
