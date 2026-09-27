# API de Gestão Hospitalar (Django + DRF + MySQL)

API RESTful para gestão hospitalar, com duas entidades relacionadas (1:N):

- **Médico**: nome, especialidade, crm
- **Consulta**: paciente, data_consulta, valor, status, médico (FK)

Um médico pode ter várias consultas (`Medico 1:N Consulta`).

---

## 1. Pré-requisitos

- Python 3.11+ instalado
- MySQL Server instalado e rodando (local ou remoto)
- Git

---

## 2. Criar o banco de dados no MySQL

Abra o MySQL (Workbench, terminal ou DBeaver) e rode:

```sql
CREATE DATABASE hospital_db CHARACTER SET utf8mb4;
```

---

## 3. Clonar/baixar o projeto e criar o ambiente virtual

```bash
# entrar na pasta do projeto
cd hospital_api

# criar o ambiente virtual
python -m venv .venv

# ativar (Windows)
.venv\Scripts\Activate

# ativar (Linux/Mac)
source .venv/bin/activate
```

---

## 4. Instalar as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> **Se `mysqlclient` der erro ao instalar (comum no Windows):**
> Instale o "Microsoft C++ Build Tools" ou, mais simples, troque para o driver 100% Python:
> ```bash
> pip uninstall mysqlclient
> pip install PyMySQL
> ```
> E no arquivo `config/__init__.py`, adicione:
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

---

## 5. Configurar as variáveis de ambiente

Copie o arquivo de exemplo e edite com os dados do seu MySQL:

```bash
copy .env.example .env      # Windows
cp .env.example .env        # Linux/Mac
```

Edite o `.env`:

```
DEBUG=True
SECRET_KEY=django-insecure-chave-de-desenvolvimento
DB_NAME=hospital_db
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_HOST=localhost
DB_PORT=3306
```

---

## 6. Rodar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

(As migrações da app `api` já vêm prontas no projeto, mas rodar `makemigrations` não tem problema — o Django não recria nada se não houver mudanças.)

---

## 7. (Opcional) Criar um superusuário para acessar o /admin

```bash
python manage.py createsuperuser
```

---

## 8. Rodar o servidor

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

---

## 9. Endpoints disponíveis

### Médicos
| Método | URL | Ação |
|---|---|---|
| GET | `/api/medicos/` | Lista todos os médicos |
| GET | `/api/medicos/<id>/` | Detalha um médico |
| POST | `/api/medicos/` | Cria um médico |
| PUT | `/api/medicos/<id>/` | Atualiza (completo) |
| PATCH | `/api/medicos/<id>/` | Atualiza (parcial) |
| DELETE | `/api/medicos/<id>/` | Remove |

Exemplo de body (POST):
```json
{
  "nome": "Dra. Ana Souza",
  "especialidade": "Cardiologia",
  "crm": "12345-SP"
}
```

### Consultas
| Método | URL | Ação |
|---|---|---|
| GET | `/api/consultas/` | Lista todas as consultas |
| GET | `/api/consultas/<id>/` | Detalha uma consulta |
| POST | `/api/consultas/` | Cria uma consulta |
| PUT | `/api/consultas/<id>/` | Atualiza (completo) |
| PATCH | `/api/consultas/<id>/` | Atualiza (parcial) |
| DELETE | `/api/consultas/<id>/` | Remove |

Exemplo de body (POST):
```json
{
  "paciente": "João Pereira",
  "data_consulta": "2026-10-05T14:30:00",
  "valor": "250.00",
  "status": "AGENDADA",
  "medico_id": 1
}
```

### Filtros disponíveis em `/api/consultas/`
- `?status=AGENDADA`
- `?medico=1`
- `?paciente=joão` (busca parcial, sem diferenciar maiúsculas/minúsculas)
- `?valor_min=100&valor_max=500`

Exemplo combinando filtros:
```
GET /api/consultas/?status=AGENDADA&valor_min=100&valor_max=500
```

### Filtro disponível em `/api/medicos/`
- `?especialidade=Cardiologia`

---

## 10. Testando

Use o Postman, Insomnia, Thunder Client (VS Code) ou `curl` para testar todos os verbos HTTP acima.

---

## 11. Estrutura do projeto

```
hospital_api/
├── manage.py
├── requirements.txt
├── .env.example
├── config/
│   ├── settings.py      # configuração do MySQL, apps, DRF
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── api/
    ├── models.py         # Medico, Consulta
    ├── serializers.py    # ModelSerializer com serializer aninhado
    ├── filters.py        # ConsultaFilter (valor_min, valor_max, paciente)
    ├── services.py       # regras de criação (camada de serviço)
    ├── views.py          # ModelViewSet + DjangoFilterBackend
    ├── urls.py           # DefaultRouter
    ├── admin.py
    └── migrations/
```
