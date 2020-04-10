import tensorflow as tf
tf.enable_eager_execution()

# data
x_data = [1,2,3,4,5]
y_data = [1,2,3,4,5]

# W, b initialize
W = tf.Variable(2.9)
b = tf.Variable(0.5)

# Learning_rate initialize
learning_rate = 0.01

# 1. Gradient descent 기본 구조
with tf.GradientTape() as tape: #with 구문안에 있는 변수들의 정보들을 tape에 기록해 놓는다.
    hypothesis = W * x_data + b
    cost = tf.reduce_mean(tf.square(hypothesis - y_data))

W_grad, b_grad = tape.gradient(cost, [W, b]) # 개별 미분값(기울기값)을 구해서 튜플로 반환한다.

W.assign_sub(learning_rate * W_grad) # 기울기를 얼만큼 반영할 것인가를 러닝rate를 곱해서 표현
b.assign_sub(learning_rate * W_grad)
##########################################

# 2. 실제 구현 코드
##########################################
W = tf.Variable(2.9)
b = tf.Variable(0.5)

for i in range(100):
    with tf.GradientTape() as tape:# W, b 변수를 여러번 업데이트 시키는 과정
        hypothesis = W * x_data + b
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))

    W_grad, b_grad = tape.gradient(cost, [W, b])

    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * W_grad)
    if i % 10 == 0:
        print("{:5}|{:10.5}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))



# Predict(예측모델 만들어보기)
x_data = [1,2,3,4,5]
y_data = [1,2,3,4,5]
