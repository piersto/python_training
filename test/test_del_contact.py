def test_delete_first_contact(app):
    app.open_home_page_edit()
    app.session.login(username="admin", password="secret")
    app.del_contact.(DelContact)
    app.go_to_home_page()
    app.session.logout()
