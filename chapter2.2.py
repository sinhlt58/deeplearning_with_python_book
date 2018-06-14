import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# x = np.array([[[1,2,3],[1,2,3],[1,2,3]], [[1,2,3],[1,2,3],[1,2,3]]])
#
# print (train_images.ndim)
#
# print (train_images[1].shape)
# digit = train_images[3][0:20, 0:20]
# #
# plt.imshow(digit, cmap=plt.cm.binary)
# plt.show()

my_slice = train_images[10:11, 0:20, 0:20]
print (my_slice.shape)