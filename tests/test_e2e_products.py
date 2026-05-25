from pages.product_page import ProductPage
from api.product_client import ProductClient

def test_create_and_verify_product_e2e(page):
    
    product_page = ProductPage(page)
    api_client = ProductClient()
    test_title = "Portfolio Camera"

    
    product_data = api_client.create_product(title=test_title, body="High-end DSLR")
    assert product_data["title"] == test_title

    
    product_page.navigate()
    product_page.go_to_guide()
    
    
    product_page.verify_product_visible("Guide") 
    
    print(f"Successfully verified E2E flow for: {test_title}")