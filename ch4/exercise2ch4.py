# check whetater the string is palindrome or not
def is_palindrome(string):
    reverse=string[::-1]
    if (reverse==string):
        return True
    return False
string=input("enter a string : ")
print(is_palindrome(string))