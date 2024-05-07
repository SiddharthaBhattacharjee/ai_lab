import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
x = [1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11, 12, 13, 14]
y1 = [3, 3, 7, 8, 9, 11, 15, 17, 17, 18, 21, 25, 27, 29]
y2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# Create a scatter plot for y1 (blue points)
plt.scatter(x, y1, color='blue', label='y1 (scatter points)')

# Create a dashed line plot for y2 (green line)
plt.plot(x, y2, linestyle='--', color='green', label='y2 (dashed line)')

# Customize the plot (add labels, title, legend, etc.)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Points and Dashed Line')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
