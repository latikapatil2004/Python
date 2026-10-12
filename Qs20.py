'''
Word Frequency
Write a Python program to take a sentence from the user and store each word and its frequency in a 
dictionary. Display the resulting dictionary'''



sentence=input("enter the String")
words=sentence.split()
freq={}
for word in words:
    if word in freq:
        freq[word]=freq[word]+1
    else:
        freq[word]=1
        
print(freq)
    