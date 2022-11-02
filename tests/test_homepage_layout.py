import pytest
from playwright.sync_api import expect
from pom.homepage_elements import HomePage




# @pytest.mark.smoke
def test_homepage_layout(set_up) -> None:
    # Assess - Given
    page = set_up
    home_page = HomePage(page)

    # Act - When/And
    page.wait_for_timeout(5000)
    page.locator("a:has-text('Home')").click()

    # Assert - Then
    expect(home_page.left_header).to_be_visible()
    expect(home_page.right_header).to_be_visible()
