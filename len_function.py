## Write a Python program that takes a sentence as input and
## counts the number of words in the sentence
sentence = input("Enter the sentence : ")
words = sentence.split()
length= len(words)
print("Total words in this sentence is " , length)
