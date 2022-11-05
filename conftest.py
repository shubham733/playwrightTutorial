import os
import time

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
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
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
    page.wait_for_load_state(timeout=10000)
    time.sleep(2)
    context.storage_state(path='state.json')

    yield context




@pytest.fixture()
def set_up(context_creation, playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://master.eb.uat.simplelegal.dev/", timeout=0)
    page.set_default_timeout(5000)

    yield page
    browser.close()







