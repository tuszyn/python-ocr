"""
Skrypt przeprwadza prosty preprocesing obrazów w postaci zamiany ich na czerń i biel,
a następnie wykonuje OCR.

Autor: Jakub Tuszyński
"""

from PIL import Image
import config
import os
import pytesseract

# Ścieżka do pliku wykonywalnego tesseracta
pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
# ścieżka do obrazów
images_path = os.chdir(config.IMAGES_PATH)


def preprocess_and_ocr(images_path):
    """
    Przetwarza obrazy na czerń i biel i zapisuje wyniki OCR do folderu.
    """
    for index, file in enumerate(os.listdir(images_path)):
        # otwieramy obraz i konwertujemy go na czerń i biel
        image_file = Image.open(file)
        gray = image_file.convert("L")
        blackwhite = gray.point(lambda x: 0 if x < 200 else 255, "1")
        # dokonujemy OCR
        text = pytesseract.image_to_string(blackwhite, lang="pol")
        # Przygotowujemy nazwy plików z wynikami OCR i zapisujemy do wskazanej lokacji
        text_filename = os.path.splitext(file)[0] + ".txt"
        text_location = os.path.join(config.OCR_SAVE_LOCATION, text_filename)
        with open(text_location, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    preprocess_and_ocr(images_path)
