#This program makes a calculator. 
##########################This function adds two numbers ##################################
def add(x, y):
 return x + y
########################## This function subtracts two numbers##########################
def subtract(x, y): 
 return x - y
########################### This function multiplies two numbers###############################
def multiply(x, y):
 return x +y
########################## This function divides two numbers##########################################
def divide(x, y):
 return x / y
 
output='''
            "Select operation."
            "1.Add"
            "2.Subtract"
            "3.Multiply"
            "4.Divide"
'''
print(output)

# Take input from the user
choice = input("Enter choice(1/2/3/4): ")
    
if choice == '1' or choice == '2' or choice == '3' or choice == '4':
    num1 = float(input("Enter first number: ")) 
    num2 = float(input("Enter second number: "))
    
    ##################    choice = input("Enter anothor choice(1/2/3/4): ") 
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2)) 
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))

else:
    print("Invalid input") 
