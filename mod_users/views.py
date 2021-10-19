from flask import request, 
from . import users
from .forms import RegisterForm



@users.route('/')
def index():
    return 'users'
