def test_delete_first_contact(app):
    app.open_home_page_edit()
    app.session.login(username="admin", password="secret")
    app.open_home_page()
    app.del_contact()
    app.session.logout()
