start_num=0
end_num = 100
current_num = start_num
while current_num<=end_num:
    current_divisor=2
    is_current_number_prime=True
    while (current_divisor<current_num):
        if current_num%current_divisor==0:
            is_current_number_prime=False
            break
        current_divisor=current_divisor+1
    if is_current_number_prime :
        print (current_num,"is prime")
    current_num=current_num+1
print ("All Done")