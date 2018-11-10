# -*- coding: utf-8 -*-

def test_add_contact(app):
    app.open_home_page_edit()
    app.session.login(username="admin", password="secret")
    app.test_edit_contact()
    app.session.logout()


