import matplotlib.pyplot as plt
import numpy as np

def plot_function(expression, x_range=(-10, 10), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = expression(x)
    plt.plot(x, y)

def input_function():
    expr = input("Enter a function f(x): ")
    expr = expr.replace("^", "**")  # Replace ^ with ** for exponentiation
    return lambda x: eval(expr)

def main():
    print("Welcome to the Python Graphing Calculator")
    print("Enter a mathematical function to plot (e.g., x**2, np.sin(x))")
    while True:
        func = input_function()
        plot_function(func)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Graph of f(x)')
        plt.grid(True)
        plt.show()
        another = input("Do you want to plot another function? (y/n): ")
        if another.lower() != 'y':
            break
    print("Exiting the Graphing Calculator")

if __name__ == "__main__":
    main()