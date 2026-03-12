import numpy as np
import pandas as pd
import seaborn as sns
import csv
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('/Users/shivapanuganti/Desktop/test-python/myenv/health.csv')
print(data.shape)
print(data.head())
print(data.info())
print(data.describe())

def identify_columns(dataframe): #When you run this function with a DataFrame, it will print the count and names of the numeric and categorical features present in the DataFrame. This can be useful for understanding the data types of different columns and identifying which columns may require specific types of analysis or preprocessing.
    # Identify numeric features
    numeric_features = []
    categorical_features = []

    for feature in dataframe.columns:
        if dataframe[feature].dtype != 'O':
            numeric_features.append(feature)
        else:
            categorical_features.append(feature)

    # Print the results
    print(f"We have {len(numeric_features)} numerical features: {numeric_features}")
    print(f"We have {len(categorical_features)} categorical features: {categorical_features}")
identify_columns(data)


# distribution of ages by blood type
# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a violin plot to show the distribution of ages by blood type
sns.violinplot(x='Blood Type', y='Age', data=data, ax=ax, palette='muted')

# Set plot title and axis labels
ax.set_title('Distribution of Ages by Blood Type', fontsize=16, fontweight='bold')
ax.set_xlabel('Blood Type', fontsize=12)
ax.set_ylabel('Age', fontsize=12)


# Adjust the plot layout
# This function automatically adjusts the padding between subplots and labels to improve readability and avoid overlapping elements.
plt.tight_layout()

# Display the plot
# This command renders the plot and shows it in a separate window or notebook output.
plt.show()

# Calculate category counts
category_counts = data.groupby(['Admission Type', 'Medical Condition']).size()

# Create a pie chart to analyze admission type by medical condition
fig, ax = plt.subplots(figsize=(19, 19))
category_counts.plot(kind='pie', ax=ax, autopct='%1.1f%%') #display the percent value rounded to 1 decimal place

# Set plot title and legend
ax.set_title('Admission Type by Medical Condition', fontsize=16, fontweight='bold')
legend = ax.legend(title='Medical Condition', fontsize=10.9, loc='upper left', bbox_to_anchor=(0.96, 1.1))

# Set aspect ratio to be equal so that pie is drawn as a circle
ax.set_aspect('equal')

# Display the chart
plt.show()

