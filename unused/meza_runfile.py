from io import open, StringIO
from meza import io

fs_base = '/Users/Sam/Source/categorisation/'
training_url = fs_base + 'categorised-txns-training-set.csv'

records = io.read_csv(training_url)
f = StringIO()