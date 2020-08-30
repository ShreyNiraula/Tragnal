from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# secret key for forms generated using secret library run in python shell
app.config['SECRET_KEY'] = 'a385017a22e6173599a522533327e94f'
# database setting
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

# actual data
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#The socketio.run() function encapsulates the start up of the web server
# and replaces the app.run() standard Flask development server start up

#this tells where to look for login when login_required action (eg for account page) is needed
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# this is done after db=SQLAlchemy so that no circular inversion
from tragnal2 import routes

