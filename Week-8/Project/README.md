This projects contains a hybrid framework structure: 
Hybrid Framework = POM + Data-Driven + PyTest + Utility-Based Design

**_Folder Structure_**
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

**Data Driven Framework**:
Config
-----> config.ini - base_url and browser=chrome
-----> config_reader.py --reads config dynamically

**Pytest framework**:
conftest.py --> fixtures(setup/teardown),driver lifecycle

reports - collects output

**Flow:**
pytest starts
   ↓
find test_basic_auth
   ↓
see "driver" → call fixture
   ↓
get_driver()
   ↓
get_browser() → config.ini
   ↓
Chrome launches
   ↓
yield driver → test starts
   ↓
LoginPage(driver)
   ↓
BasePage init → WaitUtils init
   ↓
test calls method → driver.get()
   ↓
assertion happens
   ↓
test ends
   ↓
fixture resumes → driver.quit()

**Day Wise Execution**

Day 1- created structure on Day 1 and executed a simple login case
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

**project Structure**

<img width="316" height="535" alt="image" src="https://github.com/user-attachments/assets/0ccdefa9-eecc-4945-b012-f91865840e94" />
******************************************

**Failed test case screenshot**
<img width="1549" height="786" alt="image" src="https://github.com/user-attachments/assets/b55bdbe1-a5b5-4d74-8e38-7f835f220123" />

****************************************
**Passed case**
<img width="1673" height="887" alt="image" src="https://github.com/user-attachments/assets/30fc9acb-0152-4467-bdee-151ab23011b6" />






