from PIL import Image
from PIL import ImageFilter
import time
import numpy as np
import threading
import multiprocessing

# set time.1
t1 = time.time()

# Load
im = Image.open('camImage1.png')

# MedianFilter
img_1 = im.filter(ImageFilter.MedianFilter(5))

# Gray
img_a = img_1.convert('L')

# Threshold
threshold = 10
img_b = img_a.point(lambda p: p > threshold and 255)

# set time.2
t2 = time.time()

# from image to array
pic_nums = np.array(img_b)
pic_nums[pic_nums > 0] = 1
'''print(pic_nums)'''
'''print(pic_nums.shape)'''

final_array_sum = [[0]*5 for a in range(5)]
final_array = [[0]*5 for a in range(5)]

# set time.3
t3 = time.time()
#
# origin version
def Origin(l):
    sum_k = 0
    x_k = 0
    for k in range(1, 6):
        for j in range(96*(l-1)+1, 96*l):
            for i in range(128*(k-1)+1, 128*k):
                if pic_nums[j][i] == 0:
                    sum_k = sum_k + 1

        if (sum_k >= 500 and sum_k <= 2500):
            x_k = 1
        final_array_sum[l-1][k-1] = sum_k
        final_array[l-1][k-1] = x_k
        sum_k = 0
        x_k = 0
    '''
    print('Origin output:')
    print('Origin took {} seconds'.format(time.time() - starttime))
    print('Final array is:',final_array)
    '''
# Running for Origin
def runBaseLine():
    starttime = time.time()
    for i in range(0, 5):
        Origin(i)
    print('BaseLine output:')
    print('Baseline took {} seconds'.format(time.time() - starttime))
    print('Final array is:', final_array)

# Run for Multithread
def runMultithread():
    threads = list()
    starttime = time.time()
    for element in range(0, 5):
        threads.append(threading.Thread(target=Origin, args=(element,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('Multithread output:')
    print('Multithread took {} seconds'.format(time.time() - starttime))
    print('Final array is:', final_array)

# Runing for Multiprocessing
def runMultiprocessing():
    starttime = time.time()
    processes = list()
    for i in range(0, 5):
        p = multiprocessing.Process(target=Origin, args=(i,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
    print('Multiprocessing output:')
    print('Multiprocessing took {} seconds'.format(time.time() - starttime))
    print('Final array is:', final_array)

# set time.4
t4 = time.time()

if __name__ == '__main__':
    runBaseLine()
    runMultithread()
    runMultiprocessing()
    '''
    print(final_array)
    print("Runtime t4-t1 : %f s" % (t4 - t1))
    img_b.show()
    '''
