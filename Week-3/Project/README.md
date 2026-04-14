## Week 3 – Advanced Selenium Automation

This week focuses on mastering advanced Selenium concepts used in real-world QA automation. The goal is to handle dynamic web elements, complex user interactions, and validate application behavior effectively.

---

##  Topics Covered

###  1. Dropdown Handling

* Used Selenium's `Select` class to interact with dropdown elements
* Performed selection using:

  * `select_by_visible_text()`
  * `select_by_value()`
  * `select_by_index()`

---

###  2. Alert Handling

Handled different types of browser alerts:

* **Simple Alert** → `accept()`
* **Confirmation Alert** → `accept()` / `dismiss()`
* **Prompt Alert** → `send_keys()` + `accept()`

✔ Also validated alert messages using:

```python
alert.text
```

---

###  3. Form Automation (Real-World Scenario)

Automated a complete user form including:

####  Text Fields

* First Name, Last Name, Email, Mobile Number using `send_keys()`

####  Radio Buttons

* Selected gender using XPath and click action

####  Checkboxes

* Selected hobbies dynamically

####  Date Picker

* Handled calendar widget by:

  * Selecting month and year
  * Clicking specific date

####  File Upload

* Uploaded image using:

```python
send_keys(file_path)
```

####  Dynamic Dropdowns (Advanced)

* Handled React-based dropdowns (State & City)
* Used XPath with visible text selection

---

### 4. Scrolling & Element Visibility

* Used JavaScript Executor to scroll:

```python
driver.execute_script("arguments[0].scrollIntoView();", element)
```

---

###  5. Waits (Basic Introduction)

* Used `time.sleep()` for synchronization
* Learned importance of **Explicit Waits** for real-world stability

---

###  6. Form Submission & Validation

* Submitted the form successfully
* Captured confirmation popup message
* Extracted and printed table data for validation:

```python
rows = driver.find_elements(By.XPATH, "//table//tr")
for row in rows:
    print(row.text)
```
---

##  Key Learnings

* Handling dynamic and complex UI elements
* Understanding DOM structure for better XPath creation
* Working with alerts and popups
* Automating real-world forms end-to-end
* Performing validation after actions (important for QA)
  
---

##  Outcome

By the end of Week 3:

* Able to automate complex user interactions
* Confident in handling real-world web applications
* Strong understanding of Selenium advanced features

---

##  Next Step

➡ Moving to **API Testing** to enhance backend validation skills and become a complete QA engineer.
