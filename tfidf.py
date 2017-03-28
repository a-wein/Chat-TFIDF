import sys
import random
import math
import re
import collections
import time


def loaddata(filename):
    text = open(filename, "r")
    lines = text.read().splitlines()
    reviews = []
    for i in range(len(lines)):
    	l1 = lines[i][-1:]
    	l2 = lines[i][:-1]
        review = (l2,l1)
        reviews.append(review)
    text.close()
    return reviews

def buildWords(lines):
	for i in lines:
		if "@facebook" not in i:
			