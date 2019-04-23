'''
Flask application: report_persistence

Persistence service, which creates requests to the
database graph database.
The service handles requests for Report object.
Model of the object is defined in the database/report.py
'''

from flask import Flask, request, json
from database.database import *

app = Flask(__name__)
connect_to_db()

@app.route("/innoreports/report/getReport?<id>", methods=['GET'])
def get_report_by_id(id):
    assert request.method == 'GET'
    return db_match_report(id)

@app.route("/innoreports/report/getAllReports", methods=['GET'])
def get_all_reports():
    assert request.method == 'GET'
    return db_get_all_reports()

@app.route("/innoreports/report/getReportHistory?<token>", methods=['GET'])
def get_report_history(token):
    assert request.method == 'GET'
    return db_get_report_history(token)

# Update of the user's token
@app.route("/innoreports/report/updateReport", methods=['PUT'])
def update_report():
    assert request.method == 'PUT'
    if request.headers['Content-Type'] == 'application/json':
        return db_update_report(json.loads(request.json)[0])
# Creation of the new user in database
@app.route("/innoreports/user/createReport", methods=['POST'])
def post_report():
    assert request.method == 'POST'
    if request.headers['Content-Type'] == 'application/json':
            return db_post_report(json.loads(request.json)[0])
