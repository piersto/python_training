def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.go_to_home_page()
    app.del_contact()
    app.session.logout()
