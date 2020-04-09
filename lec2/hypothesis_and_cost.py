import tensorflow as tf

x_data = [1,2,3,4,5]
y_data = [1,2,3,4,5]

W = tf.Variable(2.9)
b = tf.Variable(0.5)

# hypothesis 구하는 코드
hypothesis = W * x_data + b
print(hypothesis)

# cost 구하는 코드
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

