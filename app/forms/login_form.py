from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(message="Please enter a username."), Length(max=32)], 
        render_kw={"placeholder": "Enter your username"}
    )

    password = PasswordField('Password', 
        validators=[DataRequired(message="Please enter a password."), Length(max=32)], 
        render_kw={"placeholder": "Enter your password"}
    )

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
