class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        app.login.auth(login="test4738@test.com", password="Password11")
        assert app.login.is_auth, "You are not authorized, check auth data"
