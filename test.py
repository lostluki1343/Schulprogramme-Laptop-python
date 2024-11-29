import tkinter as tk
from tkinter import messagebox

# Funktion, um den Alert zu zeigen
def show_alert():
    # Neues Tkinter-Fenster erstellen (wird für messagebox benötigt, aber bleibt unsichtbar)
    root = tk.Tk()
    root.withdraw()  # Versteckt das Hauptfenster

    # Zeige die Alert-Message
    messagebox.showinfo("Hinweis", "Dies ist eine Alert-Nachricht!")

    # Hauptfenster zerstören
    root.destroy()

# Alert-Fenster anzeigen
show_alert()
