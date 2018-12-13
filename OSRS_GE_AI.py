import urllib.request, json
import re
import math
import collections
from collections import deque
from get_item import get_catalogue, get_graph

# x is examples in training set
# y is set of attributes
# label is target attributes
# Node is a class which has properties values, childs, and next
# root is top node in the decision tree

class Node(object):
	def __init__(self):
		self.value = None
		self.next = None
		self.childs = None

# Simple class of Decision Tree
# Aimed for who want to learn Decision Tree, so it is not optimized
class DecisionTree(object):
	def __init__(self, sample, attributes, labels):
		self.sample = sample
		self.attributes = attributes
		self.labels = labels
		self.labelCodes = None
		self.labelCodesCount = None
		self.initLabelCodes()
		# print(self.labelCodes)
		self.root = None
		self.entropy = self.getEntropy([x for x in range(len(self.labels))])

	def initLabelCodes(self):
		self.labelCodes = []
		self.labelCodesCount = []
		for l in self.labels:
			if l not in self.labelCodes:
				self.labelCodes.append(l)
				self.labelCodesCount.append(0)
			self.labelCodesCount[self.labelCodes.index(l)] += 1

	def getLabelCodeId(self, sampleId):
		return self.labelCodes.index(self.labels[sampleId])

	def getAttributeValues(self, sampleIds, attributeId):
		vals = []
		for sid in sampleIds:
			val = self.sample[sid][attributeId]
			if val not in vals:
				vals.append(val)
		# print(vals)
		return vals

	def getEntropy(self, sampleIds):
		entropy = 0
		labelCount = [0] * len(self.labelCodes)
		for sid in sampleIds:
			labelCount[self.getLabelCodeId(sid)] += 1
		# print("-ge", labelCount)
		for lv in labelCount:
			# print(lv)
			if lv != 0:
				entropy += -lv/len(sampleIds) * math.log(lv/len(sampleIds), 2)
			else:
				entropy += 0
		return entropy

	def getDominantLabel(self, sampleIds):
		labelCodesCount = [0] * len(self.labelCodes)
		for sid in sampleIds:
			labelCodesCount[self.labelCodes.index(self.labels[sid])] += 1
		return self.labelCodes[labelCodesCount.index(max(labelCodesCount))]

	def getInformationGain(self, sampleIds, attributeId):
		gain = self.getEntropy(sampleIds)
		attributeVals = []
		attributeValsCount = []
		attributeValsIds = []
		for sid in sampleIds:
			val = self.sample[sid][attributeId]
			if val not in attributeVals:
				attributeVals.append(val)
				attributeValsCount.append(0)
				attributeValsIds.append([])
			vid = attributeVals.index(val)
			attributeValsCount[vid] += 1
			attributeValsIds[vid].append(sid)
		# print("-gig", self.attributes[attributeId])
		for vc, vids in zip(attributeValsCount, attributeValsIds):
			# print("-gig", vids)
			gain -= vc/len(sampleIds) * self.getEntropy(vids)
		return gain

	def getAttributeMaxInformationGain(self, sampleIds, attributeIds):
		attributesEntropy = [0] * len(attributeIds)
		for i, attId in zip(range(len(attributeIds)), attributeIds):
			attributesEntropy[i] = self.getInformationGain(sampleIds, attId)
		maxId = attributeIds[attributesEntropy.index(max(attributesEntropy))]
		return self.attributes[maxId], maxId

	def isSingleLabeled(self, sampleIds):
		label = self.labels[sampleIds[0]]
		for sid in sampleIds:
			if self.labels[sid] != label:
				return False
		return True

	def getLabel(self, sampleId):
		return self.labels[sampleId]

	def id3(self):
		sampleIds = [x for x in range(len(self.sample))]
		attributeIds = [x for x in range(len(self.attributes))]
		self.root = self.id3Recv(sampleIds, attributeIds, self.root)

	def id3Recv(self, sampleIds, attributeIds, root):
		root = Node() # Initialize current root
		if self.isSingleLabeled(sampleIds):
			root.value = self.labels[sampleIds[0]]
			return root
		# print(attributeIds)
		if len(attributeIds) == 0:
			root.value = self.getDominantLabel(sampleIds)
			return root
		bestAttrName, bestAttrId = self.getAttributeMaxInformationGain(
			sampleIds, attributeIds)
		# print(bestAttrName)
		root.value = bestAttrName
		root.childs = []  # Create list of children
		for value in self.getAttributeValues(sampleIds, bestAttrId):
			# print(value)
			child = Node()
			child.value = value
			root.childs.append(child)  # Append new child node to current
									   # root
			childSampleIds = []
			for sid in sampleIds:
				if self.sample[sid][bestAttrId] == value:
					childSampleIds.append(sid)
			if len(childSampleIds) == 0:
				child.next = self.getDominantLabel(sampleIds)
			else:
				# print(bestAttrName, bestAttrId)
				# print(attributeIds)
				if len(attributeIds) > 0 and bestAttrId in attributeIds:
					toRemove = attributeIds.index(bestAttrId)
					attributeIds.pop(toRemove)
				child.next = self.id3Recv(
					childSampleIds, attributeIds, child.next)
		return root

	def printTree(self):
		if self.root:
			roots = deque()
			roots.append(self.root)
			while len(roots) > 0:
				root = roots.popleft()
				print(root.value)
				if root.childs:
					for child in root.childs:
						print('({})'.format(child.value))
						roots.append(child.next)
				elif root.next:
					print(root.next)


def test():
	f = open('playtennis.csv')
	attributes = f.readline().split(',')
	attributes = attributes[1:len(attributes)-1]
	print(attributes)
	sample = f.readlines()
	f.close()
	for i in range(len(sample)):
		sample[i] = re.sub('\d+,', '', sample[i])
		sample[i] = sample[i].strip().split(',')
	labels = []
	for s in sample:
		labels.append(s.pop())
	print(sample)
	print(labels)
	decisionTree = DecisionTree(sample, attributes, labels)
	print("System entropy {}".format(decisionTree.entropy))
	decisionTree.id3()
	decisionTree.printTree()

# Here starts the code for our predictive AI
def calc_recent_trend(catalogue):
    """Calculates the trend between the last 2 days"""
    for id in catalogue:
        daily = list(collections.OrderedDict(get_graph(id)['daily']).items())
        today = daily[-1][1]
        yesterday = daily[-2][1]

        if today - yesterday == 0:
            yield 'stay'
        elif today - yesterday > 0:
            yield 'rise'
        elif today - yesterday < 0:
            yield 'fall'


def calc_seven_trend(catalogue):
    """Calculates the trend between the last 7 days"""
    for id in catalogue:
        daily = list(collections.OrderedDict(get_graph(id)['daily']).items())
        today = daily[-1][1]
        week = daily[-8][1]

        if today - week == 0:
            yield 'neutral'
        elif today - week > 0:
            yield 'positive'
        elif today - week < 0:
            yield 'negative'


def is_expensive(price) :
    #print(price)
    #print(type(price))
    #high = re.compile('\d+\.\d+[bkm]')
    if type(price) is int:
        return 'cheap'
    else:
        return 'expensive'


def predict():
    """ID3 will output a decision tree built from the training set, which will
    be used to predict whether prices will rise or fall.
    """
    attributes = []
    # id = int(re.search('\d+', input("Enter the item id: ")).group())
    # print(id)

    attributes = ['day7', 'day30', 'day90', 'day180', 'price']
    catalogue = [  # Holds the list of items used to build the decision tree
        12397, 12395, 153, 1957, 548, 20997, 5104,
        11449, 1217, 10338, 12934, 554, 314, 2,
        855, 229, 1059, 2653, 596, 12297, 890,
        453, 565
    ]
    # print(catalogue)

    sample = []
    recent = calc_recent_trend(catalogue)
    week = calc_seven_trend(catalogue)
    for item in catalogue:
        info = get_catalogue(item)['item']
        sample.append(
            [
                next(week),
                info['day30']['trend'],
                info['day90']['trend'],
                info['day180']['trend'],
                is_expensive(info['current']['price']),
                next(recent)
            ]
        )
        # print(info['name'])
    # print(sample)
    # print(calc_recent_trend(id)[-1])

    labels = []
    for s in sample:
        labels.append(s.pop())
    print(sample)
    print(labels)
    decisionTree = DecisionTree(sample, attributes, labels)
    print("System entropy {}".format(decisionTree.entropy))
    decisionTree.id3()
    decisionTree.printTree()


if __name__ == "__main__":
    # test()
    predict()