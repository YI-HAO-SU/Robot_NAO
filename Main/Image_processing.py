# Image recognition
from PIL import Image
from PIL import ImageFilter
import time
import numpy as np

# set time.1
t1 = time.time()

# Load picture
# In NAO we can set the path
im = Image.open('e.png')

# Blur
img_c = im.filter(ImageFilter.SHARPEN)
img_e = img_c.filter(ImageFilter.BLUR)

# MedianFilter
img_1 = img_c.filter(ImageFilter.MedianFilter(5))

# Gray
img_a = img_1.convert('L')

# Threshold Setting
threshold = 100
img_b = img_a.point(lambda p: p > threshold and 255)

# Resize to reduce the loading
resized_image = img_b.resize((100, 100), Image.ANTIALIAS)

# set time.2
t2 = time.time()

# from image to array
pic_nums = np.array(resized_image)
pic_nums[pic_nums > 0] = 1
print(pic_nums)
print(pic_nums.shape)

# setting final_array parameter
sum_k = 0
x_k = 0
final_array_sum = [[0]*5 for a in range(5)]
final_array = [[0]*5 for a in range(5)]

# set time.3
t3 = time.time()

# load in every pixel
for l in range(1, 6):
    for k in range(1, 6):
        for j in range(20*(l-1)+1, 20*l):
            for i in range(20*(k-1)+1, 20*k):
                # accumulate
                if pic_nums[j][i] == 0:
                    sum_k = sum_k + 1

        # if safe the condition
        if (sum_k >= 10 and sum_k <= 30):
            x_k = 1
        final_array_sum[l-1][k-1] = sum_k
        final_array[l-1][k-1] = x_k
        # initialize parameter
        sum_k = 0
        x_k = 0

# set time.4
t4 = time.time()

# output the final result then put it to action stage
print(final_array)

# every work stage time calculate
'''
print("Runtime t2-t1 : %f s" % (t2 - t1))
print("Runtime t3-t1 : %f s" % (t3 - t1))
print("Runtime t4-t1 : %f s" % (t4 - t1))
'''
# show the image after processing
resized_image.show()
