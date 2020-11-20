# Classes and Objects

Believe it or not, whenever we've worked with turtle in Python, we've been using classes and objects! Observe the code below:
```
import turtle
t = turtle.Pen()
```
Here, we are creating an object from the pen class in the turtle library. In this example, t is the object! The proper definition of an object is a collection of data that functions can act on. The functions that can act on an object are called methods.
```
t.forward(100)
```
In the example above, .forward() is a method (or function) that acts on our object t. The method .forward(), as well as any other method that acts on a pen object (e.g. .backward(), .pensize(), .pencolor(), .left(), .right(), etc.) are all defined in the object's class (in this case, the pen class). A class is basically like the blueprint for how to create and interact with an object.

I like to think about it like this: If a human is a Python object, then a class is the human's DNA. The DNA, like a class, tells us every characteristic about the human (object). The DNA also defines everything that a human can do (e.g. run, jump, eat, speak, read, etc.). These things that the human can do can be considered methods, or functions that act on the human object.

In order to define a class, it's as simple as saying the following:
```
class human():
  pass
```
We use pass so the code doesn't give an error. Once you put some methods (functions) inside, you can remove pass from your class. If I wanted to create an object of class human, all I would need to do is the following:
```
h = human()
```
I've successfully created an object (h) of class human. Navigate to the python file to learn more about objects and classes!
