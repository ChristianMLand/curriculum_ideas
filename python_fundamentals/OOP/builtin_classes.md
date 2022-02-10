# TODO 
- better explanations and usage examples
- protocol
    - duck typing
- abc
    - abstractmethod
    - using ...

# Enums
Enums are a very unique type of class in python used for defining a set of fixed options to be used in your program somewhere. It has several unique properties, so let's take a look at a few of them.
- class attributes defined inside the enum, have the enum as their type
- enum attributes have names and values similar to key, value pairs in a dictionary
- passing in a value to the class constructor, will return you the matching enum if exists
- the auto method will generate unique integer values for your enums if their values are arbitrary
```py
from enum import Enum, auto

class Method(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()

print(Method.GET)# prints Method.GET
print(Method.GET.name)# prints GET
print(Method.GET.value)# prints 1
print(type(Method.GET))# prints <enum 'Method'>
print(Method(1))# prints Method.GET
```

# Dataclasses
Dataclasses, as the name suggests, are classes with the goal of being purely a container for data. Although dataclasses can have methods, it's generally considered best practice top keep the focus of the class on the data itself. Dataclasses allow us to write our classes in a more convenient way, and handles many standard dunder methods that we may want to implement by default.
- create a dataclass using the `@dataclass` decorator
- instance attributes for a dataclass can be writing like class attributes, but with type annotations rather than assigning a value
```py
from dataclasses import dataclass

@dataclass
def Point:
    x: int
    y: int

p = Point(1,0)
print(p)# prints Point(x=1, y=0)
print(p.x, p.y)# prints 1 0
```
# Protocols

# Abstract Base Classes
