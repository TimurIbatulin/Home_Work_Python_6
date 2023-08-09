import portfolio

c = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
v = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}


print(portfolio.calculate_portfolio_value(c, v))
print(portfolio.calculate_portfolio_return(100, 150))

q = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
w = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 800.50}
print(portfolio.get_most_profitable_stock(q, w))


# print(calculate_portfolio_value(c, v))ss
