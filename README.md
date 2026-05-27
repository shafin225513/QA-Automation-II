# QA Automation Framework: API & E2E Suite

A professional-grade automation repository demonstrating industry-standard testing patterns. This suite transitions from basic scripting to a scalable **Page Object Model (POM)** architecture and **Hybrid E2E testing** (API + UI).

##  Key Technical Features
* **Hybrid E2E Testing:** Optimizes execution speed by seeding data via API before UI verification.
* **Page Object Model (POM):** Decouples UI locators from test logic for high maintainability.
* **Asynchronous Playwright:** Utilizes the `pytest-playwright` plugin for modern, non-blocking automation.
* **API Client Abstraction:** Centralized `requests` logic to handle backend interactions.

##  Project Structure
* `api/`: Contains `product_client.py` for direct backend interaction (POST/GET).
* `pages/`: Contains `product_page.py` UI definitions and locators (The "Map" of the application).
* `tests/`: 
    * `test_e2e.py`: The "3-Piece" logic (API Creation -> UI Verification).
All connected via __init__.py
* `browser_fixture.py`: Global configuration and professional fixture setup.
* `tests/api`:
  *  `test_product_api.py`: Pure API validation (Get/Post status codes & schemas).


## 🛠️ Setup & Execution

### Installation
```bash
pip install pytest-playwright requests
playwright install chromium --with-deps
