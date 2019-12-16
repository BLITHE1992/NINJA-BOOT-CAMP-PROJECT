from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app= Flask(__name__)

app.config["Mongodb_name"]="mongotask"
app.config["MONGO_URI"]='mongodb+srv://BlitheSiddiqui:saqib6454@todoapp-oqqes.mongodb.net/test?retryWrites=true&w=majority'

mongo=PyMongo(app) 
CORS(app) 

@app.route('/')
def collect():
    return ""

@app.route('/api/tasks', methods=["GET"])
def get_all_tasks():
    tasks=mongo.db.task
    result=[]
    for field in tasks.find():
        result.append({'_id':str(field['id'])})
        result.append({'title':(field['title'])})
    return jsonify(result)

@app.route('/api/tasks', methods= ["POST"])
def add_task():
    tasks = mongo.db.tasks
    title = request.get_json()['title']

    task_id=tasks.insert({'title':title})
    new_task=tasks.find_one({'_id':task_id})

    result={'title':new_task['title']}
    return jsonify({'result':result})

@app.route('/api/tasks/<id>', methods= ["PUT"])
def update_task(id):
    tasks = mongo.db.tasks
    title = request.get_json()['title']

    new_task=tasks.find_one_and_update({
        '_id':ObjectId(id)},
       {"$set":{"title":title
       }},
                             upsert=False)
    new_task = tasks.find_one({"_id": ObjectId(id)})


    result={'title':new_task['title']}
    return jsonify({'result':result})

@app.route('/api/tasks/<id>', methods= ["DELET"])
def del_tasks(id):
    tasks = mongo.db.tasks

    response = tasks.delete_one({"_id": ObjectId(id)})
    if response.delete_count == 1:
        result= {"message":"record deleted"}
    else:
        result={"message": "NO recorded found"}

    return jsonify({"result":result})







if __name__=='__main__':
    app.run(debug=True, port=5002)