#WordCloud of my linkdin profile: https://www.linkedin.com/in/iamprateek/

# Start with loading all necessary libraries

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator #We will use these modules to achive our goal
import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image

#Words which are uninteresting and can be avoided in cloud
stopwords = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "also", "these", "other", "after", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "says", "again", "about", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "in", "said", "what", "like", "not", "would", "could", "up", "one", "back", "out", "get", "going", "know", "then", "want","so","asked","into","down", "on", "for", "us"]

# Full profile - https://www.linkedin.com/in/iamprateek/

with open('mylinkdin.txt', 'r', encoding="utf-8") as file:
	file_contents = file.read() #Saving file content into variable called 'file_contents'


punctuations = '''''!()-[]{};:'"\,<>./?@#$%^&*_~''' 

# remove punctuation from the string and make it lower case
text = ""
for char in file_contents.lower():
	if char not in punctuations:
		text = text + char

#Appearance
wc = WordCloud(width = 1584, height = 396,
background_color = "white",
max_words = 1000,
stopwords = stopwords)

			   
wc.generate(text)

#Plotting
#plt.imshow(wc, interpolation = 'bilinear')
#plt.axis('off')
#plt.show()

wc.to_file('mylinkdin2.png')
