

def mult_callback(a,b):
    return a*b


def add_callback(a,b):
    return a+b


def pow_callback(a,b):
    return pow(a,b)

def print_table(n, operator_str, operation_cbk):
    for i in range(1, 10):
        print(i, operator_str, n,"=", operation_cbk(i,n))


print_table(2, "x", mult_callback)
print()
print_table(2, "+", add_callback)
print()
print_table(2, "^", pow_callback)
