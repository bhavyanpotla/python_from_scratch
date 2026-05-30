print(round(22.67))         #23
print(round(22.47))         #22
print(round(22.57))         #23
print(round(22.50))         #22===> it will return the nearest "even integer"
print(round(22.673,1))      #22.7
print(round(22.673,2))      #22.67
print(round(22.673,3))      #22.673
print(round(22.673,0))      #23.0
print(round(674,2))         #674
print(round(674,0))         #674
print(round(674,-1))         
# this type of cases handle with (10^(-number given))=pre-answer ;then pre-answer multiple lo daggar ga unna daniki round cheyali
print(round(674,-1))        #670 {(10^(-(-1)))=10 ; so 670 or 680 ; 674 is near to 670}
   # finally 670//

print(round(674,-2))        #700  {600 or 700 ; so 700//}   
print(round(674,-3))        #1000 {0 or 1000 ; so 1000//}
print(round(674,-4))        #0    {4 is greater than the number taken digits (3)}
print(round(665,-1))        #660
print(round(675,-1))        #680
print(round(6.75,1))        #6.8
print(round(6.85,1))        #6.8
print(round(674.1012,-1))   #670.0
print(round(1212,-2))       #1200



