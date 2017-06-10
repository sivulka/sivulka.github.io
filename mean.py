# Write a simple function to compute the mean and standard # deviation of data set
import math
####################
# mean ####################
def mean(data):
# assign the length of the data set
L = len(data)
# initialise the mean value

m=0
for i in range(0,L): m = m + data[i]
m=m/L
# a short way is: m /= L
# return the result for later use
return m
########################
# standard deviation ########################
def std_dev(data):
L = len(data) m = mean(data)
# initialise error from mean of each # data point
err = 0
for i in range(0,L):
err = err + (data[i] - m)**2 err = math.sqrt(err / (L - 1))
return err
data = [2.2 ,2.4 ,2.5 ,2.6 ,2.8] mean_val = mean(data)
std_dev_val = std_dev(data)
print 'the mean value is', mean_val
print 'the standard deviation is', std_dev_val