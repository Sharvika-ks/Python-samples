choice=int(input('Choose 1.addition 2.subtraction 3.Multiplication 4.division  ::  '))
if choice==1:
   a,b=input('enter a and b').split(",")
   a,b=int(a),int(b)
   print(a+b)
elif choice==2:
   a,b=input('enter a and b').split(",")
   a,b=int(a),int(b)
   print(a-b)
elif choice==3:
   a,b=input('enter a and b').split(",")
   a,b=int(a),int(b)
   print(a*b)
elif choice==4:
   a,b=input('enter a and b').split(",")
   a,b=int(a),int(b)
   print(a/b)
else:
    print('Invalid input') 
    
 