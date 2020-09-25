"""age=int(input("Enter your age"))
if age<=0:
    print("UNBORN")
elif age<=150:
    print("ALIVE")
else :
    print("VAMPIRE")


num=int(input("Enter a number"))
if num%2==0 and num%3==0:
    print("BOTH")
elif num%2==0 or num%3==0:
    print("ONE")
else :
    print("NEITHER")
"""

hour=int(input("How many hours do you work??"))
salary=0
if hour>=0 and hour<=40:
    salary = hour*8
    print("YOU MADE ",salary,'DOLLARS THIS WEEK')
elif hour>40 and hour<=50:
    salary =(40*8)+(hour-40)*9
    print("YOU MADE ",salary,'DOLLARS THIS WEEK')
elif hour>50 and hour<=168:
    salary = (40*8)+(10*9)+((hour-50)*10)
    print("YOU MADE ",salary,'DOLLARS THIS WEEK')
else:
    print("INVALID")
#print("YOU MADE ",salary,'DOLLARS THIS WEEK')
