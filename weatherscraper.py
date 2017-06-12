import os.path
import datetime
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup

met_towers = { 
  "Point Buchon" : "DCPTB",
  "Los Osos Cemetery" : "DCLOC",
  "Foothill" : "DCFH",
  "Service Center" : "DCSC",
  "Energy Education Center" : "DCEEC",
  "Davis Peak" : "DCDP",
  "Grover Beach" : "DCGB"
}


# converts a string of m/s to a string of mph
def parse_wind_speed(speed):
    val = round(float(speed) * 2.23694, 0)

    if val < 0:
        return "invalid wind"
    
    return str(int(val))


# rounds wind direction degrees and removes decimal places
def parse_wind_dir(dir):
    val = round(float(dir), 0)
  
    if val < 0:
        print ("wind below 0")
        return "invalid wind dir"
    
    if val > 360:
        print ("wind above 360")
        return "invalid wind dir"
    
    return str(int(val))


# returns data to be written to .obs file
# mm/dd/yyyy,hh:mm,[Temp F],[Dew Point F],[Wind Direction Degrees] 
# [Wind speed MPH],[sky conditions (%)],[weather],[station pressure (mb)]
def parse_row(row):
  
    date_object = datetime.strptime(row[3], "%I:%M%p, %A, %B %d, %Y")
    date_str = (datetime.strftime(date_object, "%m/%d/%Y,%H:%M"))
  
    seq = (date_str, "-99", "-99", parse_wind_dir(row[2]), parse_wind_speed(row[1]),
    "-99", "-99", "-99")
  
    print (seq)
    return seq


# returns data table of elements found at given url
def parse_website(url):
    # open website
    response = urllib2.urlopen(url)
    html_doc = response.read()

    # parse using BeautifulSoup
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    # finds html elements on page
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    # finds all non empty table data
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    return data


# generates the folder name based on system time Observations_YYYY-MM-DD-HH
def build_folder_name():
    date_str = str(datetime.now()).replace(" ", "").replace(":","")
    # place '-' inbetween DD and HH
    date_str = date_str[:10] + '-' + date_str[10:]    
    # strips the trailing characters from time string, leaving YYYY-MM-DD-HH
    date_str = date_str[:-11]
    return 'Observations_' + date_str


def main():
    # where data files are written to
    save_path = 'C:/NRC/RASCAL43/Downloaded_Met_Data/'
    #save_path = 'C:/Users/telsbree/git/pge-weather-scraper/'
    folder_name = build_folder_name()
        
    # joins the specified directory with the folder name    
    folder_path = os.path.join(save_path, folder_name)    

    # creates directory if not already made
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)

    web_data = parse_website("http://www.pge.com/about/edusafety/dcpp/index.jsp")


    # for each tower, create or append to file
    # write a line of data to file
    for row in web_data:
      tower = met_towers[row[0]]
      file_path = os.path.join(folder_path, tower + '.obs')
  
      # check to see if file exists
      if os.path.isfile(file_path):
        new_file = False
      else:
        new_file = True
  
      f = open(file_path, 'a')
      # write column header if file is
      if new_file:
        f.write("date (mm/dd/yyyy),time (hh:mm),temperature (F),dew point (F),wind direction (deg),wind speed (mph),sky conditions (%),weather,station pressure (mb)\n")

      # write formatted data to file
      row_list = parse_row(row)
      
      if row_list[3] == "invalid wind dir":
        print ("invalid wind dir found")
      elif row_list[4] == "invalid wind":
        print ("invalid wind found")
      else:
        s = ","
        row_str = s.join(row_list)
        f.write(row_str + "\n")
        f.close()

if __name__ == "__main__":
        main()
