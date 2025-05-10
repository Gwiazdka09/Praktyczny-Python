import sys

if len(sys.argv) != 2:
    sys.exit("Użycie: python liczenielinii.py <ścieżka_do_pliku.py>")

plik = sys.argv[1]

try:
    with open(plik, "r", encoding="utf-8") as f:
        linie = f.readlines()
        print(f"Liczba wszystkich lini: {len(linie)}")
except FileNotFoundError:
    print(f"Plik: '{plik}' nie istnieje")