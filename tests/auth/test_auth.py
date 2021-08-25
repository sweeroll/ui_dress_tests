from common.constants import LoginConstants


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_auth_page()
        app.login.auth("admin", "Vjcrdf2!")
        assert app.login.is_auth(), "We are not auth"

    def test_auth_invalid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        app.open_auth_page()
        app.login.auth("admin", "admin1")
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    def test_auth_empty_password(self, app):
        """
        Steps
        1. Open main page
        2. Auth with empty password
        3. Check auth result
        """
        app.open_auth_page()
        app.login.auth("admin", "")
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    def test_auth_empty_login(self, app):
        """
        Steps
        1. Open main page
        2. Auth with empty login
        3. Check auth result
        """
        app.open_auth_page()
        app.login.auth("", "Vjcrdf2!")
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"