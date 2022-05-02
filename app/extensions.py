from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_mail import Mail
from flask_jwt_extended import JWTManager

mail = Mail()


def init_app(app):
    JWTManager(app)
    CORS(app)
    mail.init_app(app)
    