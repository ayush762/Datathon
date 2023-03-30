from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import time

authors = []
quotes = []

def scrape_website(page_number):
  page_num = str(page_number) #Convert the page number to a string
  URL = 'https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html' #append the page number to complete the URL
  webpage = requests.get(URL)  #Make a request to the website
  soup = BeautifulSoup(webpage.text, "html.parser") #Parse the text from the website
  quoteText = soup.find_all('class', attrs={'class':'kdnug-4ff8bed466176632c9eee04d803e498c kdnug-ros-mobile-in-content'}) #Get the tag and it's class
  for i in quoteText:
        quote = i.text.strip().split('\n')[0]#Get the text of the current quote, but only the sentence before a new line
        author = i.find('span', attrs={'class':'kdnug-4ff8bed466176632c9eee04d803e498c kdnug-ros-mobile-in-content'}).text.strip()
        #print(quote)
        quotes.append(quote)
        #print(author)
        authors.append(author)