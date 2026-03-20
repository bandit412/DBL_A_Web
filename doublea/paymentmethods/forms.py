from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PaymentForm(FlaskForm):
    methodname = StringField('Method Name', validators=[DataRequired()])
    submit = SubmitField('Payment')