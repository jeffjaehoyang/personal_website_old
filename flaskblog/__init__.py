from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Message, Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flaskblog.config import Config

mail = Mail()
flatpages = FlatPages()
freezer = Freezer()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	with app.app_context():
		flatpages.init_app(app)
		freezer.init_app(app)
		db.init_app(app)
		mail.init_app(app)
		bcrypt.init_app(app)
		login_manager.init_app(app)
		from flaskblog import routes

	return app
	