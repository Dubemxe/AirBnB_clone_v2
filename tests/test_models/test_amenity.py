#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_checker(self):
        '''Checkes name availability'''
        self.name = "Amenity"
        self.value = Amenity
        if not isinstance(self.value, str):
            raise TypeError("Name must be in characters")
        pass

if __name__ == "__main__":
    unittest.main()
