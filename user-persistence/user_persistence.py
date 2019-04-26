'''
Flask application: user_persistence

Persistence service, which creates requests to the
database graph database.
The service handles requests for User object.
Model of the object is defined in the database/user.py
'''

from flask import Flask, request, json
from database.database import *

app = Flask(__name__)
connect_to_db()

# Search user with specified <email>
@app.route("/innoreports/user/getUser", methods=['POST'])
def get_user_by_email():
    assert request.method == 'POST'
    return db_match_user(request.form['email'])

# Update of the user's token
@app.route("/innoreports/user/updateToken", methods=['PUT'])
def put_token():
    assert request.method == 'PUT'
    if request.headers['Content-Type'] == 'application/json':
        return db_put_token(json.loads(request.json)[0])

# Creation of the new user in database
@app.route("/innoreports/user/createUser", methods=['POST'])
def post_user():
    assert request.method == 'POST'
    if request.headers['Content-Type'] == 'application/json':
            return db_post_user(json.loads(request.json)[0])
