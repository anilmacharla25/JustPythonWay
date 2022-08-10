
import time
import ctypes

user32 = ctypes.WinDLL('user32')
while True:
    
    print(user32.GetForegroundWindow())
    time.sleep(1)
