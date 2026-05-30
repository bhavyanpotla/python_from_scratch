# BMI=weight/height^2

w=int(input('===> Enter the weight in(kgs):'))
h=float(input('===> Enter the height in(Mts):'))
print('--------------------------')
print('YOU\'RE DETAILS')
print('Weight=',w)  
print('Height=',h)
print('--------------------------')
bmi=w/h**2
print('BMI=',bmi)
if bmi<=18.5:
    print('--------------------------')
    print('bmi category: UNDERWEIGHT')
    print('--------------------------')
elif 18.5<=bmi<=24.9:
    print('--------------------------')
    print('bmi category: HEALTHYWEIGHT')
    print('--------------------------')
elif 25.0<=bmi<=29.9:
    print('--------------------------')
    print('bmi category: OVERWEIGHT')
    print('--------------------------')
elif bmi>=30.0:
    print('--------------------------')
    print('bmi category: OBESE')
    print('--------------------------')



 