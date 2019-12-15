from flask import Flask ,request,jsonify
from flask_pymongo import PyMongo
from pymongo import ReturnDocument

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://BlitheSiddqiui:saqib6454@cluster0-z5mbi.mongodb.net/test?retryWrites=true&w=majority'


mongo = PyMongo(app) 

list_T = [
    {
        "_id": 10,
        "title": "Assignment complete",
        "description": "we have to complete the Part 1 before Friday",
        "done": True
    },
    {
        "_id": 20,
        "title": "Polish the Skills ",
        "description": "We have to polish our skills asap",
        "done": False
    }
]

@app.route("/todo/api/v1.0/tasks", methods = ["GET"])
def getting_tasks():
    collection = mongo.db.collection 
    data = collection.find()
    all_task=[]
    for i in data:
        all_task.append(i)
    return jsonify({"result":all_task})

@app.route("/todo/api/v1.0/tasks/<task_id>", methods = ["GET"])
def get_task(task_id):
    collection = mongo.db.collection
    data = collection.find_one({"_id":int(task_id)})
    return jsonify({"result":data})

@app.route("/todo/api/v1.0/tasks" , methods = ["POST"])
def add_task():
    collection = mongo.db.collection
    update_task = request.get_json()
    
    collection.insert({'_id':update_task['_id'],'title':update_task['title'],'description':update_task['description'],'done':bool(update_task['done'])})
    return "Task added"

@app.route("/todo/api/v1.0/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    collection = mongo.db.collection 
    update_task = request.get_json()
    find_id = collection.find_one({'_id':int(task_id)})
    if (find_id):
        update = False
        for i in update_task:
            if i != '_id':
                collection.find_one_and_update({'_id':int(task_id)},{'$set':{i:str(update_task[i])}},return_document=ReturnDocument.AFTER)
                update = True
        if (update):
            return "task updated"
        elif (update == False):
            return "cant update id"
    return "id not found"
    
    

@app.route("/todo/api/v1.0/tasks/<task_id>", methods = ["DELET"])
def delete_task(task_id):
    collection = mongo.db.collection
    del_task = collection.find_one({'_id':int(task_id)})
    if (del_task):
        collection.find_one_and_delete({'_id':int(task_id)})
        return "Deleted"
    return "Not Found"


app.run(debug=True)
