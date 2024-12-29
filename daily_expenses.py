budget=float(input("Enter your daily budget: "))
x=int(input("Enter the number of items: "))
currency=input("Enter the currency(e.g. USD or BDT or EUR): ")
spend=0
most_expensive=("", 0)
for x in range(x):
    Item_name = input(f"Name of the Items {x+1} is: ")
    Item_price=float(input(f"Enter the {Item_name} price: "))
    spend+=Item_price
    if Item_price>most_expensive[1]:
        most_expensive=(Item_name, Item_price)
    budget_left = budget - spend
    if spend >budget:
        print(f"You don't have enough {currency} to spend")
        print(f"You have only: {budget_left}{currency} left!!!")
        break
    else: continue
print(f"Total spend is: {spend}{currency}")
print(f"You have: {budget_left}{currency} left from your daily budget")
ave_exp=spend/x
print(f"The average expenses is: {ave_exp}{currency}")

print(f"Most expensive item is {most_expensive}{currency}")



