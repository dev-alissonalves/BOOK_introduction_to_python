product_value = float(input("What is the value of the product (R$): "))
consumer_discount = float(input("What is the discount percentage for the consumer (10% default): "))
discount_value_in_real = product_value * (consumer_discount / 100)
total_value = product_value - discount_value_in_real

print(f"Considering a discount of R$ {discount_value_in_real} ({consumer_discount:.0f}%) the total is: R$ {total_value:.1f}.")

