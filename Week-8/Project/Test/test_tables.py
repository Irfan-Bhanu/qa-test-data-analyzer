from pages.tables import table

def test_tables(driver):
    driver.get("https://the-internet.herokuapp.com/tables")

    page= table(driver)

    row_count=page.get_row_count()
    print("Rows:",row_count)

    assert (row_count > 0)

    data=page.get_row_data(2)
    print(data)