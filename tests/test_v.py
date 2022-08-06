import sys
import unittest
sys.path.append('../')
from derivada import v

class test_v(unittest.TestCase):

    def test_1(self):
        self.assertEqual(v('∅'), '∅')

    def test_2(self):
        self.assertEqual(v('ε'), 'ε')

    def test_3(self):
        self.assertEqual(v('a'), '∅')

    def test_4(self):
        self.assertEqual(v('ab'), '∅')

    def test_5(self):
        self.assertEqual(v('a*'), 'ε')

    def test_6(self):
        self.assertEqual(v('a+b'), '∅')

    def test_7(self):
        self.assertEqual(v('a+b*'), 'ε')

unittest.main()
