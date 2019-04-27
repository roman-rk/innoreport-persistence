from py2neo import Graph, NodeMatcher
from database.report import *
import configparser

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
    matcher = NodeMatcher(GRAPH)
    rep = Report()
    rep.rId = id
    GRAPH.pull(rep)
    return str(clear_report(rep))

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
    if data["rId"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    if 'SUBMITS' in data.keys():
        u = User()
        u.email = data['SUBMITS']
        GRAPH.pull(u)
        report.SUBMITS.add(u)
    if 'BELONGS' in data.keys():
        for id in data['BELONGS']:
            e = Entity()
            e.eId = int(id)
            GRAPH.pull(e)
            report.BELONGS.add(e)
    GRAPH.create(report)
    print(report)
    GRAPH.pull(report)
    return str(report.rId)

def db_update_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    if data["rId"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    if 'SUBMITS' in data.keys():
        u = User()
        u.email = data['SUBMITS']
        GRAPH.pull(u)
        report.SUBMITS.append(u)
    if 'BELONGS' in data.keys():
        e = Entity()
        for id in data['BELONGS']:
            e.eId = id
            GRAPH.pull(e)
            report.BELONGS.append(e)
    GRAPH.push(report)
    GRAPH.pull(report)
    return str(report.rId)
