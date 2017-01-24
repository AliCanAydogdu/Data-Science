Files and Loops

//Opening Files

To open a file in Python, we use the open() function.

  open("story.txt", "r")

//Reading Files

We use the read() function to read the contents of "story.txt" into a File object, and assign that object to g:

  f = open("test.txt", "r")
  g = f.read()

//Splitting Files

In Python, we can use the split() method to turn a string object into a list of strings, like so:

  sample = "john,plastic,joe"
  split_list = sample.split(",")
  # split_list is a list of _strings_: ["john", "plastic", "joe"]

//List of Lists

The following code:

- splits each element in three_rows (which contains the first three elements from rows) on the comma delimiter (,)
- appends the resulting list (split_list) to a new list we create (final_list)
- displays the final list using the print() function

  three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
  final_list = []

  for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
    print(final_list)

// Splitting Elements In a List

Let's now convert the full dataset, rows, into a list of lists using the logic from the previous step.


  f = open('crime_rates.csv', 'r')
  data = f.read()
  rows = data.split('\n')
  print(rows[0:5])
  final_data = []
  for row in rows:
      split_list = row.split(',')
      final_data.append(split_list)
      print(final_data[0:5])

// Challenge

Create a list of integers named int_crime_rates that contains just the crime rates - as integers - from the list rows.

  f = open('crime_rates.csv', 'r')
  data = f.read()
  rows = data.split('\n')
  print(rows[0:5])
  int_crime_rates = []
  for row in rows:
    split_list = row.split(',')
    x = int(split_list[1])
    int_crime_rates.append(x)
