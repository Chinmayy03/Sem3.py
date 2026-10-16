# Electricity Bill Generator

# 1. Accept details from the user
consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

# 2. Perform Calculations
units_consumed = current_reading - previous_reading
energy_charge = units_consumed * cost_per_unit
electricity_duty = 0.05 * energy_charge
fixed_charge = 100.00
net_bill = energy_charge + electricity_duty + fixed_charge

# 3. Display the bill in a neat format
print("\n==========================================")
print("             ELECTRICITY BILL             ")
print("==========================================")
print("Consumer Name:      ", consumer_name)
print("Consumer ID:        ", consumer_id)
print("------------------------------------------")
print("Previous Reading:   ", previous_reading, "kWh")
print("Current Reading:    ", current_reading, "kWh")
print("Total Units Used:   ", units_consumed, "kWh")
print("------------------------------------------")
print("Energy Charge:       ₹", energy_charge)
print("Electricity Duty:    ₹", electricity_duty)
print("Fixed Meter Charge:  ₹", fixed_charge)
print("------------------------------------------")
print("NET BILL AMOUNT:     ₹", net_bill)
print("==========================================")
