from datetime import date

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from doublea import db
from doublea.events.forms import NewEventForm
from doublea.models import Event

events = Blueprint('events', __name__)

@events.route('/events_management')
def events_management():
    # Example: filtering for a specific month
    events = Event.query.filter(Event.eventdate >= date.today())
    return render_template('events_management.html', title='Events', events=events)

@events.route('/events/new', methods=['GET','POST'])
@login_required
def new_event():
    form = NewEventForm()
    #events = Event.query.all()
    if form.validate_on_submit():
        event = Event(
            eventtitle = form.eventtitle.data,
            event_location = form.location.data,
            eventdate = form.eventdate.data,
            start_time = form.start.data,
            end_time = form.end.data,
            description = form.description.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Your event has been created!', 'success')
        return redirect(url_for('events.events_management'))
    return render_template('create_event.html', tittle='New Event', form=form, legend='New Event')