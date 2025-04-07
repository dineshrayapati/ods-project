import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column):
    """Plot a histogram for a specific column"""
    plt.figure(figsize=(8, 5))
    sns.histplot(data[column], kde=True, bins=30, color='skyblue')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_boxplot(data, column):
    """Plot a boxplot for a specific column"""
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=data[column], color='lightgreen')
    plt.title(f'Boxplot of {column}')
    plt.ylabel(column)
    plt.grid(True)
    plt.show()

def plot_correlation_heatmap(data):
    """Plot a heatmap of the correlation matrix"""
    plt.figure(figsize=(10, 8))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', square=True)
    plt.title('Correlation Heatmap')
    plt.show()
