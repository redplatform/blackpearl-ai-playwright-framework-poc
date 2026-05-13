from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_successful_login(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    # 1. Open the platform portal
    login_page.navigate()

    # 2. Enter official practice sandboxed credentials
    login_page.login("standard_user", "secret_sauce")

    # 3. Synchronize structural rendering checks
    home_page.inventory_container.first.wait_for(state="visible")

    # 4. Verify system authentication state
    assert home_page.get_logo_text() == "Swag Labs"
