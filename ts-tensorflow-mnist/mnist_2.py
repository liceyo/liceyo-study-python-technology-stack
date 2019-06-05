import os
import time

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 获取cpu数量
cpu_num = int(os.environ.get('CPU_NUM', 2))
# 配置使用cpu（设置这里的线程数，效率明显变化）
# 注：四核八线程的机器，线程数都设置为4效率还要好点，但是没有经过大样本测试
config = tf.ConfigProto(device_count={"CPU": cpu_num},
                        inter_op_parallelism_threads=4,  # 控制运算符op内部的并行
                        intra_op_parallelism_threads=4,  # 控制多个运算符op之间的并行计算
                        log_device_placement=False)
# 配置是否训练
config_is_train = False
# 配置保存路径
config_save_path = 'MNIST_save/mnist.ckpt'
# 配置保存读取目录
config_save_read_path = 'MNIST_save/'
# 配置训练保存的次数
config_global_step = 4
# 配置可视化日志路径
config_board_path = 'MNIST_board/'
# 本次训练迭代次数
config_train_num = 500


# 初始化权重
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# 初始化偏置量
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 卷积
def conv2d(x, w):
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


# 池化
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


with tf.name_scope('definition'):
    # 占位符：表示任意的MNIST图像
    x = tf.placeholder(tf.float32, [None, 784])
    # 占位符：实际分布
    y_ = tf.placeholder("float", [None, 10])
## 第一层卷积网络
with tf.name_scope('first_conv'):
    # 卷积的权重张量：前两个维度是patch的大小，接着是输入的通道数目，最后是输出的通道数目
    W_conv1 = weight_variable([5, 5, 1, 32])
    # 偏置量
    b_conv1 = bias_variable([32])
    # 把x变成一个4d向量，其第2、第3维对应图片的宽、高，最后一维代表图片的颜色通道数
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    # x_image和权值向量进行卷积
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    # max pooling
    h_pool1 = max_pool_2x2(h_conv1)
## 第二层卷积网络
with tf.name_scope('second_conv'):
    # 权重张量
    W_conv2 = weight_variable([5, 5, 32, 64])
    # 偏置量
    b_conv2 = bias_variable([64])
    # 卷积
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    # 池
    h_pool2 = max_pool_2x2(h_conv2)
## 密集连接层
with tf.name_scope('compressed'):
    # 权重张量
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    # 偏置量
    b_fc1 = bias_variable([1024])
    # reshape
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    # 卷积
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
## 过拟合
with tf.name_scope('over_fitting'):
    # 代表一个神经元的输出在dropout中保持不变的概率
    keep_prob = tf.placeholder("float")
    # 屏蔽神经元的输出外，自动处理神经元输出值的scale
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
## 输出层
with tf.name_scope('output'):
    # 权重张量
    W_fc2 = weight_variable([1024, 10])
    # 偏置量
    b_fc2 = bias_variable([10])
    # softmax回归计算概率分布
    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
    # 计算交叉熵
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
    # ADAM优化器来做梯度最速下降
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
## 预测
with tf.name_scope('check'):
    # 检测我们的预测是否真实标签匹配
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    # 布尔值转换成浮点数，然后取平均值
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
## 保存
with tf.name_scope('save'):
    # 保存训练数据(max_to_keep:只保留最后一次训练数据)
    saver = tf.train.Saver(max_to_keep=1)


def train_mnist():
    ## 启动session
    with tf.Session(config=config) as sess:
        # 下载训练数据
        mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
        # 运行变量初始化
        sess.run(tf.initialize_all_variables())
        try:
            # 恢复模型数据(自动获取最后一次保存的模型)
            restore_path = tf.train.latest_checkpoint(config_save_read_path)
            saver.restore(sess, restore_path)
            print('恢复模型数据成功')
        except Exception as e:
            print('恢复模型数据失败')
        if config_is_train:
            # 开始训练数据（目前电脑不支持GPU跑Tensorflow）
            start_time = int(round(time.time() * 1000))
            for i in range(config_train_num):
                # 获取训练数据
                batch_xs, batch_ys = mnist.train.next_batch(50)
                # 每100次迭代输出一次日志
                if i > 0 and i % 100 == 0:
                    end_time = int(round(time.time() * 1000))
                    interval, start_time = end_time - start_time, end_time
                    # 打印日志
                    train_accuracy = accuracy.eval(feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1.0})
                    print("step %d,interval %dms, training accuracy %g" % (i, interval, train_accuracy))
                # 运行训练模型
                train_step.run(feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 0.5})
            # 保存模型数据
            saver.save(sess, config_save_path, global_step=config_global_step)
        # 可视化记录日志
        with tf.summary.FileWriter(config_board_path, sess.graph) as summary_writer:
            # 评估模型
            test_accuracy = accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})
            print("test accuracy %g" % test_accuracy)


def mnist(image_arr: list):
    labels = [[1. if i == j else 0. for j in range(10)] for i in range(10)]
    with tf.Session() as sess:
        # 运行变量初始化
        sess.run(tf.initialize_all_variables())
        try:
            # 恢复模型数据(自动获取最后一次保存的模型)
            restore_path = tf.train.latest_checkpoint(config_save_read_path)
            saver.restore(sess, restore_path)
            print('恢复模型数据成功')
        except Exception as e:
            print('恢复模型数据失败')
        result = correct_prediction.eval(feed_dict={x: [image_arr] * 10, y_: labels, keep_prob: 1.0})
        return [i for i in range(10) if result[i] == 1.][0]
