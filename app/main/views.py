from flask import render_template
from . import main
from . forms import ProjectForm

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/project/new')
def new_project():

    form = ProjectForm()

    return render_template('new_project.html', form = form)

@main.route('/home')
def home():

    return render_template('home.html')

@main.route('/projects/details')
def project_details():
    return render_template('details.html')