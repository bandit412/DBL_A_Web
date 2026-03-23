from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from doublea.models import Store, Transaction

from doublea import db
from doublea.stores.forms import StoreForm

stores = Blueprint('stores', __name__)

@stores.route("/store_management")
def store_management():
    page = request.args.get('page', 1, type=int)
    stores = Store.query.order_by(Store.storename, Store.storelocation).paginate(page=page, per_page=10)
    return render_template('store_management.html', title='Stores', stores=stores)

@stores.route('/store/new', methods=['GET','POST'])
@login_required
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        store = Store(storename=form.name.data, storelocation=form.location.data)
        db.session.add(store)
        db.session.commit()
        flash('Your Store has been created!', 'success')
        return redirect(url_for('stores.store_management'))
    return render_template('new_store.html',title='New Store',form=form, legend='New Store')

@stores.route("/store/<int:store_id>")
@login_required
def store(store_id):
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        one_store= Store.query.filter_by(storeid=store_id).first_or_404()
        store_transactions = Transaction.query.filter_by(storeid=store_id)\
            .order_by(Transaction.transactiondate.desc()).paginate(page=page, per_page=10)
        return render_template('store.html',
                           title=one_store.storename,
                           one_store=one_store,
                           store_transactions=store_transactions)
    else:
        abort(403)