#Q4- Program for toy vendor discounts...
product_code = int(input("Enter product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging-based): "))
order_amount = float(input("Enter the order amount: "))

if product_code == 1:  # Battery-based toys
    if order_amount > 1000:
        discount = order_amount * 0.10
    else:
        discount = 0
elif product_code == 2:  # Key-based toys
    if order_amount > 100:
        discount = order_amount * 0.05
    else:
        discount = 0
elif product_code == 3:  # Electrical Charging-based toys
    if order_amount > 500:
        discount = order_amount * 0.10
    else:
        discount = 0
else:
    print("Invalid product code")
    discount = 0

net_amount = order_amount - discount
print("The net amount to be paid after discount is Rs.", net_amount)
