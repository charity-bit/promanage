from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, EmailField
from wtforms.validators import DataRequired, ValidationError
from ..models import User

class ProjectForm(FlaskForm):

    name = StringField('Project name', validators=[DataRequired()])
    uploader = StringField('Name to appear on project', validators=[DataRequired()])
    details = TextAreaField('Project description', validators=[DataRequired()])
    completion_date = DateField('Date expected to complete', validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField('Add Project')

class SubtaskForm(FlaskForm):

    name = StringField('Subtask name', validators=[DataRequired()])
    details = TextAreaField('Subtask description', validators=[DataRequired()])
    completion_date = DateField('Date expected to complete', validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField('Add Subtask')

class MemberForm(FlaskForm):

    email = EmailField('Enter Email of member', validators=[DataRequired()])
    submit = SubmitField('Add member')

class EditForm(FlaskForm):

    name = StringField('Project name', validators=[DataRequired()])
    uploader = StringField('Name to appear on project', validators=[DataRequired()])
    details = TextAreaField('Project description', validators=[DataRequired()])
    completion_date = DateField('Date expected to complete', validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField('Add Project')

class DeleteForm(FlaskForm):

    submit = SubmitField('Delete Project')
