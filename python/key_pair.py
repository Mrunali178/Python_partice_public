arr = [1, 4, 45, 6, 10, 8]
x = 16

def find_key_pair(l,n):
    key_pair={}
    for index,value in enumerate(l):
        if n-value in key_pair:
            print(key_pair)
            return True
        else:
            key_pair[value]=index
    print(key_pair)
    return False

print(find_key_pair(arr,x))
