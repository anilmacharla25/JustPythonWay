from pywinauto.application import Application
import win32api
import pywinauto
from pywinauto import keyboard
from pywinauto import timings
import time
from pywinauto.keyboard import SendKeys
app = Application().Start(cmd_line=u'"C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_10.2102.13.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe" ')
notepad = app.Notepad
notepad.Wait('ready')
time.sleep(2)
notepad.maximize()
# notepad.MenuItem(u'&Help').click_input()

notepad[u'Edit'].type_keys("help")
notepad.MenuItem(u'&File->&Save\tCtrl+S').click_input()

app = Application().Connect(title=u'Save As', class_name='#32770')
saveas=app.SaveAs
app.SaveAs.print_control_identifiers()
app.SaveAs.child_window(class_name="Edit").type_keys("help")
app.SaveAs.child_window(title="&Save", class_name="Button").click_input()
