from flask import Flask,  jsonify, request


app= Flask(__name__)
users=[
    {
    '_id':4001,
    'title':'AI',
    'description':'Make sure the title of the job position and description match'
    'Done':'True'
    },
    {
    '_id':4002,
    'title':'CNC',
    'description':'Make sure the title of the job position and description match''
    'Done': 'True'
    },
    {
    '_id':4003,
    'title':'Block Chain',
    'description':'Make sure the title of the job position and description match'
    'Done': 'True'
    }]


@app.route("/todo/api/v1.0/tasks", methods=['GET'])
def get_all_tasks():
    return jsonify({"task":"task", 'title':'title'})

#@app.route("/todo/api/v1.0/tasks/abc", methods=['GET'])
#def  abc():
   


@app.route("/todo/api/v1.0/tasks/", methods=['POST'])
def create_tasks()   
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': 'False'
    }
           tasks.append(task)

@app.route("/todo/api/v1.0/tasks/[task_id]", methods=['PUT'])
def update_all(task_id):
    dict.update([task])

@app.route("/todo/api/v1.0/tasks/[task_id]", methods=['DELET'])
def task(task_id):
    if one_id in task_id:
        del ({'id:'})
        return({'message':'Are you sure'})
    else:
        return({'message':"you are completely remove})












if __name__=='__main__':
    app.run(debug=True, port=5002)