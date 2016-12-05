#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:19:43 2016

@author: sandeepkatypally
"""

from tableReader import Table
from sklearn.cluster import MiniBatchKMeans
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics.pairwise import pairwise_distances_argmin
import warnings
from sk import rdivDemo
import time
import random
import math
warnings.filterwarnings("ignore")


list1=list2=[]
a12Score = olda12Score = 0
datasets = ['iris.csv']

def recall(p_labels, actuals, label):
	tp =0
	tn=0
	fn=0
	fp = 0
	for i,p in enumerate(p_labels):
		a = actuals[i]
		if( a == label):
			if(a == p):
				tp +=1
			else:
				fn +=1
		else:
			if(a ==p):
				tn +=1
			else:
				fp +=1
	return float(tp)/(fn + tp + 1)


def naiveBayes(trainData, testData):
    dtrain, ltrain = [x[:-1] for x in trainData ], [x[-1] for x in trainData]
    dtest = [x[:-1] for x in testData ]
    NB = GaussianNB()
    NB.fit(dtrain,ltrain)
    p_labels = NB.predict(dtest)
    return p_labels

def a12(list_1, list_2):
    more = same = 0.0
    for x in sorted(list_1):
        for y in sorted(list_2):
            if x == y:
                same += 1
            elif x > y:
                more += 1
    return (more + 0.5*same) / (len(list_1)*len(list_2))

def eraPrint(p_labels, test):
    global list1, list2, a12Score, olda12Score
    t_label = [x[-1] for x in test]
    recall_class_one = recall(p_labels,t_label,'setosa')
    recall_class_two = recall(p_labels,t_label,'versicolor')
    recall_class_three = recall(p_labels,t_label,'virginica')

    print "Recall  of Class 1 is " + "%.2f"%(recall_class_one)
    print "Recall of Class 2 is " + "%.2f"%(recall_class_two)
    try: 
        print "Recall of Class 3 is " + ".2f"%(recall_class_three)
    except:
        print "Recall of Class 3 is " + str(recall_class_three)
    flag=0
    if len(list1)==0:
        list1 = [recall_class_one, recall_class_two, recall_class_three]
        list2 = list1
        flag = 1
    else:
        list1 = list2
        list2 = [recall_class_one, recall_class_two, recall_class_three]

    olda12Score = a12Score
    a12Score = a12(list1, list2)

    if flag==0:
        print "A12 Score is " + str(a12Score)
    if math.fabs(olda12Score - a12Score) > 0.2 * olda12Score:
        print "Detected Anamoly!!"
    print ""


for dataset in datasets:
	table = Table(dataset)
	table.addRow()
	count=0
	data_list=[]

	for i,x in enumerate (table.rows):
		if i < 100:
			data_list.append(x)
		else:
			break
	data_list = data_list * 10

	class_a = table.rows[0:50]
	class_b = table.rows[50:100]
	class_c = table.rows[100:150]

	for i in range (10):
		data_list += class_a[0:10] + class_b[0:30] + class_c[0:50] + class_c[0:10]
		random.shuffle(class_a)
	

	print '##########--Era 1---###########'
	test_list = train_list = data_list[0 : 100]
	eraPrint (naiveBayes(train_list, test_list), test_list)

	for i in xrange(1, 20):
		print '##########---Era ' + str(i+1) + '---###########'
		train_list = data_list[0 : i * 100]
		test_list = data_list[i * 100 : (i+1) * 100]
		eraPrint (naiveBayes(train_list, test_list), test_list)

