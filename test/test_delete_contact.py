# -*- coding: utf-8 -*-

def test_delete_contact(app):
    app.go_to_home_page()
    app.delete_contact.del_contact()
    app.delete_contact.close_alert_and_get_its_text()
