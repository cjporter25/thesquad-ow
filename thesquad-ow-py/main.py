from PIL import ImageGrab
import pytesseract
import cv2
import numpy as np
import keyboard  # Install using: pip install keyboard
import time

# Define the path to the Tesseract executable if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screenshot():
    # Capture the entire screen
    screenshot = ImageGrab.grab() 
    screenshot_np = np.array(screenshot)
    # Convert RGB to BGR (OpenCV uses BGR format)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    return screenshot_cv

def save_screenshot(image, filename='screenshot.png'):
    cv2.imwrite(filename, image)

def perform_ocr(image):
    # Convert the image to text using Tesseract OCR
    text = pytesseract.image_to_string(image)
    return text

def main():
    print("Press 's' to capture a screenshot. Press 'q' to quit.")
    while True:
        # Wait for the 's' key to be pressed
        if keyboard.is_pressed('s'):
            print("Capturing screenshot...")
            screenshot = capture_screenshot()
            save_screenshot(screenshot)
            text = perform_ocr(screenshot)
            print("Recognized text:", text)
            time.sleep(1)  # Wait a moment to avoid multiple captures from a single press

        # Exit the loop if 'q' is pressed
        if keyboard.is_pressed('q'):
            print("Quitting...")
            break

if __name__ == "__main__":
    main()