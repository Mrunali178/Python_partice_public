# min and max function --> to find max and min values of the list
numbers=[6,60,2]
print(min(numbers))
print(max(numbers))

# define a function which retrun greatest difference means max-min value
def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(numbers))