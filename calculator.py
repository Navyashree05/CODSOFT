def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def main():
    while True:
        print("\nSelect Operation")
        print(
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Exit\n"
        )

        try:
            operation = int(input("Enter choice of operation 1/2/3/4/5: "))
            if operation == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if operation not in [1, 2, 3, 4]:
                print("Invalid Input. Please choose a valid operation.")
                continue

            n1 = float(input("Enter the First Number: "))
            n2 = float(input("Enter the Second Number: "))

            if operation == 1:
                print(n1, "+", n2, "=", addition(n1, n2))

            elif operation == 2:
                print(n1, "-", n2, "=", subtraction(n1, n2))

            elif operation == 3:
                print(n1, "*", n2, "=", multiplication(n1, n2))

            elif operation == 4:
                # Handle division by zero
                if n2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(n1, "/", n2, "=", division(n1, n2))

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()