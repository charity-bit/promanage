from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(255),nullable = False,unique = True)
    role = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    pic_path = db.Column(db.String(255),default='avtar.png')
    email = db.Column(db.String(255),nullable = False,unique = True)
    secure_password = db.Column(db.String(255),nullable = False) 
   
    def save_user(self):
        db.session.add(self)
        db.session.commit()



    @property
    def password(self):
        raise AttributeError('You cannot Read Attribute Error')

    @password.setter
    def password(self,password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)

    def __repr__(self):
        return f'User: {self.fullname} {self.email}'


