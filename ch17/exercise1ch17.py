# wirte a code for raising exception ZeroDivideException and valueerror
def divide(m,n):
    try:
        return m/n
    except ZeroDivisionError:
        print("division by zero not possible enter valid input..")
    except TypeError:
        print("input integer or float...")
    except:
        print("unexpected error...")
print(divide(2,0))