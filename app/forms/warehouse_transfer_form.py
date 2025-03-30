from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class WarehouseTransferForm(FlaskForm):
    source_warehouse_id = SelectField("Source Warehouse", coerce=int, validators=[DataRequired()])
    destination_warehouse_id = SelectField("Destination Warehouse", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Transfer Items")
