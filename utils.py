'''
FUNCTION SET utils.py

A set of functions to facilitate my Olympics medal scraping project.

Stephen M. February, 2022
'''

#################################### IMPORTS ###################################

import requests
import numpy as np
import pandas as pd
from lxml import html

################################### FUNCTIONS #################################


# Scraping function. Scrapes medal tally data from Olympics official website
def medal_count():

  # Initialize empty lists to hold countries and their medal counts.
  countries = []
  medal_count = []
 
  # Get HTML data from Olympic URL.
  page = requests.get('https://olympics.com/beijing-2022/olympic-games/en/results/all-sports/medal-standings.htm')
  
  # Create a Tree Object from the HTML data.
  tree = html.fromstring(page.content)
  
  # Isolate table data (table rows 'tr') from the Tree.
  table_rows = tree.xpath('//tr')
  
  # Loop through table rows.
  for i, row in enumerate(table_rows):
    
    # First row is the header, not interested.
    if i == 0:
      continue
  
    # The rows of interest contain 8 elements: 
    # Rank, Name of Country (NOC), Gold, Silver, Bronze, Total, Abbreviated NOC
    # Only interested in elements 1 - 4. W
    for j, item in enumerate(row.iterchildren()):
      if (j < 1) or (j > 4):
        continue
  
      # Extract element of interest. Remove unwanted characters.
      data = item.text_content().strip('\r')
      
      # If the data is a country name, it will have length > 2
      if len(data) > 2:
        if data == 'Total': # Ignore these entries.
          continue
        else:
          countries.append(data)

      # If the data is numeric, it will have length <= 2.
      if len(data) <= 2:
        if data == '': # Ignore these entries.
          continue
        else:
          medal_count.append(int(data))

  # Clean up the lists and disregard unwated data.
  L = len(countries)
  medal_count = medal_count[0:L*3]
  medal_count = np.array(medal_count).reshape(L,3)

  # Compute medal totals.
  totals = np.sum(medal_count, axis=1)

  # Package everything into a pandas DataFrame.
  final_data = pd.DataFrame({'Country': countries,
                             'Gold': medal_count[:,0],
                             'Silver': medal_count[:,1],
                             'Bronze': medal_count[:,2],
                             'Total': totals})
  
  
  return final_data    