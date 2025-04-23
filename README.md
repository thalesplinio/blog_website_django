<h1 style="text-align:center;">Blog Com Django e PostegreSQL</h1>

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintainer](https://img.shields.io/badge/Lcence-MIT-blue)

</br>

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-FFD642?style=for-the-badge&logo=python&logoColor=3670A0)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
</br>
</br>

<p align="center">
    <img src="imgreadme/02image.png" alt="Tela inicial do site já preenchida" width="600px"/>
</p>

Status: Em desenvolvimento.

### 💻 Blog com Django e PostgreSQL, um pequeno portfólio para devs.

#### Sobre o projeto

#### 📌 <em>Este projeto foi feito para fins de estudos da linguagem python utilizando o framework Django com o banco de dados PostgreSQL, conta com a própria área administrativa do django onde pode ser feito as configurações do site e suas postagens.</em>

#### Tecnologias utilizadas

- Python 3.13
- Django 5.0
- PostgreSQL 16.8

## 🚀 Iniciando o projeto

> <em>Baixe o projeto e execute os comandos.</em>

- 🔧 Para linux

```Python
# Criando ambiente virtual
python3 -m venv venv

# Ativando o ambiente virtual
sourve venv/bin/activate
```

- 🔧 Para windows

```Python
# Criando ambiente virtual
python -m venv venv

# Ativando o ambiente virtual
venv/Scripts/Activate
```

- Instale as depencencias contidas em requirements.txt

```python
# No terminal execute
pip install -r requirements.txt
```

#### 📌 Para que o Django funcione perfeitamente adicione suas configurações do postgres no arquivo .env (após inserido remova o '-exemple' deixando apenas .env), execute os seguintes comandos para fazer as migrações do banco de dados.

```python
# No terminal execute
python manage.py makemigations
python manage.py migrate
```

### Se deu tudo certo você verá uma página assim

<p align="center">
    <img src="imgreadme/01img.png" width="400px"/>
</p>
### 📌 Agora precisamos criar um super usuário para acessar a área administrativa e fazer as configurações do site.

```python
# No terminal execute
python manage.py createsuperuser
```

> <em>Crie um super usuário entre na área administrativa e crie suas configurações</em> </br>

> <em>Em site Setup é onde deve ser feito as configurações como nome do site, descrições e o que deseja mostrar.</em> </br>

> <em>Em Blog é onde deve ser feito as configurações para o blog, como tags, categorias e posts, e tem uma área para 'sobre mim' onde configurei para mostar um pequeno resumo sobre mim.</em> </br>

## 📌 Mais imagens do projeto

- ### Tela inicial com site com o tema escuro aplicado

<p align="center">
    <img src="imgreadme/03image.png" alt="Tela inicial do site já preenchida com tema escuro" width="600px"/>
</p>

---

- ### Página da postagem
<p align="center">
    <img src="imgreadme/04image.png" alt="Tela de uma postagem sobre o python" width="600px"/>
</p>

---

- ### Menu projetos, listando projetos ou postagens com noticias.
<p align="center">
    <img src="imgreadme/05image.png" alt="menu projetos, listando 2 projetos" width="700px"/>
</p>

#### Autor: Thales Plinio.
