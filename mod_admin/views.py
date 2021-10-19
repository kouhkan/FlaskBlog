from flask import session, request, render_template, abort, flash
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin
from .utils import admin_only_view


@admin.route('/')
@admin_only_view
def index():
    return 'admin page'


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('Form is not valid', category='error')
            return render_template('admin/login.html', form=form)
            
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        
        if not user:
            flash('User does not exist', category='error')
            return render_template('admin/login.html', form=form)


        if not user.check_password(form.password.data):
            flash('Password is not correct', category='error')
            return render_template('admin/login.html', form=form)
        
        if not user.is_admin():
            flash('User is not admin', category='error')
            return render_template('admin/login.html', form=form)


        session['email'] = user.email
        session['user_id'] = user.id
        session['role'] = user.role
        return f'Welcome...{user.username}'
    if session.get('role') is not None:
        return "You're logged in"
    return render_template('admin/login.html', form=form)
