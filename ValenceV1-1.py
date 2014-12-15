#-------------------------------------------------------------------------------
# Name:        ValenceV1.1.py
# Purpose:     sentiment analysis
#
# Author:      Mohammad Darwich
#
# Created:     15/12/2014
# Copyright:   (c) DataSentimentAnalysis.com
#-------------------------------------------------------------------------------

import string

def main():

    #get positive lexicon
    f = open("positive-words.txt", "r")
    if (f.mode == "r"):
        posLexicon1 = f.read()
        posLexicon2 = (posLexicon1.split())
        #print (posLexicon2)

    #get negative lexicon
    f = open("negative-words.txt", "r")
    if (f.mode == "r"):
        negLexicon1 = f.read()
        negLexicon2 = (negLexicon1.split())
        #print (negLexicon2)

    #read input doc
    f = open("input_doc.txt", "r")
    if (f.mode == "r"):
        input = f.read()
    #print (input)

    #preprocessing: remove punctuation
    for x in string.punctuation:
        input = input.replace(x,"")
    #print (input)

    #preprocessing: convert text to lowercase
    input = input.lower()
    #print (input)

    #tokenization: add words to a wordList
    wordsList = input.split()
    #print (wordsList)

    #check for matches in positive lexicon
    posMatches = []
    posMatchCount = 0

    for word in wordsList:
        if word in posLexicon2:
            posMatches = posMatches + [word] #add matched word to list
            posMatchCount += 1 #increment match counter
    print (posMatchCount)

    #check for matches in negative lexicon
    negMatches = []
    negMatchCount = 0

    for word in wordsList:
        if word in negLexicon2:
            negMatches = negMatches + [word] #add matched word to list
            negMatchCount += 1 #increment match counter
    print (negMatchCount)

    #comparison of pos words and neg words
    if (posMatchCount > negMatchCount):
        polarity = "POSITIVE"
    elif (posMatchCount < negMatchCount):
        polarity = "NEGATIVE"
    else:
        polarity = "NEUTRAL"

    print ("Analyzing document's polarity...")
    print ("Matched pos words (%d): " % posMatchCount, posMatches)
    print ("Matched neg words (%d): " % negMatchCount, negMatches)
    print ("Polarity of document is: %s" % polarity)

if __name__ == '__main__':
    main()
