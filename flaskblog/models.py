from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin, current_user
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	profile_img = db.Column(db.String(20), nullable=True, default='portrait.jpg')
	password = db.Column(db.String(60), nullable=False)
	blog_posts = db.relationship('BlogPost', backref='author', lazy=True)
	
	def __repr__(self):
		return f"User('{ self.username }', '{ self.email }', '{ self.profile_img }')"

class BlogPost(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	created_at = db.Column(db.DateTime(100), nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text(20), nullable=False)
	category = db.Column(db.Text(50), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"BlogPost('{ self.title }', '{ self.created_at }')"
