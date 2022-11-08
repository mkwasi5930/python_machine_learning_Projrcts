from numpy import loadtxt
from urllib.request import urlopen
url='https://goo.gl/vhm1eU'
raw_data = urlopen(url)
dataset = loadtxt(raw_data,delimeter=",")
print(dataset.shape)