import platform
import random
import re
import string
import time
import webbrowser
import pyautogui

global _characters_
try:
    import pyperclip
except ImportError:
    print("pyperclip module is required. Install it with 'pip install pyperclip'")
    exit()

def get_clip_6_digit():
    try:
        clipboard_data = pyperclip.paste()
        return str(re.findall(r'(\d{6})', clipboard_data))
    except pyperclip.PyperclipException:
        return None

def get_mail():
    try:
        clipboard_data = pyperclip.paste()
        if "@dropmail.me" in clipboard_data or "@emltmp.com" in clipboard_data or "@spymail.one" in clipboard_data or "@10mail.org" in clipboard_data:
            match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', clipboard_data)
            return str(match.group(0))
        return False
    except pyperclip.PyperclipException:
        return None

# Rest of the code remains unchanged

CF_TEXT = 1

def randomize(option, length):
    if length > 0:
        if option == '-p':
            _characters_  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif option == '-s':
            _characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif option == '-l':
            _characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif option == '-n':
            _characters_ = '1234567890'
        elif option == '-m':
            _characters_ = 'JFMASOND'
        else:
            generated_info = ''
            for counter in range(0, length):
                generated_info += random.choice()
            return generated_info

        if option == '-d':
            generated_info = random.randint(1, 28)
        elif option == '-y':
            generated_info = random.randint(1950, 2000)
        else:
            return 'error'

        return str(generated_info)
    else:
        return 'error'

# Username
# Username
_username_ = randomize('-l', 8)  # Generate a random username with letters only (length 8)
pyautogui.typewrite(_username_ + '\t\t')
print("Username:" + _username_)

# Password
_password_ = randomize('-p', 12)  # Generate a random password with letters, numbers, and symbols (length 12)
pyautogui.typewrite(_password_ + '\t' + _password_ + '\t')
print("Password:" + _password_)


pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t\n')

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('t')
pyautogui.keyUp('ctrlleft')

time.sleep(10)
pyautogui.typewrite('https://dropmail.me/\n')

pyautogui.keyDown('shift')
pyautogui.keyDown('down')
pyautogui.keyUp('down')
pyautogui.keyUp('shift')
time.sleep(10)

new_mail = True
while True:
    if not new_mail:
        pyautogui.keyDown('ctrlleft')
        pyautogui.typewrite('r')
        pyautogui.keyUp('ctrlleft')
        time.sleep(5)
    pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('down')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('c')
    pyautogui.keyUp('ctrlleft')
    new_mail = get_mail()
    if new_mail:
        print("10 min mail: " + new_mail)
        break

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('\t')
pyautogui.keyUp('ctrlleft')
time.sleep(1)
pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('v')
pyautogui.keyUp('ctrlleft')
pyautogui.press('backspace')
pyautogui.typewrite('\n')

time.sleep(10)

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('\t')
pyautogui.keyUp('ctrlleft')
time.sleep(1)

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('a')
pyautogui.keyUp('ctrlleft')
pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('c')
pyautogui.keyUp('ctrlleft')

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('\t')
pyautogui.keyUp('ctrlleft')
time.sleep(5)
pyautogui.typewrite(str(get_clip_6_digit()) + '\n')

time.sleep
