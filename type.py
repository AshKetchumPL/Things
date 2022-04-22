import pyautogui

def click(file):
    file = pyautogui.locateOnScreen(f'imgs/{file}')
    try: filepoint = pyautogui.center(file)
    except TypeError: return False
    filex, filey = filepoint
    pyautogui.click(filex, filey)
    return True

def type(msg, interval=0.09, *args, **kwargs): 
    pyautogui.write(msg, interval=interval, *args, **kwargs)
    pyautogui.press('return')
