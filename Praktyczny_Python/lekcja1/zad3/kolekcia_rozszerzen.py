import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: script.py <path>")

path = sys.argv[1]

if not os.path.exists(path):
    sys.exit(f"Ścieżka '{path}' nie istnieje.")
if not os.path.isdir(path):
    sys.exit(f"Ścieżka '{path}' nie jest katalogiem.")

def collect_unique_extensions(path):
    extensions = set()

    def recursive_helper(current_path):
        for item in os.listdir(current_path):
            full_path = os.path.join(current_path, item)
            if os.path.isfile(full_path):
                _, ext = os.path.splitext(item)
                if ext:
                    extensions.add(ext)
            elif os.path.isdir(full_path):
                recursive_helper(full_path)

    recursive_helper(path)
    return extensions

# Zbieranie rozszerzeń
unique_exts = collect_unique_extensions(path)

# Wyświetlenie wyników (posortowane dla czytelności)
print("\nUnikatowe rozszerzenia plików:")
for ext in sorted(unique_exts):
    print(ext)

if not unique_exts:
    print("Brak plików z rozszerzeniami w podanym katalogu.")
