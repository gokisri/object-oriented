class Circle:
    def __init__(self, radius_list):
        # Initialize with the list of radii
        self.radius_list = radius_list

    def get_radii(self):
        # Return the list of radii
        return self.radius_list

    def calculate_areas(self):
        # Calculate areas for each radius in the list
        return [3.14159 * r ** 2 for r in self.radius_list]

    def calculate_circumferences(self):
        # Calculate circumferences for each radius in the list
        return [2 * 3.14159 * r for r in self.radius_list]


# Example usage
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)

print("Radii:", circle.get_radii())
print("Areas:", circle.calculate_areas())
print("Circumferences:", circle.calculate_circumferences())
