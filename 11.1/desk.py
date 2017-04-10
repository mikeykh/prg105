# imports the office_furniture method as of
import office_furniture as of


# The Desk class represents a subclass of the OfficeFurniture class
# The __init__ method accepts arguments for category, material, length, width, height and price
class Desk(of.OfficeFurniture):
    """
        The Desk class extends the OfficeFurniture class and
        adds the additional methods location_drawers and number_drawers
    """
    def __init__(self, category, material, length, width, height, price, location_drawers, number_drawers):
        # will call the parent class and pass arguments to it

        of.OfficeFurniture.__init__(self, category, material, length, width, height, price)

        # Initialize location_drawers and number_drawers
        self.__location_drawers = location_drawers
        self.__number_drawers = number_drawers

    # add the mutators for location_drawers and number_drawers
    def set_location_drawers(self, location_drawers):
        self.__location_drawers = location_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    # add the accessors for  location_drawers and number_drawers
    def get_location_drawers(self):
        return self.__location_drawers

    def get_number_drawers(self):
        return self.__location_drawers

    def __str__(self):
        print_line = "Category: " + self.get_category() + \
                     "\nDrawer Location(s): " + self.__location_drawers + \
                     "\nNumber of Drawers: " + str(self.__number_drawers) + \
                     "\nMaterial: " + self.get_material() + \
                     "\nLength: " + str(self.get_length()) + \
                     "\nWidth: " + str(self.get_width()) + \
                     "\nHeight: " + str(self.get_height()) + \
                     "\nPrice: " + "${:0,.2f}".format(self.get_price())
        return print_line
        # returns a string
