from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from doublea import db
from doublea.models import PaymentMethod, Store, Transaction
from doublea.transactions.forms import NewTransactionForm, PurchaseForm, UpdateTransactionForm

transactions = Blueprint('transactions', __name__)

@transactions.route("/store_purchases")
@login_required
def store_purchases():
    if current_user.is_authenticated:
        stores= Store.query.order_by(Store.storename, Store.storelocation)
        form = PurchaseForm()
        return render_template('store_purchases.html', title='Store Purchases', stores=stores,form=form)
    else:
        abort(401)

def get_selected_value():
    selected_value = request.form.get('store_select')   
    return int(selected_value) 

@transactions.route('/transactions/get_purchases', methods=['GET','POST'])
def get_purchases():
    #page = request.args.get('page', 1, type=int)
    selected_value = int(get_selected_value())
    selected_store = Store.query.get_or_404(selected_value)
    purchases = Transaction.query.filter_by(storeid=selected_value).order_by(Transaction.transactiondate.desc(), Transaction.transactionsid.desc()) #.paginate(page=page, per_page=10)
    return render_template('transactions_by_store.html', title='Store Transactions', purchases=purchases,selected_store=selected_store)

@transactions.route("/transactions_by_market/<int:transaction_id>/update", methods=['GET','POST'])
@login_required
def update_transaction(transaction_id):
    purchase = Transaction.query.get_or_404(transaction_id)
    if transaction_id != purchase.transactionsid:
        abort(403)
    form = UpdateTransactionForm()
    if form.validate_on_submit():
        purchase.items = form.items.data
        purchase.amount = form.purchase_amount.data
        purchase.gst = form.purchase_gst.data
        db.session.commit()
        flash('Your purchase has bee updated!', 'success')
        purchases = Transaction.query.filter_by(storeid=purchase.storeid).order_by(Transaction.transactiondate.desc(), Transaction.transactionsid.desc())
        return redirect(url_for('transactions.store_purchases', purchases=purchases, storeid=purchase.storeid))
    elif request.method == 'GET':
        form.items.data = purchase.items
        form.purchase_amount.data = purchase.amount
        form.purchase_gst.data = purchase.gst
    return render_template('update_transaction.html', title='Update Transaction', form=form, legend="Update Transaction")

@transactions.route('/market_sales/create_purchase', methods=['GET','POST'])
@login_required
def create_purchase():
    form = NewTransactionForm()
    stores = Store.query.order_by(Store.storename, Store.storelocation)
    form.store_group_id.choices = [(st.storeid, f"{st.storename} - {st.storelocation}") for st in stores]
    payments = PaymentMethod.query.all()
    form.payment_group_id.choices =[(pmt.paymentmethodid, pmt.methodname) for pmt in payments]
    if form.validate_on_submit():
        purchase = Transaction(storeid=form.store_group_id.data, 
                           transactionsdate=form.purchase_date.data,
                           items=form.purchase_items.data,
                           amount=form.purchase_amount.data,
                           gst = form.purchase_gst.data,
                           methodid=form.payment_group_id.data)
        db.session.add(purchase)
        db.session.commit()
        flash('Your purchase has been created!', 'success')
        return redirect(url_for('transactions.store_management'))
    return render_template('create_purchase.html',title='New Purchase',form=form, legend='New Purchase')