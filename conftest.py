import playwright
import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def set_up(browser):
    # Assess - Given
    # browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    context.clear_cookies()
    page = context.new_page()
    # Open new page
    page.goto("https://master.eb.uat.simplelegal.dev/", timeout=0)
    page.set_default_timeout(5000)
    page.fill('input:below(:text("Email"))', "simplelegaldemo+professional@gmail.com")
    page.fill('input:below(:text("Password"))', "StartOfSummer21!")
    page.locator("button:has-text('Sign In')").click()

    yield page
    page.close()






