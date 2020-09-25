'''Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) 
and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. For example if 'n' is equal to 4
 then the output should look like the following:
 10**0=1
10**1=10
10**2=100
10**3=1000
...
...
10**n=n
'''
n = int(input("Enter a number"))
for i in range(0,n+1):
    print(10**i) 
