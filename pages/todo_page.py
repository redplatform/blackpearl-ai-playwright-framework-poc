class TodoPage:
    def __init__(self, page):
        self.page = page
        self.input_field = page.get_by_placeholder("What needs to be done?")
        self.todo_items = page.get_by_test_id("todo-item")

    def navigate(self):
        self.page.goto("https://playwright.dev")

    def add_task(self, text):
        self.input_field.fill(text)
        self.input_field.press("Enter")
