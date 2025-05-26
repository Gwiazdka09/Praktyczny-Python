import sys
import os

def detect_language_from_content(file_path):
    language_keywords = {
        "C/C++": ["#include", "#define"],
        "PHP": ["<?php"],
        "Python": ["def ", "import "],
        "HTML": ["<html", "<body", "<div"]
    }

    found_languages = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            for language, keywords in language_keywords.items():
                for keyword in keywords:
                    if keyword in content:
                        found_languages.add(language)
                        break  # Skip remaining keywords for this language

        if found_languages:
            print(f"{file_path} - Wykryte języki:")
            for lang in found_languages:
                print(f"- {lang}")
        else:
            print(f"{file_path} - Nie wykryto znanych wzorców języków.")

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
                    detect_language_from_content(file_path)
        elif os.path.isfile(path):
            detect_language_from_content(path)
        else:
            print(f"Nie znaleziono ścieżki: {path}")
