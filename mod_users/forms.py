from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    full_name = StringField()
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
