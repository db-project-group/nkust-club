from flask import Blueprint
from db.model import *
from db.data import InitData, TestData


db_data = Blueprint('data', __name__)


@db_data.cli.command("init")
def init():
    if not Committee.query.first():
        co_list = []
        cl_list = []
        j_list = []
        for committee in InitData.committees:
            co = Committee(*committee)
            co_list.append(co)
            for club in InitData.clubs[committee[1]]:
                cl = Club(club, committee[0])
                cl_list.append(cl)
                
        for job in InitData.jobs:
            j = Job(*job)
            j_list.append(j)
        
        db.session.add_all(co_list)
        db.session.add_all(cl_list)
        db.session.add_all(j_list)
        db.session.commit()

        print("Insert init data done.")
    else:
        print("Table is not empty.")


@db_data.cli.command("test")
def test():
    pass
