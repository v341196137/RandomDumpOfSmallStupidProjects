import pyautogui, time
time.sleep(5) # some time to get to the tab
pyautogui.scroll(-100000) # scrolling is functional
coords = pyautogui.locateCenterOnScreen('likebtn.png')
print(coords)
pyautogui.click(coords)