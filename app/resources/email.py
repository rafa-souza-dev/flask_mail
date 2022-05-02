from flask_restful import Resource
from decouple import config

from app.services.mail import send_mail


class SendEmail(Resource):
    def post(self):
        send_mail(
            "Teste", 
            config("MAIL_SENDER"), 
            "teste", 
        )
        
        return {"success": "ok"}, 200
