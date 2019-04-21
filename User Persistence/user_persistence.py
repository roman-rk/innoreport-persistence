'''
Flask application: user_persistence

Persistence service, which creates requests to the
neo4j graph database.
The service handles requests for User object.
Model of the object is defined in the Model/user.py
'''

from flask import Flask, request

app = Flask(__name__)


@app.route("/innoreports/user/getById?<id>", methods=['GET'])
def get_user_by_id(id):
    if request.method == 'GET':
        pass
    else:
        pass


@app.route("/innoreports/user", methods=['POST'])
def post_user():
    if request.method == 'POST':
        pass
    else:
        pass
