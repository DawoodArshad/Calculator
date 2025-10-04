def Add(x,y):
    return x + y
def Subtract(x,y):
    return x - y
def Multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return ("Error.Cant divide by zero.")
    return x / y

print("choose option:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

while True:
    choice = input("press 1,2,3,4 or q for exiting: ")
    if choice.lower() == "q":
        print("Exiting calculator")
        break
    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("tell first number: "))
            num2 = float(input("tell second number: "))
        except ValueError:
            print("Invalid input.please enter number only")
            continue

        
        if choice == "1":
            print(f"Result: {Add(num1 ,num2)}")
        elif choice == "2":
            print(f"Result: {Subtract(num1 ,num2)}")
        elif choice == "3":
            print(f"Result: {Multiply(num1 ,num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1 ,num2)}")
        else:
            print("Invalid choice")

