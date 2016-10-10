import pandas as pd

fs_base = '/Users/Sam/Source/categorisation/'
training_url = fs_base + 'categorised-txns-training-set.csv'

df = pd.read_csv(training_url)
print(df)