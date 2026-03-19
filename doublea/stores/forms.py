from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class StoreForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location= StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Store')