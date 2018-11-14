# -*- coding: utf-8 -*-

from model.add_new_contact import Contact


def test_delete_contact(app):
    app.go_to_home_page()
        if app.add_contact.count_contacts() == 0:
            app.add_user(Contact(firstname="Vasia"))
            app.submit_specified_user()
    app.delete_contact.del_contact()
