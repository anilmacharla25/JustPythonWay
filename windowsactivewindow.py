import win32gui
import time
w=win32gui
while True:
    text=w.GetWindowText (w.GetForegroundWindow())
    print(text)
    time.sleep(2)
