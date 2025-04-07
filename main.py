from visualize import
plot_histograms,plot_boxplots,
plot_correlation_heatmap
# main.py
"""
Open Data Scince(ODS) Project 
Auther:dineshrayapati
Date:2025
Description:Enter point for the project -handles loading data and basic EDA .
"""

 import pands  as pd 
import matplotlib.pyplot as plt
def load_data(path):
  """Load dataset from  the given path."""
  try:
    data=pd.read_csv(path)
    print(f"Data loaded sucessfully!")
    return data except Exception  as e:
      print(f"Error loading data:{e}")
      return None
 def basic_eda(data):
   """Perform basic EDA on the dataset."""
   print("\nFirst 5 rows:")
   print(data.head())
   print("\n Data Summary:")
   print(data.discribe())
   print("\n Missing Values:")
   print(data.isnull().sum())
  def main():
    path="data/sanple.csv"
    if data is not None:
      basic_eda(data)
      if __name__=="__main__":
       df=load_dataset()
       if df is not None:
        basic_eda(df)
        plot_histograms(df)
        plot_boxplots(df)
        plot_correlation_heatmap(df)
        main
    data=load_data(path)
