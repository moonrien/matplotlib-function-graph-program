import numpy as np
import matplotlib.pyplot as plt

#function
try:
    function1 = input("Enter the function formula (e.g., x*x - 6*x + 3): ")
    if 'x' not in function1:
        raise ValueError("Error! The function must include the variable x.")
    if not all(c.isalnum() or c in ['+', '-', '*', '/', '.', 'x', '^'] for c in function1):
        raise ValueError("The function contains invalid characters.")
except ValueError as e:
    print(e)

#Input x range
try:
    range_x = list(map(float, input("Enter the range for variable x (space-separated, e.g., -10 10): ").split()))
    if len(range_x) != 2:
        raise ValueError("Please provide exactly two numbers separated by a space.")
    if range_x[0] >= range_x[1]:
        raise ValueError("The range must have the start smaller than the end.")
except ValueError as e:
    print("Error: ", e)
else:
    print("Here is the function and its range:", function1, range_x)

#list of x values and calculate y values
x_values = np.linspace(range_x[0], range_x[1], 100)
y_values = []

for x in x_values:
    try:
        y = eval(function1)
        y_values.append(y)
    except ZeroDivisionError:
        y_values.append(float('inf'))  # Vertical asymptote
    except Exception as e:
        y_values.append(float('nan')) 
        print(f"Error while calculating the function for x = {x}: {e}")

#The graph
plt.plot(x_values, y_values, label=f'y = {function1}')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # X-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Y-axis
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Graph')
plt.legend()
plt.grid()
plt.show()
