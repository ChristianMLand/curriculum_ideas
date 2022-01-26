# TODO

# Lambdas
Previously we learned that we can define functions in python using `def`, which so far has satisfied all our function making needs. However, imagine we wanted to make a function where we could apply some operation to every element in a list. Now if we know that operation is going to be the same every time, we can handle that with a simple for loop, but what if we want to be able to apply any operation we want? Well, I suppose we could define a function for each potential operation we might want to apply, and then pass in that function to our map function. 
```py

def square(n):
    return n * n

def invert(n):
    return n * -1

def map(arr, func):
    new_arr = []
    for element in arr:
        new_arr.append(func(element))
    return new_arr

my_list = [1,2,3,4,5]
print(map(my_list,square))
print(map(my_list,invert))
```
However, this bloats our file with functions that we may only need to use once in this very specific situation, not to mention the functions being very simple with only a single return statement. So what alternatives do we have then? Lambdas are anonymous functions often used for this very purpose of passing a simple function as an argument to another function.
```py
my_list = [1,2,3,4,5]
print(map(my_list,lambda x: x * x))
print(map(my_list,lambda x: x * -1))
```