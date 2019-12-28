from flask import Blueprint,render_template,request,redirect,url_for
from bson import ObjectId # For ObjectId to work
import os
from src.mongoConnect import db
todos = db.todo #Select the collection name
title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"
# method call when request id fro \ , \uncompleted

simple_templates = Blueprint('simple_templates', __name__)

@simple_templates.route("/")
@simple_templates.route("/uncompleted")
def tasks ():
    #Display the Uncompleted Tasks
    todos_l = todos.find({"done":"no"})
    a2="active"
    return render_template('index.html',a2=a2,todos=todos_l,t=title,h=heading)

@simple_templates.route("/list")
def lists ():
    #Display the all Tasks
    todos_l = todos.find()
    a1="active"
    return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)

@simple_templates.route("/completed")
def completed ():
    #Display the Completed Tasks
    todos_l = todos.find({"done":"yes"})
    a3="active"
    return render_template('index.html',a3=a3,todos=todos_l,t=title,h=heading)

@simple_templates.route("/done")
def done ():
    #Done-or-not ICON
    id=request.values.get("_id")
    task=todos.find({"_id":ObjectId(id)})
    if(task[0]["done"]=="yes"):
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"no"}})
    else:
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"yes"}})
    redir=redirect_url()    
    return redirect(redir)

@simple_templates.route("/action", methods=['POST'])
def action ():
    #Adding a Task
    name=request.values.get("name")
    desc=request.values.get("desc")
    date=request.values.get("date")
    pr=request.values.get("pr")
    todos.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
    return redirect("/list")

@simple_templates.route("/remove")
def remove ():
    #Deleting a Task with various references
    key=request.values.get("_id")
    todos.remove({"_id":ObjectId(key)})
    return redirect("/")

@simple_templates.route("/update")
def update ():
    id=request.values.get("_id")
    task=todos.find({"_id":ObjectId(id)})
    return render_template('update.html',tasks=task,h=heading,t=title)

@simple_templates.route("/action3", methods=['POST'])
def action3 ():
    #Updating a Task with various references
    name=request.values.get("name")
    desc=request.values.get("desc")
    date=request.values.get("date")
    pr=request.values.get("pr")
    id=request.values.get("_id")
    todos.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})
    return redirect("/")

@simple_templates.route("/search", methods=['GET'])
def search():
    #Searching a Task with various references
    key=request.values.get("key")
    refer=request.values.get("refer")
    if(key=="_id"):
        todos_l = todos.find({refer:ObjectId(key)})
    else:
        todos_l = todos.find({refer:key})
    return render_template('searchlist.html',todos=todos_l,t=title,h=heading)
