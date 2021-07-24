import unittest


class TestInitial(unittest.TestCase):
  def setUp(self):
    self.square = lambda x: x * x

  def test_square(self):
    square_four = self.square(4)
    self.assertEqual(square_four, 16)
    
  def test_two_plus_two(self):
    self.assertEqual(2 + 2, 4)

  def tearDown(self):
    self.square = None
    