import unittest
import hackthon1

class TestFunctions(unittest.TestCase):
	def test_that_my_function_return_correct_result(self):
		result = hackthon1.function("The Quick brown fox jumped")	
		expected = "jumped"
		self.assertEquals(result,expected)
		
		