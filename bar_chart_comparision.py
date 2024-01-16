import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given mean values and custom colors
mean_values = {
    'Audio': 2.636979167,
     'Audio To Visual': 3.748013393,
    'Audio And Visual': 2.70996875
   
}

custom_colors = {
  'Audio': '#90EE90',
    'Audio To Visual': '#FF7F50',
    'Audio And Visual': '#FDFD96'
}

# Create a DataFrame from the mean values
df_mean = pd.DataFrame(list(mean_values.items()), columns=['Category', 'Mean Value'])

# Set up figure and axis with larger figsize
plt.figure(figsize=(8, 6))

# Plot a bar plot using seaborn with custom colors
ax = sns.barplot(x='Category', y='Mean Value', data=df_mean, palette=custom_colors, ci=None)

# Display exact values on each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=10)

# Customize plot
plt.xlabel('', fontsize=12)
plt.ylabel('Mean Value', fontsize=12)
plt.title('Mean Values Across Categories', fontsize=14)
plt.ylim(0, 5)  # Adjust y-axis limits as needed
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()