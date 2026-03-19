#import os
#import secrets
from flask import url_for #, current_app
#from flask_login import current_user
from flask_mail import Message
#rom PIL import Image
from doublea import mail

def send_reset_password(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.useremail])
    msg.body = f'''To reset your password vist the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)