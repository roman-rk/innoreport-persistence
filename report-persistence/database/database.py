from py2neo import Graph, NodeMatcher
from database.report import *
import configparser
import uuid
import json

GRAPH = None

def __init__():
    pass

def connect_to_db():
    global GRAPH
    dburl = r"http://10.90.138.222:7474"
    GRAPH = Graph(dburl)

def db_match_report(id):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    rep = Report()
    rep.rId = id
    GRAPH.pull(rep)
    data = clear_report(rep)
    return str(data)

def db_get_all_reports():
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    matches = list(map(dict, list(matcher.match("Report"))))
    print(matches)
    return str(matches)

def db_get_report_history(email):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    u = User()
    u.email = email
    GRAPH.pull(u)
    result = list()
    for rep in u.SUBMITS:
        GRAPH.pull(rep)
        result.append(clear_report(rep))
    return str(result)


def db_post_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    print(data)
    report = make_report(data)
    report.rId = str(uuid.uuid4())
    print(report)
    if 'submits' in data.keys():
        u = User()
        u.email = data['submits']
        GRAPH.pull(u)
        report.SUBMITS.add(u)
    if 'belongs' in data.keys():
        for id in data['belongs']:
            e = Entity()
            e.eId = int(id)
            GRAPH.pull(e)
            report.BELONGS.add(e)
    print(report.rId)
    GRAPH.create(report)
    GRAPH.pull(report)
    print(report.rId)
    return str(report.rId)

def db_update_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    report = Report()
    report.rId = data['rId']
    GRAPH.pull(report)
    report = make_report(data, report)
    if 'submits' in data.keys():
        u = User()
        u.email = data['submits']
        GRAPH.pull(u)
        report.SUBMITS.append(u)
    if 'belongs' in data.keys():
        for id in data['belongs']:
            e = Entityt()
            e.eId = id
            GRAPH.pull(e)
            report.BELONGS.append(e)
    GRAPH.push(report)
    GRAPH.pull(report)
    return str(report.rId)
