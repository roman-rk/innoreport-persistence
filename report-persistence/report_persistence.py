'''
Flask application: report_persistence

Persistence service, which creates requests to the
database graph database.
The service handles requests for Report object.
Model of the object is defined in the database/report.py
'''

from flask import Flask, request, json
from database.database import *
import ast

app = Flask(__name__)
connect_to_db()

@app.route("/innoreports/report/getReport", methods=['GET'])
def get_report_by_id():
    assert request.method == 'GET'
    return db_match_report(request.args.get('id', ''))

@app.route("/innoreports/report/getAllReports", methods=['GET'])
def get_all_reports():
    assert request.method == 'GET'
    return db_get_all_reports()

@app.route("/innoreports/report/getReportHistory", methods=['GET'])
def get_report_history():
    assert request.method == 'GET'
    return db_get_report_history(request.args.get('email', ''))

# Update of the user's token
@app.route("/innoreports/report/updateReport", methods=['PUT'])
def update_report():
    assert request.method == 'PUT'
    if request.headers['Content-Type'] == 'application/json':
        return db_update_report(ast.literal_eval(request.json))


# Creation of the new user in database
@app.route("/innoreports/report/createReport", methods=['POST'])
def post_report():
    assert request.method == 'POST'
    if request.headers['Content-Type'] == 'application/json':
            return db_post_report(ast.literal_eval(request.json))
