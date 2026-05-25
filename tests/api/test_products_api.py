import requests

def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) > 0
    
    assert "title" in data[0]

def test_create_post():
    payload = {
        "title": "Learning QA",
        "body": "I am mastering API testing!",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    
    
    assert response.status_code == 201
    assert response.json()["title"] == "Learning QA"