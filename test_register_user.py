# test_register_user.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_register_user():
    # Setup
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://automationexercise.com")

    # Verify home page is visible
    assert "Automation Exercise" in driver.title

    # Click 'Signup / Login'
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    # Verify 'New User Signup!' is visible
    assert "New User Signup!" in driver.page_source

    # Enter name and email address
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()

    # Verify 'ENTER ACCOUNT INFORMATION' is visible
    assert "Enter Account Information" in driver.page_source

    # Fill in required details
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.ID, "days").send_keys("1")
    driver.find_element(By.ID, "months").send_keys("January")
    driver.find_element(By.ID, "years").send_keys("2000")
    driver.find_element(By.NAME, "newsletter").click()
    driver.find_element(By.NAME, "optin").click()
    driver.find_element(By.NAME, "first_name").send_keys("Test")
    driver.find_element(By.NAME, "last_name").send_keys("User")
    driver.find_element(By.NAME, "company").send_keys("Company")
    driver.find_element(By.NAME, "address1").send_keys("123 Street")
    driver.find_element(By.NAME, "address2").send_keys("Suite 1")
    driver.find_element(By.NAME, "country").send_keys("United States")
    driver.find_element(By.NAME, "state").send_keys("CA")
    driver.find_element(By.NAME, "city").send_keys("San Francisco")
    driver.find_element(By.NAME, "zipcode").send_keys("94101")
    driver.find_element(By.NAME, "mobile_number").send_keys("1234567890")
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # Verify account created and delete
    assert "ACCOUNT CREATED!" in driver.page_source
    driver.find_element(By.XPATH, "//button[text()='Continue']").click()
    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    assert "ACCOUNT DELETED!" in driver.page_source

    # Cleanup
    driver.quit()