import matplotlib.pyplot as plt
import numpy as np

# Mean values
conditions = ['Audio', 'Audio to Visual', 'Audio and Visual']
mean_values = [1.7817, 2.13185, 2.433]

# Variance values
variance_values = [5.216751, 8.77461, 9.503026]

# Plotting
fig, ax = plt.subplots()

# Set bar width
bar_width = 0.35

# Set colors for bars and text annotations
mean_color = 'skyblue'
variance_color = 'lightcoral'
text_color_mean = 'black'
text_color_variance = 'black'

# Plotting mean values
mean_bars = ax.bar(np.arange(len(conditions)) - bar_width/2, mean_values, bar_width, color=mean_color, label='Mean')

# Plotting variance values
variance_bars = ax.bar(np.arange(len(conditions)) + bar_width/2, variance_values, bar_width, color=variance_color, label='Variance')

# Adding mean values as text annotations
for i, mean_value in enumerate(mean_values):
    ax.text(i - bar_width/2, mean_value + 0.05, f'{mean_value:.2f}', ha='center', va='bottom', fontsize=8, color=text_color_mean)

# Adding variance values as text annotations
for i, variance_value in enumerate(variance_values):
    ax.text(i + bar_width/2, variance_value + 0.05, f'{variance_value:.2f}', ha='center', va='bottom', fontsize=8, color=text_color_variance)

# Labels and title
plt.xlabel('Conditions')
plt.ylabel('Values')
plt.title('Comparison of Mean and Variance for Three Conditions')
plt.xticks(np.arange(len(conditions)), conditions)
plt.legend()

# Set x-axis limits to include values up to 10
plt.xlim(-0.5, len(conditions) - 0.5)  # Adjust the limits here

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show the plot
plt.show()
