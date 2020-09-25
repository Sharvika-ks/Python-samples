"""
Using a for loop, write a program which asks the user to type an integer, n,
 and then prints the sum of all numbers from 1 to n (including both 1 and n).

"""
sum1=0
n=int(input("Enter a number:")) 
for i in range(1,n+1) :
    sum1=sum1+i
print(sum1)  