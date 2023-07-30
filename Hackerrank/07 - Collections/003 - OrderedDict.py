# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Score: 20
from collections import OrderedDict

number_of_products = int(input())
products_sold = OrderedDict()
for _ in range(number_of_products):
    product_info = list(input().split())
    product_price = int(product_info[len(product_info)-1])
    product_name = " ".join(product_info[:len(product_info)-1])
    try:
        products_sold[product_name] += int(product_price)
    except KeyError:
        products_sold[product_name] = int(product_price)

[print(key, value) for key, value in products_sold.items()]
