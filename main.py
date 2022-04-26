import pyotp
import pyperclip
from pynput import mouse
import pyautogui

def on_click(x,y, button, pressed):
  skey = pyperclip.paste()
  totp = pyotp.TOTP(skey)
  print(button)
  if button == mouse.Button.middle and pressed:
    pyautogui.write(totp.now())
    print(skey, totp.now())

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()