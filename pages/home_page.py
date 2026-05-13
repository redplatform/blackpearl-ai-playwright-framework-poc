class HomePage:
    def __init__(self, page):
        # Ensure double underscores on both sides
        self.page = page
        self.app_logo = page.locator(".app_logo")
        self.inventory_container = page.locator("#inventory_container")

    def get_logo_text(self):
        return self.app_logo.text_content()
