  > Dictionaries
  #To figure out what score Sue got on the test, we'd first have to write a loop to find the index corresponding to the element Sue in the students list. We'd then have to find the value for that index in scores. Here's how we could do this:

  indexes = [0,1,2,3]
  name = "Sue"
  score = 0
  for i in indexes:
      if students[i] == name:
          score = scores[i]
  print(score)

  > Indexing a Dictionary

  president_ranks = {}
  president_ranks["FDR"] = 1
  president_ranks["Lincoln"] = 2
  president_ranks["Aquaman"] = 3
  fdr_rank = president_ranks["FDR"]
  lincoln_rank = president_ranks["Lincoln"]
  aquaman_rank = president_ranks["Aquaman"]

  > Defining a dictionary

  random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
  print(random_values)
  animals ={
      7:"raven",
      8:"goose",
      9:"duck"
      }
      times = {
      "morning":9,
      "afternoon":14,
      "evening":19,
      "night":23
      }

  > Count the number of times that each element occurs in the list named pantry that appears in the code block below. 

  pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
  pantry_counts ={}
  for item in pantry:
      if item in pantry_counts:
          pantry_counts[item] = pantry_counts[item] + 1
          else:
          pantry_counts[item] = 1
