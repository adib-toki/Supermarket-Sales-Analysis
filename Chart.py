import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("supermarket_sales.csv")
df["Revenue"] = df["Unit_Price"]*df["Quantity"]
p = df.groupby("Branch")["Revenue"].sum()
x = df.groupby("Product_Line")["Revenue"].sum()
y = df["Payment"].value_counts()
z = df.groupby("Product_Line")["Quantity"].sum()
#Branch vs Revenue
plt.figure(figsize=(8,5))
plt.bar(p.index,p.values)
plt.title("Branch vs Revenue")
plt.xlabel("Branch")
plt.ylabel("Revenue")
plt.show()
#Product Line vs Revenue
plt.figure(figsize=(8,5))
plt.bar(x.index,x.values)
plt.title("Product Line vs Revenue")
plt.xlabel("Product Line")
plt.ylabel("Revenue")
plt.show()
#Payment Method vs Number of Orders
plt.figure(figsize=(8,5))
plt.bar(y.index,y.values)
plt.title("Payment Method vs Number of Orders")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.show()
#Product Line vs Quantity Sold
plt.figure(figsize=(8,5))
plt.bar(z.index,z.values)
plt.title("Product Line vs Quantity Sold")
plt.xlabel("Product Line")
plt.ylabel("Quantity Sold")
plt.show()