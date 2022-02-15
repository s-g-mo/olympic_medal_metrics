'''
SCRIPT olympic_medal.py

This script scrapes medal tally data from the Olympic website and computes the
weighted-medal total for each. It then prints out the rankings according to
this metric.

Stephen M. February, 2022
'''

#################################### IMPORTS ###################################

import metrics, utils
from datetime import datetime

##################################### MAIN #####################################

# Scrape country and medal data from the web.
data = utils.medal_count()

# Compute the weighted total metric for each country.
data['Weighted Total'] = metrics.weighted_total(data.iloc[:,1:4].to_numpy())

# Print out a time-stamp and table with countries ranked by weighted total.
print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
print(data.sort_values('Weighted Total')[::-1])

###################################### END #####################################
