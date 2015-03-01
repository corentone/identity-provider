from flask.ext.script import Server, Shell, Manager
from app import create_app


def _make_context():
    return dict(app=create_app())


manager = Manager(create_app())
manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()