# (c) 2014 Digital Humanities Lab, Faculty of Humanities, Utrecht University
# Author: Julian Gonggrijp, j.gonggrijp@uu.nl

"""
    Database object for use throughout the Flask side of the project.
"""

import flask.ext.sqlalchemy as fsqla

db = fsqla.SQLAlchemy()
