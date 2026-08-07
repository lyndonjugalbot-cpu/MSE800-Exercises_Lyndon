"""
BMI (Body Mass Index) Calculator - CLI.

Usage:
    python bmi.py --weight 70 --height 1.75
    python bmi.py -w 70 -H 1.75 --unit metric
    python bmi.py -w 154 -H 69 --unit imperial

Run without arguments to be prompted interactively instead.
"""

"Python's standard library module for parsing command-line arguments"
import argparse

"gives access to system-level functions"
import sys

"Enum lets us define a fixed set of named, readable categories"
from enum import Enum


def main(): 
    """Entry point for the BMI calculator CLI."""
    args = parse_args(sys.argv[1:])
 
    try:
        # Fall back to interactive prompts if weight/height weren't passed as flags
        if args.weight is None or args.height is None:
            weight, height, unit = prompt_for_measurements()
        else:
            weight, height, unit = args.weight, args.height, args.unit
 
        if unit == "imperial":
            weight, height = convert_imperial_to_metric(weight, height)
 
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
 
        print(f"\nBMI: {bmi:.2f}")
        # category is a BMICategory enum member, so we use .value to get
        # the readable string (e.g. "Normal weight") for printing.
        print(f"Category: {category.value}")
 
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

        
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

def convert_imperial_to_metric(weight_lb: float, height_in: float):
    """Convert weight in pounds and height in inches to kilograms and metres."""
    weight_kg = weight_lb * 0.45359237
    height_m = height_in * 0.0254
    return weight_kg, height_m

def parse_args(argv: list[str]):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate Body Mass Index (BMI) from weight and height.",
    )
    parser.add_argument(
        "-w", "--weight", type=float, default=None,
        help="Weight (kg for metric, lb for imperial).",
    )
    parser.add_argument(
        "-H", "--height", type=float, default=None,
        help="Height (m for metric, in for imperial).",
    )
    parser.add_argument(
        "-u", "--unit", choices=["metric", "imperial"], default="metric",
        help="Unit system for the supplied weight/height (default: metric).",
    )
    return parser.parse_args(argv)

def prompt_for_measurements():
    """Interactively prompt the user for unit, weight, and height."""
    unit = input("Unit system (metric/imperial) [metric]: ").strip().lower() or "metric"
    while unit not in ("metric", "imperial"):
        unit = input("Please enter 'metric' or 'imperial': ").strip().lower()
 
    weight_label = "Weight in kg: " if unit == "metric" else "Weight in lb: "
    height_label = "Height in m: " if unit == "metric" else "Height in inches: "
 
    weight = float(input(weight_label).strip())
    height = float(input(height_label).strip())
    return weight, height, unit


 
 
if __name__ == "__main__":
    main()