import pytest

from models.auth import AuthData
from models.personal_data import PersonalData as PD


@pytest.mark.personal_data
class TestPersonalData:
    def test_valid_edit_basic_personal_data(self, app):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successfully editing
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            auth_data = AuthData(login="rishat", password="Rishat-9173")
            app.login.auth(auth_data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.edit_personal_data(personal_data)
        assert app.personal_data.is_changed(), "Personal data not changed!"

    @pytest.mark.parametrize("field", ["name", "last_name", "email"])
    def test_edit_basic_personal_data_without_required_field(self, app, field):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successfully
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            auth_data = AuthData(login="rishat", password="Rishat-9173")
            app.login.auth(auth_data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, field, "")
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize("email", ["nilluziafmail.ru", "@mail.ru", "111"])
    def test_edit_basic_personal_data_with_incorrect_email(self, app, email):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with incorrect email
        6. Check editing is not successfully
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            auth_data = AuthData(login="rishat", password="Rishat-9173")
            app.login.auth(auth_data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "email", email)
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize(
        "name, last_name",
        [
            ["123", "123"],
            ["---", "---"],
            ["\xbdR6\x10\x7f", "\xbdR6\x10\x7f"],
            [PD().random().url, PD().random().url],
            [PD().random().image_url, PD().random().image_url],
        ],
    )
    @pytest.mark.xfail
    @pytest.mark.bug
    def test_edit_incorrect_name_lastname(self, app, name, last_name):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit name or(and) lastname as digits
        6. Check editing is not successfully
        """
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            auth_data = AuthData(login="rishat", password="Rishat-9173")
            app.login.auth(auth_data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "name", name)
        setattr(personal_data, "last_name", last_name)
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"
