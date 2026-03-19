from flask import Blueprint, render_template

from doublea import db

transactions = Blueprint('transactions', __name__)

@transactions.route("/store_purchases")
def store_purchases():
    return render_template('store_purchases.html')