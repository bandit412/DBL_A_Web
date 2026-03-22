from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required
from doublea.models import PaymentMethod

from doublea import db
from doublea.paymentmethods.forms import PaymentForm

paymentmethods = Blueprint('paymentmethods', __name__)

@paymentmethods.route("/payment_management")
def payment_management():
    payments = PaymentMethod.query.all()
    return render_template('payments.html', payments=payments)

@paymentmethods.route('/payment/new', methods=['GET','POST'])
@login_required
def new_payment():
    form = PaymentForm()
    if form.validate_on_submit():
        payment_new = PaymentMethod(methodname=form.methodname.data)
        db.session.add(payment_new)
        db.session.commit()
        flash('Your PaymentMethod has been created!', 'success')
        return redirect(url_for('paymentmethods.payment_management'))
    return render_template('new_payment.html',tittle='New Payment Method',form=form, legend='New Payment Method')