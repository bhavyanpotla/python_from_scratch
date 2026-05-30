pizza_size = input("What pizza would you like to have small(s)/medium(m)/large(l): ")
bill = 0

# Pizza size selection
if pizza_size == 's' or pizza_size == 'S':
    bill += 100
    print("Small pizza price is 100 rs.")
elif pizza_size == 'm' or pizza_size == 'M':
    bill += 200
    print("Medium pizza price is 200 rs.")
elif pizza_size == 'l' or pizza_size == 'L':
    bill += 300
    print("Large pizza price is 300 rs.")
else:
    print("Invalid choice, kindly try again!")

# Pepperoni option
print("Would you like pepperoni?")
print("1. Yes")
print("2. No")
pepperoni = input("Enter your choice: ")

if pepperoni == '1':
    bill += 30
    print("Pepperoni added (30 rs).")

# Extra cheese option
print("Do you want extra cheese?")
print("1. Yes")
print("2. No")
cheese = input("Enter your choice: ")

if cheese == '1':
    bill += 20
    print("Extra cheese added (20 rs).")

print("----------------------------")
print(f"Your final bill is {bill} rs")
print("----------------------------")
print("*** Thank You, Visit Again ***")





