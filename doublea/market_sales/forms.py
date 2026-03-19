from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField

class SalesForm(FlaskForm):
    market = SelectField('Market', validate_choice=False)
    submit = SubmitField('Get Sales')

class UpdateMarketSale(FlaskForm):
    description = StringField('Description')
    sale_amount = StringField('Amoint')
    submit = SubmitField("Update")