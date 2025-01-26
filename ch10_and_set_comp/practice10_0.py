# dictionary comprehension
square={num:num**2 for num in range(1,11)}
print(square) #o/p--> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# or
squares={f"squre of {num} is" :num**2 for num in range(1,11)}
print(squares) #o/p--> {'squre of 1 is': 1, 'squre of 2 is': 4, 'squre of 3 is': 9, 'squre of 4 is': 16, 'squre of 5 is': 25, 'squre of 6 is': 36, 'squre of 7 is': 49, 'squre of 8 is': 64, 'squre of 9 is': 81, 'squre of 10 is': 100}

#or 
for k,v in squares.items():
    print(f"{k} : {v}")
#o/p-->
# squre of 1 is : 1
# squre of 2 is : 4
# squre of 3 is : 9
# squre of 4 is : 16
# squre of 5 is : 25
# squre of 6 is : 36
# squre of 7 is : 49
# squre of 8 is : 64
# squre of 9 is : 81
# squre of 10 is : 100

# word_count
string="harshit"
word_count={char:string.count(char) for char in string}
print(word_count) #o/p--> {'h': 2, 'a': 1, 'r': 1, 's': 1, 'i': 1, 't': 1}

# if else with dc
odd_even={value:('even' if value%2==0 else 'odd') for value in range(1,6)}
print(odd_even) #o/p--> {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}