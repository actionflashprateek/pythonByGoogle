#WordCloud of Demonetization speech by Prime Minister Narendra Modi On November 8, 2016

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

# Full speech - https://www.huffingtonpost.in/2016/11/08/heres-the-full-text-of-modis-speech-on-the-discontinuation-of_a_21601525/
with open('dem.txt', 'r', encoding="utf8") as file:
	file_contents = file.read() #Saving file content into variable called 'file_contents'


punctuations = '''''!()-[]{};:'"\,<>./?@#$%^&*_~''' 

# remove punctuation from the string and make it lower case
text = ""
for char in file_contents.lower():
	if char not in punctuations:
		text = text + char

#Appearance
custom_mask = np.array(Image.open('20489081.jpg')) 
wc = WordCloud(background_color = "white",
               stopwords = stopwords,
               mask = custom_mask,
			   max_words = 2000,
			   min_word_length = 3)
			   
#contour_width = 3, contour_color = 'black'

			   
wc.generate(text)
#image_colors = ImageColorGenerator(custom_mask)
#wc.recolor(color_func = image_colors)

#Plotting
#plt.imshow(wc, interpolation = 'bilinear')
#plt.axis('off')
#plt.show()

wc.to_file('dem_wordcloud.png')
