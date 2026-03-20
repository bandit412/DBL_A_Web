from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from doublea.models import Store

from doublea import db
from doublea.stores.forms import StoreForm

stores = Blueprint('stores', __name__)

@stores.route("/store_management")
def store_management():
    page = request.args.get('page', 1, type=int)
    stores = Store.query.order_by(Store.storename, Store.storelocation).paginate(page=page, per_page=10)
    return render_template('store_management.html', stores=stores)

@stores.route('/store/new', methods=['GET','POST'])
@login_required
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        store = Store(name=form.name.data, location=form.location.data)
        db.session.add(store)
        db.session.commit()
        flash('Your Store has been created!', 'success')
        return redirect(url_for('stores.store_management'))
    return render_template('new_store.html',tittle='New Store',form=form, legend='New Store')