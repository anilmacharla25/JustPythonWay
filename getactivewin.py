from win32gui import GetWindowText, GetForegroundWindow
import time
for i in range(50):
    print(GetWindowText(GetForegroundWindow()))
    time.sleep(5)
