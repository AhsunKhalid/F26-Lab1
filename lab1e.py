
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.
quantity=4.5467
stock=10.3
product=quantity*stock
print("the product of quanity and stock is : %4.0f" %product)
print("the product of quanity and stock is : %7.2f" %product)