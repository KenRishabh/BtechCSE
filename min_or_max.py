# min and max function

numbers = [6,60,2]
print(min(numbers))
print(max(numbers))

# difference of max and min

def greatest_diff(l):
    return max(l) - min(l)

print(greatest_diff(numbers))