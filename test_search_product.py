# test_search_product.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_search_product():
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Step 1: Launch browser
        driver.get("http://automationexercise.com")
        driver.maximize_window()  # Maximize the window for better visibility

        # Step 2: Verify that home page is visible successfully
        assert "Automation Exercise" in driver.title, "Home page is not visible"
        print("Home page is visible successfully.")

        # Step 3: Click on 'Products' button
        products_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Products"))
        )
        products_button.click()

        # Step 4: Verify user is navigated to ALL PRODUCTS page successfully
        assert "All Products" in driver.title, "Not navigated to ALL PRODUCTS page"
        print("Navigated to ALL PRODUCTS page successfully.")

        # Step 5: Enter product name in search input and click search button
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search_product"))
        )
        search_input.send_keys("T-shirt")  # Enter product name
        search_button = driver.find_element(By.ID, "submit_search")
        search_button.click()

        # Step 6: Verify 'SEARCHED PRODUCTS' is visible
        assert "SEARCHED PRODUCTS" in driver.page_source, "'SEARCHED PRODUCTS' is not visible"
        print("'SEARCHED PRODUCTS' is visible.")

        # Step 7: Verify all the products related to the search are visible
        products_list = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "product"))
        )
        assert len(products_list) > 0, "No products related to the search are visible"
        print("Related products are visible.")

    finally:
        # Wait for 10 minutes before closing the browser
        print("Test completed. Closing in 10 minutes...")
        time.sleep(600)  # Wait for 10 minutes (600 seconds)
        driver.quit()

if __name__ == "__main__":
    test_search_product()
