import time
import win32api
import win32con
import win32gui

__all__ = ['FindWindow', 'RestoreWindow', 'SetWindowPos', 'EnumChildWindows', 'LButtonClick']

FindWindow = lambda classname, title: win32gui.FindWindow(classname, title)

# 激活并显示窗口。如果窗口被最小化或最大化，
# 系统将它恢复到原来的大小和位置。应用程序在恢复最小化窗口时应该指定此标志。
RestoreWindow = lambda hwnd: win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

SetWindowPos = lambda hwnd, x, y, width, height: win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, x, y, width, height, win32con.SWP_SHOWWINDOW)

def EnumChildWindows(hwnd):
    result = {}
    def enum_proc(hwnd, lParam):
        classname = win32gui.GetClassName(hwnd)
        lParam[classname] = hwnd
        return True
    win32gui.EnumChildWindows(hwnd, enum_proc, result)
    return result

_PostMessage = lambda hwnd, msg, wParam, lParam: win32api.PostMessage(hwnd, msg, wParam, lParam)

_LButtonDown = lambda hwnd, x, y: _PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))

_LButtonUp = lambda hwnd, x, y: _PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(x, y))

def LButtonClick(hwnd, x, y):
    _LButtonDown(hwnd, x, y)
    time.sleep(0.1)
    _LButtonUp(hwnd, x, y)
