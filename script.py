import urllib.request
from bs4 import BeautifulSoup

# open website
response = urllib.request.urlopen("http://www.pge.com/about/edusafety/dcpp/index.jsp")
html_doc = response.read()

# parse using BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")

data = []
# finds an html table on page
table = soup.find('table')
# finds an html table body
table_body = table.find('tbody')

# finds all html table rows
rows = table_body.find_all('tr')

# finds all non empty table data 
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    
print (data)