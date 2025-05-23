import pytest
from playwright.sync_api import sync_playwright

def test_wiki():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://auth.wikimedia.org/enwiki/wiki/Special:UserLogin?useformat=desktop&usesul3=1&returnto=Main_Page&centralauthLoginToken=47c07ad64c196bdeb4b9a1a18e829cdb")
        
        assert "Log in - Wikipedia" in page.title()
        browser.close()
