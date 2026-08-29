from datetime import datetime

import pytest
from playwright.sync_api import Playwright
from pages.sauce_demo import SauceDemo
from utils.config_reader import ConfigReader

@pytest.fixture
def sauce_demo(app_page):
    return SauceDemo(app_page)

@pytest.fixture
def test_context():
    return {}

@pytest.fixture(scope="session")
def config_data():
    config_data = ConfigReader()
    return config_data

def pytest_addoption(parser):
    parser.addoption( "--headless", action="store", default=None, help="Run in headless or headed mode")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()


    if report.when == "call" and report.failed:
        page = getattr(item, "page", None)

        if page:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = (
                f"reports/screenshots/{item.name}_{timestamp}.png"
            )

            page.screenshot(path=screenshot_path)

            print(
                f"Test Case {item.name} Failed and screenshot was taken: "
                f"{screenshot_path}"
            )


@pytest.fixture(scope="session")
def app_browser(request, config_data, playwright : Playwright):

    browser = request.config.getoption("--browser")

    if browser:
        browser_name = browser[0]
    else:
        browser_name = config_data.get_browser()

    if browser_name == "chromium":
        browser_type = playwright.chromium
    elif browser_name == "firefox":
        browser_type = playwright.firefox
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    headless_option = request.config.getoption("--headless")

    if headless_option is not None:
        if headless_option.lower() == "true":
            headless_value = True
        elif headless_option.lower() == "false":
            headless_value = False
        else:
            raise ValueError(f"Unsupported headless value: {headless_option}")
    else:
        headless_value = config_data.get_headless()


    browser = browser_type.launch(
            headless=headless_value
        )

    yield browser

    browser.close()

@pytest.fixture
def app_page(app_browser, config_data,request):
    context = app_browser.new_context(no_viewport= True)
    page = context.new_page()
    page.set_default_timeout(config_data.get_timeout())
    page.goto(config_data.get_base_url())
    request.node.page = page

    yield page
    context.close()
