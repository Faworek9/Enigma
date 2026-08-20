import customtkinter as ctk
from engine import EnigmaEngine

# --- LOGIKA GUI ---
def akcja_szyfruj():
    wprowadzony_tekst = pole_tekstowe.get()
    if wprowadzony_tekst:
        # Convert position letters (A-Z) to indices (0-25)
        rotor_positions = [ord(menu_rotor1_pos.get()) - ord('A'), ord(menu_rotor2_pos.get()) - ord('A'), ord(menu_rotor3_pos.get()) - ord('A')]
        # Convert ring values (1-26) to indices (0-25)
        ring_settings = [int(menu_rotor1_ring.get()) - 1, int(menu_rotor2_ring.get()) - 1, int(menu_rotor3_ring.get()) - 1]
        rotor_order = [menu_rotor1_order.get(), menu_rotor2_order.get(), menu_rotor3_order.get()]
        plugboard_preset = menu_plugboard.get()

        if len(set(rotor_order)) != 3:
            etykieta_wyniku.configure(text="Wynik: Wybierz unikalne wirniki I/II/III")
            return

        engine = EnigmaEngine(
            rotor_positions=rotor_positions,
            ring_settings=ring_settings,
            rotor_order=rotor_order,
            plugboard_preset=plugboard_preset,
        )
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
app.geometry("500x760")

tytul = ctk.CTkLabel(app, text="Szyfrator Enigma", font=("Arial", 20, "bold"))
tytul.pack(pady=15)

# Rotor configuration
etykieta_rotory = ctk.CTkLabel(app, text="Konfiguracja wirników (Slot 1 = lewy/wolny):", font=("Arial", 12))
etykieta_rotory.pack(pady=(5, 5))

ramka_rotory = ctk.CTkFrame(app)
ramka_rotory.pack(pady=5)

wartosci_pozycji = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
wartosci_pierscienia = [str(i) for i in range(1, 27)]
wirniki = ["I", "II", "III"]

ctk.CTkLabel(ramka_rotory, text="Miejsce").grid(row=0, column=0, padx=8, pady=(8, 4))
ctk.CTkLabel(ramka_rotory, text="Wirnik").grid(row=0, column=1, padx=8, pady=(8, 4))
ctk.CTkLabel(ramka_rotory, text="Pozycja").grid(row=0, column=2, padx=8, pady=(8, 4))
ctk.CTkLabel(ramka_rotory, text="Pierścień").grid(row=0, column=3, padx=8, pady=(8, 4))

ctk.CTkLabel(ramka_rotory, text="1").grid(row=1, column=0, padx=8, pady=4)
menu_rotor1_order = ctk.CTkOptionMenu(ramka_rotory, values=wirniki, width=80)
menu_rotor1_order.set("I")
menu_rotor1_order.grid(row=1, column=1, padx=8, pady=4)
menu_rotor1_pos = ctk.CTkOptionMenu(ramka_rotory, values=wartosci_pozycji, width=70)
menu_rotor1_pos.set("A")
menu_rotor1_pos.grid(row=1, column=2, padx=8, pady=4)
menu_rotor1_ring = ctk.CTkOptionMenu(ramka_rotory, values=wartosci_pierscienia, width=70)
menu_rotor1_ring.set("1")
menu_rotor1_ring.grid(row=1, column=3, padx=8, pady=4)

ctk.CTkLabel(ramka_rotory, text="2").grid(row=2, column=0, padx=8, pady=4)
menu_rotor2_order = ctk.CTkOptionMenu(ramka_rotory, values=wirniki, width=80)
menu_rotor2_order.set("II")
menu_rotor2_order.grid(row=2, column=1, padx=8, pady=4)
menu_rotor2_pos = ctk.CTkOptionMenu(ramka_rotory, values=wartosci_pozycji, width=70)
menu_rotor2_pos.set("A")
menu_rotor2_pos.grid(row=2, column=2, padx=8, pady=4)
menu_rotor2_ring = ctk.CTkOptionMenu(ramka_rotory, values=wartosci_pierscienia, width=70)
menu_rotor2_ring.set("1")
menu_rotor2_ring.grid(row=2, column=3, padx=8, pady=4)

ctk.CTkLabel(ramka_rotory, text="3").grid(row=3, column=0, padx=8, pady=(4, 8))
menu_rotor3_order = ctk.CTkOptionMenu(ramka_rotory, values=wirniki, width=80)
menu_rotor3_order.set("III")
menu_rotor3_order.grid(row=3, column=1, padx=8, pady=(4, 8))
menu_rotor3_pos = ctk.CTkOptionMenu(ramka_rotory, values=wartosci_pozycji, width=70)
menu_rotor3_pos.set("A")
menu_rotor3_pos.grid(row=3, column=2, padx=8, pady=(4, 8))
menu_rotor3_ring = ctk.CTkOptionMenu(ramka_rotory, values=wartosci_pierscienia, width=70)
menu_rotor3_ring.set("1")
menu_rotor3_ring.grid(row=3, column=3, padx=8, pady=(4, 8))

# Plugboard preset configuration
etykieta_plugboard = ctk.CTkLabel(app, text="Preset łącznicy:", font=("Arial", 12))
etykieta_plugboard.pack(pady=(10, 5))

presety_plugboard = ["Brak", "Domyślny", "Szyfr Rejewskiego", "Płachty Zygalskiego", "Zegar Różyckiego"]
menu_plugboard = ctk.CTkOptionMenu(app, values=presety_plugboard, width=200)
menu_plugboard.set("Brak")
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