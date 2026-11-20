import csv
import matplotlib.pyplot as plt

sales = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Tablet": 20000,
    "Headphones": 10000
}

# Store data in CSV file
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Sales"])
    for product, amount in sales.items():
        writer.writerow([product, amount])

# Display sales details
print("Retail Sales Report")
for product, amount in sales.items():
    print(product, ":", amount)

total = sum(sales.values())
print("Total Sales:", total)

# Create sales dashboard
plt.bar(sales.keys(), sales.values())
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.show()
