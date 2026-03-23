import datetime

from flask import Blueprint, render_template, request
from doublea import db
from doublea.models import Market, Store

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    markets = Market.query.order_by(Market.market)
    stores = Store.query.order_by(Store.storename, Store.storelocation).paginate(page=page, per_page=10)
    return render_template('home.html',markets=markets, stores=stores)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

