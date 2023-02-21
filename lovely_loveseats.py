lovely_loveseat_description= """
Lovely Loveseat. Tuffed polyester blend on wood. 32 inches high x 40 inches x 30 inches deep. Red or white.
"""

#price for loveseat
lovely_loveseat_price = 254.00

#another variable
stylish_settee_description = """
stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
#price for stylish settee
stylish_settee_price = 180.50

#new variable
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall.
Brown with cream shade.
"""
#price luxurious lamp
luxurious_lamp_price = 52.15

#store sales tax
sales_tax = .088

#customer purchase
customer_one_total =0
customer_one_total+=lovely_loveseat_price

#customer's purchases'description
customer_one_itemization=""
customer_one_itemization+=lovely_loveseat_description+luxurious_lamp_description

#calculating sales task
customer_one_tax = 0
customer_one_tax += customer_one_total * sales_tax
#updating customer total
customer_one_total+=customer_one_tax

#printing out the receipt
#printing out heading of itemization
print("Customer One Items:")
print(customer_one_itemization)
#total cost
print("customer One Total")
print(customer_one_total)














