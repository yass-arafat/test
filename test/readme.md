## About
This project is about doing some simple CRUD operations following DDD(Domain Driven Design) and TDD(Test Driven Design) architecture.

## Installation

### Pre-Requisites:
- Python 3.9.6
- Sqlite 3.11.1

to run the project following commands:

environment set-up
```python
pip install -r requirements.txt
export Flask_APP=App.py
```
database set up:
```python
flask db init
flask db migrate
flask db upgrade
```
run the project
```python
flask run
```

unit test
```python
pytest tests/test.py
```



