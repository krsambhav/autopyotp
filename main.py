import pyotp
import pyperclip
from pynput import mouse
from pynput import keyboard
import pyautogui

def on_click(x,y, button, pressed):
  skey = pyperclip.paste()
  totp = pyotp.TOTP(skey)
  if button == mouse.Button.middle and pressed:
    pyautogui.write(totp.now())
    print(skey, totp.now())

def on_press(key):
  skey = pyperclip.paste()
  totp = pyotp.TOTP(skey)
  if key == keyboard.Key.right:
    pyautogui.write(totp.now())
    print(skey, totp.now())

listener = mouse.Listener(on_click=on_click)
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()