import customtkinter as ctk
from engine import EnigmaEngine

# --- LOGIKA GUI ---
def akcja_szyfruj():
    wprowadzony_tekst = pole_tekstowe.get()
    if wprowadzony_tekst:
        rotor1_pos = int(menu_rotor1.get())
        rotor2_pos = int(menu_rotor2.get())
        rotor3_pos = int(menu_rotor3.get())
        plugboard_preset = menu_plugboard.get()
        
        engine = EnigmaEngine(rotor1_pos, rotor2_pos, rotor3_pos, plugboard_preset)
        wynik = engine.encrypt(wprowadzony_tekst)
        etykieta_wyniku.configure(text=f"Wynik: {wynik}")
        
        # Add to history
        pole_historii.configure(state="normal")
        pole_historii.insert("end", f"{wprowadzony_tekst.upper()} -> {wynik}\n")
        pole_historii.configure(state="disabled")
        pole_historii.see("end")


def kopiuj_wynik():
    wynik_tekst = etykieta_wyniku.cget("text")
    if wynik_tekst.startswith("Wynik: "):
        wynik = wynik_tekst.replace("Wynik: ", "")
        app.clipboard_clear()
        app.clipboard_append(wynik)
        przycisk_kopiuj.configure(text="Skopiowano!")
        app.after(1500, lambda: przycisk_kopiuj.configure(text="Kopiuj wynik"))


def wyczysc_historie():
    pole_historii.configure(state="normal")
    pole_historii.delete("1.0", "end")
    pole_historii.configure(state="disabled")


# --- KONFIGURACJA OKNA DESKTOPOWEGO ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Enigma Desktop")
app.geometry("400x650")

tytul = ctk.CTkLabel(app, text="Szyfrator Enigma", font=("Arial", 20, "bold"))
tytul.pack(pady=15)

# Rotor positions configuration
etykieta_rotory = ctk.CTkLabel(app, text="Pozycje wirników:", font=("Arial", 12))
etykieta_rotory.pack(pady=(5, 5))

ramka_rotory = ctk.CTkFrame(app)
ramka_rotory.pack(pady=5)

wartosci = [str(i) for i in range(26)]
menu_rotor1 = ctk.CTkOptionMenu(ramka_rotory, values=wartosci, width=60)
menu_rotor1.set("0")
menu_rotor1.grid(row=0, column=0, padx=5)

menu_rotor2 = ctk.CTkOptionMenu(ramka_rotory, values=wartosci, width=60)
menu_rotor2.set("0")
menu_rotor2.grid(row=0, column=1, padx=5)

menu_rotor3 = ctk.CTkOptionMenu(ramka_rotory, values=wartosci, width=60)
menu_rotor3.set("0")
menu_rotor3.grid(row=0, column=2, padx=5)

# Plugboard preset configuration
etykieta_plugboard = ctk.CTkLabel(app, text="Preset łącznicy:", font=("Arial", 12))
etykieta_plugboard.pack(pady=(10, 5))

presety_plugboard = ["Domyślny", "Szyfr Rejewskiego", "Płachty Zygalskiego", "Zegar Różyckiego"]
menu_plugboard = ctk.CTkOptionMenu(app, values=presety_plugboard, width=200)
menu_plugboard.pack(pady=5)

pole_tekstowe = ctk.CTkEntry(app, placeholder_text="Wpisz słowo...", width=250)
pole_tekstowe.pack(pady=10)

przycisk = ctk.CTkButton(app, text="Zaszyfruj", command=akcja_szyfruj)
przycisk.pack(pady=10)

etykieta_wyniku = ctk.CTkLabel(app, text="Wynik pojawi się tutaj", font=("Arial", 14))
etykieta_wyniku.pack(pady=5)

przycisk_kopiuj = ctk.CTkButton(app, text="Kopiuj wynik", command=kopiuj_wynik, width=150)
przycisk_kopiuj.pack(pady=5)

etykieta_historii = ctk.CTkLabel(app, text="Historia szyfrowań:", font=("Arial", 12))
etykieta_historii.pack(pady=(15, 5))

pole_historii = ctk.CTkTextbox(app, width=300, height=150, state="disabled")
pole_historii.pack(pady=5)

przycisk_wyczysc = ctk.CTkButton(app, text="Wyczyść historię", command=wyczysc_historie, width=150)
przycisk_wyczysc.pack(pady=5)

if __name__ == "__main__":
    app.mainloop()