import math
arr = [2,5,6,1,3]
highest_number =-9999
second_highest_number =-9999

for i in arr:
    if(i>highest_number):
        highest_number =i
    elif highest_number>i and second_highest_number<=i:
        second_highest_number = i 




