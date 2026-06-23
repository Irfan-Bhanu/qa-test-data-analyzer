# Data-Driven Selenium Automation Framework

A Selenium-Python automation framework built using the Page Object Model (POM) design pattern and Pytest. The framework supports reusable page objects, configuration management, explicit waits, HTML reporting, screenshot capture on failure, parallel execution, and data-driven testing using CSV, JSON, and Excel files.

## Project Objective

To build a scalable Selenium-Python automation framework using industry-standard design patterns including Page Object Model (POM), Data-Driven Testing, Pytest, Reporting, Logging, and Framework Utilities.

The framework demonstrates real-world automation capabilities and serves as the foundation for future API Testing and AI-driven QA initiatives.


This projects contains a hybrid framework structure: 
Hybrid Framework = POM + Data-Driven + PyTest + Utility-Based Design

## Advanced Selenium Framework Features

✔ Window Handling

✔ ActionChains (Hover, Right Click, Double Click, Drag & Drop)

✔ JavaScript Executor

✔ Logging Framework

✔ Retry Mechanism

✔ Custom Markers

✔ Data-Driven Testing

✔ Parallel Execution

✔ HTML Reporting & Screenshots


## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* OpenPyXL
* ConfigParser
* Pytest-HTML
* Pytest-XDist

## Implemented Features

### Framework

✔ Page Object Model (POM)
✔ BasePage Design
✔ Driver Factory
✔ Config Reader
✔ Pytest Fixtures

### Selenium

✔ Login Automation
✔ Alerts
✔ Dynamic Controls
✔ Tables
✔ Checkboxes
✔ File Upload
✔ Frames / iFrames
✔ Dropdowns
✔ Advanced XPath

### Reporting

✔ HTML Reports
✔ Screenshots on Failure

### Data Driven Testing

✔ CSV Integration
✔ JSON Integration
✔ Excel Integration
✔ pytest.parametrize

### Execution

✔ Parallel Execution using pytest-xdist

## Folder Structure
**PyTest framework:**
tests/-->test_login.py - This contains test cases and it is entry point for execution

**Page Object Model(POM)**:
Pages
-->Basepage.py - It contains common reusable actions like click,type,find
-->login_page.py - represents one page. contains locators and actions of login_page
-->Dynamic_page.py - contains locators for dynamic page


**FrameWork core(Custom utility layer)**:
utils
----> driver_factory.py - browser setup and driver creation
----> waits_utils.py - wait for elements and wait for clickable


**Configuration Management**
-----> config.ini - base_url and browser=chrome
-----> config_reader.py --reads config dynamically

**Pytest framework**:
conftest.py --> fixtures(setup/teardown),driver lifecycle

reports - stores HTML execution reports

## Folder Structure

```text
Project
│
├── tests/
│   ├── test_login.py
│   ├── test_tables.py
│   └── test_dynamic_controls.py
│
├── pages/
│   ├── BasePage.py
│   ├── login_page.py
│   └── dynamic_page.py
│
├── utils/
│   ├── driver_factory.py
│   ├── waits_utils.py
│   └── data_reader.py
│
├── config/
│   ├── config.ini
│   └── config_reader.py
│
├── testdata/
│   ├── login_data.csv
│   ├── login_data.json
│   └── login_data.xlsx
│
├── reports/
├── screenshots/
└── conftest.py
```


## Framework Execution Flow
Test Case
↓
Pytest Fixture
↓
Driver Factory
↓
Config Reader
↓
Browser Launch
↓
Page Object
↓
BasePage Methods
↓
Wait Utilities
↓
Element Interaction
↓
Assertion
↓
Report & Screenshot
↓
Driver Quit


## Development execution timeline

Day 1:
✔ Created framework folder structure
✔ Implemented browser launch
✔ Executed first login automation test
✔ Established Page Object Model foundation
**************************************
Day 2- I implemented Page Object Model with fixtures and explicit waits to build a stable and maintainable automation framework.
*****************************************

Day 3:
✔upgraded conftest.py to save screenshot. use hookimpl fixtures to save screenshot.
✔created dynamic_page.py and test_dynamic control for better structures
✔created html report using installing pip install pytest -html and pytest --html=reports/report.html
✔done parallel execution by installing pip install pytest -xdist and execute pytest -n 2 which will help to run each test in different window at same time

*******************************************

Day 4 : 
✔Handling alerts
✔Handling iframes
✔Handle dropdown
✔Integrating them in framework

**************************************

Day 5:
✔ Handle tables
✔ Handle checkboxes
✔ Upload files
✔ Learn advanced XPath
✔ Learn dynamic XPath
✔ Traverse elements

***************************************
Day 6:
✔pytest parameterize
✔Read data from CSV
✔Read data from json
✔Read data from excel - pip install openpyxl
✔Connect Excel/CSV data to Login Framework
****************************************
## Day 7 - Windows & Tabs Handling

### Concepts Covered

✔ Multiple Browser Windows
✔ Window Handles
✔ Switching Between Windows
✔ Parent and Child Windows
✔ driver.close() vs driver.quit()

### Implementation

* Opened new browser windows using Selenium
* Captured window handles using `driver.window_handles`
* Switched between parent and child windows
* Closed specific windows and returned to parent window
* Implemented window handling inside the Page Object Model framework

### Key Learning

Understanding window handles is essential when testing applications that open new tabs, payment gateways, authentication pages, or external links.

********************************************

## Day 8 - Advanced User Interactions (ActionChains)

### Concepts Covered

✔ Hover Actions
✔ Right Click (Context Click)
✔ Double Click
✔ Drag and Drop
✔ Keyboard Actions

### Implementation

* Used ActionChains to simulate real user interactions
* Hovered over hidden elements and validated dynamic content
* Performed right-click actions and handled resulting alerts
* Executed double-click actions and validated success messages
* Implemented drag-and-drop functionality
* Learned keyboard shortcuts using ActionChains

### Key Learning

ActionChains allows Selenium to simulate complex user interactions beyond simple clicks and text entry.

*************************************************

## Day 9 - Scrolling & JavaScript Executor

### Concepts Covered

✔ Scroll Down
✔ Scroll Up
✔ Scroll To Element
✔ JavaScript Click

### Implementation

* Added reusable scrolling methods to BasePage
* Implemented JavaScript Executor utility methods
* Performed scrolling to dynamic page sections
* Used JavaScript click when Selenium click was unreliable

### Key Learning

JavaScript Executor is a powerful fallback mechanism when standard Selenium actions fail due to overlays, animations, or hidden elements.

*********************************************

## Day 10 - Framework Enhancements

### Concepts Covered

✔ Logging
✔ Retry Mechanism
✔ Custom Markers

### Implementation

* Added logging framework using Python logging module
* Implemented INFO, WARNING and ERROR level logs
* Configured pytest-rerunfailures for flaky test retries
* Added custom markers for selective execution
* Executed tests using marker-based filtering

### Key Learning

Framework-level enhancements improve maintainability, debugging, execution efficiency, and scalability of automation projects.

---

## Screenshots

**project Structure**

<img width="316" height="535" alt="image" src="https://github.com/user-attachments/assets/0ccdefa9-eecc-4945-b012-f91865840e94" />
******************************************

**Failed test case screenshot**
<img width="1549" height="786" alt="image" src="https://github.com/user-attachments/assets/b55bdbe1-a5b5-4d74-8e38-7f835f220123" />

****************************************
**Passed case**
<img width="1673" height="887" alt="image" src="https://github.com/user-attachments/assets/30fc9acb-0152-4467-bdee-151ab23011b6" />


## Future Enhancements

* API Testing Framework using Requests
* Cross-Browser Execution
* Jenkins CI/CD Integration
* Docker Integration
* Selenium Grid
* GitHub Actions
* AI-Powered Test Analytics

## Final Selenium Framework Capabilities

### Framework Design

✔ Page Object Model (POM)
✔ BasePage Design
✔ Driver Factory
✔ Config Reader
✔ Utility Layer
✔ Reusable Framework Architecture

### Selenium Features

✔ Alerts
✔ Frames / iFrames
✔ Windows & Tabs
✔ Dynamic Controls
✔ Dropdowns
✔ Tables
✔ Checkboxes
✔ File Upload
✔ Advanced XPath

### ActionChains

✔ Hover
✔ Right Click
✔ Double Click
✔ Drag & Drop
✔ Keyboard Actions

### JavaScript Executor

✔ Scroll Down
✔ Scroll Up
✔ Scroll To Element
✔ JavaScript Click

### Reporting & Execution

✔ HTML Reports
✔ Screenshots on Failure
✔ Logging
✔ Parallel Execution
✔ Retry Mechanism
✔ Custom Markers

### Data Driven Testing

✔ CSV Integration
✔ JSON Integration
✔ Excel Integration
✔ Pytest Parametrize


