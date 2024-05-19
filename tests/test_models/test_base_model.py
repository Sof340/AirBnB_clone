import unittest
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    def test_unique_id(self):
        base_1 = BaseModel()
        base_2 = BaseModel()
        """
        let test whether two ids of two intances of the object BaseModel have the same value.
        """
        
        self.assertNotEqual(base_1.id, base_2.id)

    def test_updated_variable(self):
        """
        Let test whether the variable updated at is correctly updated.
        """
        base_1 = BaseModel()
        value_now = base_1.updated_at
        base_1.save()
        self.assertNotEqual(value_now, base_1.updated_at)
