"""
File::obj_poll.py
Author::Kevin.P.Barnett
Date::Apr.21.2019
"""
import uuid


class Poll:
    def __init__(self, args):
        self.id = str(uuid.uuid4())
        self.name = args['name']
        self.description = args['description']
        self.can_add = args['can_add']
        self.multi_select = args['multi_select']
        self.options = args['options']

    def __str__(self):
        return 'Poll(id: %s, name: %s, description: %s, can_add: %s, multi: %s)' %\
               (self.id, self.name, self.description, self.can_add, self.multi_select)
