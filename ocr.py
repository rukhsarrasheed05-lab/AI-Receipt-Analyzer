import pytesseract
from PIL import Image
# Tesseract OCR ka exact path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text
# -------------------------------
# Test code
if __name__ == "__main__":
    # Image load karo
    image = Image.open(r"C:\Users\Acer\OneDrive\Desktop\AI Receipt Analyzer\926-9265741_ocr-sample-receipt-optical-character-recognition.png")  # yahan apni image ka naam likho

    # Function call
    text = extract_text(image)

    # Print result
    print(text)