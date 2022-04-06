# WIP

# Four Pillars
## Abstraction
> Hide the implementation details of the class and only show the essential attributes.

This is accomplished through the usage of access modifiers as well as techniques like composition. This is useful for providing a simple to use interface for the end user while still being able to have complex functionality behind the hood.

## Encapsulation
> Bundling data and methods (functionality) together into a class.

Wrapping coupled data and methods together into a class not only helps with organization and debugging, but also allows for information hiding and abstraction to take place.

## Inheritance
> A class' ability to inherit attributes and methods from other classes.

Inheritance is great for when you have multiple classes with similar attributes and it logically makes sense to be grouped together in a hierarchy. 

## Polymorphism
> Classes that inherit from each other being able to invoke the same method with the same parameters and it having different implementation details.

Polymorphism is useful when a subclass needs a method to function differently than it's parent class, without changing how it's invoked.

# SOLID Principles
## **S**ingle responsibility principle
> Every class and every function should have only one responsiblity

Try to not have your functions or classes do too much, seperating the responsibilities into multiple functions/classes not only helps with organization and debugging, but also tends to make your code more reusable and extensible.

## **O**pen-closed principle
> Software should be open for extension, but closed for modification

This means that once some piece of code is "complete", if you later need to add or change some functionality of it, rather than going in and modifying the original code, you should write new code that works with the old code instead. A great example of this is the decorator pattern!

## **L**iskov substitution principle
> An instance of a parent class should be able to be replaced with an instance of a subclass without breaking the program.

This essentially means that overriden methods in a subclass should have the same function signature as the parent class, as well as retaining the same semantic meaning to the paramaters and return of the function. 

## **I**nterface segregation principle
> Multiple specialized interfaces are better than one general-purpose interface.

The reasoning for this, is so that you don't end up with classes implementing an interface where they don't actually need all of it's methods and attributes. If there is a situation where a class only needs some of the functionality of the interface, rather than the whole thing, you should split the interface up further until that is no longer true.

## **D**ependency inversion principle
> Depend upon abstractions rather than concrete implementations.

# General tips
- Model your classes based on behaviours not properties
- Model your data based on properties and not on behaviours
- favor composition over inheritance
- When thinking about whether to use an abstract base class, an interface, or composition, consider the the following:
## IS 
> "Example: a truck IS drivable"

This is used for describing _interfaces_. It's often useful to pull out functionality into an interface, because we can then have other unrelated classes implement the same interface, without actually knowing anything about each other. A great example of this would be a boat class. A boat is so different from a truck, that it doesn't make sense for there to be any sort of heirarchical relationship between the two, and yet they both can be driven. By pulling out Drivable into an interface, we can then later have something like a Driver class, which can work with anything that implements the Drivable interface. Because Truck and Boat both implement Drivable, the Driver class doesn't need seperate logic for driving a Truck vs driving a Boat.
## IS A
> "Example: a truck IS A vehicle"

This is used for describing _base classes_ for inheritance.
## HAS A 
> "Example: a truck HAS A radio"

This is used for describing _composition_. The truck doesn't need to know how the radio works in order to function, so all of the radio implementation details can be _abstracted_ into its own class, and _composed_ as an attribute of the Truck class. Without composition, if you ever wanted to upgrade the radio in the Truck, you would have to go into the Truck class and modify all of the methods that had to do with the radio. Instead, now we can simply swap out the radio object for a a new one, and we don't need to modify any of the Truck logic.
