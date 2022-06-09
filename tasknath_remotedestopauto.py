from pywinauto.application import Application
import win32api
import pywinauto
from pywinauto import keyboard
from pywinauto import timings
import time
from pywinauto.keyboard import SendKeys
import pyautogui
from PIL import Image
import cv2


app = Application().Start(cmd_line=u'"C:\Windows\system32\mstsc.exe" ')
keyboard.SendKeys('10.200.80.115')
#app.RemoteDesktopConnection.print_control_identifiers()
connect=app.RemoteDesktopConnection.child_window(title="Co&nnect", class_name="Button").wrapper_object()
connect.click_input()
time.sleep(10)
#app.RemoteDesktopConnection.print_control_identifiers()
#keyboard.SendKeys('Secure@2022')
pyautogui.press("down")

time.sleep(1)


keyboard.SendKeys('mquery')
#app.RemoteDesktopConnection.print_control_identifiers()

pyautogui.press("down")
time.sleep(1)
pwd=pyautogui.password('Enter password (text will be hidden)')
time.sleep(5)
keyboard.SendKeys(pwd)
pyautogui.press('enter')
time.sleep(4)
pyautogui.press('left')
time.sleep(4)
pyautogui.press('enter')
time.sleep(35)

coord=pyautogui.locateOnScreen("Okbutton.png",grayscale=True,confidence =.5)
x,y= pyautogui.center(coord)
time.sleep(2)
pyautogui.moveTo(x,y,5)
pyautogui.click()
time.sleep(20)
pyautogui.press("win")
print("done")
closebutton=pyautogui.locateOnScreen("microsoftteams.png",grayscale=True,confidence =.5)
x,y= pyautogui.center(closebutton)
time.sleep(2)
pyautogui.moveTo(x,y,5)
pyautogui.click()
ibmtool=pyautogui.locateOnScreen("ibmtool.png",grayscale=True,confidence =.5)
x,y= pyautogui.center(ibmtool)
time.sleep(2)
pyautogui.moveTo(x,y,5)
pyautogui.click(clicks=2, interval=0.25)
time.sleep(2)






