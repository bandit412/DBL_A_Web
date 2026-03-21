from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class PurchaseForm(FlaskForm):
    market = SelectField('Stores', validate_choice=False)
    submit = SubmitField('Get Purchases')

class UpdateTransactionForm(FlaskForm):
    items = StringField('Description')
    purchase_amount = StringField('Amount')
    purchase_gst = StringField('GST')
    submit = SubmitField("Update")