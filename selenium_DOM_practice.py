from selenium import webdriver
import time

# Use webdriver manager to automatically download and install the chromedriver executable
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://sandbox-sponsors.pointsville.com/")

time.sleep(5)

# Using JavaScriptExecutor to interact with Shadow DOM elements
js = "return document.querySelector('amplify-authenticator > amplify-sign-in').shadowRoot.querySelector('amplify-form-section > amplify-auth-fields').shadowRoot.querySelector('div > amplify-username-field').shadowRoot.querySelector('amplify-form-field').shadowRoot.querySelector('input')"
username = driver.execute_script(js)

js = "return document.querySelector(\"amplify-authenticator > amplify-sign-in\").shadowRoot.querySelector(\"amplify-form-section > amplify-auth-fields\").shadowRoot.querySelector(\"div > amplify-password-field\").shadowRoot.querySelector(\"amplify-form-field\").shadowRoot.querySelector(\"#password\")"
password = driver.execute_script(js)

js = "return document.querySelector(\"amplify-authenticator > amplify-sign-in\").shadowRoot.querySelector(\"amplify-form-section > amplify-auth-fields\").shadowRoot.querySelector(\"div > amplify-password-field\").shadowRoot.querySelector(\"amplify-form-field\").shadowRoot.querySelector(\"#password-hint > div > amplify-button\")"
resetPwdLink = driver.execute_script(js)

js = "arguments[0].setAttribute('value', 'NaveenAutomationLabs')"
driver.execute_script(js, username)
driver.execute_script(js, password)

driver.execute_script("arguments[0].click();", resetPwdLink)
