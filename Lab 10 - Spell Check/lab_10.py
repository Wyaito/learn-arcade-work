import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)
dictionary = open('dict.txt')
dict_list = []
for line in dictionary:
    line = line.strip()
    dict_list.append(line)
dictionary.close()
print('--- linear search ---')

