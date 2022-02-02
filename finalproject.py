import sys
import warnings
from numpy import mean
from numpy import std
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from matplotlib import pyplot
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
if not sys.warnoptions:
    warnings.simplefilter('ignore')
df = pd.read_excel(r'E:\samvedna\class 12\weight.xlsx', sheet_name='USD_INR')   #reading the excel file
d1=df.ix[:, 0]    
data1 = d1.values       #obtaining x-axis values
d2=df.ix[:, 1]
data2 = d2.values       #obtaining y-axis values
print('data1: mean=',mean(data1),'stdv=',std(data1))    #obtaining mean and standard deviation data for pearsons correlation
print('data2: mean=',mean(data2),' stdv=',std(data2))
#plot
plt.suptitle('Correlation b/w dollar and rupees', fontsize=12)
plt.title('High Positive correlation',fontsize=10)
plt.xlabel("Year")                #defining the labels
plt.ylabel("Rupees per dollar")     
pyplot.scatter(data1, data2)      #subsituting values in terms of x and y axis for plotting scatter plot
plt.scatter(d1,d2,color='teal')
corr,_= pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)      #to summarize the strength of linear relationship between two variables
print('It shows positive correlation')
pyplot.show()
print()
##################################################################################
df = pd.read_excel(r'E:\samvedna\class 12\weight.xlsx', sheet_name='speed&time')
d1=df.ix[:, 0]
data1 = d1.values
d2=df.ix[:, 1]
data2 = d2.values
print('data1: mean=',mean(data1),'stdv=',std(data1))
print('data2: mean=',mean(data2),' stdv=',std(data2))
# plot
plt.suptitle('Scatter graph to show correlation b/w speed and time', fontsize=12)
plt.title("High Negative Correlation",fontsize=10)
plt.xlabel("Time for reaching 400km in distance")
plt.ylabel("Speed")
pyplot.scatter(data1, data2)
plt.scatter(d1,d2,color='darkorchid')
corr, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)
print('It shows negative correlation')
pyplot.show()
print()
###################################################################################
df = pd.read_excel(r'E:\samvedna\class 12\weight.xlsx', sheet_name='iit selections')
d1=df.ix[:, 0]
data1 = d1.values
d2=df.ix[:, 1]
data2 = d2.values
print('data1: mean=',mean(data1),'stdv=',std(data1))
print('data2: mean=',mean(data2),' stdv=',std(data2))
# plot
plt.suptitle('Scatter graph to show correlation b/w # of selections over a period of time', fontsize=12)
plt.title("Weak Positive Correlation",fontsize=10)
plt.xlabel("# of students")
plt.ylabel("# of selection")
pyplot.scatter(data1, data2)
plt.scatter(d1,d2,color='firebrick')
corr, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)
print('It shows poor correlation')
pyplot.show()
