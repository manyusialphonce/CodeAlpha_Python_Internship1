# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310
}

total_value = 0
portfolio = {}

print("Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        portfolio[stock] = value
        total_value += value
    else:
        print("Stock not available.")

print("\nPortfolio Summary:")
for stock, value in portfolio.items():
    print(stock, ":", value)

print("Total Investment Value:", total_value)

# Save to file
with open("portfolio.txt", "w") as file:
    for stock, value in portfolio.items():
        file.write(f"{stock}: {value}\n")
    file.write(f"Total Investment: {total_value}")