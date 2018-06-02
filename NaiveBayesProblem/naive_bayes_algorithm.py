#! /usr/bin/env python

import csv
import random
import math

# load raw data through data file
def loadcsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

# split the data into training set and test set
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return  [trainSet, copy]

# separate the data by different class
def separateByClass(dataset):
	separated  = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance =  sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

filename = 'pima_indians_data.csv'
dataset = loadcsv(filename)

# dataset = [[1],[2],[3],[4],[5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
# print('Split {0} rows into train with {1} and test with {2}').format(len(dataset), train, test)

# dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1]]
separated = separateByClass(dataset)
# print('Separated instances: {0}').format(separated)

numbers = [1,2,3,4,5]
print('Summary of {0}: mean={1}, stdev={2}').format(numbers, mean(numbers), stdev(numbers))