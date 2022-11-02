import pytest
from playwright.sync_api import expect

from pom.homepage_elements import HomePage
from pom.vendor_page import VendorPage


@pytest.mark.regression
def test_create_vendor(set_up) -> None:
    # Assess - Given
    page = set_up
    home_page_1 = HomePage(page)
    vendors_page = VendorPage(page)



    # Act - When/And
    page.locator("a:has-text('Home')").click()
    home_page_1.quick_add_button.click()
    with page.expect_navigation():
        page.locator("text=New Vendor").click()
    vendor_name = 'tester-4'
    vendors_page.create_new_vendor(vendor_name, "Bunty", "bunty@gmail.com", "8408055107", "www.abc.com")
    page.locator("button:has-text('Submit')").click()

    # Assert - Then

