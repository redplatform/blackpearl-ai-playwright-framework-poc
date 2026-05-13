class LoginPage:
    def __init__(self, page):
        # Must have exactly TWO underscores on each side: __init__
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    def navigate(self):
        # Must use full protocol URL string
        self.page.goto("https://saucedemo.com")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
