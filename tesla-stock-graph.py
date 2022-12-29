import matplotlib.pyplot as plt
import warnings

def make_graph(data, title):
    # Get the date and close price columns
    dates = data["Date"]
    close_prices = data["Close"]

    # Suppress the warning
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

        # Create a figure
        fig = plt.figure(figsize=(8, 6), dpi=100)

        # Create a subplot
        ax = fig.add_subplot(111)

        # Plot the close prices
        ax.plot(dates, close_prices)

        # Set the title of the graph
        ax.set_title(title)

    # Show the figure
    plt.show()


make_graph(tesla_data, "Tesla Stock Price")
