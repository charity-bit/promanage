import datetime
from flask import render_template,flash,redirect,url_for
from sqlalchemy import alias
from . import main
from . forms import ProjectForm
from flask_login import current_user

from ..models import Project,User

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/project/new',methods=['POST','GET'])
def new_project():

    form = ProjectForm()

    if form.validate_on_submit():
        project_name = form.name.data
        project_details = form.details.data
        project_alias = form.uploader.data
        completion_date = form.completion_date.data
        
        # destructing completion date
        completion_month = completion_date.month
        completion_year = completion_date.year
        completion_day = completion_date.day

        
        now = datetime.datetime.now()
        completion_object = datetime.datetime(completion_year,completion_month,completion_day)

        
        if not project_name:
            flash("Project Name Cannot be Empty")

        elif not project_details:
            flash("Your project must have a description")

        elif not project_alias:
            flash("Your project must have an alias")
        
        elif not completion_date:
            flash("Please indicate the expected completion date")

        elif completion_object < now:
            flash("oops,you cannot complete the project yesterday")

        else:
            new_project = Project(name = project_name,alias = project_alias,description = project_details,owner_id = current_user.id,completion_date = completion_date )
            new_project.save_project()
            
            return redirect(url_for('main.index'))

    return render_template('new_project.html', form = form)

@main.route('/home')
def home():

    projects = Project.query.all()

    # query state projects
    completeprojects =Project.query.filter_by( iscomplete = True)
    not_completeprojects = Project.query.filter_by(iscomplete = False)


    iscomplete = completeprojects.count()
    notcomplete = not_completeprojects.count()
    
    
    for project in projects:
        completion_date = project.completion_date
        
        # destructing completion date
        completion_month = completion_date.month
        completion_year = completion_date.year
        completion_day = completion_date.day

        now = datetime.datetime.now()
        completion_object = datetime.datetime(completion_year,completion_month,completion_day)

        if completion_object > now:
            project.iscomplete = False

        else:
            project.iscomplete = True


        project.save_project()
        

         


    return render_template('home.html',projects = projects,iscomplete  = iscomplete,notcomplete = notcomplete)

@main.route('/project/details/<int:id>')
def project_details(id):
    project = Project.query.filter_by(id = id).first()
    current_user_id = current_user.id

    if project is None:
        flash("project cannot be found")

    return render_template('details.html',id = id,project = project)