# Aim: classify sentiment of text only.
# No price data.
# +1 positive, 0 neutral, -1 negative

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import jieba
import json
import numpy as np

import tensorflow as tf
from tensorflow.contrib import learn

# get base vector
bvfile = open(sys.argv[1],'r')
for l in bvfile:
    bv = json.loads(l)
bvfile.close()
bvlen = len(bv)

# get text vectors
vec = []
vecfile = open(sys.argv[2],'r')
for l in vecfile:
    if l[0:10] >= '2016-01-04':
        vec.append([l[0:10],json.loads(l[15:-1])])
vecfile.close()
N = len(vec)

# get sentiment labels (computational method)
senfile = open(sys.argv[3],'r')
sen = []
for l in senfile:
    l = l.replace('\n','')
    line = l.split(',')
    day = line[0]
    pos = int(line[1])
    neg = int(line[2])
    if (pos>0 or neg <=50):
        label = [1,0,0]
    elif (neg <= 100):
        label = [0,1,0]
    else:
        label = [0,0,1]
    newline = [day,label]
    sen.append(newline)
senfile.close()
##print(N == len(sen)) # True, hence N = len(sen) = len(vec)

# :::RNN:::

# load data
xs = np.array([vec[i][1] for i in range(0,N)])
ys = np.array([sen[i][1] for i in range(0,N)])

# Parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

# Network Parameters
n_hidden_1 = 5 # 1st layer number of features
n_hidden_2 = 5 # 2nd layer number of features
n_input = bvlen # MNIST data input (img shape: 28*28)
n_classes = 3 # MNIST total classes (0-9 digits)

x = tf.placeholder(tf.float32, [N,bvlen])
y = tf.placeholder(tf.float32, [N,n_classes])

# <variables

# <cost <-- find the softmax error function

# <model

# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
pred = multilayer_perceptron(x, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)




init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = N
        # Loop over all batches
        for i in range(total_batch):
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={x: xs,
                                                          y: ys})
            # Compute average loss
            avg_cost += c / total_batch
            print(i,'/',N)
        # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", \
                "{:.9f}".format(avg_cost))
    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy:", accuracy.eval({x: xs, y: ys}))
