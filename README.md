# Gestor de projetos

A aplicação é um gestor de projetos institucional, e trabalha na arquitetura de micro-serviços.
O projeto gira em torno de uma API de gerenciamento de projetos, que permite a criação, exclusão e edição de tarefas e projetos.
A API também  conta com um sistema de autenticação que usa JWT.


---

## 📌 Visão Geral

Este projeto é uma API modular voltada ao gerenciamento de entidades relacionadas à administração de projetos públicos e seus atores.

---

## 🧩 Estrutura do Projeto

```
projeto/
├── manage.py
├── projeto/                    -Projeto principal do Django
├── auth_manager_api/           -Auth n Projects API
├── sistema_auth/               -App para autenticação
├── projeto_service/            -App para projetos
├── tarefa_service/             -App para tarefas       
├── atores_service/             -App para atores/papeis
├── orgao_service/              -App para orgaos
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
source venv/bin/activate  # ou venv\Scripts\activate no Windows
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
- Suporte a Session e Token Authentication

---

## 🔁 Endpoints Principais

| Caminho                       | Descrição                        |
|------------------------------|----------------------------------|
| `/admin/`                    | Painel admin do Django           |
| `/site/auth/`                | Autenticação                     |
| `/site/projetos/`            | Módulo de Projetos               |
| `/site/tarefas/`             | Módulo de Tarefas                |
| `/site/atores/`              | Módulo de Atores                 |
| `/site/orgaos/`              | Módulo de Órgãos                 |
| `/auth_api/`                 | API de autenticação              |
| `/api/v1/`                   | API REST com router              |

---

## 📄 Documentação OpenAPI

- Esquema: `http://127.0.0.1:8000/api/schema/`
- Swagger UI (se habilitado): `http://127.0.0.1:8000/api/docs/`

Configuração:
```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'Auth n Projects API',
    'DESCRIPTION': 'API criada para ser um serviço de gereciamento de projetos.',
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

Padrão:
```python
ENGINE: django.db.backends.sqlite3
```

Em produção, recomenda-se PostgreSQL.

---

## 🔐 Segurança

Ajustar permissões para produção:
```python
'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
]
```

---

## 🗂 Sugestão de Modularização

```
api/
├── auth/
├── projetos/
├── tarefas/
├── atores/
├── orgaos/
```

---

## 📎 Observações

- `DEBUG = True` só deve ser usado em desenvolvimento.
- Altere `SECRET_KEY` para produção.
- Estrutura modular permite fácil manutenção e escalabilidade.

