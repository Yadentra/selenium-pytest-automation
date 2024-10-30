# Selenium PyTest Automation

This repository contains automation scripts using **Selenium** and **PyTest** to complete various testing tasks. Each script demonstrates a specific functionality, including Google search automation, user registration, and product search on a demo site.

## Prerequisites

- **Python 3.7+**
- **Selenium** for browser automation
- **PyTest** for running tests
- **WebDriver Manager** to manage ChromeDriver

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/selenium-pytest-automation.git
   cd selenium-pytest-automation

2. Install dependencies:

pip install selenium pytest webdriver-manager


3. Run the tests: Use PyTest to run each test file individually or all tests at once:

pytest test_google_search.py       # Run Google search test
pytest test_register_user.py       # Run user registration test
pytest test_search_product.py      # Run product search test



## Project Structure

- **test_google_search.py**: Automates Google search with dynamic dropdown handling.

- **test_register_user.py**: Automates user registration, account creation, and deletion on Automation Exercise.

- **test_search_product.py**: Automates product search functionality.


## Task Descriptions

- **Task 1: Google Search Automation**

Automates a Google search for a given term, handling dynamic dropdown and verifying that a new results page is opened.

- **Task 2: User Registration**

Simulates the user registration flow on automationexercise.com, including signup, account creation, and account deletion.

- **Task 3: Product Search**

Automates product search functionality on automationexercise.com, verifying that the searched products are displayed.

- **Task 4: Setup PyTest**

PyTest is installed and used as the test runner for all tasks.
