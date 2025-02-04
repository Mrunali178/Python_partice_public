#multiple inheritance -- single chils multiple parent
class A:
    def class_a_method(self):
        return 'hello from class a'
    def hello(self):
        return "hello class a"
class B:
    def class_b_method(self):
        return 'hello from class b'
    def hello(self):
        return "hello class b"
class C(B,A): #class C(A,B) 
    pass

instance_a=C()
print(instance_a.class_a_method())  #o/p-->hello from class a
instance_b=C()
print(instance_b.class_b_method())   #o/p-->hello from class b

# but if a call hello method it will be called as pr oreder gib=ven in braces as this method is in both class here first A then B hence A hello method will be called
instance_b=C()
print(instance_b.hello())  #o/p--> hello class a ---->as class C(A,B) is the sequnece but if 

#class C(B,A) b hello method will be called ---> o/p--> hello class b
# other than help we can see mro by using mro method (gives o/p in list form) and .__mro__(p/p in tuple form) but using help gives in readble format

print(C.mro())  #o/p--> [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(C.__mro__)  #o/p--> (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

