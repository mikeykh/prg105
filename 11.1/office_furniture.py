# the OfficeFurniture class holds general information
# about office furniture for sale
# it will be the parent class for desks, chairs, ect.


class OfficeFurniture(object):
    """
        accepts material, length, width, height, and price
    """
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    # Add Mutator Methods
    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    # Add Accessor Methods
    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    # String Method
    def __str__(self):
        line_item = "Category: " + self.__category + \
                    " material-" + self.__material + \
                    " length-" + str(self.__length) + \
                    " width-" + str(self.__width) + \
                    " height-" + str(self.__height) + \
                    " price= ${:0,.2f}".format(self.__price)
        return line_item
        # returns a string
