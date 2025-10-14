import unittest
import hackthon1

class TestFunctions(unittest.TestCase):
	def test_that_my_function_does_not_take_empty_list(self):
		self.assertRaises(ValueError, hackthon1.function, [])
	
	#def test_that_my_function_take_only_list_that_contain_integer(self):
		#self.assertRaises(ValueError, hackthon1.function, ["Ade","1"])


	def test_that_my_function_take_on_list_that_contain_string(self):
		self.assertRaises(ValueError, hackthon1.function, ["Ade","1"])

	def test_that_my_function_does_not_take_empty_list_2(self):
		self.assertRaises(ValueError, hackthon1.function, [[],[]])


	#def test_that_my_function_return_correct_result(self):
		#result = hackthon1.function()
		#expected = 10