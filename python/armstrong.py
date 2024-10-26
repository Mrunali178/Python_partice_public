num = 1534
def check_armstrontg(num):
    temp = num
    derived_num =0
    while(temp>0):
        reminder= temp%10
        derived_num = derived_num + (reminder*reminder*reminder)
        temp = temp//10
    if(num==derived_num): return True
    return False

print(check_armstrontg(num))


        