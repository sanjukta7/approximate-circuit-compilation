
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data for demonstration
np.random.seed(10)
data1 = np.random.normal(100, 20, 200)
data2 = np.random.normal(80, 30, 200)
data3 = np.random.normal(90, 25, 200)

# Create a box plot
plt.figure(figsize=(8, 6))  # Adjust figure size
plt.boxplot([data1, data2, data3], patch_artist=True)

# Customize colors and styles
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, orange, green
boxprops = dict(facecolor='lightblue', color='black', linewidth=2)
medianprops = dict(color='black', linewidth=2)
whiskerprops = dict(color='black', linewidth=2)
capprops = dict(color='black', linewidth=2)

plt.boxplot([data1, data2, data3], patch_artist=True, boxprops=boxprops, medianprops=medianprops,
            whiskerprops=whiskerprops, capprops=capprops)

# Add labels and title
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.ylabel('Values')
plt.title('Box Plot Example')

# Remove unnecessary elements
plt.grid(False)
plt.tight_layout()

# Show plot
plt.show()