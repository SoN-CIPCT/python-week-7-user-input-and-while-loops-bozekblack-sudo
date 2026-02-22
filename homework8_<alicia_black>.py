pizza_orders = ["Pepperoni", "Cheese", "Veggie", "Hawaiian", "Meat Lovers"]
finished_pizzas = []
for pizza in pizza_orders:
    print(f"Your {pizza} pizza pie is finished!")
    finished_pizzas.append(pizza)
print("\nAll pizzas have been completed.")
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")