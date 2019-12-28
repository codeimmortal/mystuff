from flask import  Flask,render_template,request,redirect,url_for # For flask implementation
from src.routes.databaseRoute import simple_templates
from src.routes.fileOperationRoute import fileOperation_templates
from src.routes.emailRoutes import mailOperation_templates
from flask_mail import Mail
from flask_mail import Message
# declare the app variable
app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'himmsharma.99@gmail.com',
    MAIL_PASSWORD = '*Hnivi11H*',
))
mail = Mail(app)
app.register_blueprint(simple_templates)
app.register_blueprint(fileOperation_templates, url_prefix='/file')
app.register_blueprint(mailOperation_templates, url_prefix='/email')
app.debug = True
# redirecting routes to index
def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')

@app.route("/send", methods=['POST'])
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
        print("mail error")
        return "mail error"
if __name__ == "__main__":
    app.run()