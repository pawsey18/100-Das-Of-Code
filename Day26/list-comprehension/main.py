
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)


# Comparing two lists of files with comprehension
with open("file1.txt") as f1, open('file2.txt') as f2:
    file_one = [line.strip() for line in f1]
    file_two = [line.strip() for line in f2]
    number_list_one = list(map(int, file_one))
    number_list_two = list(map(int, file_two))

# Note to self: Look more into zip and map
result = [i for i, j in zip(file_one, file_two) if i == j]
# Write your code above 👆

print(result)
