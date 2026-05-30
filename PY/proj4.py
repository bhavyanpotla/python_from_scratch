#love calculator
#commented one is my method!
"""
him=input("enter his name:").lower()
her=input("enter her name:").lower()
print(f'his name is {him}')
print(f'her name is {her}')
t_count1=him.count('t')
r_count1=him.count('r')
u_count1=him.count('u')
e_count1=him.count('e')
l_count1=him.count('l')
o_count1=him.count('o')
v_count1=him.count('v')
e_count1=him.count('e')

t_count2=her.count('t')
r_count2=her.count('r')
u_count2=her.count('u')
e_count2=her.count('e')
l_count2=her.count('l')
o_count2=her.count('o')
v_count2=her.count('v')
e_count2=her.count('e')

true_sum=t_count1+t_count2+r_count1+r_count2+u_count1+u_count2+e_count2+e_count1
love_sum=l_count1+l_count2+o_count1+o_count2+v_count1+v_count2+e_count1+e_count2

print(f"love percentage between them is {true_sum}{love_sum}%")
"""

name1=input('what is ur name?:')
name2=input('what is his/her name?:')
combine=name1+name2 
low=combine.lower()

t=low.count('t')
r=low.count('r')
u=low.count('u')
e=low.count('e')
true=t+r+u+e

l=low.count('l')
o=low.count('o')
v=low.count('v')
e=low.count('e')
love=l+o+v+e

love_percentage=int(str(true)+str(love))
print(f'love_percentage:{love_percentage}%')

if love_percentage>=80:
    print('u can buy alekhya chitti pickles!')
elif love_percentage<30:
    print('career meedha focus chey mundhu!')
else :
    print('love lavada manaki vodhu dabbe manaki mudhu')
    


