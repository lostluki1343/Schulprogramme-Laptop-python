from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox
import time

# WebDriver starten (z. B. Chrome)
driver = webdriver.Firefox()  # oder webdriver.Firefox() für Firefox
driver.get("https://letto.htlstp.ac.at/lettohtlstp/letto/login.jsf")  # URL deiner Letto-Software

# Warte kurz, bis die Seite geladen ist
time.sleep(3)

# Beispiel: Anmeldedaten eingeben
username_field = driver.find_element(By.ID, "j_idt22:username")  # ID des Benutzernamenfelds
password_field = driver.find_element(By.ID, "j_idt22:pwd")  # ID des Passwortfelds

username_field.send_keys("lukas.schloegl")
password_field.send_keys("Lotte1442005!")

# Anmeldebutton klicken
button1 = driver.find_element(By.ID, "j_idt22:login")  # ID des Buttons
button1.click()

# Warte, bis die nächste Seite geladen ist
time.sleep(3)
button2 = driver.find_element(By.ID, "j_idt374:j_idt376:4:j_idt393")  # ID des Buttons
button2.click()

time.sleep(3)
button3 = driver.find_element(By.ID, "j_idt1584:j_idt1586:0:j_idt1603")  # ID des Buttons
button3.click()

time.sleep(3)
button3 = driver.find_element(By.ID, "questionForm:j_idt1772")  # ID des Buttons
button3.click()

time.sleep(3)
button3 = driver.find_element(By.ID, "questionForm:j_idt1772")  # ID des Buttons
button3.click()

time.sleep(3)
button3 = driver.find_element(By.ID, "questionForm:j_idt1772")  # ID des Buttons
button3.click()

time.sleep(3)





anfangswert=0
endwert=2
schrittweite=0.05
einheit=""



j=anfangswert - schrittweite
while j<endwert:

    button6 = driver.find_element(By.ID, "questionForm:pruefen")  # ID des Buttons
    feld1 = driver.find_element(By.ID, "questionForm:mcq:0:inpCq")
    
    feld1.clear()
    j=j + schrittweite
    round(j,1)
    feld1.send_keys(j, einheit)
    button6.click()
    
    time.sleep(4)

    span_element = driver.find_element(By.XPATH, "//span[input[@id='questionForm:mcq:0:inpCq']]")
    span_class = span_element.get_attribute("class")
    
    if (span_class == "ergTrue ui-inputwrapper-filled"):
        print("Richtiger Wert gefunden!")
        break 
    

    
