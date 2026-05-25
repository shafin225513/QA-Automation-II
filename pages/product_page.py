from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://jsonplaceholder.typicode.com/", wait_until="networkidle")

    def go_to_guide(self):
        
        self.page.locator("nav >> text=Guide").click()

    def verify_product_visible(self, text_to_find: str):
        
        expect(self.page.get_by_text(text_to_find).first).to_be_visible()