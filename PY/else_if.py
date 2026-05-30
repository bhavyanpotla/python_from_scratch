a=int(input('Enter the value of "a":'))
 

if a%2==0 : 
    print('"a" is an even number')
else:
    print('"a" is a odd number')

year=int(input('Enter a year:'))
if year%4==0:
    if year%100==0:
         if year%400==0:
              print(f'yah bro {year} is a leap year')
        
    else : 
        print(f'yah bro {year} is a leap year')

else:
    print(f"{year} isn't a leap year")