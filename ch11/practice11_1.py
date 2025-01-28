# **kwargs (keyword argument)
# same as ars but is of type dictionary ars is tuple
# kwargs as an parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i,j in kwargs.items():
        print(f"{i}:{j}")
    
func(first_name="mru",last_name="Bavi")
