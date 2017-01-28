 > Filtering the List

 # The data set contains first names shared by at least 100 people. Let's limit it those shared by at least 1,000 people.

 numerical_list[len(numerical_list)-1]
 thousand_or_greater =[]
 for numerical in numerical_list:
     name = numerical[0]
     population = numerical[1]
     if (numerical[1] >= 1000):
        thousand_or_greater.append(name)
        print(thousand_or_greater[0:10])
