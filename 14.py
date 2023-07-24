def calculate_profit_loss(cost_price, sell_price):
    if sell_price >= cost_price:
        profit = sell_price - cost_price
        profit_percentage = (profit / cost_price) * 100
        return "Profit", profit, profit_percentage
    else:
        loss = cost_price - sell_price
        loss_percentage = (loss / cost_price) * 100
        return "Loss", loss, loss_percentage

try:
    cost_price = float(input("Enter the cost price: "))
    sell_price = float(input("Enter the sell price: "))

    if cost_price < 0 or sell_price < 0:
        print("Cost price and sell price cannot be negative.")
    else:
        result, amount, percentage = calculate_profit_loss(cost_price, sell_price)
        print(f"{result} amount: {amount:.2f}")
        print(f"{result} percentage: {abs(percentage):.2f}%")
except ValueError:
    print("Invalid input. Please enter valid numbers for cost price and sell price.")
