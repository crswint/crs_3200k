#Homework 4
#Christopher Swint
#Ch 6: 8, Ch 7: 10, Ch 9: 7, 10


#8) a)if population < 10000000
#           print population
#   b)if population > 10000000 and population < 35000000:
#           print population
#   c)if population / area > 1:
#           print "Densley Populated"
#   d)if population / area > 1:
#           print "Densley Populated"
#     else:
#           print "Sparsely Populated"


#10) time = 0
#    rat_1_weight = 10.0
#    growth_rate = 0.04
#  a)while rat_1_weight < 12.5:
#       rat_1_weight = rat_1_weight + growth_rate * rat_1_weight
#       print rat_1_weight
#       time = time + 1
#  b)time = 0
#    rat_1_weight = 10.0
#    rat_2_weight = 10.0
#    rat_1_rate = 0.11
#    rat_2_rate = 0.01
#    while rat_1_weight <= (rat_2_weight * 1.1):
#        rat_1_weight = rat_1_weight + rat_1_rate * rat_1_weight
#        rat_2_weight = rat_2_weight + rat_2_rate * rat_2_weight
#        print rat_1_weight
#        time = time + 1


#7)  def count_doubles(x):
#        """ Takes a dictionary as an arguement and returns the number of values
#        that appear more than once."""
#        x = list(x.values())
#        duplicates = []
#        for i in x:
#           if i not in duplicates and x.count(i) > 1:
#                duplicates.append(i)
#
#        num_duplicates = len(duplicates)
#        return num_duplicates



#10)  def d_intersect(x, y):
#        """ Takes two dictionaries as arguements and returns a dictionary that
#        contains only the key/value pairs found in the originals."""
#
#        x_dict = set(list(x.items()))
#        y_dict = set(list(y.items()))
#        x_ints_y_set = x_dict.intersection(y_dict)
#        x_ints_y_dict = dict(x_int_y_set)
#        return x_ints_y_dict