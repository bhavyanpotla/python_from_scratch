# program for picking one among a grp to pay the bill in the restaurant  
#("without using the random.choice()")
print('DISCLAIMER : This is totally a computer generated selection!!!')
names=input('enter the names of the payers(by seperating with comma\'s):')   #bhavyan,vishnu,deepak,hemanth,lokesh,gokul,banu 
names_splitted=names.split(",")
print(names_splitted)
length=len(names_splitted)-1
print(length)
 
import random
index=random.randint(0,length)
name_payer_final=names_splitted[index]
print(f'MR./MRS./MS.{name_payer_final} will pay the bill(using randint)')

name_payer_choice=random.choice(names_splitted)
print(f'MR./MRS./MS.{name_payer_choice} will pay the bill(using randchoice)')

