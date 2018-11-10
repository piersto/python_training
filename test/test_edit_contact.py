# -*- coding: utf-8 -*-

def test_edit_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.edit_contact(updated_first_name="New first name")
    app.session.logout()


