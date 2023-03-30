import requests
from bs4 import BeautifulSoup


url="https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html"

r=requests.get(url)
htmlContent= r.content
# print(htmlContent)

# parse the html 
soup=BeautifulSoup(htmlContent,"html.parser")
# print(soup.prettify)

#html tree traversal

# print(soup.find_all('li',class_="post-66316 post type-post status-publish format-standard hentry category-g05-opinions-interviews tag-career tag-data-science tag-data-science-skills tag-data-scientist tag-dj-patil tag-hilary-mason tag-kirk-d-borne"))
# for i in 

soup.find( class_ = "kdnug-4ff8bed466176632c9eee04d803e498c kdnug-ros-mobile-in-content" )
print(soup)


# # x = print(soup.find("ol").get_text())
# for i in range (0,23):
#     data1 = soup.find('ol start = "i" ')
#     for li in data1.find_all("li"):
#        print(li.text, end=" ")