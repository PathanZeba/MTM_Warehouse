from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, NumberRange

class ItemToTransferForm(FlaskForm):
    warehouse_item_id = IntegerField("Item ID", validators=[DataRequired()])
    quantity_to_transfer = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=1)])

class ItemTransferForm(FlaskForm):
    source_warehouse_id = SelectField("Source Warehouse", coerce=int, validators=[DataRequired()])
    destination_warehouse_id = SelectField("Destination Warehouse", coerce=int, validators=[DataRequired()])
    items_to_transfer = FieldList(FormField(ItemToTransferForm), min_entries=1)  # ✅ Multiple items ka support
    submit = SubmitField("Transfer Items")
