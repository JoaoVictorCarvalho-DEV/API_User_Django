
# Trabalho de Desenvolvimento Rápido de Aplicações em Python

---

## 🎓 Introdução

Este trabalho foi proposto pelo professor **Roney Malaguti**, responsável pela disciplina **Desenvolvimento Rápido de Aplicações em Pythons**, ministrada no turno noturno da **Universidade Wyden – UniRuy**, no dia **20 de fevereiro de 2025**.

Para a realização da atividade, os discentes foram organizados em grupos com, no máximo, seis integrantes. O objetivo consistia no desenvolvimento de um **projeto em Python**, utilizando um **framework à escolha dos alunos**, a ser apresentado no dia **29 de maio de 2025**. A entrega oficial deveria ser realizada por meio de um repositório no GitHub.

Com base nessas diretrizes, foi criado este repositório para o envio do projeto pelos seguintes membros da equipe:

- Dimitrius Khouri Mariano dos Santos  
- Guilherme Miguel Neto Santa Rosa 
- Luiz Fernando Ferreira Barbosa
- João Victor Miranda  
- Júlio Cesar Trabuco

---

## 💻 Sobre o Desenvolvimento do Projeto

A proposta do sistema foi sugerida por **Rafael Borges**, coordenador da SEMIT, com orientação do professor **Pedro Kislansky**, gerente da SEMIT e docente da UniRuy. O projeto foi desenvolvido como parte da disciplina de **Análise e Desenvolvimento de Sistemas**, sob a supervisão do professor **Roney Malaguti**.

A equipe realizou reuniões com representantes da coordenação para levantamento das demandas reais e, a partir disso, elaborou um **Documento de Requisitos** que serviu como guia para a implementação da solução.

---

## 🚀 Funcionalidades Principais  
*(Com base em sugestões de colegas e exigências de Rafael Borges)*

- ✅ Cadastro, visualização e edição de **projetos**
- ✅ Atribuição e acompanhamento de **tarefas**
- ✅ Registro de **atores** envolvidos nos projetos
- ✅ Gerenciamento de **órgãos institucionais**
- ✅ **Autenticação de usuários** via JWT
- ✅ API RESTful completa com documentação via **Swagger (OpenAPI)**

---

## 🔧 Funcionalidades Extras Implementadas  
*(Com base em sugestões de colegas e exigências do professor Roney Malaguti)*

- ✅ **Chat interno** entre usuários  
- ✅ **Quadro Kanban** com as etapas: *A Fazer*, *Executando* e *Concluídas*  
- ✅ **Dashboard institucional** com indicadores:
  - Total de usuários ativos  
  - Quantidade de projetos em andamento  
  - Distribuição de tarefas por status  
  - Órgãos participantes  

- ✅ **Documentação e suporte completos**, incluindo:
  - 📄 Documento de Requisitos do Sistema (DRS)  
  - 📘 Documentação técnica com fluxogramas e modelo entidade-relacionamento (ER)  
  - 📂 README detalhado para desenvolvedores  
  - ❓ FAQ com perguntas frequentes  
  - 🧑‍🏫 Manual do Usuário ilustrado  
  - 🧠 Código-fonte totalmente **comentado** para facilitar entendimento


---

## 📁 Gestor de Projetos

**Gestor de Projetos** é uma aplicação Django estruturada em arquitetura de **microserviços**, voltada para o **gerenciamento institucional de projetos**, incluindo tarefas, atores, órgãos e autenticação.  
A **API** e suporta autenticação via **JWT**, além de login tradicional por sessão.

---

## 🧩 Estrutura do Projeto

```
projeto/
├── manage.py
├── projeto/                    ← Projeto principal do Django
├── auth_manager_api/           ← Módulo de autenticação (JWT & Sessions)
├── sistema_auth/               ← Suporte à autenticação local
├── projeto_service/            ← Módulo de projetos
├── tarefa_service/             ← Módulo de tarefas       
├── atores_service/             ← Módulo de atores/papéis
├── orgao_service/              ← Módulo de órgãos
├── templates/                  
├── db.sqlite3
└── requirements.txt
```

---

## 🛠️ Requisitos

- Python 3.10+
- pip
- Git

---

## ⚙️ Instalação

```bash
git clone https://github.com/JoaoVictorCarvalho-DEV/API_User_Django.git
cd API_User_Django
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## 🚀 Execução

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Autenticação

- Modelo customizado: `auth_manager_api.CustomUser`
- Suporte a:
  - Autenticação por sessão (`SessionAuthentication`)
  - Autenticação por token (`JWT via djangorestframework-simplejwt`)

---

## 🔁 Endpoints Principais

| Caminho                       | Descrição                        |
|------------------------------|----------------------------------|
| `/admin/`                    | Painel administrativo do Django  |
| `/site/auth/`                | Tela de login/autenticação       |
| `/site/projetos/`            | Módulo de gerenciamento de projetos |
| `/site/tarefas/`             | Módulo de tarefas                |
| `/site/atores/`              | Módulo de atores e papéis        |
| `/site/orgaos/`              | Módulo de órgãos institucionais  |
| `/auth_api/`                 | API de autenticação via JWT      |
| `/api/v1/`                   | API REST geral (DRF router)      |

---

## 📄 Documentação OpenAPI

- Esquema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)
- Swagger UI (se habilitado): [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

Configuração:
```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'Auth & Projects API',
    'DESCRIPTION': 'API criada para ser um serviço de gerenciamento de projetos.',
    'VERSION': '1.0.0',
}
```

---

## 🌐 Localização e Fuso Horário

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

---

## 🧾 Banco de Dados

- Desenvolvimento:
```python
ENGINE = 'django.db.backends.sqlite3'
```

- Produção recomendada: PostgreSQL ou outro banco relacional robusto.

---

## 🔐 Segurança

Recomendações para ambiente de produção:
```python
DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
]
```

---

## 🗂 Modularização por App

```
auth_manager_api/    ← Autenticação e criação de usuários
projeto_service/     ← CRUD de projetos
tarefa_service/      ← CRUD de tarefas
atores_service/      ← Atores, papéis e permissões
orgao_service/       ← Órgãos e setores institucionais
```

---

## 📌 Status do Projeto

🚧 Em desenvolvimento  
Funcionalidades básicas de CRUD e autenticação já implementadas.

---

## 📜 Licença

Este projeto está licenciado sob os termos da **MIT License**.

---



