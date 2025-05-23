import pytest
from playwright.sync_api import sync_playwright

#pytest with playwright
def test_google():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")
        
        assert "Google" in page.title()
        browser.close()
