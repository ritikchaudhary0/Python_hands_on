##### Project: To find what product items are low in quantity so that you can restock them-----------------------------------------------------------------------------------------

laptop_product = ["Laptop", 899.00, "USD", 2, 3.34, "Hardware"]
keyboard_product = ["Keyboard", 29.50, "USD", 6, 4.80, "Peripherals"]
mouse_product = ["Mouse", 13.99, "USD", 14, 2.45, "Peripherals"]
hdmi_cable_product = ["HDMI Cable", 9.50, "USD", 58, 5.0, "Accessories"]
printer_product = ["Printer", 58.20, "USD", 21, 3.75, "Peripherals"]
headphones_product = ["Headphones", 26.99, "USD", 5, 4.77, "Accessories"]
docking_station_product = ["Docking Station", 65.41, "USD", 1, 4.9, "Hardware"]

inventory_products = [laptop_product, keyboard_product, mouse_product, hdmi_cable_product, printer_product, headphones_product, docking_station_product]

restock_products = []
for product_list in inventory_products:
    
    quantity = product_list[3]
    if quantity == 1:
        restock_products.append(product_list)

print(restock_products)

#Output-- [['Docking Station', 65.41, 'USD', 1, 4.9, 'Hardware']]


##### Modifying code to compute the total non-hardware product quantities----------------------------------------------------------------------------------
quantity_sum = 0
for product_list in inventory_products:
    category = product_list[5]
    quantity = product_list[3]
    if category != 'Hardware':
        quantity_sum = quantity + quantity_sum
print(quantity_sum)

#Output-- 104

##### Modify the code to get What are all of the products that cost less than $50?, We will analyze this from our daily sales data------------------------------------------------------------------
#We want to isolate all the orders with a purchase total less than or equal to $50.

opened_file = open('daily_sales.txt')
#file = opened_file.read()

#print(file)
orders_50_and_under = []
for order in opened_file:
    #print(order)
    order_list = order.split(',')
    #print(order_list)
    order_number = order_list[0]
    #print(order_number)
    purchase_total = float(order_list[2])
    #print(purchase_total)
    if purchase_total <= 50:
        orders_50_and_under.append(order_number)

print(orders_50_and_under)
#Output- ['4', '28']

### Modify code to What hardware products cost less than $20...............................?
