# Olympic Medal Metric

I thought this would be a fun project to do, to refresh myself on web-scraping.

It's fun to look at Olympic medal counts as the games progress, but it
always kind of annoys me how countries are most often ranked. Most often, medal
tally tables rank countries by the total number of gold medals, and only
consider silver and bronze for breaking ties. Another common metric for ranking
a country's performance is simply their total medal count. 

I think a better metric than both of these is a weighted-total. In my
opinion, the most natural weighting is gold=3, silver=2, and bronze=1. I think
that such a metric is a more complete representation of a country's overall
performance. Of course, I'm obviously biased, because this metric helps boost 
Canada's position quite a bit (at the time of publishing). You're welcome, Canada!

Run the main script (olympic_medal.py) in your terminal and it will output a nice time-stamped
table ranking countries by their weighted-total medal count.

Some fun next steps would be to figure out how to implement this table +
automatic updates into a website, or to build an app that can update on 
demand.

Requires: 
  - Python3
  - Numpy
  - Pandas
  - lxml
