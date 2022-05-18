from flask import render_template
from . import auth
from  .forms import LoginForm, RegistrationForm






@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()   
    

    return render_template('auth/register.html',registration_form = form)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()   
    

    return render_template('auth/login.html',login_form = form)