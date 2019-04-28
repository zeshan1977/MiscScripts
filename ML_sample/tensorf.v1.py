import tensorflow as tf
"""
node1=tf.constant(3.0)
node2=tf.constant(4.0)

node3 = (node1*node2) +node1 - node2

#session places the obejcets on the graphw
"""

#Model parameters
m=tf.Variable([.3],tf.float32)
x=tf.Variable([.5],tf.float32)

c=tf.placeholder(tf.float32)

y=(m*x)+c # value that we will feed in
linear_model_output=tf.placeholder(tf.float32) #output we will get thru the model

squaredelta=tf.square(y-linear_model_output)
loss=tf.reduce_sum(squaredelta)

init=tf.global_variables_initializer()

#lauch the graph
sess=tf.Session()

#print sess.run([node1,node2])
sess.run(init)

print sess.run(loss,{x:[1,2,3,4],linear_model_output:[0,-1,-2,-4]})

FileWriter  = tf.summary.FileWriter('graph',sess.graph)

sess.close()


"""
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)

adder_node= a+b

sess.close()
"""


