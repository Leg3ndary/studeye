import pytesseract
from PIL import ImageGrab

def get_text(point: int) -> str:
    """
    Read an image and use pytesseract to return the text in the image.
    """
    bbox = (81, 135, 500, 300)

    img = ImageGrab.grab(bbox)

    text = pytesseract.pytesseract.image_to_string(img)

    return text
