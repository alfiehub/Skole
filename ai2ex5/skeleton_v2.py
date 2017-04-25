import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
from math import e
import csv
from time import time

def logistic_z(z): 
    return 1.0/(1.0+np.exp(-z))

def logistic_wx(w,x): 
    return logistic_z(np.inner(w,x))

def std_logistic(w, x):
    return logistic_z(np.inner(w,x))
    #return 1.0/(1.0+e**(-np.inner(w, x)))

def std_logistic_diff(w, x, var='w1'):
    if var == 'w1':
        return (x[0]*e**(-np.inner(w,x)))/(1.0+e**(-np.inner(w,x)))**2
    elif var == 'w2':
        return (x[1]*e**(-np.inner(w,x)))/(1.0+e**(-np.inner(w,x)))**2
    elif var == 'w3':
        return (x[2]*e**(-np.inner(w,x)))/(1.0+e**(-np.inner(w,x)))**2

def euclidean_distance(w, x_n, y_n):
    return ((std_logistic(w, x_n)-y_n)**2)/2

def euclidean_distance_diff(w, x_n, y_n, var='w1'):
    return (std_logistic(w, x_n)-y_n)*std_logistic_diff(w, x_n, var=var)


def classify(w,x):
    x=np.hstack(([1],x))
    return 0.0 if (std_logistic(w,x) < 0.5) else 1.0

#x_train = [number_of_samples,number_of_features] = number_of_samples x \in R^number_of_features
def stochast_train_w(x_train,y_train,learn_rate=0.1,niter=1000):
    x_train=np.hstack((np.array([1]*x_train.shape[0]).reshape(x_train.shape[0],1),x_train))
    dim=x_train.shape[1]
    num_n=x_train.shape[0]
    w = np.random.rand(dim)
    index_lst=[]
    for it in range(niter):
        if(len(index_lst)==0):
            index_lst=random.sample(range(num_n), k=num_n)
        xy_index = index_lst.pop()
        x=x_train[xy_index,:]
        y=y_train[xy_index]
        for i in range(dim):
            update_grad = euclidean_distance_diff(w, x, y, var=('w%d' % (i+1)))  ### something needs to be done here
            w[i] = w[i] - learn_rate*update_grad ### something needs to be done here
    return w

def batch_train_w(x_train,y_train,learn_rate=0.1,niter=1000):
    x_train=np.hstack((np.array([1]*x_train.shape[0]).reshape(x_train.shape[0],1),x_train))
    dim=x_train.shape[1]
    num_n=x_train.shape[0]
    w = np.random.rand(dim)
    index_lst=[]
    for it in range(niter):
        for i in range(dim):
            update_grad=0.0
            for n in range(num_n):
                update_grad += euclidean_distance_diff(w, x_train[n], y_train[n], var='w%d' % (i+1)) # something needs to be done here
            w[i] -= learn_rate*update_grad/num_n
    return w

def train_and_plot(xtrain,ytrain,xtest,ytest,training_method,learn_rate=0.1,niter=10):
    plt.figure()
    start = time()
    #train data
    data = pd.DataFrame(np.hstack((xtrain,ytrain.reshape(xtrain.shape[0],1))),columns=['x','y','lab'])
    ax=data.plot(kind='scatter',x='x',y='y',c='lab',cmap=cm.copper,edgecolors='black')

    #train weights
    w=training_method(xtrain,ytrain,learn_rate,niter)
    training_time = time() - start
    error=[]
    y_est=[]
    for i in range(len(ytest)):
        error.append(np.abs(classify(w,xtest[i])-ytest[i]))
        y_est.append(classify(w,xtest[i]))
    y_est=np.array(y_est)
    data_test = pd.DataFrame(np.hstack((xtest,y_est.reshape(xtest.shape[0],1))),columns=['x','y','lab'])
    data_test.plot(kind='scatter',x='x',y='y',c='lab',ax=ax,cmap=cm.coolwarm,edgecolors='black')
    plt.show()
    print("error=",np.mean(error))
    print("%rs" % training_time, error.count(1.0), len(error))
    return w, training_time, error.count(1.0), len(error)


x_train, y_train = [], []
with open('data/data_big_nonsep_train.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        x_train.append(np.array([float(row[0]), float(row[1])]))
        y_train.append(float(row[2]))

x_test, y_test= [], []
with open('data/data_big_nonsep_test.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        x_test.append(np.array([float(row[0]), float(row[1])]))
        y_test.append(float(row[2]))

train_and_plot(np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test), stochast_train_w, learn_rate=0.1, niter=1000)
#train_and_plot(np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test), batch_train_w, learn_rate=0.1, niter=1000)
Ts = [10, 20, 50, 100, 200, 500, 1000, 2000]
training_times = []
error_counts = []
for T in Ts:
    w, training_time, error_count, total = train_and_plot(np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test), stochast_train_w, learn_rate=0.1, niter=T)
    training_times.append(training_time)
    error_counts.append(error_count)


