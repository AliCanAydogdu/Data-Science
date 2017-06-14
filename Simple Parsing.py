f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates = []
for row in rows:
    split_list = row.split(',')
    x = int(split_list[1])
    int_crime_rates.append(x)
