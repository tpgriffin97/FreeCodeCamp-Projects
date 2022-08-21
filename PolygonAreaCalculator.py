class Rectangle:
    """
    In this project you will use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.
    """
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_area(self):
        self.area = self.width * self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width >= 50:
            return "Too big for picture."
        picture += ("*" * self.width + "\n") * self.height
        return picture

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


# Child class of the Rectangle class
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side


