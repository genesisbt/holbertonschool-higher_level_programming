import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        # Test if the constructor sets id correctly when provided
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_constructor_without_id(self):
        # Test if the constructor sets a non-None id when not provided
        b = Base()
        self.assertIsNotNone(b.id)

    def test_from_json_string(self):
        # Test if from_json_string converts JSON string to list of dictionaries correctly
        json_str = '[{"id":  1, "width":  1, "height":  2, "x":  0, "y":  0}, {"id":  2, "size":  3, "x":  0, "y":  0}]'
        objs = Base.from_json_string(json_str)
    
        # Check if the first object has the keys for a Rectangle
        self.assertIsInstance(objs[0], dict)
        self.assertIn('width', objs[0])
        self.assertIn('height', objs[0])
    
        # Check if the second object has the key for a Square
        self.assertIsInstance(objs[1], dict)
        self.assertIn('size', objs[1]) 

    def test_from_json_string(self):
        # Test if from_json_string converts JSON string to list of objects correctly
        json_str = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 2, "size": 3, "x": 0, "y": 0}]'
        objs = Base.from_json_string(json_str)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertIsInstance(objs[1], Square)

    def test_save_to_file(self):
        # Test if save_to_file writes correct JSON strings to corresponding files
        r = Rectangle(1, 2)
        s = Square(3)
        Base.save_to_file([r, s])
        with open("Rectangle.json", 'r') as file:
            rect_json = file.read()
        with open("Square.json", 'r') as file:
            square_json = file.read()
        self.assertEqual(rect_json, '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')
        self.assertEqual(square_json, '[{"id": 2, "size": 3, "x": 0, "y": 0}]')

    def test_create(self):
        # Test if create method returns instances with attributes set correctly
        rect_dict = {'id': 1, 'width': 1, 'height': 2, 'x': 0, 'y': 0}
        square_dict = {'id': 2, 'size': 3, 'x': 0, 'y': 0}
        rect = Rectangle.create(**rect_dict)
        square = Square.create(**square_dict)
        self.assertIsInstance(rect, Rectangle)
        self.assertIsInstance(square, Square)

    def test_load_from_file(self):
        # Test if load_from_file returns instances correctly from corresponding files
        r = Rectangle(1, 2)
        s = Square(3)
        Base.save_to_file([r, s])
        rect_list = Base.load_from_file(Rectangle)
        square_list = Base.load_from_file(Square)
        self.assertEqual(len(rect_list), 1)
        self.assertEqual(len(square_list), 1)
        self.assertIsInstance(rect_list[0], Rectangle)
        self.assertIsInstance(square_list[0], Square)

if __name__ == '__main__':
    unittest.main()
