import sys
import os
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("Usage: script.py <path>")

path = sys.argv[1]

if not os.path.exists(path):
    sys.exit(f"Ścieżka '{path}' nie istnieje.")
if not os.path.isdir(path):
    sys.exit(f"Ścieżka '{path}' nie jest katalogiem.")

# Wariant A - os.walk
def list_os_walk(path):
    result = []
    for dirpath, dirnames, filenames in os.walk(path):
        for name in dirnames + filenames:
            full_path = os.path.normpath(os.path.join(dirpath, name))
            result.append(full_path)
    return result

# Wariant B - pathlib.Path.rglob('*')
def list_pathlib_rglob(path):
    result = [os.path.normpath(str(p)) for p in Path(path).rglob('*')]
    return result

# Wariant C - rekurencyjnie
def list_recursive_manual(path):
    result = []

    def recursive_helper(current_path):
        for item in os.listdir(current_path):
            full_path = os.path.normpath(os.path.join(current_path, item))
            result.append(full_path)
            if os.path.isdir(full_path):
                recursive_helper(full_path)

    recursive_helper(path)
    return result

# Uruchom wszystkie trzy warianty
list1 = sorted(list_os_walk(path))
list2 = sorted(list_pathlib_rglob(path))
list3 = sorted(list_recursive_manual(path))

# Wyświetl wyniki
print("\n--- Using os.walk ---")
print("\n".join(list1))

print("\n--- Using pathlib.rglob ---")
print("\n".join(list2))

print("\n--- Using manual recursion ---")
print("\n".join(list3))

# Porównanie wyników
if list1 == list2 == list3:
    print("\n✅ Wszystkie metody zwróciły identyczne wyniki.")
else:
    print("\n❌ Wyniki się różnią!")
