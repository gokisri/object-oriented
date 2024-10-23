# tv.py

class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.on_off_status = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume is at maximum.")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is at minimum.")

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            print(f"Channel {channel} is not available. Staying on channel {self.channel}.")

    def reset(self):
        self.channel = 1
        self.volume = 50
        print("TV has been reset to default settings.")

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}."
