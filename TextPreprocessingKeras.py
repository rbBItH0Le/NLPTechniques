# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:03:28 2021

@author: rohan
"""
import csv
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
stopwords =[ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
sentences = []
labels = []
with open("bbc-text.csv", 'r') as csvfile:
    readers=csv.reader(csvfile,delimiter=',')
    next(readers)
    for row in readers:
        labels.append(row[0])
        sentence=row[1]
        for word in stopwords:
            token=" "+word+" "
            sentence=sentence.replace(token," ")
            sentence=sentence.replace("  "," ")
        sentences.append(sentence)
        
tokenizer=Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

word_index=tokenizer.word_index
sequencer=tokenizer.texts_to_sequences(sentences)
padded=pad_sequences(sequencer,padding='post')
print(padded[0])

tokenizer1=Tokenizer(oov_token="<OOV>")
tokenizer1.fit_on_texts(labels)
sseq=tokenizer1.texts_to_sequences(labels)
