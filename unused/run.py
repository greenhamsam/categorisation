from csv import DictReader

url_base = '/Users/Sam/Source/categorisation/'
training_url = url_base + 'categorised-txns-training-set.csv'
f = open(training_url)
data = DictReader(f)

for key, group in grouped:
	print(key)
	keyfunc = itemgetter('amount')
	sub_records = sorted(group, key=keyfunc)
	sub_grouped = groupby(sub_records, keyfunc)
	low_count, low_key = 0, None

	for sk, sg in sub_grouped

