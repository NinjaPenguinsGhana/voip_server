from flask import Flask, request, jsonify
from . app import app, db

from . models import Commands


@app.route('/add_cmd', methods=['POST'])
def add_cmd():
    post_data = request.get_json()

    command = post_data.get('command')
    new_cmd = Commands(command)

    db.session.add(new_cmd)
    db.session.commit()

    return jsonify("Succesfully Created Command")


@app.route('/get/<id>', methods=['GET'])
def get_one(id):  
    command = Commands.query.filter_by(id=id).first()
    print('cmd1 - {}'.format(command.command))
    result = {
        "id": command.id,
        "command": command.command
    }
    return jsonify(result)


@app.route('/dummy', methods=['GET'])
def get_dummy():  

    name = {'name': 'Holly'} 
    trans = {
        "transactions": [
            {
            "date": "1990-01-02",
            "type": "C",
            "amount": "+100"
            }]
    }
    return jsonify(name, trans)

