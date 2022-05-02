from flask_restful import Api

from app.resources import email


def init_app(app):
    api = Api(app, prefix="/api")
    api.add_resource(email.SendEmail, "/mail")
