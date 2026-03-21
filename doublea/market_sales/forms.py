from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class SalesForm(FlaskForm):
    market = SelectField('Market', validate_choice=False)
    submit = SubmitField('Get Sales')

class UpdateMarketSale(FlaskForm):
    description = StringField('Description')
    sale_amount = StringField('Amoint')
    submit = SubmitField("Update")

class MarketSalesForm(FlaskForm):
    market_group_id = SelectField('Market', coerc=int)
    market_date = DateField('Market Date', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    payment_group_id = SelectField('PaymentMethod', coerc=int)