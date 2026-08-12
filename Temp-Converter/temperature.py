# Temperature conversion classes 
class Temperature:
    """Base class for a parsed temperature value and its conversion."""

    unit_name = ""
    converted_unit_name = ""

    # Initialize with a numeric value (float or int).
    def __init__(self, value: float):
        self.value = value

    # Convert this temperature's value to the other unit.
    def convert(self) -> float:
        raise NotImplementedError

    # Return the converted value rounded to two decimal places.
    def converted_value(self) -> float:
        return round(self.convert(), 2)


# Subclasses for specific temperature units
class Fahrenheit(Temperature):
    unit_name = "Fahrenheit"
    converted_unit_name = "Celsius"

    def convert(self) -> float:
        return (self.value - 32) * 5 / 9

# Subclasses for specific temperature units
class Celsius(Temperature):
    unit_name = "Celsius"
    converted_unit_name = "Fahrenheit"

    def convert(self) -> float:
        return self.value * 9 / 5 + 32
