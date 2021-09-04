"""A class that can be used to represent a car."""
'''Example From: Python Crash Course 2nd Edition chapter 9
https://github.com/ehmatthes/pcc/blob/master/chapter_09/car.py'''

class Car():
    """A simple attempt to represent a NEW car."""

    def __init__(self, manufacturerIn, modelIn, yearIn):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturerIn
        self.model = modelIn
        self.year = yearIn
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
