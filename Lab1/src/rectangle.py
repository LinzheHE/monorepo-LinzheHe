"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractmethod

class Shape(ABC):   
    @abstractmethod
    def set_values(self, width, height):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_values(self, width, height):
        self._width = width
        self._height = height
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height

    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Call a member function
    rect.set_values(5, 6)

    # Print out the area function
    print("area:", rect.area())

    # test the getters
    print("width and height:", rect.get_width(), " ", rect.get_height())
