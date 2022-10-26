from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.skip(reason="Not Ready")
def test_run(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Act - When/And
    page.locator("button", has_text="Log In").click(timeout=2000)
    page.locator("button", has_text="Log In").click(timeout=2000)
    print(page.content())
    page.locator("button", has_text="Log in with Email").click()
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("bunty.shelar123@gmail.com")
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill("Bunty@123")
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    page.locator("[aria-label=\"bunty\\.shelar123 account menu\"]").click()

    # Assert - Then
    assert page.is_visible("text=My Orders")


    # Click text=My Orders
    # with page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1/account/my-orders"):
    # with page.expect_navigation():
    #     page.locator("text=My Orders").click()
    # ---------------------
    context.close()
    browser.close()

