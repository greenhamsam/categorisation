'''
Doesn't work

import csv
from io import StringIO

url_base = '/Users/Sam/Source/categorisation/'
training_url = url_base + 'categorised-txns-training-set.csv'
csvf = StringIO(training_url.read().decode())
reader = csv.reader(csvf, delimiter=',')

with open(f,'rb') as file:
    rows = csv.reader(file, 
                      delimiter = ',', 
                      quotechar = '"')
    data = [data for data in rows]

print(data)