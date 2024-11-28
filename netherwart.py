from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keybord=Controller()
import time

time.sleep(10)    
print("programm startet")




keybord.press(" ")

for i in range (9):

        keybord.press("d")
        time.sleep (19.5)
        keybord.release("d")
        time.sleep (0.5)

        keybord.press("w")
        time.sleep (1.2)
        keybord.release("w")
        time.sleep (0.5)

        keybord.press("a")
        time.sleep (19.5)
        keybord.release("a")
        time.sleep (0.5)

        keybord.press("w")
        time.sleep (1.2)
        keybord.release("w")
        time.sleep (0.5)
    

keybord.press("d")
time.sleep (19.5)
keybord.release("d")
time.sleep (0.5)


for i in range (9):
        keybord.press("a")
        time.sleep (19.5)
        keybord.release("a")
        time.sleep (0.5)

        keybord.press("s")
        time.sleep (1.2)
        keybord.release("s")
        time.sleep (0.5)

        keybord.press("d")
        time.sleep (19.5)
        keybord.release("d")
        time.sleep (0.5)

        keybord.press("s")
        time.sleep (1.2)
        keybord.release("s")
        time.sleep (0.5)


keybord.press("a")
time.sleep (19.5)
keybord.release("a")
time.sleep (0.5)

keybord.press("g")
keybord.release("g")


keybord.release(" ")