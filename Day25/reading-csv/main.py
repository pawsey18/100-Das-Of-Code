# # with open('weather_data.csv') as data_file:
# #     data = data_file.readlines()
#
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         # print(row[1])
# #
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
#
# # print(temperatures)
# # Square bracelet, is sometimes used with for loops - It is called List Comprehension
# # used for a way to create a new list from an old list.
# # res = [int(i) for i in temperatures]
# # print(res)
# # or just convert
#
#
# # Working with CSV files, as we can see would be quite difficult to work with if we had a number
# # of files to work with. So, that's why we can use Pandas.
#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# average_total = 0
# for num in temp_list:
#     average_total += num
#
# average = average_total / len(temp_list)
# print(f'The average of the temperature is: {int(average)}')
#
# # we can use the built in method  sum(temp_list) / len(temp_list instead of for first example to get the mean.
#
# # pandas, you can use the data['temp'] series and call .mean() to get the average instead of the other two examples
#
# # Get the highest number
# # using the series
# highest_number = data['temp'].max()
# print(highest_number)
#
# # Get column
# print(data['condition'])
# # we can use these headings as attributes.
# # case sensitive
# print(data.condition)
#
# # get data row
# print(data[data.day == 'Monday'])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp * 9 / 5 + 32
# print(monday_temp)
#
# # create a dataframe
# data_dict = {
#     'students': ['John', 'James', 'Johnny'],
#     'scores': [76, 78, 89]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(new_data)
#
# # creating a new csv file
#
# # data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

dict_data = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(dict_data)
df.to_csv('squirrel_count.csv')
