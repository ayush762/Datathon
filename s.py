import requests
from bs4 import BeautifulSoup

main_url = "https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html"

# Getting individual cities url
re = requests.get(main_url)
soup = BeautifulSoup(re.text, "html.parser")
city_tags = soup.find_all('li', class_="kdnug-4ff8bed466176632c9eee04d803e498c kdnug-ros-mobile-in-content")  # Bottom page not loaded dynamycally
cities_links = [main_url + tag["href"] for tag in city_tags]

print(cities_links)