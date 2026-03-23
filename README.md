# DBL_A_Web
Python/Flask Web Application with PostgeSQL backend database.

## Development
This is a development project to recrete an ASP.NET web application in Python/Flask with a PostgreSQL database backend.

### Package List
```
Package           Version
----------------- -------
bcrypt            5.0.0
blinker           1.9.0
click             8.3.1
distlib           0.4.0
dnspython         2.8.0
email-validator   2.3.0
filelock          3.25.2
Flask             3.1.3
Flask-Bcrypt      1.0.1
Flask-Login       0.6.3
Flask-Mail        0.10.0
Flask-SQLAlchemy  3.1.1
Flask-WTF         1.2.2
idna              3.11
itsdangerous      2.2.0
Jinja2            3.1.6
MarkupSafe        3.0.3
pip               26.0.1
platformdirs      4.9.4
psycopg2-binary   2.9.11
python-discovery  1.2.0
SQLAlchemy        2.0.48
typing_extensions 4.15.0
virtualenv        21.2.0
Werkzeug          3.1.6
WTForms           3.2.1
```

### Directory Tree
```
DBL_A_Web/
├── DBL_A_Transactions.sql
├── Dbl_A_Transactions_ERD
├── doublea/
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── __pycache__/
│   │   ├── __init__.cpython-312.pyc
│   │   ├── __init__.cpython-314.pyc
│   │   ├── config.cpython-312.pyc
│   │   ├── config.cpython-314.pyc
│   │   ├── models.cpython-312.pyc
│   │   └── models.cpython-314.pyc
│   ├── config.py
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── handlers.cpython-312.pyc
│   │   └── handlers.py
│   ├── events/
│   │   ├── __pycache__/
│   │   │   ├── forms.cpython-312.pyc
│   │   │   └── routes.cpython-312.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── routes.cpython-312.pyc
│   │   │   └── routes.cpython-314.pyc
│   │   └── routes.py
│   ├── market_sales/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── forms.cpython-314.pyc
│   │   │   ├── routes.cpython-312.pyc
│   │   │   └── routes.cpython-314.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── markets/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── routes.cpython-312.pyc
│   │   │   └── routes.cpython-314.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── models.py
│   ├── paymentmethods/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── routes.cpython-312.pyc
│   │   │   └── routes.cpython-314.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── main.css
│   │   ├── icons/
│   │   │   ├── apple-touch-icon.png
│   │   │   ├── favicon-96x96.png
│   │   │   ├── favicon.ico
│   │   │   ├── favicon.svg
│   │   │   ├── site.webmanifest
│   │   │   ├── web-app-manifest-192x192.png
│   │   │   └── web-app-manifest-512x512.png
│   │   └── img/
│   │       ├── 401_Sad_Face.png
│   │       ├── 403_Sad_Face.png
│   │       ├── 404_Sad_Face.png
│   │       ├── 500_Sad_Face.png
│   │       └── Dbl_A_Transactions_ERD.png
│   ├── stores/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── routes.cpython-312.pyc
│   │   │   └── routes.cpython-314.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── templates/
│   │   ├── _layout.html
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_event.html
│   │   ├── create_purchase.html
│   │   ├── create_sale.html
│   │   ├── errors/
│   │   │   ├── 401.html
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── events_management.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── market.html
│   │   ├── market_management.html
│   │   ├── market_sales.html
│   │   ├── market_sales_by_market.html
│   │   ├── new_market.html
│   │   ├── new_payment.html
│   │   ├── new_store.html
│   │   ├── payments.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   ├── store.html
│   │   ├── store_management.html
│   │   ├── store_purchases.html
│   │   ├── transactions_by_store.html
│   │   ├── update_sale.html
│   │   └── update_transaction.html
│   ├── transactions/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── routes.cpython-312.pyc
│   │   │   └── routes.cpython-314.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   └── users/
│       ├── __init__.py
│       ├── __pycache__/
│       │   ├── __init__.cpython-312.pyc
│       │   ├── __init__.cpython-314.pyc
│       │   ├── forms.cpython-312.pyc
│       │   ├── forms.cpython-314.pyc
│       │   ├── routes.cpython-312.pyc
│       │   ├── routes.cpython-314.pyc
│       │   ├── utils.cpython-312.pyc
│       │   └── utils.cpython-314.pyc
│       ├── forms.py
│       ├── routes.py
│       └── utils.py
├── README.md
└── run.py
```

## Depoloyment
Once the development is complete the task is to:
* backup the database to be installed on a local server
* copy web code to local server, including installing required packages
* setup the local server with a WSGI server
* TEST TEST TEST

## Maintenance
After deployment the code will likley need to be refined and updated:
* add new features
