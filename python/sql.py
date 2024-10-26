word = "aeiouksIAE"
count = 0
def find_no_of_vovwels(x):
    count=0
    # vowels =  ["A", "E","I","O","U","a","e","i","o","u"]
    vowels="aeiouAEIOU"
    # x = x.lower()
    for i in x:
        if( i in vowels):
            count+=1
    return count

def find_each_no_of_vowel(x):
    dict_vowel={"a":0,"e":0,"i":0,"o":0,"u":0}
    x= x.lower()
    for i in x:
        if i in dict_vowel:
            dict_vowel[i]+=1
        else:
            continue
    # vowel_list=[(i,count) for i,count in dict_vowel.items()]
    return dict_vowel
print(find_no_of_vovwels(word))
print(find_each_no_of_vowel(word))
print(set(word))
