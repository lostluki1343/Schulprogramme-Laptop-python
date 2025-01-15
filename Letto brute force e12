from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox
import time

# Definiere die E12-Reihe
E12_VALUES = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

aufgabeNr = 1  # Auswahl der Aufgabe
beispielNr = 8    # Auswahl des Beispiels
feldNr = 1  # Auswahl des Feldes
einheit = "kOhm"  # Einheit der Werte

# WebDriver starten (z. B. Chrome)
driver = webdriver.Firefox()  # oder webdriver.Chrome() für Chrome
driver.get("https://letto.htlstp.ac.at/lettohtlstp/letto/login.jsf")  # URL deiner Letto-Software

# Warte kurz, bis die Seite geladen ist
time.sleep(3)

# Anmeldedaten eingeben
username_field = driver.find_element(By.ID, "j_idt25:username")
password_field = driver.find_element(By.ID, "j_idt25:pwd")

username_field.send_keys("erwin.mot")
password_field.send_keys("Aderleiste30")

button1 = driver.find_element(By.ID, "j_idt25:login")
button1.click()

time.sleep(3)

button2 = driver.find_element(By.ID, f"j_idt360:j_idt362:{aufgabeNr - 1}:j_idt379")
button2.click()

time.sleep(3)
button3 = driver.find_element(By.ID, "j_idt422:j_idt424:0:j_idt441")
button3.click()

for n in range(beispielNr - 1):
    time.sleep(5)
    button4 = driver.find_element(By.ID, "questionForm:j_idt610")
    button4.click()

time.sleep(3)

# E12-Reihe durchprobieren
for value in E12_VALUES:

    for multiplier in [1 ,10, 100]:
        time.sleep(1)
        test_value = round(value * multiplier, 3)
        
        button6 = driver.find_element(By.ID, "questionForm:pruefen")
        feld1 = driver.find_element(By.ID, f"questionForm:mcq:{feldNr - 1}:inpCq")
        
        feld1.clear()
        feld1.send_keys(f"{test_value} {einheit}")
        button6.click()

        time.sleep(6)

        span_element = driver.find_element(By.XPATH, f"//span[input[@id='questionForm:mcq:{feldNr - 1}:inpCq']]")
        span_class = span_element.get_attribute("class")

        if span_class == "ergTrue ui-inputwrapper-filled":
            print(f"Richtiger Wert gefunden: {test_value} {einheit}")

            driver.quit()
            exit()

# Wenn kein richtiger Wert gefunden wurde
driver.quit()
print("Kein richtiger Wert gefunden.")
