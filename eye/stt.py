import pytesseract
from PIL import ImageGrab

def get_text(x: int, y: int) -> str:
    """
    Read an image and use pytesseract to return the text in the image.
    """
    # Left, upper, right, lower
    bbox = (x - 250, y - 100, x + 250, y + 100)

    img = ImageGrab.grab(bbox)
    img.show()

    text = pytesseract.pytesseract.image_to_string(img)

    return text
