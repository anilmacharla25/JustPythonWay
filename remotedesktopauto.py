from pywinauto.application import Application
import win32api
import pywinauto
from pywinauto import keyboard
from pywinauto import timings
import time
from pywinauto.keyboard import SendKeys


app = Application().Start(cmd_line=u'"C:\Windows\system32\mstsc.exe" ')

pywinauto.mouse.move(coords=(1025, 430))
pywinauto.mouse.click(button='left', coords=(1025, 430))
pywinauto.mouse.move(coords=(900, 280))
pywinauto.mouse.click(button='left', coords=(900,280))
time.sleep(1)
keyboard.SendKeys('test123')
app.RemoteDesktopConnection.print_control_identifiers()
connect=app.RemoteDesktopConnection.child_window(title="Co&nnect", class_name="Button").wrapper_object()
connect.click()
