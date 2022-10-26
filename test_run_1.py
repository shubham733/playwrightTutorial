import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


# @pytest.mark.skip(reason="Not Ready")
# @pytest.mark.parametrize("email", ["simplelegaldemo+professional@gmail.com",
#                                              pytest.param("new@new.com", marks=pytest.mark.xfail),
#                                              pytest.param("new1@gmail.com", marks=pytest.mark.xfail)])
# @pytest.mark.parametrize("password", ["StartOfSummer21!",
#                                              pytest.param("new@new.com", marks=pytest.mark.xfail),
#                                              pytest.param("new1@gmail.com", marks=pytest.mark.xfail)])
def test_run_1(playwright: Playwright):
    # Assess - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    context.clear_cookies()
    # Open new page
    page = context.new_page()
    page.goto("https://master.eb.uat.simplelegal.dev/accounts/login/?next=/", timeout=0)
    page.set_default_timeout(3000)

    # Act - When/And
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("simplelegaldemo+professional@gmail.com")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("StartOfSummer21!")
    page.locator("button:has-text('Sign In')").click()
    page.locator("[data-testid=\"quick_add\"] svg").click()
    # with page.expect_navigation():
    #     page.locator("text=New Matter").click()
    # page.locator("[data-testid=\"drawer_attribute_0\"]").click()
    # page.locator("[data-testid=\"drawer_attribute_0\"]").fill("tester1")
    # page.locator(".css-ackcql").first.click()
    # page.locator("#react-select-2-option-0").click()
    # page.locator(".css-1d8n9bt .css-ackcql").click()
    # page.locator("#react-select-3-option-0").click()
    # page.locator("section:has-text(\"Optional Fields\")").nth(2).click()
    # page.locator("#slm_drawer_custom_attribute_3").click()
    # page.locator("#slm_drawer_custom_attribute_3").fill("test")
    # with page.expect_navigation():
    #     page.locator("[data-testid=\"create_matter_btn\"]").click()
    # with page.expect_navigation():
    #     page.locator("text=Publish Matter").click()

    context.close()
    browser.close()

#
# with sync_playwright() as playwright:
#     test_run_1(playwright)
