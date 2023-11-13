# Project: To find what product items are low in quantity so that you can restock them---

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

#Output--
[['Docking Station', 65.41, 'USD', 1, 4.9, 'Hardware']]
