import os.path
import datetime
import urllib.request
from bs4 import BeautifulSoup

# where data files are written to
# TODO save_path = 'C:/NRC/RASCAL43/Downloaded_Met_Data/'
save_path = 'C:/Users/telsbree/git/pge-weather-scraper/'

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
    
# generates the file name based on system time, remove whitespace and colons
date_str = str(datetime.datetime.now()).replace(" ", "").replace(":","")
# place '-' inbetween DD and HH
date_str = date_str[:10] + '-' + date_str[10:]    
# strips the trailing characters from time string, leaving YYYY-MM-DD-HH
date_str = date_str[:-11]
    
# joins the specified directory with the filename    
file_path_name = os.path.join(save_path, 'Observations_' + date_str + ".obs")    

# open file for writing, creates file if not found
f = open(file_path_name, 'w')
f.write(str(data))