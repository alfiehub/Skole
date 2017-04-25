import tensorflow as tf
import numpy as np
import csv

w = tf.Variable(tf.zeros([2,1]), tf.float32)

x = tf.placeholder(tf.float32, [None,2])
y = tf.placeholder(tf.float32, [None,1])

# model
model = tf.sigmoid(tf.transpose(w)*x)
print(model)

# loss
loss = tf.square(model - y)/2

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)

# trainer
train = optimizer.minimize(loss)

# training data
x_train, y_train = [], []
with open('data/data_small_nonsep_train.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        x_train.append([float(row[0]), float(row[1])])
        y_train.append([float(row[2])])
#print(x_train)

#x_test, y_test= [], []
#with open('data/data_big_nonsep_test.csv') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter='\t')
#    for row in spamreader:
#        x_test.append([float(row[0]), float(row[1])])
#        y_test.append(float(row[2]))

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train, {x:x_train, y: y_train})

curr_W, curr_loss  = sess.run([w, loss], {x:x_train, y:y_train})
print("W: %s loss: %s"%(curr_W, curr_loss))
