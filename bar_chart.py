
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data (replace with your actual data)
scenarios = ['S1', 'S2', 'S3', 'S4']
mean_times = [2.492285714, 1.883875, 8.649142857, 1.96675]  # Replace None with actual values
						
error_counts = [0, 3, 2, 0]  # Replace None with actual values
no_response_counts = [0, 0, 1, 5]  # Replace with the count of 'No Response' for each scenario

# Create a DataFrame
df = pd.DataFrame({'Scenario': scenarios, 'Mean Time': mean_times, 'Error Count': error_counts, 'No Response Count': no_response_counts})

# Set up figure and axis with larger figsize
plt.figure(figsize=(10, 6))

# Plot the grouped bar plot
sns.barplot(x='Scenario', y='Mean Time', data=df, color='lightblue', label='Mean Time')
sns.barplot(x='Scenario', y='Error Count', data=df, color='salmon', label='Error Count')
sns.barplot(x='Scenario', y='No Response Count', data=df, color='gray', label='No Response Count', alpha=0.5)

# Add labels to each bar
for index, value in enumerate(mean_times):
    if not pd.isna(value):
        plt.text(index, value + 0.2, str(value), ha='center', va='bottom', fontsize=10, color='black')

for index, value in enumerate(error_counts):
    if not pd.isna(value):
        plt.text(index, value + 0.2, str(value), ha='center', va='bottom', fontsize=10, color='black')

for index, value in enumerate(no_response_counts):
    plt.text(index, value + 0.2, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Customize plot
plt.ylabel('Counts / Mean Time', fontsize=12)
plt.xlabel('Scenarios', fontsize=12)
plt.title('Comparison of Mean Time, Error Count, and No Response Count For Audio to Visual', fontsize=14)
plt.legend()  # Show legend for different categories

# Adjust ylim to make sure mean value fits within the plot
plt.ylim(0, max([max(mean_times), max(error_counts), max(no_response_counts)]) + 2)

plt.tight_layout()  # Adjust layout to prevent clipping of text
plt.show()