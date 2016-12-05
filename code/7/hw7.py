#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:12:58 2016

@author: sandeepkatypally
"""
from tableReader import Table
from sklearn.naive_bayes import GaussianNB
import warnings
from sk import rdivDemo
import time
from random import shuffle
warnings.filterwarnings("ignore")

def train_test(data, folds=5, index=0):
    l = len(data)
    test = []
    train = []
    
    for i in range(0, folds):
        if i == index:
            test = [data[x] for x in range(int(i * l / folds),int((i + 1) * l / folds))]
        else:
            for x in range(int(i * l / folds),int((i + 1) * l / folds)):
            	train.append(data[x])
    train_label = [x[-1] for x in train]
    test_label = [x[-1] for x in test]

    return train,test, train_label, test_label

def recall(predicted_labels, actuals, label):
    tp =0
    tn=0
    fn=0
    fp = 0
    for i,p in enumerate(predicted_labels):
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
    return float(tp)/(fn + tp+1)

def falseAlarm(predicted_labels, actuals, label):
    tp =0
    tn=0
    fn=0
    fp = 0
    for i,p in enumerate(predicted_labels):
        a = actuals[i]
        if( a  == label):
            if(a == p):
                tp +=1
            else:
                fn +=1
        else:
            if(a ==p):
                tn +=1
            else:
                fp +=1
    return float(fp)/(tn + fp +1)

def naiveBayes(train, test, train_label, test_label):
    dtrain = [x[:-1] for x in train ]
    dtest = [x[:-1] for x in test ]
    NB = GaussianNB()
    NB.fit(dtrain,train_label)
    predicted_labels = NB.predict(dtest)
    return predicted_labels

datasets = ['ant-1.7.csv', 'arc.csv','tomcat.csv', 'xalan-2.7.csv']
class_variable = ['Iris-setosa', 1, 0, 0, 0]
for dataset,cv in zip(datasets,class_variable):
    table = Table(dataset)

    table.addRow()
    recall_for_diff_algos={}
    recall_for_diff_algos['nb'] =['nb']
    recall_for_diff_algos['width'] =['width']
    recall_for_diff_algos['freq'] =['freq']
    fAlarm_for_diff_algos={}
    fAlarm_for_diff_algos['nb'] =['nb']
    fAlarm_for_diff_algos['width'] =['width']
    fAlarm_for_diff_algos['freq'] =['freq']

    nb_time = 0;
    width_time = 0;
    freq_time = 0;

    data_width = []
    data_freq = []
	
    data_freq = sorted(table.rows, key = lambda iris: iris[0])
    min_length = data_freq[0][0]
    max_length = data_freq[-1][0]
    data_freq = sorted(table.rows, key = lambda iris: iris[1])
    min_width = data_freq[0][1]
    max_width = data_freq[-1][1]
	
    for index in range(0,25):	
        if(index%5 ==0):
            shuffle(table.rows)
        train,test,train_label, test_label = train_test(table.rows,5, index%5)
        start_time = time.time()
        predicted_labels = naiveBayes(train,test, train_label, test_label)
        nb_time += (time.time() - start_time)
        recall_for_diff_algos['nb'].append(recall(predicted_labels,test_label, cv))
        fAlarm_for_diff_algos['nb'].append(falseAlarm(predicted_labels,test_label, cv))
		
        data_freq = sorted(table.rows, key = lambda iris: iris[0])
        for i,rec in enumerate(data_freq):
            if (i < 50):
                rec[0] = 0 
            elif(i<100):
                rec[0] = 1
            else:
                rec[0] = 2

        data_freq = sorted(table.rows, key = lambda iris: iris[1])
        for i,rec in enumerate(data_freq):
            if (i < 50):
                rec[1] = 0
            elif(i < 100):
                rec[1] = 1
            else:
               rec[1] = 2

        train,test,train_label, test_label = train_test(data_freq,5, index%5)

        start_time = time.time()
        predicted_labels = naiveBayes(train,test, train_label, test_label)
        freq_time += (time.time() - start_time)
        recall_for_diff_algos['freq'].append(recall(predicted_labels,test_label, cv))
        fAlarm_for_diff_algos['freq'].append(falseAlarm(predicted_labels,test_label, cv))
		
        data_width = table.rows
        for rec in data_width:
            if (rec[0] >= min_length and rec[0] < min_length + (max_length-min_length)/3):
                rec[0] = 0 
            elif(rec[0] >= min_length + (max_length-min_length)/3 and rec[0] < min_length + ((max_length-min_length)*2)/3):
                rec[0] = 1
            else:
                rec[0] = 2

            if (rec[1] >= min_width and rec[1] < min_width + (max_width-min_width)/3):
                rec[1] = 0 
            elif(rec[1] >= min_width + (max_width-min_width)/3 and rec[1] < min_width + ((max_width-min_width)*2)/3):
                rec[1] = 1
            else:
                rec[1] = 2

        train,test,train_label, test_label = train_test(data_width,5, index%5)

        start_time = time.time()
        predicted_labels = naiveBayes(train,test, train_label, test_label)
        width_time += (time.time() - start_time)
        recall_for_diff_algos['width'].append(recall(predicted_labels,test_label, cv))
        fAlarm_for_diff_algos['width'].append(falseAlarm(predicted_labels,test_label, cv))
			

    print dataset,"****************************************"
    print  ""
    print "recall for ", dataset,"is",
    print (rdivDemo(recall_for_diff_algos.values()))
    print "false alarm for ", dataset," is",
    print (rdivDemo(fAlarm_for_diff_algos.values()))
    print " Runtime :"
    print "nb is ", nb_time/5, " sec";
    print "frequency is ", freq_time/5, " sec";
    print "width is ", width_time/5, " sec";
    print  ""
