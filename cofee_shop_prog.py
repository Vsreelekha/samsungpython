import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook

# Load Data from Excel File
file_path = "Coffe_Business_Data.xlsx"



xls = pd.ExcelFile(file_path)  

coffee_seeds_df = pd.read_excel(xls, 'Coffee Seeds')
coffee_sales_df = pd.read_excel(xls, 'Coffee Sales')
customer_feedback_df = pd.read_excel(xls, 'Customer Feedback')
sweetener_sales_df = pd.read_excel(xls, 'Sweetener Sales')

# Analyzing the Best Coffee Seed Supplier
def best_supplier(df):
    seeds_summary = df.groupby('Supplier').agg({'Sales Generated ($)': 'sum'}).sort_values(by='Sales Generated ($)', ascending=False)
    print("Best Supplier Based on Sales:\n", seeds_summary)

#  Peak Sales Hours
def peak_sales_hours(df):
    df['Hour'] = pd.to_datetime(df['Time']).dt.hour
    hourly_sales = df.groupby('Hour').agg({'Sales Generated ($)': 'sum'})
    print("\nPeak Sales Hours:\n", hourly_sales)
    hourly_sales.plot(kind='bar', color='purple')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Total Sales ($)')
    plt.title('Peak Sales Hours')
    plt.show()

#  Product Popularity
def product_popularity(df):
    product_sales = df.groupby('Product').agg({'Quantity Sold': 'sum'}).sort_values(by='Quantity Sold', ascending=False)
    print("\nProduct Popularity:\n", product_sales)
    product_sales.plot(kind='bar', color='blue')
    plt.xlabel('Product')
    plt.ylabel('Total Quantity Sold')
    plt.title('Product Popularity')
    plt.show()

# Price Sensitivity
def price_sensitivity(df):
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Price ($)'], df['Quantity Sold'], color='red', alpha=0.6)
    plt.xlabel('Price ($)')
    plt.ylabel('Quantity Sold')
    plt.title('Price Sensitivity Analysis')
    plt.grid()
    plt.show()
    
    correlation = df[['Price ($)', 'Quantity Sold']].corr().iloc[0, 1]
    print(f"\nCorrelation between Price and Sales Quantity: {correlation:.2f}")
    
    if correlation < 0:
        print("🔻 Higher prices decrease sales (Price-sensitive).")
    elif correlation > 0:
        print("🔺 Higher prices increase sales (Unusual trend, consider checking data).")
    else:
        print("⚖️ No clear relationship between price and quantity sold.")

# Execute Functions
best_supplier(coffee_seeds_df)

peak_sales_hours(coffee_sales_df)
product_popularity(coffee_sales_df)
price_sensitivity(coffee_sales_df)