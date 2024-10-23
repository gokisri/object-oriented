# part 2.py

from tv import TV  # Import the TV class

class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = "Wide"
        self.backlight = "LED"

    def display_details(self):
        return (f"{self.brand} LED TV Details:\n"
                f"Screen Thickness: {self.screen_thickness} inches\n"
                f"Energy Usage: {self.energy_usage} watts\n"
                f"Lifespan: {self.lifespan} years\n"
                f"Refresh Rate: {self.refresh_rate} Hz\n"
                f"Viewing Angle: {self.viewing_angle}\n"
                f"Backlight: {self.backlight}\n")


class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = "Standard"
        self.backlight = "Plasma"

    def display_details(self):
        return (f"{self.brand} Plasma TV Details:\n"
                f"Screen Thickness: {self.screen_thickness} inches\n"
                f"Energy Usage: {self.energy_usage} watts\n"
                f"Lifespan: {self.lifespan} years\n"
                f"Refresh Rate: {self.refresh_rate} Hz\n"
                f"Viewing Angle: {self.viewing_angle}\n"
                f"Backlight: {self.backlight}\n")

# Example usage
led_tv = LedTV("Samsung", 1200, 55, 1.2, 150, 10, 120)
plasma_tv = PlasmaTV("Panasonic", 1000, 60, 1.5, 200, 8, 60)

led_tv.increase_volume()
led_tv.set_channel(45)
print(led_tv.status())  # Samsung at channel 45, volume 51
print(led_tv.display_details())

plasma_tv.decrease_volume()
plasma_tv.set_channel(60)  # Invalid channel
print(plasma_tv.status())  # Panasonic at channel 1, volume 49
print(plasma_tv.display_details())
