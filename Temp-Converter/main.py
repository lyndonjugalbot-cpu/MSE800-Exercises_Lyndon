#import the TemperatureConverter class from the converter module
from converter import TemperatureConverter

PROMPT = "Enter a temperature (e.g. F51 or C11), or 'exit' to quit: "

#main function to run the temperature converter CLI
def main():
    #create an instance of the TemperatureConverter class
    converter = TemperatureConverter()

    #loop to continuously prompt the user for input until they choose to exit
    while True:
        raw_input = input(PROMPT)

        if raw_input.strip().lower() in ("exit", "quit"):
            break

        try:
            print(converter.convert(raw_input))
        except ValueError as exc:
            print(exc)


if __name__ == "__main__":
    main()
