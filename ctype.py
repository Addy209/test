from ctypes import WinDLL

User32 = WinDLL('User32.dll')
print(User32.GetSystemMetrics(1))