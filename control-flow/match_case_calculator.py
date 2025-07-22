num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
  case "+":
    print(f"The result of {num1} + {num2} is {num1 + num2}")
  case "-":
    print(f"The result of {num1} - {num2} is {num1 - num2}")
  case "*":
    print(f"The result of {num1} * {num2} is {num1 * num2}")
  case "/":
    if num2 != 0:
      print(f"The result of {num1} / {num2} is {num1 / num2}")
    else:
      print("cannot divide by zero.")
  case _:
    print("Invalid operation")