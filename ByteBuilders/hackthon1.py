def function(iterable):
	#if any(element.isalpha()for element in iterable):
		#raise ValueError("Can Only take in integers")
	length_list = list()
	new_text = iterable.split(" ")
	for elements in new_text:
		length_list.append(len(elements))
		length_list.sort()
	return  max(length_list)

print(function("The Quick brown fox jumped"))
		