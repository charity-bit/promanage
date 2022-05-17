## PROMANAGE
### CONTRIBUTORS

- James Njoroge
- Orina Nyanchera
- Nina Odoyo
- Mungai Mbugua



### ABOUT

#### An app where a user can sign up and manage project and tasks allowing him/her to track project progress

### USER STORIES

A user can:
- login and sign up
- add project details using a form.
- view their projects and their details.
- delete a project when they wish.
- see the projects status.
- Enter a list of team members.
- edit an existing project.


### TECHNOLOGIES USED

- HTML
- CSS - BOOTSTRAP5
- PYTHON
- POSTGRESQL

### REQUIREMENTS

- Local machine
- A code editor e.g. VSCODE
- Installed postgresql

### INSTALLATION

```
git clone https://github.com/devjamesnjoroge/promanage/
cd best-impressions
```

**Launch virtual environment**
```
python -m venv virtual

source virtual/bin/activate
```

**Install all the app dependencies**
```
pip install -r requirements.txt 
```

**Database Setup**
edit the sqlalchemy url in config.py
replace with your database in the format:
```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

```
change the production string in manage.py to development

**Environmental variables**

Create a start.sh file in root folder 
Edit file
```
export SECRET_KEY=<YOURS>
export MAIL_USERNAME=<your email>
export MAIL_PASSWORD=<mail password>
python3 manage.py server
```

### AUTHORS INFO

* [Linkedin](https://www.linkedin.com/in/devjamesnjoroge)
* [Email](njorogehjames20@gmail.com)

### LICENSE

[MIT LICENSE](LICENSE)

[Go back to the top](#)

