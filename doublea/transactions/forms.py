from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class PurchaseForm(FlaskForm):
    market = SelectField('Stores', validate_choice=False)
    submit = SubmitField('Get Purchases')

class UpdateTransactionForm(FlaskForm):
    items = StringField('Description')
    purchase_amount = StringField('Amount')
    purchase_gst = StringField('GST')
    submit = SubmitField("Update")

class NewTransactionForm(FlaskForm):
    store_group_id = SelectField('Store')
    purchase_date = DateField('Purchase Date', validators=[DataRequired()])
    purchase_items = StringField('Description', validators=[DataRequired()])
    purchase_amount = StringField('Amount', validators=[DataRequired()])
    purchase_gst = StringField('GST', validators=[DataRequired()])
    payment_group_id = SelectField('PaymentMethod')
    submit = SubmitField("New Purchase")