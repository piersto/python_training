# -*- coding: utf-8 -*-

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.edit_contact()
    app.session.logout()


