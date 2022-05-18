from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.sql import func
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
    projects =  db.relationship('Project',backref = 'user',passive_deletes = True)
    members =  db.relationship('TeamMembers',backref = 'user')
   
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


class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),nullable = False)
    alias = db.Column(db.String(255),nullable = False)
    description = db.Column(db.Text,nullable = False)
    start_date = db.Column(db.DateTime(timezone = True),default = func.now())
    completion_date = db.Column(db.DateTime(timezone = True))
    iscomplete = db.Column(db.Boolean,default= False)
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    subtasks =  db.relationship('SubTask',backref = 'project',passive_deletes = True)
    members =  db.relationship('TeamMembers',backref = 'project')



    def save_project(self):
        db.session.add(self)
        db.session.commit()

    def remove_project(self):
        db.session.delete(self)
        db.session.commit()


class SubTask(db.Model):

    __tablename__ = 'subtasks'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),nullable = False)
    description = db.Column(db.Text,nullable = False)
    start_date = db.Column(db.DateTime(timezone = True),default = func.now())
    completion_date = db.Column(db.DateTime(timezone = True))
    iscomplete = db.Column(db.Boolean,default= False)
    project_id = db.Column(db.Integer,db.ForeignKey('projects.id',ondelete="CASCADE"),nullable = False)



    def save_subtask(self):
        db.session.add(self)
        db.session.commit()

    def remove_subtask(self):
        db.session.delete(self)
        db.session.commit()

class TeamMembers(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    project_id = db.Column(db.Integer,db.ForeignKey('projects.id'),nullable = False)

    def save_member(self):
        db.session.add(self)
        db.session.commit()

    def remove_member(self):
        db.session.delete(self)
        db.session.commit()

    

 






    

    

  