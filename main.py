import os

path = 'tweets.txt'  #Add path according to your system
file_path = f"{path}"
file1 = open(file_path, 'r')
tweets = file1.readlines()

racial_slurs = ['asshole', 'freak', 'bastard', 'niggar', 'moron']
bad_words_count = []
total_words_count = []
degree_of_profanity = []

for tweet in tweets:
    words = tweet.split(' ')
    total_words_count.append(len(words))

for tweet in tweets:
    count = 0 
    for slur in racial_slurs:
        if slur in tweet:
            count+=1
    bad_words_count.append(count)

for i in range(len(tweets)):
    degree_of_profanity.append(bad_words_count[i]/total_words_count[i])

for i in range(len(tweets)):
    print("Degree of profanity in line ", i+1, " : ",degree_of_profanity[i])

