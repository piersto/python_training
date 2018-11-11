# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="Group 1", header="group 1 -1", footer="group1-1-1"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))