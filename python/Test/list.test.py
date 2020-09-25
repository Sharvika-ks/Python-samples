'''# Type your code here
sample_list = [2, 10, 3, 5]
add=0
for num in sample_list:
    ###print(num)
    add = num
    ##print("Welcome",num)
print(add)
print("move 10 steps")
for i in range(1,10):
    print("Step number",i)
    
'''
sample_list = [2, 10, 3, 5]
add=0
ele_count=0
for num in sample_list:
    ##print("add",add ,"num",num)
    add = num+add
    ele_count+=1
average=add/ele_count

print(add)
print(ele_count)
print(avg)

