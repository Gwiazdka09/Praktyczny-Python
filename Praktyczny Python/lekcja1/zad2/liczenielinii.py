import sys

if len(sys.argv) != 2:
    sys.exit("Użycie: python liczenielinii.py <ścieżka_do_pliku.py>")

plik = sys.argv[1]

try:
    with open(plik, 'r', encoding='utf-8') as f:
        linie = f.readlines()
        print(f"Liczba wszystkich linii: {len(linie)}")
except FileNotFoundError:
    print(f"Plik '{plik}' nie istnieje.")

try:
    with open(plik, 'r', encoding='utf-8') as f:
        linie = f.readlines()

        # Ignorowanie pustych linii
        non_empty_lines = [line for line in linie if line.strip() != '']
        print(f"Liczba wszystkich linii: {len(non_empty_lines)}")

except FileNotFoundError:
    print(f"Plik '{plik}' nie nie istnieje.")


try:
    with open(plik, 'r', encoding='utf-8') as f:
        linie = f.readlines()

        # Ignorowanie pustych linii
        non_empty_lines = [line for line in linie if line.strip() != '']

        # Ignorowanie lini komentarzy
        non_comment_lines = [line for line in non_empty_lines if not line.strip().startswith('#')]

        print(f"Liczba wszystkich linii bez # i pustych: {len(non_comment_lines)}")

except FileNotFoundError:
    print(f"Plik '{plik}' nie nie istnieje.")