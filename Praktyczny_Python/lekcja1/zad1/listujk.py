# Importujemy potrzebne moduły:
import sys         # do obsługi argumentów z linii poleceń i wyjścia z programu
import os          # do pracy z plikami i katalogami w stylu POSIX/Windows
from pathlib import Path  # nowoczesny interfejs do pracy z plikami/katalogami

# Sprawdzamy, czy podano dokładnie jeden argument (ścieżkę do katalogu)
if len(sys.argv) != 2:
    sys.exit("Usage: script.py <path>")  # kończymy program z komunikatem

path = sys.argv[1]  # Pobieramy ścieżkę z argumentu

# Sprawdzamy, czy podana ścieżka istnieje
if not os.path.exists(path):
    sys.exit(f"❌ Ścieżka '{path}' nie istnieje.")

# Sprawdzamy, czy to faktycznie katalog
if not os.path.isdir(path):
    sys.exit(f"❌ Ścieżka '{path}' nie jest katalogiem.")

# === Wariant A ===
# Listowanie plików i folderów rekurencyjnie przy pomocy os.walk
def list_os_walk(path):
    result = []
    # os.walk zwraca trójki: (aktualny katalog, lista podkatalogów, lista plików)
    for dirpath, dirnames, filenames in os.walk(path):
        # Sklejamy pełną ścieżkę dla każdego pliku i folderu
        for name in dirnames + filenames:
            full_path = os.path.normpath(os.path.join(dirpath, name))  # normalizujemy ścieżkę (np. zamieniamy / na \ na Windows)
            result.append(full_path)
    return result

# === Wariant B ===
# Listowanie plików/folderów przy pomocy pathlib.Path.rglob('*')
def list_pathlib_rglob(path):
    # Używamy rglob('*') do znalezienia wszystkiego włącznie z podkatalogami
    result = [os.path.normpath(str(p)) for p in Path(path).rglob('*')]
    return result

# === Wariant C ===
# Ręczne (manualne) rekurencyjne przechodzenie drzewa katalogów
def list_recursive_manual(path):
    result = []

    # Funkcja pomocnicza wywoływana rekurencyjnie
    def recursive_helper(current_path):
        for item in os.listdir(current_path):  # listujemy elementy w bieżącym katalogu
            full_path = os.path.normpath(os.path.join(current_path, item))  # tworzymy pełną ścieżkę
            result.append(full_path)  # dodajemy do listy
            if os.path.isdir(full_path):  # jeżeli to folder, to zaglądamy głębiej
                recursive_helper(full_path)

    recursive_helper(path)  # uruchamiamy rekurencję od katalogu głównego
    return result

# === Uruchomienie wszystkich trzech wersji ===
list1 = sorted(list_os_walk(path))           # wynik z os.walk
list2 = sorted(list_pathlib_rglob(path))     # wynik z pathlib
list3 = sorted(list_recursive_manual(path))  # wynik z rekurencji ręcznej

# === Wyświetlamy wyniki każdej metody ===
print("\n--- Using os.walk ---")
print("\n".join(list1))

print("\n--- Using pathlib.rglob ---")
print("\n".join(list2))

print("\n--- Using manual recursion ---")
print("\n".join(list3))

# === Sprawdzamy, czy wszystkie listy są identyczne ===
if list1 == list2 == list3:
    print("\n✅ Wszystkie metody zwróciły identyczne wyniki.")
else:
    print("\n❌ Wyniki się różnią!")  # jeśli nie – pokazujemy ostrzeżenie
