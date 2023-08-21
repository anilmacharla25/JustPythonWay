import pyautogui
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AMacharla\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def find_dynamic_text_location(target_text):
    screen = pyautogui.screenshot()

    # Perform OCR on the captured screenshot
    detected_data = pytesseract.image_to_data(screen, output_type=pytesseract.Output.DICT)
    detected_texts = detected_data["text"]

    for index, text in enumerate(detected_texts):
        if text.strip() == target_text:
            # Extract the bounding box coordinates
            left = detected_data["left"][index]
            top = detected_data["top"][index]
            width = detected_data["width"][index]
            height = detected_data["height"][index]
            text_x = left + width // 2
            text_y = top + height // 2
            return text_x, text_y

    return None

dynamic_text = "Notes"
dynamic_text_location = find_dynamic_text_location(dynamic_text)
pyautogui.click(dynamic_text_location[0],dynamic_text_location[1])
time.sleep(0.15)
pyautogui.click(dynamic_text_location[0],dynamic_text_location[1])

if dynamic_text_location is not None:
    print(f"Dynamic text '{dynamic_text}' found at coordinates: ({dynamic_text_location[0]}, {dynamic_text_location[1]})")
else:
    print(f"Dynamic text '{dynamic_text}' not found on the screen")
