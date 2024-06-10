import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import requests
import urllib
import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
lem = WordNetLemmatizer()
nltk.data.path.append("C:\\Users\\Kalim\\AppData\\Roaming\\nltk_data")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = stopwords.words("english")

class Analysis:
    def stopword_data(self):
        auditor = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_Auditor.txt",encoding="ISO-8859-1")
        currencies = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_Currencies.txt",encoding="ISO-8859-1")
        dateandnums= open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_DatesandNumbers.txt",encoding="ISO-8859-1")
        generic = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_Generic.txt",encoding="ISO-8859-1")
        genericlong = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_GenericLong.txt",encoding="ISO-8859-1")
        geographic = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_Geographic.txt",encoding="ISO-8859-1")
        names = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\StopWords\\StopWords_Names.txt",encoding="ISO-8859-1")
        return auditor,currencies,dateandnums,generic,genericlong,geographic,names
    
    def master_dict_data(self):
        # Positive-words
        fileneg1 = open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\MasterDictionary\\positive-words.txt")
        fileneg1.seek(0)
        pos_words=fileneg1.read().split()
        
        #Negative words
        fileneg2= open("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Providedfiles\\MasterDictionary\\negative-words.txt")
        fileneg2.seek(0)
        neg_words=fileneg2.read().split()
        
        return pos_words,neg_words
    
    def text_corpus(self,x):
        auditor,currencies,dateandnums,generic,genericlong,geographic,names = self.stopword_data()
        string_format = str(x).lower()
        lower_words = re.sub('[^a-zA-Z]+'," ",string_format).strip()
        token= word_tokenize(lower_words)
        token_word = [t for t in token if t not in (auditor,currencies,dateandnums,generic,genericlong,geographic,names)]
        lemmitized = [lem.lemmatize(w) for w in token_word]
        return lemmitized
    
    def count_syllable(self,word):
        vowels = ["a","e","i","o","u","y"]
        count = 0 
        pre_char_vowel = False
        
        for char in word:
            if char in vowels:
                count+=1
                pre_char_vowel = True
            else:
                pre_char_vowel =False
        return count
    
    def complexity_per(self,words):
        num_complex_word =sum(1 for word in words if self.count_syllable(word)>=2)
        total_words = len(words)
        num_of_complex_word = num_complex_word
        per_complex_word = (num_of_complex_word /total_words) * 100
        return per_complex_word,num_complex_word
    
    def count_syllable_per_word(self,words):
        syllable_per_words  = {word : self.count_syllable(words) for word in words}
        return syllable_per_words
    
    def pronoun_count(self,word_list):
        list_of_words  = ["I","we","my","ours","us"]
        list_word_counts = 0
        for word in word_list:
            if word in list_of_words:
                list_word_counts +=1
        return list_word_counts
                
    def avg_word_len(self,words):
        count = 0 
        for i in words:
            for j in i:
                count+=1
        return count
        
            

    
    