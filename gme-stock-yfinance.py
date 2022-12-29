import yfinance as yf

# Get the stock data for GameStop
gme_data = yf.Ticker("GME").history(period="1y")

# Reset the index
gme_data.reset_index(inplace=True)

# Save the data to a CSV file
gme_data.to_csv("gme_data.csv")

# Display the first five rows of the data
print(gme_data.head())
