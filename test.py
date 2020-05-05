#
# from pyautogui import typewrite
#
# print("enter folder name: ")
#
# folder = input()
# typewrite("Default Value")
# print (folder)
import win32console

_stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)

def input_def(prompt, default='Hola'):
    keys = []
    for c in unicode(default):
        evt = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
        evt.Char = c
        evt.RepeatCount = 1
        evt.KeyDown = True
        keys.append(evt)

    _stdin.WriteConsoleInput(keys)
    return raw_input(prompt)

if __name__ == '__main__':
    name = input_def('Folder name: ')
    print(name)
