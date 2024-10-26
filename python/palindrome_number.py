num = 123
def check_palindrome_number(num):
    temp = num
    reverse = 0
    while(temp>0):
        reminder = temp %10 
        reverse = (reverse*10)+ reminder
        temp = temp//10
    
    if(reverse==num):
        return True
    return False

print(check_palindrome_number(num))

        

