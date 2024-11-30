from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_search_product():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://automationexercise.com")
        driver.maximize_window()

        assert "Automation Exercise" in driver.title, "Home page is not visible"
        print("Home page is visible successfully.")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Products"))
        ).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='All Products']"))
        ), "Not navigated to ALL PRODUCTS page"
        print("Navigated to ALL PRODUCTS page successfully.")

        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search_product"))
        )
        search_input.send_keys("T-shirt")
        driver.find_element(By.ID, "submit_search").click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
        ), "'SEARCHED PRODUCTS' is not visible"
        print("'SEARCHED PRODUCTS' is visible.")

        products_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "productinfo"))
        )
        assert len(products_list) > 0, "No products related to the search are visible"
        print(f"Related products are visible. Found {len(products_list)} product(s).")

    finally:
        print("Test completed. Closing browser in 5 seconds...")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_search_product()
