import requests

def shorten_url(url):
    api_url = "http://tinyurl.com/api-create.php?url=" + url
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to shorten URL"

# Prompt the user to enter a long URL
long_url = input("Enter a long URL to shorten: ")

# Shorten the URL using the TinyURL API
short_url = shorten_url(long_url)

# Display the results
print("Long URL:", long_url)
print("Short URL:", short_url)
