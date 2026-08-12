class Temperature:
    """Base class for a parsed temperature value and its conversion."""

    unit_name = ""
    converted_unit_name = ""

    def __init__(self, value: float):
        self.value = value

    def convert(self) -> float:
        """Convert this temperature's value to the other unit."""
        raise NotImplementedError

    def converted_value(self) -> float:
        """Converted value, rounded to two decimal places."""
        return round(self.convert(), 2)


class Fahrenheit(Temperature):
    unit_name = "Fahrenheit"
    converted_unit_name = "Celsius"

    def convert(self) -> float:
        return (self.value - 32) * 5 / 9


class Celsius(Temperature):
    unit_name = "Celsius"
    converted_unit_name = "Fahrenheit"

    def convert(self) -> float:
        return self.value * 9 / 5 + 32
