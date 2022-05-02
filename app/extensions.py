from flask import Flask
from flask_restful import Api
from dynaconf import FlaskDynaconf
from flask_cors import CORS
from flask_mail import Mail
from flask_jwt_extended import JWTManager


def init_app(app):
    FlaskDynaconf(app)
    JWTManager(app)
    CORS(app)
    