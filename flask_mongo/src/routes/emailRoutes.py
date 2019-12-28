from flask_mail import Message
from mail import mail
from flask import Blueprint,render_template,request,redirect,url_for

mailOperation_templates = Blueprint('mailOperation_templates', __name__)

@mailOperation_templates.route("/send", methods=['POST'])
def send_mail():
    try:
        msg = Message("send my msg",
            sender="himmsharma.99@gmail.com",
            recipients="himmsharma.99@gmail.com"
        )
        msg.body= "hi i am here in you inbox"
        mail.send(msg)
        print('send mail')
        return "mail send"
    except Exception as e:
        print(str(e))
        return "mail error"