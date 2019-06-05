import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

# 下载训练数据
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# 占位符：表示任意的MNIST图像
x = tf.placeholder(tf.float32, [None, 784], name='x')
# 权重值
W = tf.Variable(tf.zeros([784, 10]), name='wights')
# 偏置量
b = tf.Variable(tf.zeros([10]), name='biases')
# softmax回归计算概率分布
y = tf.nn.softmax(tf.matmul(x, W) + b, name='y')
# 占位符：实际分布
y_ = tf.placeholder("float", [None, 10], name="y_")
# 计算交叉熵
cross_entropy = -tf.reduce_sum(y_ * tf.log(y), name='entropy')
# TensorFlow用梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy, name='descent')
# 检测我们的预测是否真实标签匹配(索引位置一样表示匹配)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1), name='correct')
# 布尔值转换成浮点数，然后取平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"), name='accuracy')
# 初始化变量
init = tf.initialize_all_variables()
# 启动session
with tf.Session() as sess:
    # 运行变量初始化
    sess.run(init)
    # 训练数据
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    # 运算正确率
    correct_rate = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
    with tf.summary.FileWriter("MNIST_1_board", sess.graph) as summary_writer:
        print(correct_rate)
