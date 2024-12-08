# function takes one int
# if abs is odd return True
# else return False

def is_odd(num):
    if abs(num) % 2 == 0:
        return False
    else:
        return True
    
print(is_odd(2))
print(is_odd(3))
print(is_odd(-5))