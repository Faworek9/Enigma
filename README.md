# 🔐 Enigma Desktop - Symulator Maszyny Enigma I

Profesjonalna aplikacja desktopowa w języku Python, która wiernie odwzorowuje działanie historycznej maszyny szyfrującej **Enigma I**. Projekt łączy w sobie autentyczną logikę kryptograficzną z nowoczesnym, intuicyjnym interfejsem graficznym.

![Enigma](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green?style=for-the-badge)

---

## ✨ Główne Cechy

- **🔄 Pełna symetria szyfrowania** – szyfrowanie i odszyfrowywanie odbywa się tymi samymi ustawieniami, zgodnie z zasadą działania Enigmy I
- **⚙️ Konfiguracja wirników** – pełna kontrola nad pięcioma historycznymi wirnikami (I, II, III, IV, V) z możliwością wyboru pozycji startowej (A–Z) i ustawienia pierścienia (1–26)
- **🔌 Łącznica kablowa (Plugboard)** – obsługa pustej łącznicy oraz presetów upamiętniających polskich kryptologów
- **🎯 Dynamiczny stan maszyny** – wirniki w GUI obracają się na żywo podczas szyfrowania i pozostają w nowej pozycji
- **🔄 Szybki reset** – przycisk "Powrót do ustawień początkowych" pozwala przywrócić domyślną konfigurację
- **💾 Zapis/ładowanie konfiguracji** – możliwość zapisania ustawień do pliku JSON i ich wczytania dla późniejszego użycia
- **📋 Historia szyfrowań** – automatyczne zapisywanie operacji w oknie historii
- **📑 Kopiowanie do schowka** – szybkie kopiowanie wyniku jednym kliknięciem

---

## 📜 Kontekst Historyczny & Polski Wkład

Maszyna Enigma była używana przez Niemcy podczas II wojny światowej do szyfrowania komunikacji wojskowej. Jej złamanie przez polskich kryptologów było jednym z najważniejszych osiągnięć w historii kryptografii.

**🇵🇱 Polscy kryptolodzy:**
- **Marian Rejewski** – jako pierwszy złamał szyfr Enigmy w 1932 roku, wykorzystując matematyczną analizę i teorii permutacji
- **Henryk Zygalski** – opracował "płachty Zygalskiego" – arkusze perforowane, które pozwalały na szybkie ustalenie ustawień wirników
- **Jerzy Różycki** – stworzył "zegar Różyckiego" – metodę określania, który z wirników obraca się najwolniej

### Pozycja (Grundstellung) vs Pierścień (Ringstellung)

- **Pozycja (Grundstellung)** – to litera, na której wirnik jest ustawiony w momencie rozpoczęcia szyfrowania. W GUI wybierasz ją z menu A–Z. Jest to widoczne okienko na wirniku.
- **Pierścień (Ringstellung)** – to ustawienie wewnętrznego pierścienia wirnika, które przesuwa nacięcie (notch) i zmienia moment obrotu następnego wirnika. W GUI wybierasz wartość 1–26. Jest to ukryte ustawienie wpływające na logikę obrotów.

---

## 📁 Struktura Projektu

```
Enigma/
├── engine.py      # Silnik kryptograficzny Enigmy I
├── enigma.py      # Aplikacja GUI (CustomTkinter)
├── requirements.txt # Zależności Pythona
└── README.md      # Dokumentacja projektu
```

### engine.py
Silnik kryptograficzny realizujący pełny mechanizm Enigmy I:
- **Klasa Rotor** – obsługa 5 historycznych wirników (I, II, III, IV, V) z nacięciami (notches) i mechanizmem double-stepping
- **Klasa Reflector** – implementacja reflektora B
- **Klasa Plugboard** – łącznica kablowa do podstawiania znaków
- **Klasa EnigmaEngine** – koordynacja całego procesu szyfrowania

### enigma.py
Aplikacja okienkowa stworzona w CustomTkinter:
- Konfiguracja wirników (miejsca, pozycje, pierścienie)
- Wybór presetów łącznicy kablowej
- Dynamiczna aktualizacja pozycji wirników
- Historia szyfrowań i kopiowanie wyników

---

## 🚀 Wymagania i Instalacja

### Wymagania
- Python 3.7 lub nowszy
- Biblioteka `customtkinter`

### Instalacja

1. **Klonowanie repozytorium:**
   ```bash
   git clone https://github.com/TWOJ-NICK/Enigma.git
   cd Enigma
   ```

2. **Tworzenie środowiska wirtualnego (opcjonalne, ale zalecane):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Instalacja bibliotek:**
   ```bash
   pip install -r requirements.txt
   # Lub tylko:
   pip install customtkinter
   ```

4. **Uruchomienie aplikacji:**
   ```bash
   python enigma.py
   ```

---

## 📖 Instrukcja Użycia

### Podstawowe szyfrowanie

1. **Skonfiguruj wirniki:**
   - Wybierz wirniki dla miejsc 1, 2, 3 (np. I, II, III, IV, V)
   - Ustaw pozycje startowe (A–Z) dla każdego wirnika
   - Ustaw pierścienie (1–26) dla każdego wirnika

2. **Wybierz preset łącznicy kablowej:**
   - "Brak" – pusta łącznica
   - "Domyślny" – podstawowe podstawienie
   - "Szyfr Rejewskiego" – preset upamiętniający Mariana Rejewskiego
   - "Płachty Zygalskiego" – preset upamiętniający Henryka Zygalskiego
   - "Zegar Różyckiego" – preset upamiętniający Jerzego Różyckiego

3. **Wpisz tekst do zaszyfrowania** i kliknij "Zaszyfruj"

4. **Wynik pojawi się** w etykiecie wyniku oraz w historii szyfrowań

### Jak odszyfrować wiadomość

⚠️ **Ważne:** Do odszyfrowania wiadomości należy użyć **tych samych ustawień początkowych**, na których tekst został zaszyfrowany:

1. Ustaw wirniki na te same pozycje i pierścienie, które były użyte podczas szyfrowania
2. Wybierz ten sam preset łącznicy kablowej
3. Wpisz zaszyfrowany tekst i kliknij "Zaszyfruj"
4. Wynik będzie odszyfrowaną wiadomością

Dzięki właściwościom Enigmy, proces szyfrowania jest odwracalny przy identycznych ustawieniach początkowych.

### Reset do ustawień początkowych

Kliknij przycisk **"Powrót do ustawień początkowych"**, aby:
- Przywrócić wirniki do: I, II, III
- Zresetować pozycje do: A, A, A
- Zresetować pierścienie do: 1, 1, 1
- Ustawić łącznicę na: "Brak"
- Wyczyścić etykietę wyniku

### Zapis i ładowanie konfiguracji

Aby zapisać aktualne ustawienia:
1. Skonfiguruj wirniki i łącznicę według potrzeb
2. Kliknij przycisk **"💾 Zapisz konfigurację"**
3. Wybierz lokalizację i nazwę pliku JSON
4. Wszystkie ustawienia zostaną zapisane do pliku

Aby wczytać zapisaną konfigurację:
1. Kliknij przycisk **"📂 Wczytaj konfigurację"**
2. Wybierz plik JSON z zapisanymi ustawieniami
3. Wszystkie parametry zostaną przywrócone do zapisanych wartości

Ta funkcja jest szczególnie przydatna przy wielokrotnym używaniu tych samych ustawień szyfrowania.

---

## 🎯 Presety Łącznicy Kablowej

Aplikacja oferuje presetów upamiętniających polskich kryptologów:

| Preset | Opis |
|--------|------|
| Brak | Pusta łącznica – brak podstawień |
| Domyślny | Podstawowe podstawienie (A↔U, E↔I) |
| Szyfr Rejewskiego | Preset upamiętniający Mariana Rejewskiego |
| Płachty Zygalskiego | Preset upamiętniający Henryka Zygalskiego |
| Zegar Różyckiego | Preset upamiętniający Jerzego Różyckiego |

---

## 📝 Licencja

Ten projekt jest stworzony w celach edukacyjnych, aby upamiętnić wkład polskich kryptologów w złamanie szyfru Enigmy.

---

## 🤝 Wkład w projekt

Wszelkie sugestie, poprawki i wkład są mile widziane!