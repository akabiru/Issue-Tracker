#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role, Department, Issue
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'production')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    '''Returns application and database instances
    to the shell importing them automatically
    on `python manager.py shell`.
    '''
    return dict(app=app, db=db, User=User, Role=Role,
                Department=Department, Issue=Issue)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
