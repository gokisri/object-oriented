class Circle:
    __pi = 3.141  # Private class variable for Pi

    def __init__(self, radius_list):
        # Initialize with the list of radii
        self.__radius_list = radius_list  # Private instance variable for storing radii

    def get_radii(self):
        # Return the list of radii
        return self.__radius_list

    def calculate_areas(self):
        # Calculate areas for each radius in the list using the class's private Pi value
        return [self.__pi * r ** 2 for r in self.__radius_list]

    def calculate_circumferences(self):
        # Calculate circumferences for each radius using the class's private Pi value
        return [2 * self.__pi * r for r in self.__radius_list]


# Example usage
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)

print("Radii:", circle.get_radii())
print("Areas:", circle.calculate_areas())
print("Circumferences:", circle.calculate_circumferences())
