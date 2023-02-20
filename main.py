import requests
import json

# Prompt the user to enter a search term
search_term = input("Enter a search term: ")

# Make a request to the Giphy API
api_key = "NM7NSJsOVIBFUO0EKTDSmkyROwStnCrK"
url = f"https://api.giphy.com/v1/gifs/search?q={search_term}&api_key={api_key}&limit=5"
response = requests.get(url)

# Extract the URLs of the first 5 GIFs from the response
data = json.loads(response.text)
gif_urls = [item["images"]["downsized"]["url"] for item in data["data"]]

# Print the URLs of the GIFs
for url in gif_urls:
    print(url)
