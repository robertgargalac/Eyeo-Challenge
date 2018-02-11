import unittest
import script


class KnownValues(unittest.TestCase):

    def test_money1(self):
        script.input = lambda: '5.47'
        result = script.coins()
        expected = '5 dollars\n1 quarter\n2 nickels\n2 pennies\n'
        self.assertEqual(expected, result)

    def test_money2(self):
        script.input = lambda: '99999999999999999999.99'
        result = script.coins()
        expected = '99999999999999999999 dollars\n3 quarters\n2 nickels\n4 pennies\n'
        self.assertEqual(expected, result)

    def test_money3(self):
        script.input = lambda: '0.55'
        result = script.coins()
        expected = '2 quarters\n1 dime\n'
        self.assertEqual(expected, result)

    def test_money4(self):
        script.input = lambda: '199'
        result = script.coins()
        expected = '199 dollars\n'
        self.assertEqual(expected, result)

    def test_money5(self):
        script.input = lambda: '1.5'
        result = script.coins()
        expected = '1 dollar\n2 quarters\n'
        self.assertEqual(expected, result)

if __name__ == '__main__':

    unittest.main()