# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('SolarPowerData.csv')

# Display dataset details
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Shape (Rows, Columns):")
print(df.shape)

# Plot the distribution of generated power
plt.figure(figsize=(10, 6))
sns.histplot(df['generated_power_kw'], bins=30, kde=True, color='blue')
plt.title('Distribution of Generated Power (kW)', fontsize=16)
plt.xlabel('Generated Power (kW)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)
plt.show()

# Additional plot 1: Boxplot for detecting outliers in generated power
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='generated_power_kw', color='orange')
plt.title('Boxplot of Generated Power (kW)', fontsize=16)
plt.xlabel('Generated Power (kW)', fontsize=14)
plt.grid(True)
plt.show()

# Additional plot 2: Line plot to show trends in generated power (if time column exists)
if 'timestamp' in df.columns:
    # Convert timestamp to datetime for proper plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')  # Sort by time
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['generated_power_kw'], color='green', linewidth=1)
    plt.title('Temporal Trends in Generated Power', fontsize=16)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Generated Power (kW)', fontsize=14)
    plt.grid(True)
    plt.show()
else:
    print("\nNo 'timestamp' column found for the line plot.")

# Additional plot: Correlation heatmap
plt.figure(figsize=(10, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=16)
plt.show()