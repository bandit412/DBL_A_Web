from datetime import datetime, timezone

from doublea import db, login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

class Role(db.Model):
    __tablename__ = 'db_user_role'
    roleid = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(10), nullable = False)
    role_users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return f"Role('{self.rolename}')"

class User(db.Model, UserMixin):
    __tablename__ = 'db_user'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    useremail = db.Column(db.String(120), unique=True, nullable=False)
    userpassword = db.Column(db.String(60), nullable=False)
    roleid = db.Column(db.Integer, db.ForeignKey('db_user_role.roleid'), nullable=False)

    def get_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.userid})

    @staticmethod
    def verify_reset_token(token, expiration=60):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=expiration)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.useremail}')"
    
    def get_id(self):
           return (self.userid)
    
class Store(db.Model):
    __tablename__ = 'store'
    storeid = db.Column(db.Integer, primary_key=True)
    storename = db.Column(db.String(30), nullable = False)
    storelocation = db.Column(db.String(30), nullable = False)
    transactions = db.relationship('Transaction', backref='purchase', lazy=True)

    def __repr__(self):
        return f"Store('{self.storename}','{self.storelocation}')"

class Market(db.Model):
    __tablename__ = 'markets'
    marketsid = db.Column(db.Integer, primary_key=True)
    market = db.Column(db.String(60), nullable = False)
    sales = db.relationship('MarketSales', backref='customer_sale', lazy=True)

    def __repr__(self):
        return f"Market('{self.market}')"

class PaymentMethod(db.Model):
    __tablename__ = 'paymentmethod'
    paymentmethodid = db.Column(db.Integer, primary_key=True)
    methodname = db.Column(db.String(20), nullable = False)
    store_payments = db.relationship('Transaction', backref='store_purchase', lazy=True)
    market_payments = db.relationship('MarketSales', backref='market_purchase', lazy=True)

    def __repr__(self):
        return f"PaymentMethod('{self.methodname}')"
    
class Transaction(db.Model):
    __tablename__ = 'transactions'
    transactionsid = db.Column(db.Integer, primary_key=True)
    transactiondate = db.Column(db.Date, nullable=False)
    storeid = db.Column(db.Integer, db.ForeignKey('store.storeid'), nullable=False)
    items = db.Column(db.String(250), nullable=False)
    amount = db.Column(db.Numeric(8,2), nullable=False)
    gst = db.Column(db.Numeric(5,2), nullable=False)
    paymentid = db.Column(db.Integer, db.ForeignKey('paymentmethod.paymentmethodid'), nullable=False)

    def __repr__(self):
        return f"Transaction('{self.transactiondate}, {self.items}, {self.amount}, {self.gst}')"
    
class MarketSales(db.Model):
    __tablename__ = 'marketsales'
    marketsalesid = db.Column(db.Integer, primary_key=True)
    marketid = db.Column(db.Integer, db.ForeignKey('markets.marketsid'), nullable=False)
    marketdate = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(6,2), nullable=False)
    description = db.Column(db.String(60), nullable=False)
    methodid = db.Column(db.Integer, db.ForeignKey('paymentmethod.paymentmethodid'), nullable=False)

    def __repr__(self):
        return f"MarketSales('{self.market_date}, {self.desctiption}, {self.amount}')"

class Event(db.Model):
    __tablename__='calevent'
    eventid = db.Column(db.Integer, primary_key=True)
    eventtitle = db.Column(db.String(100), nullable=False)
    event_location = db.Column(db.String(30), nullable=False)
    eventdate = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __rep__(self):
        return f"Event('{self.eventtitle}, {self.event_location}, {self.eventdate}, {self.start_time}')"