# python-ocr
Prosty skrypt dokonujący preprocessingu obrazów oraz OCR.
# Instalacja
W pierwszej kolejnosci należy zainstalować [tesseracta](https://tesseract-ocr.github.io/tessdoc/Home.html), czyli silnik przeprowadzający OCR.
Podczas instalacji trzeba pamietać o doinstalowaniu paczki dla języka polskiego.

Wymagany jest również Python w wersji co najmniej 3.7

Klonujemy repozytorium
```
git clone https://github.com/tuszyn/python-ocr.git
```
przechodzimy do sklonowanego folderu
```
cd python-ocr
```
i instalujemy zależności zależności
```
pip install -r requirements.txt
```
# Użytkowanie
Na samym początku trzeba w pliku config.py zmienić ścieżki do:
- Pliku wykonywalnego tesseracta
- Folderu z obrazami do przetworzenia
- Folderu w którym ma zostać zapisany wynik OCR

Obecnie są tam podane ścieżki przykładowe.
Po zmianie ścieżek uruchamiamy program.

# Uwagi
Skrypt był testowany na razie tylko pod Windowsa, więc nie ma gwarancji działania na systemach Linuxowych.
