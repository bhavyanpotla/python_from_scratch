height=float(input('what\'s your height in feet:'))
if height>=3:
    print("you are eligible to ride")
    age=int(input("what's your age? :"))
    if age<7:
        bill=150
        print("fare=150rs")
    elif age<=18:
        bill=250
        print("fare=250rs")
    else:
        bill=500
        print("fare=500rs")
    want_photo = input("do u want to take photos(yes/no)?")
    if want_photo == 'yes': 
        bill=bill+50
    print(f"your total bill is {bill}")

else:
    print("you are not eligible to ride , BYE! ")