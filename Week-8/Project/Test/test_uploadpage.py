from pages.upload_page import upload_page


def test_uploadpage(driver):
    pages=upload_page(driver)

    driver.get("https://the-internet.herokuapp.com/upload")

    filepath = (r"C:\Users\bhanu\Downloads\login_data_excel.xlsx")

    pages.choose_file_upload(filepath)
    pages.upload_file_upload()

    assert "File Uploaded!" in driver.page_source


