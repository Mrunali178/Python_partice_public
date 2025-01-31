#lecture no.-155
#1. Iterable
# An iterable is any object in Python that can be looped over (e.g., using a for loop). These objects have the ability to produce an iterator using the iter() function.

# Key Characteristics:
# It is an object that can return its items one by one.
# It does not store the current state of iteration.
# Examples of iterables:
# Lists ([1, 2, 3])
# Tuples ((1, 2, 3))
# Strings ("hello")
# Sets, dictionaries, and ranges.
# Example:

my_list = [1, 2, 3]  # List is an iterable
for item in my_list:
    print(item)  # Outputs: 1
                            # 2
                            # 3
# You can create an iterator from an iterable using the iter() function:

my_list = [1, 2, 3]
iterator = iter(my_list)  # Converts the list to an iterator
#if we directly apply next function to an iterable it will give typeerror
l=[1,2,3]
# next(l)  #o/p--> TypeError: 'list' object is not an iterator

#if we call next function directly on a iteratoe it will work

# 2. Iterator
# An iterator is a special object that represents a stream of data. It remembers where it is in the iteration process and provides elements one at a time when requested.

# Key Characteristics:
# It is created by calling iter() on an iterable.
# It has a __next__() method to get the next value.
# Once the items are exhausted, it raises a StopIteration error.
# An iterator can only be traversed once.
# Example:
# python
# Copy
# Edit
my_list = [1, 2, 3]  # Iterable
iterator = iter(my_list)  # Create an iterator

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# # next(iterator) would raise StopIteration


# Key Differences:-
# Feature	    Iterable	                                Iterator
# Definition	Can be looped over (e.g., using for).	    Produces the next item using next().
# State	        Does not track iteration state.	            Keeps track of its position in the iterable.
# Usage	        Used as the source for iteration.	        Used to get one value at a time.
# Examples	    Lists, strings, dictionaries, etc.	        Result of iter() on an iterable.
# Exhaustion	Can be converted to an iterator again.	    Once finished, cannot be restarted.

# How They Work Together
# Iterable → Iterator: You can create an iterator from an iterable using iter().

# Iterator → Values: You can use next() on an iterator to get the values one at a time.

# Example Combining Both Concepts:

my_list = [1, 2, 3]  # This is an iterable
squares=map(lambda a:a**2,my_list) # iterator

print(next(squares))  # Output: 1
print(next(squares))  # Output: 4
print(next(squares))  # Output: 9
# next(iterator) would raise StopIteration (at the end of the list)

#iterator can directly use next() functon but iterable can't it have to first use iter function then the next functionn can work 
# Summary
# Iterable: Something you can loop over (e.g., lists, strings, etc.).
# Iterator: A tool to get items one by one from an iterable. It's what powers iteration under the hood.