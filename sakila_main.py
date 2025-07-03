from sakila_db import *
import matplotlib.pyplot as plt
# print(load_customers())
customers_df = load_customers()
print(customers_df)


langas, grafikas = plt.subplots()