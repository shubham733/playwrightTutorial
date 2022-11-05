import pytest
from playwright.sync_api import expect
from pom.homepage_elements import HomePage




# @pytest.mark.smoke
def test_page_layout(ebill_set_up) -> None:
    # Assess - Given
    page, page2 = ebill_set_up
    home_page = HomePage(page, page2)

    # Act - When/And
    page.wait_for_timeout(5000)
    page.locator("a:has-text('Home')").click()

    # Assert - Then
    expect(home_page.left_header).to_be_visible()
    expect(home_page.right_header).to_be_visible()


    # Act - When/And
    page2.wait_for_timeout(5000)
    page2.locator("a:has-text('Home')").click()

    # Assert - Then
    expect(home_page.left_header2).to_be_visible()
    expect(home_page.right_header2).to_be_visible()
