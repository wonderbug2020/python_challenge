#First to import the required dependencies.
import os
import re
import statistics as st

#Now to load the text file into a variable
with open("resource/paragraph_3.txt", "r") as myfile:
    data = myfile.read()

#Finding the word count is a single line of code, but there are variations that can be used depending on what you want
#Simply using split we are grabing words based on blank spaces. There is an alternative, findall, that grabs words based on not letters, ie -'s
#One one hand, using the split means that lion's is treated as 1 word instead of two, but words also include .'s like the end of sentences.
#This second mother might throw off our average word length by a small amount, if someone was that concerned about them, they could easily be removed
word_count = data.split()

#Next to find the number of sentences. This is again a 1 line answer and was actually provided for us
#This is similar to our previous answer but instead of using the default ' ' blank space, we've replaced
# it with common sentence enders . ! and ?
sentence_count = re.split("(?<=[.!?]) +", data)

#The third answer asks for the average word length, which is fairly easy since we have a list of the words
#First a list and a counter storage variable
word_length_list = []
word_length = 0
for word in word_count:
    word_length = len(word) #again, words still have .'s and ,'s but we are just going to leave those in.
    word_length_list.append(word_length)

#now to but this in a variable for average word word length
average_wl = round(st.mean(word_length_list),1)

#Finally, the average sentence length is just word count / sentence count
average_sl = len(word_count)/len(sentence_count)

line_1 = "Paragraph Analysis\n"
line_2 = "--------------------\n"
line_3 = f"Approximate Word Count: {str(len(word_count))}\n"
line_4 = f"Approximate Sentence Count: {str(len(sentence_count))}\n"
line_5 = f"Average Letter Count: {str(average_wl)}\n"
line_6 = f"Average Sentence Length: {str(average_sl)}\n"

#Here is where I print the report to the terminal
print(line_1 + line_2 + line_3 + line_4 + line_5 + line_6)

#Finally, to save the report to a file in the analysis folder
f = open("analysis/report.txt","w+")
f.write(line_1 + line_2 + line_3 + line_4 + line_5 + line_6)
