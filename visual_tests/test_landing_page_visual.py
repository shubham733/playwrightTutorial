import os
import pytest
from playwright.sync_api import expect
from pom.homepage_elements import HomePage
PASSWORD = os.environ['PASSWORD']


# @pytest.mark.smoke
def test_visual_landing(page, assert_snapshot) -> None:
    # Assess - Given
    home_page = HomePage(page)
    page.goto("https://master.eb.uat.simplelegal.dev/", timeout=0)
    page.fill('input:below(:text("Email"))', 'drew.swartz+professional@simplelegal.com')
    # page.fill('input:below(:text("Password"))', utils.secret_config.PASSWORD)
    page.fill('input:below(:text("Password"))', PASSWORD)
    page.locator("button:has-text('Sign In')").click()

    # Act - When/And
    page.locator("a:has-text('Home')").click()

    # Assert - Then
    expect(home_page.left_header).to_be_visible()
    expect(home_page.right_header).to_be_visible()
    assert_snapshot(page.screenshot())
