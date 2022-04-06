# TODO
- Decorators that can accept functions with parameters
- Decorators that can have parameters of their own
- Class decorators

# Decorators
At this point we've worked with multiple decorators, `@classmethod`, `@staticmethod`, `@app.route()`, and most recently `@property`. But what exactly are decorators, and how do they work? There are two main types of decorators, function decorators, and class decorators. We will be focusing on function decorators for now, but will touch on class decorators in the future.

## Function Decorators
>Function decorators are functions that wrap around another function, in order to add some extra functionality without having to modify the original code. 

The first thing we should address is the syntax of how we use a decorator, and what that's doing behind the scenes. The `@` syntax that python uses, is actually just shorthand. It's the same as calling the decorator like a function, and passing in the function you want to wrap as an argument.
>Example usage of a decorator
```py
@test
def hello_world(self):
    return 'hello_world'

# is the exact same as

def hello_world(self):
    return 'hello_world'
hello_world = test(hello_world)
```
So that explains what the decorator syntax is doing, but what does a decorator actually look like? Let's take a look at a very basic example.
```py
# a decorator that prints out the result of whatever function its wrapping
def log(func):# function that takes another function as a parameter
    def wrapper():#create an inner function for the purpose of wrapping around the original function
        result = func()# call the original function and store the result in a variable
        print(f'The result of the function is: {result}')# print out the result
        return result
    return wrapper # return the wrapper function, effectively replacing the original function with it

@log#apply the log decorator to the hello_world function
def hello_world():
    return 'hello world'

hello_world()#prints 'The result of the function is: hello world'
```

There's definitely a lot going on here, so lets take a look at this line by line. First off, we create a function, that takes in another function as a parameter. Right away this throws a lot of people off, but you need to remember that functions are just another datatype in python, and can be used in the same way any other variable can, including being passed as an argument to a function! Next we define a new function inside of our decorator function. This is called a *higher-order function*, and has some really useful abilities. The most important one, is that since it was defined inside the scope of our decorator function, it has access to any other variables defined inside the same scope, including the `func` parameter. This means that once we return the `wrapper` function from our decorator and replace the original function, we still are able to have a reference to the original function through the `func` parameter. This concept is called a *closure*. This is a pretty advanced concept in computer science and can take a while to process, but as you see more examples it will hopefully start to click.

So why is that even useful? Well imagine we wanted to be able to keep track of how many times a function has been called. Without decorators and closures, we would need to modify our original function and add the counting functionality to it, which violates the `open-close` principle. The open-close principle states that functions and classes should be open for extension, but closed for modification. This means that if we want to add some new functionality to some existing code, rather than modifying the code, we should write new code that interacts with the old code in a way that achieves our goal. Decorators are a great way of accomplishing that!
```py
def counter(func):
    count = 0# declare a count variable in the decorators function scope
    def wrapper():
        nonlocal count#tell the wrapper function that count was defined in a different scope
        count += 1#increment the count
        print(f'The function has been called {count} times!')#print the count
        return func()#call the original function and return its result
    return wrapper

@counter#apply the counter decorator to the hello_world function
def hello_world():
    return 'hello_world'

hello_world()# prints hello_world has been called 1 times!
hello_world()# prints hello_world has been called 2 times!
hello_world()# prints hello_world has been called 3 times!
```
As we can see, it's actually quite simple to add this functionality with a decorator!

So far all of the decorators we have looked at have been for functions that didn't take any parameters. So how would we go about creating a decorator that can accept functions with parameters? 

```py

```

TODO
