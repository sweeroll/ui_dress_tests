from common.constants import AccountConstants
from models.auth import AuthData


class TestCourseCreation:
    def test_valid_course_creation(self, app):
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="admin", password="Vjcrdf2!")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_administration_page()
        app.login.go_to_course_page()
        assert AccountConstants.ADMINISTRATION == app.account.administration_page(), (
            "We are not on administration " "page! "
        )
        app.login.go_to_create_course_page()
        assert (
            AccountConstants.CREATE_COURSE == app.account.create_course_page()
        ), "We are not on create course page!"
