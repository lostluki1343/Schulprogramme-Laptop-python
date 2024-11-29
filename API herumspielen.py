from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
button2 = driver.find_element(By.ID, "form_uebersicht:j_idt340:0:kurs")  # ID des Buttons
button2.click()

time.sleep(7)
button3 = driver.find_element(By.ID, "form_uebersicht:j_idt828:0:activity")  # ID des Buttons
button3.click()

time.sleep(7)
button3 = driver.find_element(By.ID, "form_folder:j_idt1297:1:activity")  # ID des Buttons
button3.click()

time.sleep(4)
button4 = driver.find_element(By.ID, "j_idt423:j_idt425:0:j_idt442")  # ID des Buttons
button4.click()


time.sleep(2)





anfangswert=370
endwert=390
schrittweite=1
einheit="kg"



j=anfangswert
while j<endwert:

    button6 = driver.find_element(By.ID, "questionForm:pruefen")  # ID des Buttons
    feld1 = driver.find_element(By.ID, "questionForm:mcq:0:inpCq")
    
    feld1.clear()
    j=j + schrittweite
    round(j,1)
    feld1.send_keys(j, einheit)
    button6.click()
    
    span_element = driver.find_element(By.XPATH, "//span[input[@id='questionForm:mcq:0:inpCq']]")
    span_class = span_element.get_attribute("class")
    
    time.sleep(5)

    if (span_class == "ergTrue ui-inputwrapper-filled"):
        print("Richtiger Wert gefunden!")
        break


    
