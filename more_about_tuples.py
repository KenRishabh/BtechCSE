# lopping in tuple
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4.0)

# for loop are tuple
for i in mixed:
    print(i)
# NOTE - you can use while loop too


# tuple with one element
nums = (1) # it's not a tuple # if you want to make it tuple you have to put , after. (1,)
nums = (1,)
words = ('word1')
words = ('word1',)
print(type(nums))
print(type(words))

# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

# tuple unpacking
guitarists = ('maneli jamal', ' eddie van der', 'andrew foy')
guitarist1, guitarist2, guitarist3 = (guitarists)
print(guitarist1)


# list inside tuples
favorites = ('southern magnolia', ['tokyo ghoul theme', 'landscape'])
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)

# min(), max(), sum

print(min(mixed))
print(max(mixed))
print(sum(mixed))

