
from flask import render_template, url_for, redirect, flash
from blog import app
from blog.form import RegistrationForm,LoginForm
from blog.models import User

@app.route("/")
def index():
    title = "omer portfolio"
    return render_template("index.html",title=title)

@app.route('/about')
def about():
    title="Shahana Page"
    return render_template("about.html",title=title)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('index'))
    return render_template("register.html",title="Register",form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'omer@blog.com' and form.password.data == 'Omer123@':
            flash('You have been Logged in','success')
            return redirect(url_for('index'))
        else:
            flash('Login failed','danger')
    return render_template("login.html",title="Login",form=form)

