# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*I think for most functions they have a good name clearly describe what they do. But some are not very clear. For instance, the list(d) could be more clear if named as listKeys(d). pop(key[, default]) could be better if named as popAndGet().*


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Dictonary stores key-value pairs, while list stores values.*


3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes, we can access any element using their index.*


4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*pros: super flexible; users do not need to worry about the stored data type when define and use the containers.*
*cons: when a container contains different types of data, it is not friendly for some manipulations for all the elements in the container; and it's hard for other developers to understand the code.*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Personally I think the functions are well named. Their names are exactly what kinds request they will return, it is very straightforward.*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*No. I think most of the arguments are not necessary in developing.*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*It  It allows us to pass a dictionary of keyword arguments, where the keys are the argument names, and the values are the corresponding argument values. It makes the function more flexible because it can accept additional keyword arguments. However,  can make our code less clear and harder to understand.*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*It means the default value for that argument is None. When user does not provide value for that argument, the value of that argument will be none.*
*Yes, it can be set to anything besides Node, based on demand.*
*It allows users to omit some arguments, and it is convinient when some arguments are optional.*
