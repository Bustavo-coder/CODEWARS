user_input = input("Enter The Number To check if is a palidome \n")
palidome = ""

for letter in reversed(user_input) :
	palidome += letter

print(palidome)

if palidome == user_input :
	print("It is a palidome")
	
else : print("it is not a palidome") 
	

	
	

	