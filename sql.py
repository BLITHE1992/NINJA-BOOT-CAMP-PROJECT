from flask import Flask , jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
from flask import send_from_directory



#CONNECTION:


app = Flask(__name__)

app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_DB"] = "todo"

mysql = MySQL(app)



CORS(app)


@app.route('/', methods=['POST'])
def table():
    cur = mysql.connection.cursor()
    result = cur.execute("CREATE TABLE todo (id INTEGER, title VARCHAR(255), description VARCHAR(255), done BOOLEAN)")
    result.commit()
    return jsonify(result)


@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM todo")
    rv = cur.fetchall()
    return jsonify(rv)


@app.route('/api/task', methods=['POST'])
def add_task():
    cur = mysql.connection.cursor()
    blob = request.get_json()
    cur.execute("INSERT INTO todo (id,title,description,done) VALUES ('2', 'class', 'homework', 'False')")
    mysql.connection.commit()
    result = {'title': blob}
    return jsonify({'result': result})


@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    cur = mysql.connection.cursor()
    title = request.get_json()['title']
    cur.execute("UPDATE todo SET title = '" + str(title) + "' WHERE id = " + id)
    mysql.connection.commit()
    result = {'title': title}

    return jsonify({'result': result})


@app.route('/api/task/<id>', methods=['DELET'])
def delete_task(id):
    cur = mysql.connection.cursor()
    response = cur.execute("DELET FROM todo where id = " + id)
    mysql.connection.commit()

    if response > 0:
        result = {'message': 'record delete'}
    else:
        result = {'message': 'no record found'}

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
