# File: calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This block executes only when the file is run directly
if __name__ == "__main__":
    print("Addition =", add(10, 20))
    print("Subtraction =", subtract(20, 10))