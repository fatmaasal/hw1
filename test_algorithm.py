import unittest
from algorithm import mulsearch
class TestSearch(unittest.TestCase):
  def setUp(self):
    self.array = [10, 5, 20, 30, 7, 6]
  def test_successful(self):
    self.assertTrue(mulsearch(self.array, 5, 25))
  def test_failed(self):
    self.assertFalse(mulsearch(self.array, 6, 190))
  def test_emptyArray(self):
    self.assertFalse(mulsearch([], 10, 20))
  def test_whenArrayIsNone(self):
    self.assertFalse(mulsearch(None, 10, 30))
  def test_whensearchingnoneisfailed(self):
    self.assertFalse(mulsearch(self.array, 10, None))
if __name__ == '__main__':
    unittest.main()
