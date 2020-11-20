# 1a) Let's say we also wanted to create another class called chef, which is a child of the human class. We can link "parent" and "child" classes by putting the
# name of the parent class inside of the parentheses of the child class. Create a class called chef that is a child of the human class.
#Comment your chef code when you're done

class human():
  pass
  
  
  
  
  
 # 1b) Now that you've created a chef class, create a chef object below:
 #HINT: Look at the markdown file if you need help creating an object
 #Comment code when you're done
 
 
 
 
 
 
 
# 2a) Like we mentioned in the markdown file, objects can have have characteristics that we call properties. For example, if I was creating a chef object, I may seek
#to define it as having some characteristics (e.g. name, type of cuisine they cook, type of chef, years of experience). In order to do this, I need to use what's
#known as an initialization function. Observe the function definition below:
 
'''
def __init__(self, name, cuisine, type, experience):
  self.name = name
  self.cuisine = cuisine
  self.type_of_chef = type
  self.years_experience = experience
'''
#This function allows you to attach characteristics to your chef object. Most every class should have an __init__ function. The self parameter is necessary because
#it refers to the object you create in the class. Without the self parameter being first in every function definition, your functions wouldn't work on your objects.
#Re-define your chef class below, and then replace the pass in your chef class with the __init__ function defined above.
  
  
  
  
  
  
  
  
  
  
# 2b) Now that you have a class chef with the __init__ function inside, when you create your object, you can give it characteristics that refer to the properties
#defined in your __init__ function. To do this, when you create your object, put in a value for each property inside the parentheses.
#HINT: The format for defining an object is as follows: object_name = class(property1, property2, property3, property4). Type in actual values for the properties.
  
  
  
  
  
  
  
  
  
  
# 3a) Nice work! Now print your object and describe what you see in the output.







# 3b) Look back at your __init__ function. In that function definition, you included some lines of code that said things like self.name, self.type, etc. Instead of
# printing your object, print(object.type_of_chef), or any of the other properties defined in your __init__ functin and comment on what happens below:









###Comment all code up until this point and then keep going###

# 4a) In addition to the _init__ function, you can define other functions/methods inside your class. Go ahead and copy and paste your chef and human classes below.
#In addition to an __init__ function in your chef class, define three methods/functions that a chef could do (cooking, chopping, baking, etc.). All each function
#has to do is print the words cooking, chopping, baking etc. In the human class, include a method/function for breathing.
HINT: Don't forget to include a self parameter in your function/method definitions











# 4b) Create a chef object and give it 4 properties. Then, call the methods/functions you defined in your classes on your object.
#HINT: In turtle for example, the way to say something like this is t.forward(100), where forward is the method/function, and t is the object.








# 4c) Can you use the breathe method/function you defined in your human class on a chef object? Why or why not?









# 5a) Put everything you learned up to this point to use! Create two classes called animal and frog, where animal is a parent class of the frog class. Inside the frog
#class, include an __init__ function that has 3 properties: frog_name, frog_color, and frog_fave_food. In addition to this, define 3 methods/functions in the 
#frog class: swim, ribbit, and hop, where each method/function just prints the word swim, ribbit or hop. In the animal class, define at least one method/function
#such as breathing, eating, etc.







# 5b) Now that your classes are created, create a frog object and give it values for the name, color and favorite food. Next, print each frog property to the console.
# Then, use a couple of your methods on your frog object.











#######################BONUS QUESTION#############################


# 1) Create a circle class that outlines a circle object in such a way that when you create the object, you can give it a radius. Then, you can call methods/functions
#on the circle object to calculate the area and circumference of it.












  
  
