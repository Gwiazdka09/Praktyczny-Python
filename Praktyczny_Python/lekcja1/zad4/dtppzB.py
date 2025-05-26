import sys
import os
import re

def detect_language_with_regex(file_path):
    language_patterns = {
        "C/C++": [
            r"^#include <.*>",
            r"^#define \w+ \w+",
            r"int main\(.*\)"
        ],
        "PHP": [
            r"<\?php",
            r'echo ".*";',
            r"\$\w+ = .*;"
        ],
        "Python": [
            r"^def \w+\(.*\):",
            r"^from .* import .*",
            r"for .* in .*:"
        ],
        "HTML": [
            r"<html.*>",
            r"<body.*>",
            r"<div.*>"
        ]
    }

    found_languages = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                for language, patterns in language_patterns.items():
                    for pattern in patterns:
                        if re.search(pattern, line):
                            found_languages.add(language)
                            break  # przerywa sprawdzanie wzorców dla tego języka

        if found_languages:
            print(f"{file_path} - Wykryte języki (regex):")
            for lang in found_languages:
                print(f"- {lang}")
        else:
            print(f"{file_path} - Nie wykryto znanych wzorców języków (regex).")

    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
    except Exception as e:
        print(f"Wystąpił błąd przy {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python liczenielinii.py <plik_lub_folder_do_sprawdzenia>")
    else:
        path = sys.argv[1]

        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    detect_language_with_regex(file_path)
        elif os.path.isfile(path):
            detect_language_with_regex(path)
        else:
            print(f"Nie znaleziono ścieżki: {path}")
