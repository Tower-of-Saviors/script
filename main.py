import time

import win32con

import win32api
import win32gui
import win32ui

hWnd = win32gui.FindWindow(None, "夜神模擬器")


def click(x, y):
    lParam = win32api.MAKELONG(x, y)
    win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN,
                         win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, 0, lParam)


click(79, 337)


def screen_grab():
    rect = win32gui.GetWindowRect(hWnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    hWinDC = win32gui.GetWindowDC(hWnd)
    srcDC = win32ui.CreateDCFromHandle(hWinDC)
    memDC = srcDC.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcDC, width, height)
    memDC.SelectObject(bmp)
    memDC.BitBlt((0, 0), (width, height), srcDC, (0, 0), win32con.SRCCOPY)
    bmp.SaveBitmapFile(memDC, 'screenshot.bmp')


def get_pixel(x, y):
    hWinDC = win32gui.GetWindowDC(hWnd)
    long_colour = win32gui.GetPixel(hWinDC, x, y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def get_hex_value(rgb):
    if len(rgb) == 3:
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        r = str(hex(r)).replace('0x', '')
        g = str(hex(g)).replace('0x', '')
        b = str(hex(b)).replace('0x', '')
        hexValue = '#' + r + g + b
        return hexValue
    else:
        print('wrong rgb input')


print(get_hex_value(get_pixel(79, 123)))


screen_grab()
