# SQLite, SQlAlchemy, fastapi backend

A db project using SQLite, SQlAlchemy and fastapi

## Getting Started

### Enviroment (Linux)

- First create virtual enviroment and activate the enviroment

```
python3 -m venv .venv && source ./.venv/bin/activate
```

### Enviroment (Windows)

- Make sure you have virtualenv

```
pip install virtualenv
```

- First create virtual enviroment

```
virtualenv --python C:\Path\To\Python\python.exe venv
```

- Activate the enviroment

```
.\venv\Scripts\activate
```

### Dependencies

- To save dependancies

```
pip freeze > requirements.txt
```

- To install dependancies

```
pip install -r requirements.txt
```

### Executing program

- To run
```
python -m minitulip.app -ir
```
- help
```
python -m minitulip.app -h
```
### Database
- To create a new revision, after creating your table in db.models run this command to create an alembic revision
```
python -m minitulip.app -c
// or 
python -m minitulip.app -c -m "REVISION MESSAGE"

```

- To update and mirate you database.db us -u (This will also create the db if it is not present) 
```
python -m minitulip.app -u
```
