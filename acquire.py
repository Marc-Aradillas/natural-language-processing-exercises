import pandas as pd
import requests
import re

from bs4 import BeautifulSoup

# here we are defining a dictionary where a key is a user agent.
# dsplays who i am and alllows request to follow through
headers = {'User-Agent': 'Codeup Data Science'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all("h2")
