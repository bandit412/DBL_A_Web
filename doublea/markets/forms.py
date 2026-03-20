from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MarketForm(FlaskForm):
    name = StringField(' Market Name', validators=[DataRequired()])
    submit = SubmitField('Market')