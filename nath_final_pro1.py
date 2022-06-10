import pyautogui
import pywinauto
from pywinauto import keyboard
import win32api
import cv2
from PIL import Image

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
import re


path="C:\\Users\\AMacharla\\Desktop\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("site address")
driver.maximize_window()
time.sleep(1)
user=driver.find_element(By.XPATH, '//*[@id="doctorID"]')
time.sleep(3)
user.send_keys("rkumar11")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("password")
pyautogui.press("enter")
time.sleep(10)
try:
    time.sleep(5)
except:
    time.sleep(10)
try:
    time.sleep(2)
    keyboard.send_keys('{ENTER}')
except:
    pass

time.sleep(3)
driver.implicitly_wait(10)


time.sleep(5)
icon=pyautogui.locateOnScreen("icon.png",grayscale=False,confidence =.5)
time.sleep(1)
print(icon)
x,y= pyautogui.center(icon)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
time.sleep(1)
driver.implicitly_wait(10)

star=pyautogui.locateOnScreen("star1.png",grayscale=False,confidence =.5)
time.sleep(1)
print(star)
x,y= pyautogui.center(star)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
driver.implicitly_wait(10)

report=pyautogui.locateOnScreen("eboreport.png",grayscale=False,confidence =.5)
time.sleep(1)
print(report)
x,y= pyautogui.center(report)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
driver.implicitly_wait(10)
time.sleep(5)
keyboard.send_keys('{F11}')
time.sleep(9)


lense=pyautogui.locateOnScreen("lense.png",grayscale=False,confidence =.5)
time.sleep(1)
print(lense)
x,y= pyautogui.center(lense)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
time.sleep(3)
keyboard.send_keys('with note',with_spaces=True)
#pyautogui.write("with note")
keyboard.send_keys('{ENTER}')
time.sleep(5)

driver.implicitly_wait(10)
filter1=pyautogui.locateOnScreen("filter4.png",grayscale=False,confidence =.5)
time.sleep(1)
print(filter1)
x,y= pyautogui.center(filter1)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
driver.implicitly_wait(10)

time.sleep(3)
html=pyautogui.locateOnScreen("html.png",grayscale=True,confidence =.5)
time.sleep(1)
print(html)
x,y= pyautogui.center(html)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
time.sleep(2)

for i in range(5):
    time.sleep(0.01)
    keyboard.send_keys('{DOWN}')
time.sleep(2)
keyboard.send_keys('{ENTER}')
time.sleep(3)

driver.implicitly_wait(10)
prompt=pyautogui.locateOnScreen("prompt.png",grayscale=True,confidence =.5)
time.sleep(1)
print(prompt)
x,y= pyautogui.center(prompt)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
time.sleep(3)

run=pyautogui.locateOnScreen("run.png",grayscale=True,confidence =.5)
time.sleep(1)
print(run)
x,y= pyautogui.center(run)
#pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)

time.sleep(8)
reportimg=pyautogui.locateOnScreen("reportimg3.png",grayscale=True,confidence =.5)
time.sleep(1)
print(reportimg)
x,y= pyautogui.center(reportimg)
pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.move(0,28,0.01)

time.sleep(2)
#pyautogui.move(70,0,0.01)
time.sleep(1)
x,y=pyautogui.position()
print("our date position")
pyautogui.click(x,y)
#pywinauto.mouse.click(button='left', coords=(0, 0))
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.press('delete')
time.sleep(1)
pyautogui.write("Jun 1, 2022")
#pyautogui.click(x,y)
time.sleep(4)

ok1=pyautogui.locateOnScreen("ok2.png",grayscale=True,confidence =.5)
time.sleep(1)
print(ok1)
x,y= pyautogui.center(ok1)
pyautogui.moveTo(x,y,0.01)
print(x,y)
time.sleep(2)
pyautogui.click(x,y)
time.sleep(120)
pyautogui.hotkey('ctrl', 'f4')
time.sleep(1)
driver.quit()
print("bot successfully downloaded csv file")


















