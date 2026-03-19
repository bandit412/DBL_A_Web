from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import login_required

from doublea import db
from doublea.models import Market,MarketSales
from doublea.market_sales.forms import SalesForm, UpdateMarketSale

marketsales = Blueprint('marketsales', __name__)

@marketsales.route("/market_sales")
def market_sales():
    markets = Market.query.order_by(Market.market)
    form = SalesForm()
    return render_template('market_sales.html', markets=markets,form=form)

def get_selected_value():
    selected_value = request.form.get('market_select')   
    return int(selected_value) 


@marketsales.route('/market_sales/get_sales', methods=['GET','POST'])
def get_sales():
    #page = request.args.get('page', 1, type=int)
    selected_value = int(get_selected_value())
    selected_market = Market.query.get_or_404(selected_value)
    sales = MarketSales.query.filter_by(marketid=selected_value).order_by(MarketSales.marketdate.desc(), MarketSales.marketsalesid.desc()) #.paginate(page=page, per_page=10)
    return render_template('market_sales_by_market.html', sales=sales,selected_market=selected_market)

@marketsales.route("/market_sales_by_market/<int:marketsales_id>/update", methods=['GET','POST'])
@login_required
def update_marketsale(marketsales_id):
    market_sale = MarketSales.query.get_or_404(marketsales_id)
    if marketsales_id != market_sale.marketsalesid:
        abort(403)
    form = UpdateMarketSale()
    if form.validate_on_submit():
        market_sale.description = form.description.data
        market_sale.amount = form.sale_amount.data
        db.session.commit()
        flash('Your sale has bee updated!', 'success')
        sales = MarketSales.query.filter_by(marketid=market_sale.marketid).order_by(MarketSales.marketdate.desc(), MarketSales.marketsalesid.desc())
        return redirect(url_for('marketsales.market_sales', sales=sales, marketid=market_sale.marketid))
    elif request.method == 'GET':
        form.description.data = market_sale.description
        form.sale_amount.data = market_sale.amount
    return render_template('create_sale.html', form=form, legend="Update Sale")