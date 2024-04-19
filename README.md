# Blog App
## Env
- Python3.10
- Flask3.0
- venv
- SQLite3.37

## How to build in your local env
### 1. Build
In your project directory, after `git pull`
```
$ python3 -m venv .venv
$ . .venv/bin/activate
$ flask --app flaskr init-db
$ flask --app flaskr run
```

### 2. Add the admin user data
Generate and copy the encrypted password
```
$ python3
>>> from werkzeug.security import generate_password_hash
>>> generate_password_hash('your preferred password')
```
Insert into the table
```
$ sqlite3 instance/flaskr.sqlite
sqlite> INSERT INTO users (name, password) VALUES ('username', 'your encrypted password');
```
