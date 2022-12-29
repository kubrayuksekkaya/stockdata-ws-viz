import requests
from bs4 import BeautifulSoup

# Set the URL to scrape
url = "https://www.statista.com/statistics/270307/gamestops-revenue/"

# Send an HTTP request to the URL and store the response
response = requests.get(url)

# Parse the HTML of the page
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing the revenue data
table = soup.find("table", {"class": "table"})

# Initialize an empty list to store the revenue data
gme_revenue = []

# Iterate through the rows of the table
for row in table.find_all("tr"):
    # Get the text of the row
    data = [cell.text for cell in row.find_all("td")]
    # If the row contains data, append it to the list
    if data:
        gme_revenue.append(data)

# Convert the list to a dataframe
gme_revenue = pd.DataFrame(gme_revenue, columns=["Year", "Revenue (in million US dollars)"])

# Display the last five rows of the dataframe
print(gme_revenue.tail())
