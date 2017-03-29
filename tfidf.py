import sys
import random
import math
import re
import collections
import time
import pprint
import string

def makeDocs(filename):
	stop = ["a","br","about","above","after","again","against","all","am","an","and","any","are","arent","as","at","be","because","been","before","being","below","between","both","but","by","cant","cannot","could","couldnt","did","didnt","do","does","doesnt","doing","dont","down","during","each","few","for","from","further","had","hadnt","has","hasnt","have","havent","having","he","hed","hell","hes","her","here","heres","hers","herself","him","himself","his","how","hows","i","id","ill","im","ive","if","in","into","is","isnt","it","its","its","itself","lets","me","more","most","mustnt","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shant","she","shed","shell","shes","should","shouldnt","so","some","such","than","that","thats","the","their","theirs","them","themselves","then","there","theres","these","they","theyd","theyll","theyre","theyve","this","those","through","to","too","under","until","up","very","was","wasnt","we","wed","well","were","weve","were","werent","what","whats","when","whens","where","wheres","which","while","who","whos","whom","why","whys","with","wont","would","wouldnt","you","youd","youll","youre","youve","your","yours","yourself","yourselves","movie","film","see"]
	text = open(filename, "r")
	lines = text.read().splitlines()
	text.close()
	i = 0
	docs = []
	while i < len(lines):
		if string.count(lines[i],"@facebook") > 1:
			i += 1
			"""
			skip the line and begin a new document
			"""
			temp_doc = []
			while i < len(lines) and string.count(lines[i],"@facebook") <= 1:
				if "@facebook" not in lines[i]:
					words = [w for w in lines[i].lower().split() if w not in stop]
					for w in words:
						temp_doc.append(w)
				i += 1
			docs.append(temp_doc)
		i += 1
	for d in docs:
		num_words = len(d)
		d = collections.Counter(d)
		d["totalCount"] = num_words

	return docs


def tfIdf(word,doc,docs):
	"""
	Does the TfIdf math
	"""
	tf = doc[word]/doc["totalCount"]
	docsContaining = sum(1 for d in docs if word in d)
	idf = math.log(len(docs) / (1 + docsContaining))

	return tf*idf

def scoreDoc(doc,doclist):
	scores = {word: tfIdf(word,doc,doclist) for word in doc}
	del scores["totalCount"]
	sorted_words = sorted(scores.items(), key = lambda t: t[1])
	return sorted_words

def buildWords(filename):
	stop = ["a","br","about","above","after","again","against","all","am","an","and","any","are","arent","as","at","be","because","been","before","being","below","between","both","but","by","cant","cannot","could","couldnt","did","didnt","do","does","doesnt","doing","dont","down","during","each","few","for","from","further","had","hadnt","has","hasnt","have","havent","having","he","hed","hell","hes","her","here","heres","hers","herself","him","himself","his","how","hows","i","id","ill","im","ive","if","in","into","is","isnt","it","its","its","itself","lets","me","more","most","mustnt","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shant","she","shed","shell","shes","should","shouldnt","so","some","such","than","that","thats","the","their","theirs","them","themselves","then","there","theres","these","they","theyd","theyll","theyre","theyve","this","those","through","to","too","under","until","up","very","was","wasnt","we","wed","well","were","weve","were","werent","what","whats","when","whens","where","wheres","which","while","who","whos","whom","why","whys","with","wont","would","wouldnt","you","youd","youll","youre","youve","your","yours","yourself","yourselves","movie","film","see"]
	"""
	Read all the lines from the file
	"""
	text = open(filename, "r")
	lines = text.read().splitlines()
	text.close()
	words = []
	phrases = []
	"""
	Run through every line
	"""
	for i in lines:
		if "@facebook" not in i:
			"""
			Build words
			"""
			j = [k for k in i.lower().split() if k not in stop]
			for k in j:
				words.append(k)
	"""
	We now have a list of all the words, duplicates included
	But return a counted dict of the words
	"""
	num_words = len(words)
	words = collections.Counter(words)
	words["totalCount"] = num_words

	return words



def buildPhrases(lines,words,word_count):
	phrases = []
	"""
	For each phrase
	"""
	for i in lines:
		rank = 0
		"""
		Rank every word in the phrase according to our metric
		"""
		for j in i:
			rank += rankWord(j,words,word_count)
		phrases.append(i,rank)
	"""
	return an ordered list of the most important phrases
	"""
	return phrases.sort(key=lambda tup: tup[1])

docs = makeDocs(sys.argv[1])

common_words = buildWords(sys.argv[2])

top_words = scoreDoc(common_words,docs)

print common_words.most_common(25)

i = 1
for word, score in top_words[:25]:
	print "{0} -- {1} -- {2}".format(i,word,round(score,5))
	i += 1





