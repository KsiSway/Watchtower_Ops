#!/usr/bin/env python3
import sys
import json
import os
import pytesseract
from PIL import Image

# Explicitly point the wrapper to the system binary
# Note: On Windows host, this requires executing via WSL or a shim
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def perform_ocr(image_path):
    """Extracts text from image using Tesseract."""
    if not os.path.exists(image_path):
        return {"status": "error", "message": f"File not found: {image_path}"}
    
    try:
        # Load image and perform OCR
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        
        # Split into lines and filter empty
        intel = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not intel:
            return {"status": "success", "intel": ["[NO_TEXT_DETECTED]"]}
            
        return {"status": "success", "intel": intel}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: python osint_ocr_engine.py <image_path>"}))
        sys.exit(1)
        
    img_path = sys.argv[1]
    result = perform_ocr(img_path)
    print(json.dumps(result))
