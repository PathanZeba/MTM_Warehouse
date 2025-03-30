from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Regexp

class WarehouseInfoForm(FlaskForm):
    w_name = StringField("Warehouse Name", validators=[
        DataRequired(message="Enter valid warehouse name"),
        Regexp(r"^([A-Za-z][A-Za-z0-9 -]{3,30})$", message="Invalid warehouse name format")
    ])
    w_location = StringField("Location", validators=[DataRequired(message="Enter valid location")])
    w_pincode = StringField("Pincode", validators=[
        DataRequired(message="Enter valid postal code"),
        Regexp(r"^(^[0-9]{5}(-[0-9]{4})?$)|(^[ABCEGHJKLMNPRSTVXY]{1}[0-9]{1}[A-Z]{1} *[0-9]{1}[A-Z]{1}[0-9]{1}$)$",
               message="Invalid postal code format. Refer this: 'N2M 5C7'")
    ])
    w_total_capacity = FloatField("Total Capacity (sq. ft.)", validators=[DataRequired(message="Enter valid total capacity")])
    w_space_available = FloatField("Available Space (sq. ft.)")
    w_percent_full = FloatField("Percentage Full")
