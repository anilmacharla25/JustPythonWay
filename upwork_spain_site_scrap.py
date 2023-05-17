from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains 
import pyautogui
from pywinauto import keyboard

# Create Chrome options object
chrome_options = Options()

# Set language preference to English
chrome_options.add_argument('--lang=en')  #bihmplhobchoageeokmgbdihknkjbknd
chrome_options.add_extension(r"C:\Users\prave\Downloads\extension_4_1_0_0.crx")
time.sleep(3)
# extension_id='bihmplhobchoageeokmgbdihknkjbknd'
# chrome_options.add_extension(extension_id)
# Instantiate the Chrome driver with options
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=chrome_options)

time.sleep(5)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.maximize_window()
time.sleep(10)
pyautogui.click(1773,70)
time.sleep(2)
[keyboard.send_keys('{TAB}') for i in range(2)]
time.sleep(2)
keyboard.send_keys('{ENTER}')
time.sleep(2)
pyautogui.click(x=1542, y=351)
time.sleep(1)
# pyautogui.click(x=1542, y=351)
pyautogui.click(x=1468, y=370)
time.sleep(2)
pyautogui.click(x=1514, y=455)
time.sleep(10)


driver.get('https://www.milanuncios.com/')
time.sleep(5)
print(driver.current_url)

time.sleep(300)
