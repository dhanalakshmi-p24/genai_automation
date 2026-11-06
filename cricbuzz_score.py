from playwright.sync_api import sync_playwright
# open the browser and navigate to the Cricbuzz website --> print it --> save the screenshot of the page    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
    "https://www.cricbuzz.com/",
    wait_until="domcontentloaded"
)
    print(page.title())
    page.screenshot(path="cricbuzz_screenshot.png")
    browser.close()