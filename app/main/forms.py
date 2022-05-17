from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):

    name = StringField('Project name', validators=[DataRequired()])
    uploader = StringField('Name to appear on project', validators=[DataRequired()])
    details = TextAreaField('Project description', validators=[DataRequired()])
    date = DateField('Date expected to complete', validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField('Add Project')
