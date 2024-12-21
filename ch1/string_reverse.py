string=input("give the sring")
# length = len(string)
reverse_string=""

for i in range(len(string)-1,-1,-1):
    reverse_string=reverse_string+string[i]
print(reverse_string)

for i in string:
    reverse_string= i + reverse_string
print(reverse_string)




