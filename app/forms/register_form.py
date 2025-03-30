from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(message="Please enter a username."), Length(max=32)], 
        render_kw={"placeholder": "Enter your username"}
    )

    password = PasswordField('Password', 
        validators=[DataRequired(message="Please enter a password.")], 
        render_kw={"placeholder": "Enter your password"}
    )

    confirm_password = PasswordField('Confirm Password', 
        validators=[
            DataRequired(message="Please confirm your password."), 
            EqualTo('password', message="Passwords must match.")
        ], 
        render_kw={"placeholder": "Confirm your password"}
    )

    selected_role = SelectField('Select Role', 
        choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')], 
        validators=[DataRequired()]
    )

    manager_id = IntegerField('Manager ID', validators=[DataRequired()])

    submit = SubmitField('Register')
