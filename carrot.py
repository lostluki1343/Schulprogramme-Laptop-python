from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keybord=Controller()
import time

time.sleep(10)    
print("programm startet")

keybord.press("h")
keybord.release("h")


keybord.press(" ")

for i in range (8):
    keybord.press("s")
    time.sleep (23.5)
    keybord.release("s")
    

    keybord.press("e")
    time.sleep (2)
    keybord.release("e")
    

    keybord.press("f")
    time.sleep (23.5)
    keybord.release("f")
    

    keybord.press("e")
    time.sleep (2)
    keybord.release("e")
    
    

for i in range (8):
    keybord.press("s")
    time.sleep (0.5)
    keybord.release("s")
    

    keybord.press("e")
    time.sleep (0.5)
    keybord.release("e")
    

    keybord.press("s")
    time.sleep (23)
    keybord.release("s")
    

    keybord.press("d")
    time.sleep (2)
    keybord.release("d")
    

    keybord.press("f")
    time.sleep (0.5)
    keybord.release("f")
    

    keybord.press("e")
    time.sleep (0.5)
    keybord.release("e")
    

    keybord.press("f")
    time.sleep (23)
    keybord.release("f")
    
    
    
    

    keybord.press("d")
    time.sleep (2)
    keybord.release("d")
    




keybord.release(" ")