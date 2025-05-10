import sys  # Importowanie modułu sys, który pozwala na interakcję z systemem, w tym obsługę argumentów wiersza poleceń.

# Sprawdzenie, czy użytkownik podał dokładnie jeden argument (ścieżkę do pliku).
if len(sys.argv) != 2:
    sys.exit("Użycie: python liczenielinii.py <ścieżka_do_pliku.py>")  # Jeśli nie, zakończenie programu z komunikatem o błędzie.

plik = sys.argv[1]  # Przypisanie ścieżki do pliku z argumentu wiersza poleceń do zmiennej 'plik'.

# Próba otwarcia pliku w trybie odczytu ('r') i liczenie wszystkich linii w pliku.
try:
    with open(plik, 'r', encoding='utf-8') as f:  # Otwieramy plik z określonym kodowaniem UTF-8.
        linie = f.readlines()  # Wczytujemy wszystkie linie pliku do listy 'linie'.
        print(f"Liczba wszystkich linii: {len(linie)}")  # Wyświetlamy liczbę linii w pliku.
except FileNotFoundError:  # Obsługa przypadku, gdy plik nie istnieje.
    print(f"Plik '{plik}' nie istnieje.")  # Komunikat o błędzie, jeśli plik nie został znaleziony.

# Próba otwarcia pliku i liczenie linii, ignorując puste linie.
try:
    with open(plik, 'r', encoding='utf-8') as f:  # Otwieramy plik w trybie odczytu.
        linie = f.readlines()  # Wczytujemy wszystkie linie pliku do listy 'linie'.

        # Tworzymy listę, która zawiera tylko linie, które nie są puste.
        non_empty_lines = [line for line in linie if line.strip() != '']  # 'strip()' usuwa białe znaki na początku i końcu linii.
        print(f"Liczba wszystkich linii bez pustych: {len(non_empty_lines)}")  # Wyświetlamy liczbę niepustych linii.

except FileNotFoundError:  # Obsługa przypadku, gdy plik nie istnieje.
    print(f"Plik '{plik}' nie istnieje.")  # Komunikat o błędzie, jeśli plik nie został znaleziony.

# Próba otwarcia pliku i liczenie linii, ignorując puste linie i linie komentarzy.
try:
    with open(plik, 'r', encoding='utf-8') as f:  # Otwieramy plik w trybie odczytu.
        linie = f.readlines()  # Wczytujemy wszystkie linie pliku do listy 'linie'.

        # Ignorowanie pustych linii (usuwamy białe znaki).
        non_empty_lines = [line for line in linie if line.strip() != '']  # Tworzymy listę niepustych linii.

        # Tworzymy listę, która zawiera tylko linie, które nie zaczynają się od '#'.
        non_comment_lines = [line for line in non_empty_lines if not line.strip().startswith('#')]  # Ignorujemy komentarze.

        # Wyświetlamy liczbę linii, które nie są puste ani komentarzami.
        print(f"Liczba wszystkich linii bez # i pustych: {len(non_comment_lines)}")  # Liczymy i wyświetlamy.

except FileNotFoundError:  # Obsługa przypadku, gdy plik nie istnieje.
    print(f"Plik '{plik}' nie istnieje.")  # Komunikat o błędzie, jeśli plik nie został znaleziony.
