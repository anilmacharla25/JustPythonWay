import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_handling_jquey_datepicker():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get('LT_USERNAME');
    lt_options["accessKey"] = os.environ.get('LT_ACCESS_KEY');
    lt_options["build"] = "Handling Date Pickers";
    lt_options["project"] = "Handling Date Pickers";
    lt_options["name"] = "Handling Date Pickers";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options)
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    # Handling JQuery DatePicker
    driver.get('https://www.lambdatest.com/selenium-playground/jquery-date-picker-demo')
   
    # expected dates to be selected
    from_date_target = '05/10/2023'
    to_date_target = '06/25/2023'

    from_date = '10'
    to_date  = '25'
   
   
    # From date
    # clicking on the from_date picker
    from_date_picker = driver.find_element(By.XPATH, "//input[@id='from']")
    from_date_picker.click()

    from_month = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")
    # We use the Select() method to select the target month we want
    from_month_selected = Select(from_month)
    from_month_selected.select_by_visible_text('M
