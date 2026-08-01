#Test input and output
def fibonacci(n):
    first = 0
    second = 1

    print("\nFibonacci Sequence:")

    for i in range(n):
        print(first)
        next_number = first + second
        first = second
        second = next_number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {i} is {result}")
    return result

def main():
    terms = int(input("Enter a number: "))
    fibonacci(terms)
    factorial(terms)

if __name__ == "__main__":
    main()