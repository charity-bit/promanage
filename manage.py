from flask_script import Server, Manager
from app import create_app

app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()