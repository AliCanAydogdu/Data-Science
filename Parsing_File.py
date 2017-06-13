 # Here's the code we used to parse the crime_rates.csv file.

    f = open("crime_rates.csv", 'r')
    data = f.read()
    rows = data.split('\n')
    full_data = []
    for row in rows:
      split_row = row.split(",")
      full_data.append(split_row)
