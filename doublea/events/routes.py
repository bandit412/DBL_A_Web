from datetime import date

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from doublea import db
from doublea.events.forms import NewEventForm
from doublea.models import Event

events = Blueprint('events', __name__)

@events.route('/events_management')
def events_management():
    # Example: filtering for a specific month
    events = Event.query.filter(Event.eventdate >= date.today()).order_by(Event.eventid)
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
    return render_template('create_event.html', title='New Event', form=form, legend='New Event')

@events.route("/events_management/<int:event_id>/update", methods=['GET','POST'])
@login_required
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = NewEventForm()
    if form.validate_on_submit():
        event.eventtitle = form.eventtitle.data
        event.event_location = form.location.data
        event.eventdate = form.eventdate.data
        event.start_time = form.start.data
        event.end_time = form.end.data
        event.description = form.description.data
        db.session.commit()
        flash('Your event has bee updated!', 'success')
        events = Event.query.all()
        return redirect(url_for('events.events_management', events=events))
    elif request.method == 'GET':
        form.eventtitle.data = event.eventtitle
        form.location.data = event.event_location
        form.eventdate.data = event.eventdate
        form.start.data = event.start_time
        form.end.data = event.end_time
        form.description.data = event.description
        form.submit.label.text = "Update Event"
    return render_template('create_event.html', title='Update Event', form=form, legend="Update Event")