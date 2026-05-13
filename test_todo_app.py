import refrom playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="MCP", exact=True).click()
    page.get_by_role("link", name="Snapshots").click()
    page.get_by_role("link", name="Navigation").click()
    page.get_by_role("link", name="Navigation").click()
    page.get_by_role("link", name="Keyboard & Mouse").click()
    page.get_by_role("link", name="Dialogs").click()
    page.get_by_role("link", name="Network & Mocking").click()
    page.get_by_text("ConsoleScreenshotsCode").click()
    page.get_by_role("link", name="Testing & Assertions").click()
    page.get_by_role("link", name="Profile & State").click()
    page.get_by_role("link", name="API").click()
    page.get_by_text("APIRequestAPIRequestContextAPIResponseBrowserBrowserContextBrowserServerBrowserT").click()
    page.get_by_role("link", name="Clock", exact=True).click()
    page.get_by_role("link", name="BrowserType").click()
    page.get_by_role("button", name="Node.js").click()
    page.get_by_role("link", name="Python").click()
    page.get_by_role("link", name="CDPSession", exact=True).click()
    page.get_by_role("link", name="Clock", exact=True).click()
    page.get_by_role("link", name="ConsoleMessage", exact=True).click()
    page.get_by_role("button", name="Python").click()
    page.get_by_role("link", name="Community").click()
    page.locator("body").press("ArrowDown")
    page.locator("body").press("ArrowDown")
    page.locator("body").press("ArrowDown")
    page.locator("body").press("ArrowDown")
    page.locator("body").press("ArrowDown")
    page.locator("body").press("ArrowDown")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="contributing guide").click()
    page1 = page1_info.value
    page.get_by_label("Docs sidebar").get_by_role("link", name="Feature Videos").click()
    page.goto("https://playwright.dev/python/community/welcome")
    page.get_by_role("button", name="Python").click()
    page.get_by_role("link", name="Python", exact=True).click()
    page.get_by_text("Welcome Welcome to the").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
