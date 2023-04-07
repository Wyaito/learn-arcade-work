import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)
#create dictionary list
dictionary = open('dict.txt')
dict_list = []
for line in dictionary:
    line = line.strip()
    dict_list.append(line)
dictionary.close()
#load alice in wonderland
AIW = open('AliceInWonderLand200.txt')
for line in AIW:
    word_list = []
    #AIW = open('AliceInWonderLand200.txt')
    line = split_line(line)
    word_list.append(line)
print(word_list)



print('--- linear search ---')

