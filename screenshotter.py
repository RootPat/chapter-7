import win32gui
import win32ui
import win32con
import win32api

#grab a handle to the main desktop window 
hdesktop = win32gi.GetDesktopWindow()

#Determine the size of all monitors in pixels 
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.S_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

#create device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFFromHandle(desktop_dc)

#create a memory based device context 
mem_dc = img_dc.CreateCompatibleDC()

#create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)

#copy the screen into memory device context 
mem)dc.BitBlt((0, 0) (width, height), img_dc (left,top), win32con.SRCCOPY)

#save bitmap to file 
screenshot.SaveBitmapFile(mem_dc, '')

#free program objects 
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
