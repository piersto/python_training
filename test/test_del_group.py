def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.group.delete_first_group()
    app.session.logout()
