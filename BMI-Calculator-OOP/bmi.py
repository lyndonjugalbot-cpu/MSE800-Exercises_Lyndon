"""
BMI (Body Mass Index) Calculator - CLI.

Usage:
    python bmi.py --weight 70 --height 1.75
    python bmi.py -w 70 -H 1.75 --unit metric

Run without arguments to be prompted interactively instead.
"""

"Python's standard library module for parsing command-line arguments"
import argparse

"gives access to system-level functions"
import sys

"class"
from bmi_category import BMICategory

def main(): 
    """Entry point for the BMI calculator CLI."""
    args = BMICategory.parse_args(sys.argv[1:])


    try:
        # Fall back to interactive prompts if weight/height weren't passed as flags
        if args.weight is None or args.height is None:
            weight, height = BMICategory.prompt_for_measurements()
        else:
            weight, height = args.weight, args.height
 
 
        bmi = BMICategory.calculate_bmi(weight, height)
        category = BMICategory.classify_bmi(bmi)
 
        print(f"\nBMI: {bmi:.2f}")
        # category is a BMICategory enum member, so we use .value to get
        # the readable string (e.g. "Normal weight") for printing.
        print(f"Category: {category.value}")
 
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()