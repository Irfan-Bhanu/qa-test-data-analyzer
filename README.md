# QA Test Data Analyzer & Automation Framework
Built as part of a structured QA Automation learning journey

## Overview

This project demonstrates a structured learning journey from **Python data handling** to **Selenium-based automation framework development**.

It is divided into two parts:

* **Week 1** → Data analysis using Python
* **Week 2** → Automation framework using Selenium

---
## Week 1 — Data Analysis (Python)

### Features

* Read test results from CSV files
* Clean and process test data
* Calculate pass/fail counts and percentages
* Identify failed modules
* Generate summary reports

### Technologies Used

* Python
* CSV handling
* Basic data processing

---

## Week 2 — Automation Framework (Selenium)

### Features

* Automated login testing using multiple users
* Data-driven testing using Excel
* Add-to-cart validation (real-world scenario)
* Logging using Python logging module
* Final test report generation

---

## Real-World Value

This project simulates how QA engineers automate real-world scenarios such as:
- Login validation for multiple users
- Handling different user states (valid, locked, problematic)
- Verifying application workflows (add to cart)
- Generating execution reports

It reflects practical automation testing used in real QA environments

---
##  Test Flow

1. Read user credentials from Excel
2. Launch browser using Selenium
3. Perform login for each user
4. Validate login success/failure
5. Add product to cart (if login successful)
6. Capture results and generate final report

---

##  Sample Output

```
------ FINAL TEST REPORT ------
Total Passed: 1
Total Failed: 2

standard_user → PASS
locked_out_user → FAIL
problem_user → FAIL
```

---

## Tech Stack

* Python
* Selenium WebDriver
* Pandas
* Logging
* Excel (openpyxl)

---

##  How to Run

1. Install dependencies:

```
pip install selenium pandas openpyxl webdriver-manager
```

2. Run the framework:

```
week-2/project/framework.ipynb
```

---

##  Key Learnings

* Built a mini automation framework from scratch
* Implemented data-driven testing using Excel
* Learned Selenium automation for real-world scenarios
* Applied logging and reporting techniques
* Improved debugging and error handling skills

---

## Week 3 – Advanced Selenium

In this week, I focused on handling more complex web elements and real-world scenarios using Selenium. This helped me understand how to automate complete user workflows and validate outputs.

### Topics Covered

* Dropdown handling using Select class
* Alert handling (accept, dismiss, send_keys)
* Form automation (text fields, radio buttons, checkboxes)
* Date picker handling
* File upload using send_keys
* Handling dynamic dropdowns (State & City)
* Scrolling using JavaScript
* Basic waits for synchronization
* Form submission and result validation

---

### Key Learnings

* Learned how to handle browser alerts and popups
* Understood how to work with dynamic elements and complex UI
* Gained experience in automating complete forms
* Improved XPath skills for real-world scenarios
* Learned how to validate application output after actions

---

### Files

* Selenium Advanced.ipynb

---

### Outcome

By the end of Week 3, I am able to automate advanced user interactions and validate results, which is essential for real-world QA automation.

---

### Next Step

Moving to API Testing to expand my skills beyond UI automation.



##  Future Improvements

* Integrate PyTest framework
* Add HTML reporting
* Implement Page Object Model (POM)
* Add parallel test execution

---

## Author

**Irfan Bhanu**

---

⭐ If you found this project useful, feel free to explore and improve!
