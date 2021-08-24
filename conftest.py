import pytest

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install()), base_url)
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://automationpractice.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="test4738@test.com",
        help="enter username",
    ),
    parser.addoption(
        "--password", action="store", default="Password11", help="enter password",
    ),
