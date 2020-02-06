# pythonism

# Iterators
The call of the range of large numbers does not return the list of numbers, it returns a range object that is iterable. This object generates the million values one at a time, and only as needed. This technic has great advantage, because it allows use a loop on the big range but without settong aside a huge amount of memory for it. Also, if such a loop were to be interrupted in some fashion, no time will have been spent computing unused values of the range.

#  Generators
The most convenient technique for creating iterators in Python is through the use of generators. A generator is implemented with a syntax that is very similar to a function, but instead of returning values, a yield statement is executed to indicate each element of the series


#  Decorators
Create a decorator that adds behavior to a given function
