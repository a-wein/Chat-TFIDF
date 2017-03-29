import sys
import random
import math
import re
import collections
import time
import pprint

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
	"""
	return collections.Counter(words), lines

def rankWord(word):
	"""
	Math to rank words
	TODO
	"""


def buildPhrases(lines,words):
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
			rank += rankWord(j)
		phrases.append(i,rank)
	"""
	return an ordered list of the most important phrases
	"""
	return phrases.sort(key=lambda tup: tup[1]



common_words,lines = buildWords(sys.argv[1])

phrases = buildPhrases(lines,words)

pprint.pprint(common_words.most_common(100))





