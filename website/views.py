from django.shortcuts import render, redirect
from django.forms import modelform_factory
from manage import collection
from bson.objectid import ObjectId
from django.views.generic import RedirectView

# Create your views here.
def main(req):   
    cursor = collection.find()
    tasks = []
    for record in cursor:
        tasks.append((record["task"], record["done"], record["_id"]))

    tasks.reverse()
    return render(req, "taskManager.html", {"tasks": tasks})

def addTask(req):
    if req.method == "POST":
        if len(req.POST["title"]) > 0:
            emp_rec1 = {
            "task" : req.POST["title"],
            "done" : False,
            }
            collection.insert_one(emp_rec1)
    return redirect('/')

def markAsDone(req, id):
    myquery = {"_id" : ObjectId(id)}
    newValues = {"$set": {"done": True}}
    collection.update_one(myquery, newValues)
    return redirect('/')

def deleteTask(req, id):
    collection.delete_one({"_id" : ObjectId(id)})
    return redirect('/')