from PIL import Image
import pytesseract

def getGroceriesbyReceipt(groceries):
    img = Image.open("./backend/Receipt/image.jpg")
    text = pytesseract.image_to_string(img)
    text = text.lower()
    for grocery in groceries:
        if grocery in text:
            groceries[grocery]=True
    return groceries


if __name__ == "__main__":
    print(getGroceriesbyReceipt({"banana": False, "apple":False, "milk":False}))