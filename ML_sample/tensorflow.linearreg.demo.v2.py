import tensorflow as tf
"""
node1=tf.constant(3.0)
node2=tf.constant(4.0)

node3 = (node1*node2) +node1 - node2

#session places the obejcets on the graphw
"""

#Model parameters
#w=tf.Variable([3],tf.float32)
#b=tf.Variable([5],tf.float32)

w=tf.Variable([-1.0],tf.float32) # By changing the above functions values to -1 and 1 we will have zero loss
b=tf.Variable([1.0],tf.float32)

x=tf.placeholder(tf.float32)

linear_model=(w*x)+b # value that we will feed in
y=tf.placeholder(tf.float32) #output we will get thru the model, the correct output 


squaredelta=tf.square(linear_model-y)
loss=tf.reduce_sum(squaredelta)

learning_rate_steps=0.1
optimzer=tf.train.GradientDescentOptimizer(learning_rate_steps)
train = optimzer.minimize(loss)
init=tf.global_variables_initializer()
#optimizer



#lauch the graph
sess=tf.Session()
sess.run(init)

for i in range(10000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})

print sess.run([w,b])

#print sess.run([node1,node2])

FileWriter  = tf.summary.FileWriter('graph',sess.graph)
# print sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]})
sess.close()


"""
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)

adder_node= a+b

sess.close()
"""


