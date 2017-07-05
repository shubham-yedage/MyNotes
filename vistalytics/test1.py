# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
#
#
# def func(x, a, b, c):
#     return a * np.exp(-b * x) + c
#
# xdata = np.linspace(0, 4, 50)
# print(xdata)
# y = func(xdata, 2.5, 1.3, 0.5)
# print(y)
# y_noise = 0.2 * np.random.normal(size=xdata.size)
# print(y_noise)
# ydata = y + y_noise
# print(ydata)
# plt.plot(xdata, ydata, 'b-', label='data')
#
#
# popt, pcov = curve_fit(func, xdata, ydata)
# plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')
#
#
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 2., 1.]))
# plt.plot(xdata, func(xdata, *popt), 'g--', label='fit-with-bounds')
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()





from treelib import Tree
import sys
import numpy as np
from main.utils.math_utils import average_change
import matplotlib.pyplot as plt
# import main.common.constant as con
# from pandas import Series

#
# v = [1392, 1711, 3002, 4797]
# print(str(np.std(v)) + "  " + str(np.mean(v)))
# print(con.KEY)
# v = {}
# v1 = 'hello'
# v2 = 'h'
# v= {con.KEY : v1}
# print(v.get(con.KEY))
# v = [38.00,	39.83,	42.36,	40.92,	41.67]
# print(str(average_change(v)))

# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')
# plt.title('About as simple as it gets, folks')
# plt.grid(True)
# plt.savefig("test.png")
# plt.show()

# v1 = [24578,37491,42905,65225,108249,156508,170910,182795,233715,215639]

# v1 = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190]
# print(v1)
######################################################
# v1 = [1,7,8,10,15,6,5,9,12,15]
# # v1 = [2,4,6,8,10,12,14,16,18,20]
# print(v1)
#
# k = np.arange(1, len(v1)+1)
# print(k)
# v1 = np.array(v1)
# z1 = np.polyfit(k,v1,1)
# print('{0}x + {1}'.format(*z1))
#
# v2 = [(z1[0]*x+z1[1]+1) for x in k]
# print(v2)
#
# # v3 = [2 ** (i+2) for i in range(0,10)]
# # print(v3)
# # v3 = np.array(v3)
# # z3 = np.polyfit(v3,k,1)
# # print('{0}x + {1}'.format(*z3))
#
# plt.plot(k, v1, 'r--', k, v2, 'b--')
# plt.show()
##################################################################


# plt.plot(k, v1, 'b--')
# plt.show()

# v2 = [50,55,60,65,70,75,85,90,95,100]
# v2 = [(z1[0] * x + z1[1]) for x in k]
# v2 = [round(x, 2) for x in v2]
# print(v2)
# v2 = np.array(v2)
# z2 = np.polyfit(k,v2,1)
# print('{0}x + {1}'.format(*z2))

# k = [2012, 2013, 2014, 2015, 2016]
# plt.plot(k, v1, 'r--', k, v2, 'b--')
# plt.savefig('test.png')
# plt.show()

# data = [12, 34, 29, 38, 34, 51, 29, 34, 47, 34, 55, 94, 68, 81]
# data1 = [10 * x for x in data]
# k = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# data = [2,4,6,8,12,14,16]
# data = [1,2,3,4,50,40]
# x = np.arange(0,len(data))
# y=np.array(data)
#
# y1 = np.array(data1)
# z = np.polyfit(x,y,1)
# z1 =np.polyfit(x,y1,1)
#
# print("{0}x + {1}".format(*z))
# print("{0}x + {1}".format(*z1))
#
# print(average_change(data))
#
# plt.plot(k, data)
# plt.savefig('test1.png')
# plt.show()


# v2 = [1435.4,2158.2,2714,3154.9,3199.1,3312.3,2894.3,2343.8,2858,1124,1486,1590,1696,2166,1235,1603,1708,2257,4042,5598,8152,13197,17222,25684,43818,68662,64304,70537,93626,84263]
# v3 = [round(a-b,2) for a,b in zip(v2,v1)]
# print(v3)
#
# r = input()
# if r is '8':
#     print('your in!')
# else:
#     print('your out')
#
# report_choices = {1: 'Balance', 2: 'Cash Flow'}
# c = input()
# print('c: ' + c)
# report_choice = ''
# try:
#     report_choice = report_choices[int(c)]
# except KeyError:
#     report_choice = 'Income'
# except ValueError:
#     report_choice = 'Income'
# print(report_choice)
