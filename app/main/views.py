from unicodedata import category
from flask import render_template, url_for, flash,redirect,request
from app import app,db,bcrypt

from app.main.forms import RegistrationForm, LoginForm,PitchForm
from app.models import User,Pitch
from flask_login import login_required,logout_user,current_user,login_user

pitches= [
    {
        'author':'Valarie Rono',
        'category':'pickup-lines',
        'content':'I must be in a museum, because you truly are a work of art.',
        'date_posted':'September 3rd, 2020'

    },
    {
        'author':'Beatrice Rono',
        'category':'Interview',
        'content':'I’m Beatrice Rono, a lawyer with the government, based out of D.C. I grew up in Ohio, though, and I’m looking to relocate closer to my roots, and join a family-friendly firm. I specialize in labor law and worked for ABC firm before joining the government.',
        'date_posted':'September 24th, 2019'

    },
    {
        'author':'Sharon Rono',
        'category':'Product',
        'content':'For 130 years, Merck (known as MSD outside of the U.S. and Canada) has been inventing for life, bringing forward medicines and vaccines for many of the world’s most challenging diseases in pursuit of our mission to save and improve lives.',
        'date_posted':'July 26th, 2021'
    },
        {
        'author':'Victoria Rono',
        'category':'Promotion',
        'content':'m a sales rep at Better Than the Rest Cable. We help hotels across the U.S. pair with the perfect cable provider and plan for their region and needs. With regional experts assigned to each account, we help hotels identify the most cost-effective and guest-delighting cable plan for them.',
        'date_posted':'August 27th, 2018'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' ,pitches=pitches)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form) 

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/pitch/new", methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')
