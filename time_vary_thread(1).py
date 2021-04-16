import csv

import numpy as np
import matplotlib
import math
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt

from matplotlib.ticker import LinearLocator, MultipleLocator, FormatStrFormatter, LogLocator

plt.rcParams.update({'font.size': 20})
font_title_x = {'family': 'Arial', 'weight': 'normal', 'size': 20}


wls = [1, 8, 16, 24, 32]
# xmajorLocator = LogLocator(base=2.0, subs=(1.0, ), numdecs=4, numticks=10)
ymajorLocator = LogLocator(base=10.0, subs=(1.0, ), numdecs=4, numticks=10)

nell=[183.319444444444,57.6711111111111,45.6482777777778,42.2227222222222,40.171]
gtopdb=[24677.73,4694.991,3073.609,2470.048,2184]
dbis=[89635,15678.8,9954.17,7832.84,6546.55]
# dbis=[]
amazon=[83036.6666666667,14545.1111111111,8434.77777777778,6264.66666666667,5070.24444444444]

###### old results
# # sim_0 = [14862.6,2475.228,1372.548,1018.476,798.174]
# sim_1 = [218.6496,82.521,72.1434,67.398,65.9754]
#
# dpsim_0 = [66910.2,12408.36,6602.76,4857.486,3755.628]
# # dpsim_1 = [375.7805,100.4695,81.2955,69.825,65.797]
###------------------Set Plotting-------------------------
fig = plt.figure(0, figsize=(5.6, 4))
ax = fig.subplots()

ax.set_ylim(10, 100500)
ax.set_yscale('log')
ax.set_ylabel('Running Time (s)')
ax.set_xlabel('number of threads')

ax.yaxis.set_major_locator(ymajorLocator)
# ax.yaxis.set_minor_locator(ymajorLocator)
plt.xticks(wls)
ax.set_xticklabels([str(x) for x in wls], fontdict = font_title_x)

###------------------Read Data-------------------------
# mk = 0
# for ds in DATASETS:
#     d = []
#     with open('./data/vary_thread/' + ds.lower() + '_thr', 'r') as infile:
#         reader = csv.reader(infile, delimiter=',')
#         for row in reader:
#             for i in np.arange(0,len(wls),1):
#                 d.append(float(row[int(i)]))

# ax.plot(wls, sim_0, 'k-', marker= 'v', label=r'$FSim_{s}, \theta = 0$', markersize=12)
ax.plot(wls, nell, 'k--', marker= 'd', label='NELL', markersize=11)
ax.plot(wls, dbis, 'k:', marker= 'v', label='DBIS', markersize=12)
ax.plot(wls, amazon, 'k-', marker= 'x', label='Amazon', markersize=12)
ax.plot(wls, gtopdb, 'k-.', marker= 's', label='GtoPdb', markersize=12)
# ax.plot(wls, amazon, 'k-.', marker= 's', label='Amazon', markersize=12)
# ax.plot(wls, dpsim_1, 'k-.', marker= 'D', label=r'$FSim_{dp}, \theta = 1$', markersize=9, markerfacecolor = 'none')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width , box.height* 0.8])
plt.legend(fontsize = 18, loc = 'center', bbox_to_anchor=(0.5, 1.2),ncol=2, handlelength = 1.8, handletextpad = 1, labelspacing = 0, columnspacing=1)

# plt.legend(fontsize=18, loc = "upper right", handlelength = 1, handletextpad = 0.5, labelspacing = 0.3)
plt.tight_layout()
plt.savefig('./figures/' + 'time_vary_thread_new.pdf', format='pdf', dpi=10, bbox_inches='tight')
plt.show()