import sys
import unittest
sys.path.append('../')
from derivada import derivar

class test_v(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(derivar('a', 'a'), 'ε')

unittest.main()
