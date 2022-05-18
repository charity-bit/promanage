from flask_login import login_required,login_user,current_user,logout_user

from flask import render_template,redirect,url_for,request
from . import auth
from  .forms import LoginForm, RegistrationForm
from ..models import User






@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(fullname = form.fullname.data,email= form.email.data,role = form.role.data,password = form.password.data)
        user.save_user()
        login_user(user)
        print(user)
        
        return redirect(url_for('auth.login'))
    
   

    return render_template('auth/register.html',registration_form = form)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if  form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.home')) 
    
      
    return render_template('auth/login.html',login_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.index'))