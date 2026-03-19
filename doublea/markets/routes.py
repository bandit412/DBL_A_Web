from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from doublea.markets.forms import MarketForm
from doublea.models import Market

from doublea import db

markets = Blueprint('markets', __name__)

@markets.route("/market_management")
def market_management():
    page = request.args.get('page', 1, type=int)
    markets = Market.query.order_by(Market.market).paginate(page=page, per_page=10)
    return render_template('market_management.html', markets=markets)

@markets.route('/market/new', methods=['GET','POST'])
@login_required
def new_market():
    form = MarketForm()
    if form.validate_on_submit():
        market_new = Market(name=form.name.data)
        db.session.add(market_new)
        db.session.commit()
        flash('Your Market has been created!', 'success')
        return redirect(url_for('markets.market_management'))
    return render_template('new_market.html',tittle='New Market',form=form, legend='New Market')