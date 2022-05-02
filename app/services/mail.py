from flask import render_template
from app.extensions import mail

from flask_mail import Message
from decouple import config


def send_mail(subject, to, template, **kwargs):
    msg = Message(subject=subject, recipients=[to], sender=config("MAIL_SENDER"))
    
    msg.body = render_template(f"mails/{template}.txt", **kwargs)
    msg.html = render_template(f"mails/{template}.html", **kwargs)
    
    mail.send(msg)
    