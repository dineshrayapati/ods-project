import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(data):
    """Plot histograms for all numeric columns."""
    numeric_cols = data.select_dtypes(include='number')
    numeric_cols.hist(bins=15, figsize=(10, 6), color='skyblue', edgecolor='black')
    plt.suptitle("Histograms of Numeric Columns")
    plt.tight_layout()
    plt.show()

def plot_boxplots(data):
    """Plot boxplots to detect outliers."""
    numeric_cols = data.select_dtypes(include='number')
    for col in numeric_cols.columns:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=data[col], color='lightgreen')
        plt.title(f"Boxplot for {col}")
        plt.show()

def plot_correlation_heatmap(data):
    """Plot correlation heatmap."""
    plt.figure(figsize=(8, 6))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()
