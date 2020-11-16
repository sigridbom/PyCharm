# wiki_plot.py

# check out NLTK
#
# a small programs that grabs the text from a wikipedia article
# counts the occurence of each word and visualizes it as a bar graph
#
# remember that the text could just as well come from a pdf
# Do:
# import packages
import wikipedia
import matplotlib as plt
from wordcloud import STOPWORDS
import collections

# DO:
# get wikipedia page for Coronavirus disease 2019
# and extract the text to a var called text
wiki = wikipedia.page('Coronavirus disease 2019')
text = wiki.content
#print(text)

# DO:
# turn all the text lowercase to make it easier to do comparisons later
text = text.lower()

# DO:
# replace characters we dont want to see
text = text.replace('=', '')
text = text.replace('"', '')
text = text.replace('.', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('-', '')
text = text.replace(':', '')
text = text.replace(',', '')

# DO:
# split the text into a list called text_list
# where each entry (hopefully) is a word
# # which character do we split around?
text_list = text.split(' ')

# DO LATER IF NECESARY:
# add words to or remove words from the STOPWORDS list
my_stopwords = STOPWORDS

# DO:
# remove all the stopwords from our text_list
# go through each item of the text_list and add it to another list if
# if the current item/word is not present in the STOPWORDS list
# end with replacing the contents of text_list with the new list
cleaned = []
for word in text_list:
    if word not in my_stopwords:
        cleaned.append(word)

print(my_stopwords in cleaned)
text_list = cleaned
print(text_list[1:300])

# the most pythonic way of doing it
# text_list = [word for word in text_list if word not in my_stopwords]

# DO:
# create empty dictionary called my_dict
my_dict = {}

# DO:
# for loop through the text and count the occurence of each word
# in our dictionary
# decide what should be the key and what should be the value
# if the word is not in the dictionary then create an entry with an appropiate
# value
# else update the dictionary so the new occurence of the word is counted

for word in text_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

print(my_dict)

# my_dict = Counter(text_list) # count the occurence of each element in a list and make it into a dictionary
# default.dict from package 'collections'
# set.default for dictionaries

# DO:
# create a variable called to_print that contains a number
# that decides how many words we want to visualize
# sort the dictionary by the values (the count) and only get the number of
# words that we just decided
# this will turn the dict into a list. We will turn it back later

to_print = 10

my_list = sorted(my_dict.items(), key=lambda k_v: k_v[1], reverse=True)[:to_print] # this is continued from the previous assignment
# print out the words and counts to make sure
for word, count in my_list:
    print(word, ":", count)
#turning the list back into a dict
my_dict = dict(my_list)

# getting out all the keys and values
names = list(my_dict.keys())
values = list(my_dict.values())

# plotting all the keys and values as bar graph
plt.bar(range(len(my_dict)),values,tick_label=names)
#plt.savefig('bar.png')
plt.show()