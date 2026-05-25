import pytest
import asyncio
from playwright.async_api import async_playwright


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def page():
    async with async_playwright() as p:
        
        browser = await p.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        
        
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent="QA_Automation_Bot_1.0"
        )
        
        page = await context.new_page()
        
        yield page
        
        
        await context.close()
        await browser.close()