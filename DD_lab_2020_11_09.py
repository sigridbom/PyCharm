# csv_cloud.py
# a small program that reads text from a csv file
# visualizes it as a WordCloud

# import packages
from wordcloud import WordCloud, STOPWORDS
import csv

# open the csv file
# read the first row of headers into a var and print it
# find out the index of the text part of the tweet
# then use it to read the text of the tweet from the row and add that to
# a string variable called text

with open('./Data/covid19_tweets.csv', encoding = 'utf8') as f:
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    text = []
    for row in rows:
        text_string = str(row[9])
        text.append(text_string)
    print(len(text))

# OR
# text = ""
# for row in rows:
#   text += row[9]

# put the contents of STOPWORDS into your own variable called my_stopwords
# add or remove stopwords if necessary

my_stopwords = STOPWORDS
my_stopwords.update({'https', 'co', 'coronaviru', 'th', 'don', 've', 'amp'}) # opposite is .remove
print('https' in my_stopwords)

# generate the wordcloud
# remember to specify that it should use our stopwords
# try experimenting with collocations as well
# maybe even make it salmon-colored

my_wordcloud = \
    WordCloud(
        width = 3000, height = 2000,
        random_state = 1,  # always the same
        collocations = False,
        background_color = 'lime',
        stopwords = my_stopwords
    ).generate(" ".join(text))  # make the list into a string


# save the wordcloud to a file
my_wordcloud.to_file('./Clouds/tweets.png')

# print out that we are done creating the wordcloud
print('We are done, yay!')