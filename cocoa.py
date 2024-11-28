from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keybord=Controller()
import time

time.sleep(10)    
print("programm startet")




keybord.press(" ")

for i in range (31):
    keybord.press("w")
    time.sleep (15)
    keybord.release("w")
    time.sleep (0.5)

    keybord.press("d")
    time.sleep (0.5)
    keybord.release("d")
    time.sleep (0.5)

    keybord.press("s")
    time.sleep (15)
    keybord.release("s")
    time.sleep (0.5)

    keybord.press("d")
    time.sleep (1)
    keybord.release("d")
    time.sleep (0.5)
    

for i in range (31):
    keybord.press("w")
    time.sleep (15)
    keybord.release("w")
    time.sleep (0.5)

    keybord.press("a")
    time.sleep (0.5)
    keybord.release("a")
    time.sleep (0.5)

    keybord.press("s")
    time.sleep (15)
    keybord.release("s")
    time.sleep (0.5)

    keybord.press("a")
    time.sleep (1)
    keybord.release("a")
    time.sleep (0.5)


keybord.press("g")
keybord.release("g")

keybord.release(" ")