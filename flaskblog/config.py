import os 

class Config:
	SECRET_KEY = os.environ.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
	MAIL_SERVER = "smtp.gmail.com"
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	DEBUG = True
	FLATPAGES_AUTO_RELOAD = DEBUG
	FLATPAGES_EXTENSION = '.md'
	FLATPAGES_ROOT = 'content'
	FLATPAGES_MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']
	FLATPAGES_EXTENSION_CONFIG = {
	    'codehilite': {
	        'linenums': 'True'
	    }
	}
	POST_DIR = 'posts'
	RESUME_DIR = 'resume' 