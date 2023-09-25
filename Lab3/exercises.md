# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *It is a concrete class. In python, abstact class should inheritate from ABC.*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *To delete an instance of the Image. It is called when the instance is about to be destroyed. It is also called a finalizer or (improperly) a destructor*
1. What class does Texture inherit from?
	- *Image*
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *It inherits all the attributes and methods defined in Image*
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *I think it should be a 'has-a' relationship with Image, because an Image could have a texture, but it does not make sense to say texture is an image.*
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *Yes, it does. It is proved that I do not provide an constructor for Texture, and I use it in the constructor of Image, and my code is still working.*

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

*It depends on how you implement it. For example, if multiple threads attempt to create an instance of the singleton simultaneously, it's possible for them to create multiple instances.*  
  
