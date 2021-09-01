import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless_mode = request.config.getoption("--headless").lower()
    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = True
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            base_url,
        )
    elif headless_mode == "false":
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()),
            base_url,
        )
    else:
        raise pytest.UsageError("--headless should be true or false")
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="test4738@test.com",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Password11",
        help="enter password",
    ),
