# frete_calculator
Projeto de faculdade: um website simples para oferecer e encontrar serviços de frete.
College project: a simple website to offer and find shipping services.

# Instruções:
## Linguagem de programação utilizada no projeto PI II-A e disciplinas relacionadas:
Python 3
https://www.python.org/downloads/
*Necessita instalação para usar 

## Git
Ferramenta de versionamento para acesso e contribuição ao projeto:
https://git-scm.com/downloads
Guia -> https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 

## IDE
Escolha um: 
*Recomentado: VSCode
*Existem diversas outras opções. Essas são duas mais populares e "fáceis" de usar.
### VSCode
https://code.visualstudio.com/
+Mais versátil e customizável
+Um ambiente para praticamente qualquer projeto de programação
- Depende de extensões para ter várias funcionalidades
### Pycharm
https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
+Mais completo por padrão
-Tem versão paga e versão gratis

## GitHub
Nosso projeto no GitHub -> https://github.com/lucassmann/frete_calculator
Fazer conta (se não tem ainda) -> https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home
Um guia que eu recomendo -> https://www.git-tower.com/learn/git/commands

## VSCode Config
### 1. Extensões:
- Python Extention Pack (extensões essenciais e/ou bastante úteis para Python)
- Git Extention Pack (extensões essenciais e/ou bastante úteis para Git)
*Opcional: Python Type Hint, Python Indent, Pylance


## Rodando no Windows
1. Ajustando a política de execução (ref https://cursos.alura.com.br/forum/topico-nao-consigo-criar-o-venv-da-aula-1-do-curso-142958)
    1.1. pesquisar no windows por PowerShell
    1.2. executar como administrador
    1.3. colar esse comando: Set-ExecutionPolicy AllSigned
    1.4. se pedir confirmação, digite S e pressione Enter.
2. Rodando o projeto (ref https://www.youtube.com/watch?v=QjtW-wnXlUY)
    2.1. Abra o VSCode na pasta do projeto
    2.2. Abra o terminal no VSCode
    2.3. Digite os seguintes comandos:
        -> py -m venv venv
        -> venv\Scripts\activate
        (confirme a execução digitando R ou A)
        -> pip install flask
        -> pip install flask-sqlalchemy
        -> set FLASK_APP=app.py
        -> flask run
    2.4 entre no link para ver o projeto no navegador (copie e cole ou ALT+Click)

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
