"""
File::obj_poll.py
Author::Kevin.P.Barnett
Date::Apr.21.2019
"""

from flask import g

class Poll(g.db.Model):
    id           = g.db.Column(g.db.String(36), primary_key=True)
    author       = g.db.Column(g.db.String(9), nullable=False)
    name         = g.db.Column(g.db.String(256), nullable=False)
    description  = g.db.Column(g.db.String(1024), nullable=False)
    can_add      = g.db.Column(g.db.Boolean, nullable=False)
    multi_select = g.db.Column(g.db.Boolean, nullable=False)
    timestamp    = g.db.Column(g.db.Integer, nullable=False)
    type         = g.db.Column(g.db.String(256), nullable=False)

    options      = g.db.relationship('Option', backref='poll', lazy=True)


def getFromDict(jsonObj):
    poll = Poll()
    poll.id           = jsonObj['id']
    poll.author       = jsonObj['author']
    poll.name         = jsonObj['name']
    poll.description  = jsonObj['description']
    poll.can_add      = jsonObj['can_add']
    poll.multi_select = jsonObj['multi_select']
    poll.timestamp    = jsonObj['timestamp']
    return poll


class Option(g.db.Model):
    option_id   = g.db.Column(g.db.String(36), primary_key=True)
    option_text = g.db.Column(g.db.String(1024), nullable=False)

    poll_id     = g.db.Column(g.db.String(36), g.db.ForeignKey('poll.id'), nullable=False)

    votes       = g.db.relationship('Vote', backref='option', lazy=True)


class Vote(g.db.Model):
    vote_id   = g.db.Column(g.db.Integer, primary_key=True)

    slack_id  = g.db.Column(g.db.String(36), g.db.ForeignKey('user.slack_id'), nullable=False)
    option_id = g.db.Column(g.db.String(36), g.db.ForeignKey('option.option_id'), nullable=False)
