#ALWAYS REMEBER input function DIRECTLY RETURN "string datatype"
print(3*'"navin reddy\'s" "lectures"')
x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))
z=x+y
print("the sum of the 2 numbers is:",z)

ch=input('enter a character:')
print(ch[0]) #here 0 is placed in the index so that only one char is printed 
print(ch)    #to print the whole string or multiple chars its this   <<<<<<==


# WHAT IF U ONLY WANT THAT B AS THE ASSIGNMENT TO THE CHARACTER {DO LIKE THIS}

chr=input('enter a character:')[1]
print(chr)


print(2+6-1)
# TO EVALUTE THIS TYPE OF EXPRESSIONS THERE IS AN INBUILT FUNCTION THAT IS eval()
result = eval(input('enter an expression:'))
print(result)

print(len(ch))