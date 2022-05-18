
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))
    
#     return app