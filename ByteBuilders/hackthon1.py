def function(string):
	string = string.split(" ")
	length = [len(words) for words in string]
	highest = max(length)
	for words in string:if len(words) == highest :return words
	
print(function("The Quick brown fox jumped"))

		

	

	
	
		