## Issues version 1.0.0 05/02/2016

Help users in an organisation track their issues. An intuitive way to track all issues posted
by a user and the status of the issue.


### Install
`git clone https:github.com/makabby/issue-tracker.git`
`cd Issue-Tracker`
`virtualenv venv`
`source venv/bin/activate`
`$ pip install -r requirements.text`

### Usage
Interact with the python shell context already defined.
Made possible by `make_shell_context()` function.
```python
def make_shell_context():
    '''Returns application and database instances
    to the shell importing them automatically
    on `python manager.py shell`.
    '''
    return dict(app=app, db=db, User=User, Role=Role,
                Department=Department, Issue=Issue)
```
Initialise the shell with `Flask-Script` extension  Manager class.
```python
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
```

#### Run
Start the application with `python manage.py runserver` also made possible by
the `Flask-Script` extension.

visit http:localhost:5000
