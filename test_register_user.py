# register_user.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def register_user():
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Step 1: Launch browser
        driver.get("http://automationexercise.com")
        driver.maximize_window()  # Maximize the window for better visibility

        # Step 2: Verify that home page is visible
        assert "Automation Exercise" in driver.title, "Home page is not visible"
        print("Home page is visible.")

        # Step 3: Click on 'Signup / Login' button
        driver.find_element(By.LINK_TEXT, "Signup / Login").click()

        # Step 4: Verify 'New User Signup!' is visible
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']"))
        ), "'New User Signup!' is not visible"
        print("New User Signup is visible.")

        # Step 5: Enter name and email address
        driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys("Test User")
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("testuser@example.com")

        # Step 6: Click 'Signup' button
        driver.find_element(By.XPATH, "//button[text()='Signup']").click()

        # Step 7: Verify that 'ENTER ACCOUNT INFORMATION' is visible
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Enter Account Information']"))
        ), "'ENTER ACCOUNT INFORMATION' is not visible"
        print("Enter Account Information is visible.")

        # Step 8: Fill details
        driver.find_element(By.ID, "id_gender1").click()  # Select title
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "days").send_keys("1")
        driver.find_element(By.ID, "months").send_keys("January")
        driver.find_element(By.ID, "years").send_keys("2000")

        # Step 9: Select checkboxes
        driver.find_element(By.ID, "newsletter").click()
        driver.find_element(By.ID, "optin").click()

        # Step 10: Fill more details
        driver.find_element(By.ID, "first_name").send_keys("First")
        driver.find_element(By.ID, "last_name").send_keys("Last")
        driver.find_element(By.ID, "address1").send_keys("123 Street")
        driver.find_element(By.ID, "country").send_keys("United States")
        driver.find_element(By.ID, "state").send_keys("State")
        driver.find_element(By.ID, "city").send_keys("City")
        driver.find_element(By.ID, "zipcode").send_keys("12345")
        driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

        # Step 11: Click 'Create Account' button
        driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

        # Step 12: Verify that 'ACCOUNT CREATED!' is visible
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='ACCOUNT CREATED!']"))
        ), "'ACCOUNT CREATED!' is not visible"
        print("Account Created is visible.")

        # Step 13: Click 'Continue' button
        driver.find_element(By.XPATH, "//a[text()='Continue']").click()

        # Step 14: Verify that 'Logged in as username' is visible
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
        ), "'Logged in as username' is not visible"
        print("Logged in as username is visible.")

        # Step 15: Click 'Delete Account' button
        driver.find_element(By.LINK_TEXT, "Delete Account").click()

        # Step 16: Verify that 'ACCOUNT DELETED!' is visible
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='ACCOUNT DELETED!']"))
        ), "'ACCOUNT DELETED!' is not visible"
        print("Account Deleted is visible.")

        # Step 17: Click 'Continue' button
        driver.find_element(By.XPATH, "//a[text()='Continue']").click()

    finally:
        # Wait for a few seconds before closing the browser
        print("Test completed. Closing browser in 5 seconds...")
        time.sleep(5)  
        driver.quit()

if __name__ == "__main__":
    register_user()
