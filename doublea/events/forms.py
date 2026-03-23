from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, TimeField
from wtforms.validators import DataRequired

class NewEventForm(FlaskForm):
    eventtitle = StringField('Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    eventdate = DateField('Date', validators=[DataRequired()])
    start = TimeField('Start Time',validators=[DataRequired()])
    end = TimeField('End Time', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('New Event')