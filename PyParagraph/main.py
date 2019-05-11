# Dependencies
import re
import os

# Read in file
filepath = os.path.join("paragraph_2.txt")
with open(filepath, 'r') as text:
    paragraph = text.read()

#Declare variables
wordCount = 0.0
wordAverage = 0.0

# Split all words in read in paragraph to list
# Iterate through list to get a count a total count of letters in each word
# Calculate average word length using total letter count divided by the number of words
words = paragraph.split()
for word in words:
    wordCount += len(word)
wordAverage = wordCount / len(words)

# Declare variables
sentenceCount = 0.0
sentenceAverage = 0.0

# Split paragraph into sentences using regular expression
# Iterate through list to count number of words per sentence
# Determine average sentence length in words by dividing count by total number of sentences
sentences = re.split("(?<=[.!?]) +", paragraph)
for sentence in sentences:
    wordsInSentence = sentence.split()
    sentenceCount += len(wordsInSentence)   
sentenceAverage = sentenceCount / len(sentences)

# Print results to terminal
print (f"Paragraph Analysis")
print (f"------------------")
print (f"Approximate Word Count: {len(words)}")
print (f"Approximate Sentence Count: {len(sentences)}")
print (f"Average Letter Count: {wordAverage:,.1f}")
print (f"Average Sentence Length: {sentenceAverage:,.1f}")

# Output to file
_, filename = os.path.split(filepath)
textpath = os.path.join("output", filename)

with open(textpath, "w+") as file:
    file.write (f"Paragraph Analysis\n")
    file.write (f"------------------\n")
    file.write (f"Approximate Word Count: {len(words)}\n")
    file.write (f"Approximate Sentence Count: {len(sentences)}\n")
    file.write (f"Average Letter Count: {wordAverage:,.1f}\n")
    file.write (f"Average Sentence Length: {sentenceAverage:,.1f}\n")
file.close() 
