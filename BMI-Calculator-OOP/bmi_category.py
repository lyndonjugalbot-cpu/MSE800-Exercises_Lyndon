import argparse

"Enum lets us define a fixed set of named, readable categories"
from enum import Enum

class BMICategory(Enum):
    """
    BMI weight categories.
    """
    UNDERWEIGHT = "Underweight"
    NORMAL = "Normal weight"
    OVERWEIGHT = "Overweight"
    OBESE = "Obese"

    def calculate_bmi(weight_kg: float, height_m: float):
        """Calculate BMI given weight in kilograms and height in metres."""
        if weight_kg <= 0 or height_m <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        return weight_kg / (height_m ** 2)

    def classify_bmi(bmi: float):
        """Map a BMI value to its category (returns a BMICategory enum member)."""
        if bmi < 18.5:
            return BMICategory.UNDERWEIGHT
        elif bmi < 25.0:
            return BMICategory.NORMAL
        elif bmi < 30.0:
            return BMICategory.OVERWEIGHT
        else:
            return BMICategory.OBESE


    def parse_args(argv: list[str]):
        """Parse command-line arguments."""
        parser = argparse.ArgumentParser(
            description="Calculate Body Mass Index (BMI) from weight and height.",
        )
        parser.add_argument(
            "-w", "--weight", type=float, default=None,
            help="Weight (kg).",
        )
        parser.add_argument(
            "-H", "--height", type=float, default=None,
            help="Height (m).",
        )
    
        return parser.parse_args(argv)

    def prompt_for_measurements():
        """Interactively prompt the user for weight, and height."""

        weight_label = "Weight in kg: "
        height_label = "Height in m: "

    
        weight = float(input(weight_label).strip())
        height = float(input(height_label).strip())
        return weight, height