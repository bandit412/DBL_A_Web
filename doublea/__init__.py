from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from doublea.config import Config
from flask_mail import Mail

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from doublea.main.routes import main
    from doublea.users.routes import users
    from doublea.markets.routes import markets 
    from doublea.market_sales.routes import marketsales
    from doublea.stores.routes import stores
    from doublea.transactions.routes import transactions
    from doublea.paymentmethods.routes import paymentmethods
    from doublea.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(markets)
    app.register_blueprint(marketsales)
    app.register_blueprint(stores)
    app.register_blueprint(transactions)
    app.register_blueprint(paymentmethods)
    app.register_blueprint(errors)

    return app