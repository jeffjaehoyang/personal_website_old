from flask import render_template, url_for, flash, redirect, request
from flaskblog import bcrypt, db, mail, flatpages
from flaskblog.forms import RegistrationForm, LoginForm, ContactForm, UpdateAccountForm
from flaskblog.models import User, BlogPost
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message, Mail
from flaskblog.config import Config
from flask import current_app

@current_app.route('/')
def home():
    posts = [p for p in flatpages if 'published' in p.meta]
    posts.sort(key=lambda item:item['published'], reverse=True)
    return render_template('home.html', posts=posts[:5])

@current_app.route('/blog')
def blog():
    posts = [p for p in flatpages if 'published' in p.meta]
    posts.sort(key=lambda item:item['published'], reverse=True)
    return render_template('blog.html', posts=posts)

@current_app.route('/about')
def about():
    return render_template('about.html')

@current_app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=Config.MAIL_USERNAME, recipients=[Config.MAIL_RECIPIENT])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
         
            flash('Email successfully sent!', 'success')
            return redirect(url_for('home'))
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@current_app.route('/projects')
def projects():
    return render_template('projects.html')

@current_app.route('/resume')
def resume():
    path = '{}/{}'.format(Config.RESUME_DIR, 'resume')
    resume = flatpages.get_or_404(path)
    return render_template('resume.html', resume=resume)

@current_app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            flash(f'Successfully logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))          
        else:
            flash(f'Sorry, invalid login credentials', 'danger')

    return render_template('login.html', form=form)

@current_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@current_app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email 

    profile_img = url_for('static', filename="profile_pics/" + current_user.profile_img)
    return render_template('account.html', profile_img=profile_img, form=form)

@current_app.route('/post/<name>')
def post(name):
    path = '{}/{}'.format(Config.POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('blog_post.html', post=post)

@current_app.route('/category/<name>')
def category(name):
    posts = [p for p in flatpages if name in p.meta['category']]
    posts.sort(key=lambda item:item['published'], reverse=True)
    return render_template('blog.html', posts=posts, name=name)

