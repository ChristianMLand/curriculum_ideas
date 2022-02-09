# TODO 
- Simpler code examples
- better explanations of usage
- methods
    - `__repr__, __str__`
    - `__eq__, __gt__, __lt__`
    - `__iter__, __next__`
    - `__getitem___, __setitem__`


# Dunder/Magic Methods in Python

So far, when writing our classes in Python, the first thing that we always end up creating is our `__init__` method. We've learned that it needs to be named exactly that to work, and that we use it to assign what attributes we want our objects to have. But why does the name of this function matter, and how does Python know to call this method in particular when we invoke the class? Dunder methods in Python are functions that have already been created as a part of all classes, and the Python language utilizes those functions, in order to determine how different things should interact with that class. When we write a dunder method in our classes, we are actually ***overriding*** the original dunder method, and replacing it with our own implementation. Dunder methods are unique in that, they should never be called explicitly, and instead are called internally by the Python language itself. To better illustrate, let's take a look at some examples of dunder methods and what functionality they provide for us.

# Examples:
## `__init__`
- Used for populating and assigning the initial attributes for an instance of the class
- gets called when invoking the class itself
```py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

new_node = Node(1)# invokes the __init__ method
print(new_node.value)# prints 1
```
## `__len__`
- Used for calculating the length of an instance of a class (if applicable)
- gets called when invoking the `len()` function
```py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self, *args):
        self.head = None

        for arg in args:
            self.add_to_back(arg)

    def add_to_front(self, value):
        '''Creates a Node object from the value and adds it to the front of the SLL'''
    
    def add_to_back(self, value):
        '''Creates a Node object from the value and adds it to the back of the SLL'''

    def __len__(self):
        count = 0
        runner = self.head

        while runner != None:
            runner = runner.next
            count += 1
        return count

arr = SLL(10,9,8,7,6)
print(len(arr))# invokes the __len__ method, should print 5
```
## `__call__`
- Allows invoking an instance of the class like a function
```py
class Player:
    def __init__(self, name):
        self.name = name
        self.damage_taken = 0
        self.stamina_used = 0
        self.attacks = {}

    def add_attack(self, name, power, cost):
        '''Adds an attack object to the players attacks dictionary'''
        self.attacks[attack.name] = Attack(name, power, cost)# create instance of attack class and store it in dict

    def use_attack(self, atk_name, target):
        '''Retrieves the attack by name from the players attacks dictionary, and then calls it'''
        attack = self.attacks.get(atk_name)# retrieve instance of attack class from dict
        return attack(attacker=self, defender=target)# call instance of attack class like a function

class Attack:
    def __init__(self, name, power, cost):
        self.name = name
        self.power = power
        self.cost = cost

    def __call__(self, attacker, defender):
        attacker.stamina_used += cost
        defender.damage_taken += power
        print(f'{attacker.name} used {self.name} on {defender.name} for {self.power} damage!')

player1 = Player("Chris")
player2 = Player("Jim")
player1.add_attack(name='punch', power=20, cost=10)
player1.use_attack(name='punch', target=player2)# calculates the damage and prints the output
```
## `__str__` and `__repr__`
- Destermines how instances of the object are represented
- `__str__` is meant to be readable and useful for the end user
- `__repr__` is meant to be unambiguous and useful for debugging
```py
class 
```
