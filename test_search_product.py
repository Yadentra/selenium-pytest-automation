# test_search_product.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_search_product():
    # Setup
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://automationexercise.com")

    # Verify home page is visible
    assert "Automation Exercise" in driver.title

    # Click on 'Products' and verify navigation
    driver.find_element(By.LINK_TEXT, "Products").click()
    assert "All Products" in driver.page_source

    # Enter product name in search and verify results
    driver.find_element(By.ID, "search_product").send_keys("T-shirt")
    driver.find_element(By.ID, "submit_search").click()
    assert "SEARCHED PRODUCTS" in driver.page_source

    # Cleanup
    driver.quit()