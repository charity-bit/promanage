import datetime
from operator import sub
from flask import render_template,flash,redirect,url_for
from . import main
from . forms import ProjectForm, SubtaskForm, MemberForm
from flask_login import current_user

from ..models import Project,User,TeamMembers,SubTask

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
            flash("Project Name Cannot be Empty",category="error")

        elif not project_details:
            flash("Your project must have a description",category="error")

        elif not project_alias:
            flash("Your project must have an alias",category="error")
        
        elif not completion_date:
            flash("Please indicate the expected completion date",category="error")

        elif completion_object < now:
            flash("oops,you cannot complete the project yesterday",category="error")

        else:
            new_project = Project(name = project_name,alias = project_alias,description = project_details,owner_id = current_user.id,completion_date = completion_date )
            new_project.save_project()
            
            return redirect(url_for('main.index'))

    return render_template('new_project.html', form = form)

@main.route('/home')
def home():

    projects = Project.query.all()

    # query state projects
    # Todo: remember to query projects from Members
    #and loop to compare both user_id and project_id
    #to avoid double enteries in teammembers
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
        flash("project cannot be found",category="error")

    for subtask in project.subtasks:
        completion_date = subtask.completion_date
        
        # destructing completion date
        completion_month = completion_date.month
        completion_year = completion_date.year
        completion_day = completion_date.day

        now = datetime.datetime.now()
        completion_object = datetime.datetime(completion_year,completion_month,completion_day)

        if completion_object > now:
            subtask.iscomplete = False

        else:
            subtask.iscomplete = True
            
            subtask.save_project()


        

    return render_template('details.html',id = id,project = project)

@main.route('/project/<int:id>/add-subtask',methods=['POST','GET'])
def add_subtask(id):

    subtasks_form = SubtaskForm()
    if subtasks_form.validate_on_submit():
        name = subtasks_form.details.data
        description = subtasks_form.details.data
        completion_date = subtasks_form.completion_date.data



        completion_month = completion_date.month
        completion_year = completion_date.year
        completion_day = completion_date.day

        
        now = datetime.datetime.now()
        completion_object = datetime.datetime(completion_year,completion_month,completion_day)


        project = Project.query.filter_by(id = id).first()

        if not project:
            flash("project does not exist",category="error")

        elif not description:
            flash("description cannot be empty",category="error")
        
        elif not name:
            flash("please enter the name of the subtask",category = "error")
        
        elif not completion_date:
            flash("please enter the completion date",category="error")
        
        elif completion_object < now:
            flash("oops,you cannot complete the project yesterday",category="error")

        else:
            new_subtask = SubTask( name = name,description = description,completion_date = completion_date,project_id = id)
            new_subtask.save_subtask()

            return redirect(url_for('main.project_details',id = id))

    return render_template('subtasks.html', subtasks_form = subtasks_form,id = id)

@main.route('/project/<int:id>/add-member',methods=['POST','GET'])
def member(id):

    member_form = MemberForm()
    if  member_form.validate_on_submit():
        email = member_form.email.data

        user = User.query.filter_by(email = email).first()
        

        project = Project.query.filter_by(id = id).first()

        if not project:
            flash("project does not exist",category="error")

        elif not user:
            flash("That user does not exist",category="error")

        elif project.owner_id != current_user.id:
            flash('You are not allowed to add a member,Please consult the project owner',category = "error")

        else:
            member = TeamMembers(user_id = user.id,project_id = id)
            member.save_member()

            return redirect(url_for('main.project_details',id = id))
        



    return render_template('member.html', member_form = member_form,id = id)

