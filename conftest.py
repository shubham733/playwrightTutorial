import os
import playwright
import pytest
from playwright.sync_api import Playwright

PASSWORD = os.environ['PASSWORD']

# try:
#     PASSWORD = os.environ['PASSWORD']
# except KeyError:
#     import utils.secret_config
#     PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture(scope="session")
def context_creation(playwright):
    # Assess - Given
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    context.clear_cookies()
    page = context.new_page()
    # Open new page
    page.goto("https://master.eb.uat.simplelegal.dev/", timeout=0)
    page.set_default_timeout(5000)
    page.fill('input:below(:text("Email"))', "simplelegaldemo+professional@gmail.com")
    # page.fill('input:below(:text("Password"))', utils.secret_config.PASSWORD)
    page.fill('input:below(:text("Password"))', PASSWORD)
    page.locator("button:has-text('Sign In')").click()

    yield context



@pytest.fixture()
def set_up(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://master.eb.uat.simplelegal.dev/", timeout=0)
    page.set_default_timeout(5000)

    yield page







