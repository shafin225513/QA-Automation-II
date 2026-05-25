import requests

class ProductClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def create_product(self, title, body, user_id=1):
        payload = {"title": title, "body": body, "userId": user_id}
        response = requests.post(f"{self.base_url}/posts", json=payload)
        
        
        response.raise_for_status() 
        return response.json()