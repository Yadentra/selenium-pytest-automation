from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to Google
        driver.get("https://www.google.com")

        # Wait for the search bar to be visible
        search_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )

        # Verify that the search bar is visible
        assert search_bar.is_displayed(), "Search bar is not visible"

        # Enter the search term
        search_term = "istqb"
        search_bar.send_keys(search_term)

        # Press Enter to perform the search
        search_bar.submit()

        # Wait for the results page to load and check that the title contains the search term
        WebDriverWait(driver, 10).until(
            EC.title_contains(search_term)
        )
        assert search_term in driver.title, "Results page did not contain the expected search term in the title"

        # Wait for 05 seconds
        time.sleep(05)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()
