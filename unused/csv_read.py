import csv

url_base = '/Users/Sam/Source/categorisation/'
training_url = url_base + 'categorised-txns-training-set.csv'


with open('test.csv','rb') as file:
    rows = csv.reader(file, 
                      delimiter = ',', 
                      quotechar = '"')
    data = [data for data in rows]