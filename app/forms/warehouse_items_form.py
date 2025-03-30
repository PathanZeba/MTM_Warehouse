from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired

class WarehouseItemsForm(FlaskForm):
    item_name = StringField("Item Name", validators=[DataRequired(message="Please enter Item Name")])
    item_unit_quant = FloatField("Quantity", validators=[DataRequired(message="Please enter Quantity")])
    item_capacity_quant = FloatField("Capacity Required", validators=[DataRequired(message="Please enter Space required to store")])
    item_price_per_unit = FloatField("Price per Unit", validators=[DataRequired(message="Please enter item cost")])
