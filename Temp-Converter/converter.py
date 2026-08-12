#import the temperature classes from the temperature module
from temperature import Celsius, Fahrenheit

#declaration of constants - error message
INVALID_INPUT_MESSAGE = "Invalid input. Please enter the temperature with the correct 'C' or F' prefix."
INVALID_TEMP_MESSAGE = "Invalid temperature value. Please enter a valid number."

# Mapping of prefix to temperature class
_PREFIX_TO_CLASS = {
    "F": Fahrenheit,
    "C": Celsius,
}

# TemperatureConverter class to handle parsing and conversion
class TemperatureConverter:
    """Parses raw temperature input and produces the conversion message."""

    def parse(self, raw_input: str):
        #the prefix is the first character, the value is everything after it
        prefix = raw_input[:1]
        digits = raw_input[1:]

        #check if the prefix is valid
        if prefix not in _PREFIX_TO_CLASS:
            raise ValueError(INVALID_INPUT_MESSAGE)

        #check that the value is a real number and not letters/empty
        try:
            value = float(digits)
        except ValueError:
            raise ValueError(INVALID_TEMP_MESSAGE) from None

        #get the appropriate temperature class based on the prefix and return an instance of it
        temperature_class = _PREFIX_TO_CLASS[prefix]
        return temperature_class(value)

    #convert method to handle the conversion and formatting of the output
    def convert(self, raw_input: str) -> str:
        """Parse raw_input and return the formatted conversion message."""
        raw_input = raw_input.strip()
        temperature = self.parse(raw_input)
        converted = temperature.converted_value()

        #return the formatted string with the original and converted temperature values
        return (
            f"{raw_input} degrees {temperature.unit_name} is converted to "
            f"{converted:.2f} degrees {temperature.converted_unit_name}"
        )
