# TODO
- condense explanations and simpler examples
- naming conventions
- docstrings
- type hints/annotations
    - variable type annotations
    - return type annotations
- doctests (maybe move this to unit tests?)

# Documenting Your Code
So far we've learned a lot about the syntax and structure of python, and how we can start to make some fairly complex projects. However, as our projects get more advanced, and we start to find ourselves working on teams with other developers, it becomes more and more important to make sure that we are properly documenting our code to make it as accessible to our peers as possible. It's important to note that the level of documentation you need, depends on the scale of your project. 
## Comments
Lets start off with the most basic form of documenting, which is simply adding comments to our code. At this point you have already seen plenty of comments and potentially even written some of your own. Although this isn't a new concept, it's still important to look at some situations to see where commments make sense, and where they don't, so let's look at some examples.
```py
# BAD
def fizzbuzz():
    for i in range(101):# loop from 0-100
        if i % 15 == 0:# if i is divisible by 15
            print("FizzBuzz")# print fizzbuzz
        elif i % 3 == 0:# if i is divisible by 3
            print("Fizz")# print fizz
        elif i % 5 == 0:# if i is divisible by 5
            print("Buzz")# print buzz
        else:# if not divisible by 3,5 or 15
            print(i)# print i
# GOOD 
def fizzbuzz2():
    for i in range(1,101):
        str = ""
        if i % 3 == 0:
            str += "Fizz"
        if i % 5 == 0:
            str += "Buzz"
        # if str is falsy (empty) then print i instead
        print(str or i)
```
Notice with the first example, every line is explained with comments, but the comments don't actually provide any new information that wasn't already clear by reading the code. Now this is not necessarily bad to do for yourself while you are learning, but as soon as you reach the point where you no longer need that extra information you should remove those comments. Ideally comments should be used to give some extra clarification or explanation to a piece of code that might not be immediately obvious at a glance. As we see in the 2nd example, the only comment was placed above the `print(str or i)` line of code to explain the reasoning for using the `or` operator here, as this usage is not as common and may not be immediately obvious to someone new looking at the code.
## Docstrings
Docstrings are essentially the new step up in documenting our code after basic comments. A docstring is denoted with `"""` before and after, and allows us to write multi-line strings as comments. Also, when using an ide such as VS Code, if you hover over a function or class, it will display the docstring for you in a little popup if one has been defined. One cool thing, is we can actually write markdown in our docstrings to format them nicely when display! Let's take a look at how to write docstrings and some common conventions with them in python.
```py
def multiply(a, b):
    '''
    Multiplies the given numbers together and returns the product

    ### Example usage:
    --------------
        ``multiply(3, 5) -> 15``

    ### Parameters
    ----------
        a (int): first number to be multiplied

        b (int): second number to be multiplied

    ### Returns
    -------
        product of multiplying a and b
    '''
    return a * b
```
