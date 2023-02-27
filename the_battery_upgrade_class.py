"""..."""


from the_car_class import ElectricCar

class BatteryUpdate(ElectricCar):
    """..."""

    def __init__(self, make, model, year,new_battery_size):
        """..."""
        super().__init__(make, model, year)
        # self.battery_size = new_battery_size -> Method - 1
        self.new_battery_size = new_battery_size

    # Method - 2
    def update_battery(self):
        """..."""
        self.battery_size = self.new_battery_size


car_1 = BatteryUpdate("Audi","53","23",20)
print(car_1.describe_battery())
car_1.update_battery()
print(car_1.describe_battery())
        