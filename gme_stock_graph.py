import matplotlib.pyplot as plt

def make_graph(data, title):
    # Get the date and close price columns
    dates = data["Date"]
    close_prices = data["Close"]

    # Create a figure and a subplot
    fig, ax = plt.subplots()

    # Plot the close prices
    ax.plot(dates, close_prices)

    # Set the title of the graph
    ax.set_title(title)
    
make_graph(gme_data, "GameStop Stock Price")
