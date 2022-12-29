import yfinance as yf

# Get the stock data for Tesla
tesla_data = yf.Ticker("TSLA").history(period="1y")

# Reset the index
tesla_data.reset_index(inplace=True)

# Save the data to a CSV file
tesla_data.to_csv("tesla_data.csv")

# Display the first five rows of the data
print(tesla_data.head())
