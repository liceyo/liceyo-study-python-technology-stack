import os

import numpy as np
import scipy as scipy
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data

import mnist_2 as mn

def load_mnist_to_image():
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    # 我们把原始图片保存在MNIST_data/raw/文件夹下
    # 如果没有这个文件夹会自动创建
    save_dir = 'MNIST_image/'
    if os.path.exists(save_dir) is False:
        os.makedirs(save_dir)
    # 保存前20张图片
    for i in range(20):
        # 请注意，mnist.train.images[i, :]就表示第i张图片（序号从0开始）
        image_array = mnist.train.images[i, :]
        # TensorFlow中的MNIST图片是一个784维的向量，我们重新把它还原为28x28维的图像。
        image_array = image_array.reshape(28, 28)
        # 保存文件的格式为 mnist_train_0.jpg, mnist_train_1.jpg, ... ,mnist_train_19.jpg
        filename = save_dir + 'mnist_train_%d.jpg' % i
        # 将image_array保存为图片
        # 先用scipy.misc.toimage转换为图像，再调用save直接保存。
        scipy.misc.toimage(image_array, cmin=0.0, cmax=1.0).save(filename)
    print('Please check: %s ' % save_dir)


def image_to_array(image_path: str):
    im = Image.open(image_path)
    im.show()
    im = im.convert("L")
    data = im.getdata()
    arr = np.array(data) /255.
    return arr


image_arr = image_to_array("MNIST_image/mnist_train_17.jpg")
print(mn.mnist(image_arr))
