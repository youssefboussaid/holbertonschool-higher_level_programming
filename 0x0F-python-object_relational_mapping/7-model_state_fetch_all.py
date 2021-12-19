#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # access the table (like cursor)
    Base.metadata.create_all(engine)
    # talk to the database using a session
    mysession = Session(engine)
    states = mysession.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    mysession.close()
