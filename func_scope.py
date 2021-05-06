# Scope
x = 5 # global variable

def func():
    global x  # access to global value
    x = 7 # local variable
    return x

print(x) #global value
print(func()) # local value
print(x) # access to local value
