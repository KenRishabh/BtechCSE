#generate list with range function
#something more about pop method
#index method
#pass list to a function

## List in range
# numbers = list(range(1,11))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(numbers)

## pop
# print(numbers.pop())
# popped_item = numbers.pop()
# numbers.pop()
# print(numbers)

# #index
# print(numbers.index(1, 1, 11))
# print(numbers.index(1))

# pass list to a function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))
