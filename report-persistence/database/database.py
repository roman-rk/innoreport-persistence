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
    id = int(id)
    #print(id)
    #print(GRAPH)
    rep = Report()
    rep.id = id
    #print(clear_report(rep))
    GRAPH.pull(rep)
    return str(clear_report(rep))

def db_get_all_reports():
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    matches = list(map(dict, list(matcher.match("Report"))))
    print(matches)
    return str(matches)

def db_get_report_history(token):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    u = User()
    u.name = token
    GRAPH.pull(u)
    result = list()
    for rep in u.SUBMITS:
        GRAPH.pull(rep)
        result.append(clear_report(rep))
    return str(result)


def db_post_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    if data["id"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    GRAPH.pull(report)
    GRAPH.create(report)
    GRAPH.pull(report)
    return str(report.id)

def db_update_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    if data["id"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    GRAPH.push(report)
    GRAPH.pull(report)
    return str(report.id)
