import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    'https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html')
bs = BeautifulSoup(html, 'html.parser')

table = bs.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('Text-Editor-Data.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()