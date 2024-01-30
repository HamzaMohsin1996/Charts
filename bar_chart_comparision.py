import matplotlib.pyplot as plt
import numpy as np

# Given t-test value
t_test_value = 0.1617342878  # Replace with the actual t-test value

# Create a bar plot for the t-test value
plt.figure(figsize=(6, 4))
plt.bar(0, t_test_value, color='skyblue', edgecolor='black', linewidth=1.2)

# Add a text annotation for the t-test value
plt.text(0, t_test_value + 0.01, f'T-Test Value\n{t_test_value:.4f}', ha='center', va='bottom', fontsize=10, color='black')

# Highlight the significance level
plt.axhline(y=0.05, color='red', linestyle='--', label='Significance Level (e.g., 0.05)')

# Add labels and title
plt.xlabel('', fontsize=12)
plt.ylabel('T-Test Value', fontsize=12)
plt.title('T-Test Analysis for Driver Responses', fontsize=14)
plt.xticks([])  # Hide x-axis ticks
plt.legend()

# Adjust ylim to prevent overlap from the top
plt.ylim(0, max(t_test_value, 0.05) + 0.1)

# Remove unnecessary spines
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Display the bar plot
plt.show()
