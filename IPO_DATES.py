import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time 


url = 'https://www.ipowatch.in/p/upcoming-ipo-calendar.html'

#url = 'https://stockanalysis.com/ipos/'


xlwriter = pd.ExcelWriter("INDIAN IPO's.xlsx")

response = requests.get(url)
soup = bs(response.content, 'html.parser')

#ipo = soup.find('table' , 'tb1Data1') #economic_times data


# since it's of TABLE element(INSPECT), we can directly import using 'pd.read_html' function

tables = pd.read_html(str(soup))

#print(tables[0])

#Many tables present,so importing the first table - [0] ; header=False removes the column head

tables[0].to_excel(xlwriter, sheet_name='Upcoming IPOs', index=False , header=False, freeze_panes=(1,1))

xlwriter.save()

print("File Exported")


