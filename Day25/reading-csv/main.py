# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row[1])
#
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)
# Square bracelet, is sometimes used with for loops - It is called List Comprehension
# used for a way to create a new list from an old list.
# res = [int(i) for i in temperatures]
# print(res)
# or just convert


# Working with CSV files, as we can see would be quite difficult to work with if we had a number
# of files to work with. So, that's why we can use Pandas.

import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'])


