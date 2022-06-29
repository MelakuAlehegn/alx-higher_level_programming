#!/usr/bin/python3
'''
a class that defines a rectange
'''


class Rectangle:
    '''
    a rectangle class to define a rectange with setter
    and getter methods for height and width
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initializes the class attributes'''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return""
        else:
            for h in range(self.__height):
                for w in range(self.height - 1):
                    print(str(self.print_symbol) * self.__width)
                return str(self.print_symbol) * self.width

    def __repr__(self):
        x = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return x

    def __del__(self):
        print('{}'.format('Bye rectangle...'))
        type(self).number_of_instances -= 1

    @property
    def height(self):
        '''getter for height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height of rectangle
        raises TypeError if type is not int
        raises ValueError if value is < 0
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        '''getter for width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width of rectangle
        raises TypeError if type is not int
        raises ValueError if value is < 0
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def area(self):
        '''computes area of a rectangle'''
        return (self.width * self.height)

    def perimeter(self):
        '''computes perimeter of a rectangle
        return 0 if width or height is 0
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        static method that returns the biggest recrtangle
        raises TypeError is args are not instances
        '''
        if type(rect_1) is not Rectangle:
            raise TimeoutError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TimeoutError('rect_2 must be an instance of Rectangle')
        a1 = rect_1.area()
        a2 = rect_2.area()
        if a1 >= a2:
            return rect_1
        else:
            return rect_2
