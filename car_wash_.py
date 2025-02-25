import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load dataset
df = pd.read_csv("car_wash_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# 1. Find best months for Discounts & Surcharges
monthly_sales = df.groupby(df["date"].dt.month)["amount"].sum()
print("Best month for discounts:", monthly_sales.idxmin())  # Lowest sales
print("Best month for surcharges:", monthly_sales.idxmax())  # Highest sales

# 2. Find valuable customers who haven't visited in 2+ months
last_visits = df.groupby("cust_id")["date"].max()
inactive_customers = last_visits[last_visits < datetime(2024, 12, 31) - timedelta(days=60)]
print("Customers to send coupons to:", inactive_customers.index.tolist())

# 3. Show monthly sales
monthly_sales.plot(kind="bar", color="skyblue", title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# 4. Show sales distribution (Pie Chart)
df["hour"] = df["date"].dt.hour
df["time_slot"] = pd.cut(df["hour"], bins=[0, 6, 12, 18, 24], labels=["Midnight-6AM", "6AM-12PM", "12PM-6PM", "6PM-Midnight"], right=False)
df.groupby("time_slot")["amount"].sum().plot(kind="pie", autopct="%1.1f%%", title="Sales by Time of Day")
plt.ylabel("")
plt.show()
