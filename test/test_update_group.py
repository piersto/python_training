# -*- coding: utf-8 -*-

from model.update_group import UpdateGroup

def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.group.update_group(UpdateGroup(updated_group_name="New group name", updated_group_header="New group header", updated_group_footer="New group footer"))
    app.session.logout()
