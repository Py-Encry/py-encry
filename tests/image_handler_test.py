import unittest
import pytest
from src.pyencry.image_handler import ImageHandler

class ImageHandlerTests(unittest.TestCase):
    def test_can_import_image(self):
        expected = {"filename": "./img/Tower_Bridge_from_Shad_Thames.jpg", "format": "JPEG", "mode": "RGB", "size": (1200, 600)}
        image_handler = ImageHandler("./img/Tower_Bridge_from_Shad_Thames.jpg")
        result = image_handler.file_info()
        self.assertEqual(result, expected)

    def test_can_import_image_from_base64(self):
        expected = {"filename": None, "format": "JPEG", "mode": "RGB", "size": (1200, 600)}
        with open("./img/Tower_Bridge_from_Shad_Thames.jpg", "rb") as file:
            image_handler = ImageHandler.from_base64(file.read())
            result = image_handler.file_info()
        self.assertEqual(result, expected)

    


