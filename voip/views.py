from flask import Flask, request, jsonify
from . app import app


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

