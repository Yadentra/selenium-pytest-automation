# test_google_search.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_google_search():
    # Setup
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")

    # Verify search bar is visible
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    # Enter search term
    search_bar.send_keys("istqb")

    # Wait for suggestions and click the first suggestion
    first_suggestion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//li[@role='presentation']//span"))
    )
    first_suggestion.click()

    # Verify new page is opened
    WebDriverWait(driver, 10).until(
        EC.url_contains("search")
    )

    # Cleanup
    driver.quit()