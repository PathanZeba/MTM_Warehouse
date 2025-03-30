from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Regexp

class EmpDataForm(FlaskForm):
    name = StringField("Employee Name", validators=[DataRequired(message="Please enter Name")])
    
    email = StringField("Email", validators=[
        DataRequired(message="Please enter Email"),
        Email(message="Invalid Email")
    ])
    
    phone = StringField("Phone Number", validators=[
        DataRequired(message="Please enter Phone #"),
        Regexp(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", message="Invalid Phone #")
    ])
    
    address = StringField("Address", validators=[DataRequired(message="Please enter Address")])
    pincode = StringField("Pincode", validators=[DataRequired(message="Please enter Pincode")])
    
    warehouse_info_id = IntegerField("Warehouse ID")
