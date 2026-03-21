from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from doublea.markets.forms import MarketForm
from doublea.models import Market, MarketSales

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

@markets.route("/market/<int:market_id>")
@login_required
def market(market_id):
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        one_market= Market.query.filter_by(marketsid=market_id).first_or_404()
        market_sales = MarketSales.query.filter_by(marketid=market_id)\
          .order_by(MarketSales.marketdate.desc()).paginate(page=page, per_page=10)
        return render_template('market.html',
                           title=one_market.market,
                           one_market=one_market,
                           market_sales=market_sales)
    else:
        abort(401)