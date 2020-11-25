"""
主体代码引自 Demon_Hunter 的CSDN博客, 博客URL:https://blog.csdn.net/zhuisui_woxin/article/details/84345036
"""

import win32gui
import win32ui
import win32con
import win32api
import cv2
import numpy
import time


def get_state():
    # 第一个参数是类名，第二个参数是窗口名字
    hwnd = win32gui.FindWindow(None, "炉石传说")
    if hwnd == 0:
        return "wtf"
    width = 1960
    height = 1080
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框 DC device context
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    signedIntsArray = saveBitMap.GetBitmapBits(True)

    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im_opencv.shape = (height, width, 4)

    # if im_opencv[860][960][0] == im_opencv[860][960][1] == im_opencv[860][960][2]:
    #     return "choose"
    # if list(im_opencv[400][200]) == [60, 25, 9, 255]:
    #     if list(im_opencv[495][1505]) == [108, 185, 149, 255]:
    #         return "goon"
    #     elif list(im_opencv[495][1505]) == [133, 188, 107, 255]:
    #         return "end"
    #     else:
    #         return "their"
    # elif im_opencv[400][200][0] < 30:
    #     return "start"
    # else:
    #     return "?"

    # print(im_opencv[495][1515])
    # print(im_opencv[495][1505])
    if list(im_opencv[1070][1090]) == [8, 18, 24, 255]:
        return "ChoosingHero"
    if list(im_opencv[1070][1090]) == [17, 18, 19, 255]:
        return "Matching"
    if list(im_opencv[860][960]) == [71, 71, 71, 255]:
        return "ChoosingCard"
    temp_sum = numpy.sum(im_opencv[495][1515][:3])
    if temp_sum < 100:
        return "NotMine"
    elif temp_sum > 370:
        return "MyTurn"
    else:
        return "Uncertain"
