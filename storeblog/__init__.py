import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

application = Flask(__name__)
application.config['SECRET_KEY'] = '5d0082344355e41fe789e7bc11e49dc3'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = 'sekinatanimashaunsal@gmail.com' #os.environ.get('EMAIL_USER')
application.config['MAIL_PASSWORD'] = 'afudrhsorbbnyfik'#os.environ.get('EMAIL_PASS')
mail = Mail(application)

from storeblog import routes