import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given data
questions = ['Obstructive vs Supportive', 'Complicated vs Easy', 'Inefficient vs Efficient', 'Confusing vs Clear', 'Boring vs Exciting', 'Not Interesting vs Interesting', 'Conventional vs Inventive', 'Usual vs Leading Edge']

# Participant ratings data
participant_data = [
    [6, 6, 7, 7, 7, 7, 6, 7],
    [7, 5, 7, 7, 7, 7, 7, 7],
    [6, 6, 7, 5, 4, 4, 6, 6],
    [5, 6, 5, 6, 4, 4, 6, 6],
    [6, 7, 7, 6, 7, 7, 6, 7],
    [7, 4, 6, 5, 5, 7, 7, 7],
    [4, 5, 5, 5, 5, 5, 5, 4],
    [4, 3, 3, 3, 4, 7, 7, 1],
    [7, 7, 7, 7, 7, 7, 7, 7],
]

# Create a list to hold the data for DataFrame
data = []

# Iterate over participants, questions, and ratings
for i, p in enumerate(range(1, 9)):  # Assuming participant IDs are from 1 to 8
    for j, q in enumerate(questions):
        rating = participant_data[i][j]
        
        # Create a dictionary with participant, question, and rating
        entry = {'Participant': f'P{p}', 'Question': q, 'Rating': rating}
        data.append(entry)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Set up figure and axis with larger figsize
plt.figure(figsize=(10, 8))

# Plot swarm plot using seaborn
sns.swarmplot(x='Question', y='Rating', hue='Participant', data=df, palette='viridis', size=8, dodge=True)

# Add vertical lines connecting low and high values for each question
for question in questions:
    subset = df[df['Question'] == question]
    min_value = subset['Rating'].min()
    max_value = subset['Rating'].max()
    plt.plot([questions.index(question), questions.index(question)], [min_value, max_value], color='black', linestyle='-', linewidth=2)

    # Add horizontal lines for min and max values
    plt.hlines(y=min_value, xmin=questions.index(question) - 0.2, xmax=questions.index(question) + 0.2, color='black', linestyle='-', linewidth=2)
    plt.hlines(y=max_value, xmin=questions.index(question) - 0.2, xmax=questions.index(question) + 0.2, color='black', linestyle='-', linewidth=2)

# Calculate and plot trend line (mean values)
mean_ratings = df.groupby('Question')['Rating'].mean()
plt.plot(range(len(questions)), mean_ratings, marker='o', color='dodgerblue', linestyle='-', linewidth=2, markersize=8, label='Trend Line')

# ...

# Customize y-axis limits
plt.ylim(1, 7)

# Customize plot
plt.xlabel('Questions', fontsize=10)
plt.ylabel('Rating Value', fontsize=10)
plt.title('UEQ Without Visuals', fontsize=14)
plt.xticks(rotation=15, ha='right')  # Rotate x-axis labels for better readability
plt.legend(title='Participants', bbox_to_anchor=(1, 1), loc='upper left')

plt.show()
