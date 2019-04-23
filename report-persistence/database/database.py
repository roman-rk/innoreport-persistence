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
    rep.id = id
    return list(map(clear_report, rep.match(graph)))

def db_get_all_reports():
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    return list(map(clear_report, list(matcher.match("Report"))))

def db_get_report_history(token):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    u = User()
    u.token = token
    GRAPH.pull(u)
    result = list()
    for rep in u.SUBMITS:
        GRAPH.pull(rep)
        result.add(clear_report(rep))
    return result


def db_post_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    if data["id"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    GRAPH.pull(report)
    GRAPH.create(report)
    GRAPH.pull(report)
    return report.id

def db_update_report(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    if data["id"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    GRAPH.push(report)
    GRAPH.pull(report)
    return report.id
