
def read_integer(prompt):
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def numbers_until_zero(numbers):
    """Collect numbers until zero is encountered (break)."""
    result = []

    for number in numbers:
        result.append(number)
        if number == 0:
            break

    return result


def odd_numbers(numbers):
    """Return only odd numbers by skipping even numbers (continue)."""
    result = []

    for number in numbers:
        if number % 2 == 0:
            continue
        result.append(number)

    return result


def main():
    while True:
        print("\n--- BREAK AND CONTINUE DEMO ---")
        print("1. Demonstrate break")
        print("2. Demonstrate continue")
        print("3. Exit")

        choice = read_integer("Choose an option: ")

        if choice == 1:
            print("\nEnter numbers (0 to stop):")
            entered = []

            while True:
                number = read_integer("Enter a number: ")
                entered.append(number)

                if number == 0:
                    break

            print("Numbers entered:", entered)
            print("Loop stopped using break.")

        elif choice == 2:
            numbers = list(range(1, 11))
            print("\nOriginal numbers:", numbers)
            print("Odd numbers:", odd_numbers(numbers))

        elif choice == 3:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
