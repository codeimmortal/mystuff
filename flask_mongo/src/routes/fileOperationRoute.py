from flask import Blueprint,render_template,request,redirect,url_for

fileOperation_templates = Blueprint('fileOperation_templates', __name__)

@fileOperation_templates.route("/create", methods=['POST'])
def create ():
    #Display the all Tasks
    try:
        name = request.values.get("file_name")
        content = request.values.get("content")
        f = open(name,"w")
        f.write(content)
        f.close()
    except IOError as ioerr:
        print('error in ioerr',ioerr)
        return {
            "message": "failed"
        }
    return {
        "message": "sucess"
    }

@fileOperation_templates.route("/read", methods=['GET'])
def read ():
    #Display the all Tasks
    name = request.values.get("file_name")
    try:
        f = open(name,"r")
        fileread = f.read()
    except IOError as ioerr:
        print('error in ioerr',ioerr)
        return {
            "message": "failed"
         }
    except:
        print('some other error')
        return {
            "message": "failed with some other error"
         }
    return {
        "message": "sucess",
        "content": fileread
    }