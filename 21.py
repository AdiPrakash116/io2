import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from textblob import TextBlob



    
    text="""My name is Adithya! What about yours? It is a very beautiful day today."""
    tokenized_text=sent_tokenize(text)
    print(tokenized_text)
    
    #breaks paras into sentences.


    text="""My name is Adithya! What about yours? It is a very beautiful day today."""
    tokenized_word=word_tokenize(text)
    print(tokenized_word)
    #text into words


    
