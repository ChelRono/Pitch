from flask import render_template, url_for, flash,redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User,Pitch
from flask_login import login_required,logout_user

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

@app.route("/login", methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash(f'You have been logged in {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html',title='Login',form=form) 

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
