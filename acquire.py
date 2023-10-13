import pandas as pd
import requests
import re

from bs4 import BeautifulSoup

url = 'https://codeup.edu/blog/'

response = requests.get(url)

response