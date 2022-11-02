import pytest
from playwright.sync_api import expect
from pom.homepage_elements import HomePage


@pytest.mark.xfail(reason="url not working")
def test_create_matter(set_up) -> None:
    page = set_up
    home_page = HomePage(page)

    # Act - When/And
    home_page.quick_add_button.click()
    with page.expect_navigation():
        page.locator("text=New Matter").click()
    page.wait_for_timeout(5000)
    page.fill('input:below(:text("Matter Name"))', "New Tester - 3")
    # page.locator('input[id="react-select-2-input"]').click()
    page.locator(".css-ackcql").first.click()
    page.locator("#react-select-2-option-0").click()
    # page.wait_for_timeout(5000)
    # page.locator("div.react-app:nth-child(12) div.Body_container__BxhGX._classes_flexyCentered__rl4Yr main.Body_innerContainer__NdyHp main.Body_innerContentContainer__dVrAQ section.ReactPage_innerReactPageContainer__tfLBJ._classes_innerContentMaxWidth__kVHFx._classes_djangoResets___eoF5 div.TemplateSelection_container__MiJ5D div.SelectionPageContentContainer_container__j54u0 div.RequestInformation_wrapper__BsRRv div.RequestInformation_attributes__oCNkK:nth-child(5) div.RequestInformation_attribute__XkFcx:nth-child(3) div.css-b62m3t-container div.css-1s2u09g-control:nth-child(3) div.css-1d8n9bt > div.css-ackcql").click()
    page.wait_for_timeout(5000)
    page.locator("id=react-select-3-input").click()
    page.locator("#react-select-3-option-0").click()
    page.locator("text=Optional Fields").click()
    page.fill('input:below(:text("Matter Description"))', "test")
    # page.locator("#slm_drawer_custom_attribute_3").click()
    # page.locator("#slm_drawer_custom_attribute_3").fill("test")
    with page.expect_navigation():
        page.locator("[data-testid=\"create_matter_btn\"]").click()
    page.locator("text=Publish Matter").click()

    # Assert - Then
    expect(page.locator("text=Open")).to_be_visible()


