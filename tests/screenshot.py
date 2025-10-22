from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background (remove if you want to see the browser)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1280,800")

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to the page
    driver.get("https://www.saucedemo.com/")

    # Wait for JavaScript to render (you can also use WebDriverWait for specific elements)
    driver.implicitly_wait(5)

    # Take screenshot
    driver.save_screenshot("saucedemo.png")
    print("Screenshot saved as saucedemo.png")

finally:
    driver.quit()