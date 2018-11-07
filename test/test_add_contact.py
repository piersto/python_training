# -*- coding: utf-8 -*-

from model.add_new_contact import Contact

    
def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.add_user(Contact(firstname="Pierre", middlename="Nik", lastname="Sto", nickname="psto", title="title", company="comp", address="address", homephone="514", mobilephone="515", workphone="516", fax="517",
                  email="p@gmail.com", homepage="p.com", birthday="18", birthmonth="January", birthyear="1988", anniversaryday="16", anniversarymonth="February", anniversaryyear="1989", address_2="address second",
                  phone_2="518", notes="notes"))
    app.submit_specified_user()
    app.go_to_home_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.add_user(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", homepage="", birthday="-", birthmonth="-",
                         birthyear="", anniversaryday="-", anniversarymonth="-", anniversaryyear="", address_2="", phone_2="", notes=""))
    app.submit_specified_user()
    app.go_to_home_page()
    app.session.logout()