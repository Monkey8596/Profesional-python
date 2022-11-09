
#Intro
print('INTRO')

my_set = {3,4,5}
print('my_set =', my_set)

my_set2 = {'hola', 32.3, False, True}
print('my_set2 =', my_set2)

my_set3 = {3,3,2}
print('my_set3 =', my_set3)

#############################################

#_Add
print('ADD')

the_set = {1,2,3,4}
print(the_set)

the_set.add(5)
print(the_set)

the_set.update([5,6,7])
print(the_set)

#############################################

#Remove
print('REMOVE')

the_set.remove(7)
print(the_set)

the_set.discard(6)
print(the_set)

the_set.pop()
print(the_set)

the_set.clear()
print(the_set)

