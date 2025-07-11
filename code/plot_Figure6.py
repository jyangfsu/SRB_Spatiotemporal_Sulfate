# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:48:59 2024

@author: Jing
"""
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from wqchartpy import triangle_piper
from wqchartpy import gibbs
from wqchartpy import gaillardet
from matplotlib.pyplot import minorticks_on, tick_params



dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5

ions_WEIGHT = {'Ca'  : 40.0780,
               'Mg'  : 24.3050,
               'K'   : 39.0983,
               'Na'  : 22.9898,
               'Cl'  : 35.4527,
               'SO4' : 96.0636,
               'CO3' : 60.0092,
               'HCO3': 61.0171}

ions_CHARGE = {'Ca'  : +2,
               'Mg'  : +2,
               'K'   : +1, 
               'Na'  : +1,
               'Cl'  : -1,
               'SO4' : -2,
               'CO3' : -2,
               'HCO3': -1,}


# Load the wrapped lines taken from Gibbs (1970)
Cl_HCO3_plot_wrapped_lines = np.array([
    [0.0056, 0.0251, 0.0446, 0.0771, 0.1096,
     0.1291, 0.1454, 0.1844, 0.2104, 0.2299,
     0.2656, 0.2883, 0.3078, 0.3500, 0.3792,
     0.4052, 0.4507, 0.4799, 0.4994, 0.5351,
     0.5579, 0.5741, 0.5904, 0.6196, 0.6488,
     0.6716, 0.6976, 0.7236, 0.7495, 0.7723,
     0.7983, 0.8242, 0.8535, 0.8827, 0.9119,
     0.9444, 0.9704, 0.9931, 9.9999, 9.9999,
     0.9961, 0.9830, 0.9668, 0.9538, 0.944,
     0.9180, 0.9050, 0.8887, 0.8530, 0.8302,
     0.8074, 0.7814, 0.7554, 0.7294, 0.7132,
     0.6937, 0.6742, 0.6417, 0.6189, 0.5897,
     0.5735, 0.5605, 0.5377, 0.5150, 0.4955,
     0.4760, 0.4565, 0.4402, 0.4175, 0.4013,
     0.3785, 0.3590, 0.3395, 0.3200, 0.3070,
     0.2941, 0.2746, 0.2551, 0.2388, 0.2291,
     0.2128, 0.2063, 0.1998, 0.1997, 0.2062,
     0.2159, 0.2354, 0.2516, 0.2646, 0.2873,
     0.3002, 0.3262, 0.3489, 0.3683, 0.3878,
     0.4105, 0.4267, 0.4527, 0.4754, 0.5175,
     0.5500, 0.5694, 0.5889, 0.6148, 0.6376,
     0.6538, 0.6700, 0.6927, 0.7089, 0.7252,
     0.7479, 0.7771, 0.7965, 0.8160, 0.8322,
     0.8517, 0.8841, 0.9003, 0.9165, 0.9392,
     0.9522, 0.9684, 0.9846, 0.9975, 9.9999,
     9.9999, 0.9935, 0.9870, 0.9708, 0.9579,
     0.9385, 0.9255, 0.9061, 0.8801, 0.8607,
     0.8347, 0.8088, 0.7893, 0.7602, 0.7277,
     0.6855, 0.6531, 0.6044, 0.5623, 0.5298,
     0.4909, 0.4520, 0.4196, 0.3839, 0.3450,
     0.3158, 0.2899, 0.2672, 0.2380, 0.2088,
     0.1861, 0.1634, 0.1408, 0.1148, 0.0889,
     0.0759, 0.0630, 0.0500, 0.0371, 0.0209,
     0.0079],
    [21.4751, 19.1493, 17.0753, 15.2298, 13.0728,
     11.8826, 11.2221, 10.2041, 9.6387, 9.2797,
     8.9368, 8.7709, 8.6076, 8.6146, 8.4558,
     8.2994, 7.8425, 7.6979, 7.4111, 7.0018,
     6.7414, 6.4899, 6.3687, 5.9019, 5.6831,
     5.4718, 5.1686, 4.9767, 4.7919, 4.6137,
     4.5284, 4.4446, 4.3627, 4.2822, 4.2033,
     4.2059, 4.208, 4.1299, 4.1299, 10.1674,
     10.1674, 11.4037, 12.7896, 14.0724, 15.4849,
     17.6996, 19.8518, 21.8417, 24.487, 27.9908,
     30.2081, 33.2299, 35.8599, 38.6981, 40.9758,
     43.3849, 46.8245, 50.5243, 54.5265, 58.8385,
     61.1188, 62.2861, 67.2201, 69.8165, 73.9212,
     76.7813, 81.2954, 84.446, 89.4052, 92.8702,
     96.4574, 102.1283, 104.0659, 110.1841, 114.4615,
     116.6475, 121.1607, 125.8485, 130.7259, 138.4373,
     146.5855, 161.3088, 174.141, 191.656, 219.2029,
     236.7142, 260.6201, 281.4751, 298.2091, 322.1122,
     347.8662, 383.045, 421.755, 455.5326, 482.6745,
     521.3635, 563.0834, 608.2554, 657.0104, 751.9576,
     828.1041, 877.4449, 929.7256, 985.244, 1044.0127,
     1085.1491, 1127.9064, 1195.1847, 1242.2777, 1291.2262,
     1368.2463, 1506.707, 1596.481, 1724.3402, 1826.9677,
     1973.2861, 2258.0322, 2485.9166, 2684.8419, 3013.3769,
     3317.2855, 3582.7378, 3944.3137, 4178.8072, 4178.8072,
     62336.9735, 62336.9735, 56633.1044, 49506.8651, 42458.3638,
     35717.6411, 33073.3075, 28909.8381, 24787.6514, 22513.9619,
     20058.1172, 17870.1583, 16545.0928, 14739.4207, 13643.1016,
     12151.1174, 11247.3165, 9825.9309, 8585.2422, 7795.8054,
     6682.5559, 5839.1344, 5201.5485, 4459.0392, 3822.2836,
     3277.0691, 2919.6032, 2551.907, 2273.401, 1875.816,
     1703.6475, 1460.8193, 1252.6024, 1053.6071, 886.2253,
     805.035, 731.2828, 677.1427, 603.4295, 517.4845,
     452.3967]])
  
Na_Ca_plot_wrapped_lines = np.array([
    [0.0083, 0.0277, 0.0505, 0.0668, 0.0830,
     0.1090, 0.1253, 0.1481, 0.1611, 0.1871,
     0.2067, 0.2294, 0.2457, 0.2718, 0.2880,
     0.3174, 0.3500, 0.3956, 0.4379, 0.4802,
     0.5225, 0.5681, 0.6039, 0.6429, 0.6819,
     0.7144, 0.7534, 0.7729, 0.7924, 0.8119,
     0.8314, 0.8509, 0.8737, 0.8997, 0.9225,
     0.9420, 0.9615, 0.9843, 0.9973, 9.9999,
     9.9999, 0.9932, 0.9866, 0.9636, 0.9406,
     0.9209, 0.9045, 0.8881, 0.8716, 0.8519,
     0.8322, 0.8026, 0.7663, 0.7367, 0.7070,
     0.6774, 0.6543, 0.6279, 0.6146, 0.5916,
     0.5783, 0.5617, 0.5419, 0.5383, 0.5513,
     0.5739, 0.6096, 0.6453, 0.6778, 0.6940,
     0.7135, 0.7362, 0.7653, 0.8010, 0.8399,
     0.8724, 0.8983, 0.9340, 0.9469, 0.9696,
     0.9891, 0.9955, 9.9999, 9.9999, 0.9003,
     0.8871, 0.8410, 0.8278, 0.7949, 0.7619,
     0.7290, 0.6830, 0.6369, 0.5942, 0.5516,
     0.5089, 0.4399, 0.4005, 0.3545, 0.3118,
     0.2658, 0.2296, 0.1836, 0.1442, 0.1047,
     0.0718, 0.0454, 0.0092],
    [108.9257, 97.0774, 88.1725, 80.1044, 74.1755,
     66.0907, 61.199, 56.6553, 52.4686, 47.6497,
     44.9668, 40.842, 39.2892, 35.6808, 33.0399,
     30.5792, 28.2983, 24.7192, 21.5954, 18.5101,
     15.5659, 12.5986, 11.0093, 9.0844, 7.3545,
     6.3061, 5.2036, 4.6375, 4.2938, 3.8267,
     3.543, 3.2184, 2.9232, 2.6046, 2.321,
     2.1489, 1.9896, 1.8419, 1.7386, 1.7386,
     7514.32, 7514.32, 7234.9489, 6582.7621, 5989.366,
     5553.6776, 5051.7878, 4683.7185, 4179.9779, 3730.8803,
     3394.141, 2808.0488, 2153.0926, 1714.648, 1365.4861,
     1087.4256, 899.4273, 702.6564, 592.1454, 508.812,
     420.6893, 334.8554, 271.6992, 204.138, 175.1691,
     144.6326, 114.8937, 91.2695, 78.2591, 68.4377,
     59.8414, 50.3607, 39.2599, 30.5983, 22.9525,
     18.2353, 14.4912, 11.7332, 10.262, 8.6362,
     7.5514, 7.267, 7.267, 45278.8769, 45278.8769,
     39640.8983, 28715.7533, 25624.1396, 20408.7169, 15947.8034,
     12461.9512, 9558.8684, 7473.2267, 6069.0146, 5023.5351,
     4238.2048, 3072.823, 2592.1249, 2065.5649, 1614.6797,
     1311.4464, 1044.6506, 816.7192, 650.65, 508.5584,
     412.8464, 341.5145, 261.8588]])


unit = 'mg/L'
############################## Na-Ca plot #################################

fig = plt.figure(figsize=(8, 7.5))


ax1 = fig.add_subplot(221)
ax1.semilogy()
ax1.plot(Na_Ca_plot_wrapped_lines[0], Na_Ca_plot_wrapped_lines[1],
         'k--', lw=1)
ax1.set_xlim(0, 1)
ax1.set_ylim(1, 45000)

'''
minorticks_on()
tick_params(which='major', direction='in', length=4, width=1.25)
tick_params(which='minor', direction='in', length=2.5, width=1.25)

ax1.spines['top'].set_linewidth(1.25)
ax1.spines['top'].set_color('k')
ax1.spines['bottom'].set_linewidth(1.25)
ax1.spines['bottom'].set_color('k')
ax1.spines['left'].set_linewidth(1.25)
ax1.spines['left'].set_color('k')
ax1.spines['right'].set_linewidth(1.25)
ax1.spines['right'].set_color('k')
'''
ax1.text(0.775, 5, 'Rainfall', fontname='cursive', ha='left',
         fontsize=10)
ax1.text(0.025, 155, 'Rock \ndominancy', va='center',
         fontname='cursive', fontsize=10)
ax1.text(0.725, 10000,'Seawater', fontname='cursive', ha='left',
         fontsize=10)

ax1.set_xlabel('$Na^+$/($Na^+$+$Ca^{2+}$) [Molar ratio]', weight='normal')
ax1.set_ylabel('$TDS$ [mg/L]',weight='normal')
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
#[label.set_fontsize(10) for label in labels]



ax1.text(0.05, 12000, '(a)')   
 
for i in range(3):
    if i == 0 :
        tmp_df = dfc1
        color = '#FE0000'
    if i == 1 :
        tmp_df = dfc2
        color = '#00FE00'
    if i == 2 :
        tmp_df = dfc3
        color = 'blue'
        
      
    tmp_df['Sample'] = tmp_df['ID'] 
    tmp_df['Label'] = tmp_df['River'] 
    tmp_df['Alpha'] = 0.8
    tmp_df['HCO3'] = tmp_df['HCO3_mgL_tit'] 
    tmp_df['CO3'] = 0
    
    tmp_df.loc[tmp_df['River']=='Huai River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Huai River', 'Marker'] = 's'
    tmp_df.loc[tmp_df['River']=='Huai River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Marker'] = 'o'
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Marker'] = '*'
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Sha River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Sha River', 'Marker'] = 'v'
    tmp_df.loc[tmp_df['River']=='Sha River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Ying River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Ying River', 'Marker'] = 'D'
    tmp_df.loc[tmp_df['River']=='Ying River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Marker'] = '^'
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='GW', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='GW', 'Marker'] = 'X'
    tmp_df.loc[tmp_df['River']=='GW', 'Size'] = 40
    
    
    
    df = tmp_df[['Sample', 'Label', 'Color', 'Marker', 'Size', 'Alpha', 
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]
   
    df['Alpha'] = 0.6


    Labels = []
    for i in range(len(df)):
        if (df.at[i, 'Label'] in Labels or df.at[i, 'Label'] == ''):
            TmpLabel = ''
        else:
            TmpLabel = df.at[i, 'Label']
            Labels.append(TmpLabel)
    
        try:
            if unit == 'mg/L':
                x = df.at[i, 'Na'] / ions_WEIGHT['Na'] / \
                    (df.at[i, 'Na'] / ions_WEIGHT['Na'] + \
                     df.at[i, 'Ca'] / ions_WEIGHT['Ca'])

            elif unit == 'meq/L':
                x = df.at[i, 'Na'] / ions_WEIGHT['Na'] / ions_CHARGE['Na'] / \
                    (df.at[i, 'Na'] / ions_WEIGHT['Na'] / ions_CHARGE['Na'] + \
                     df.at[i, 'Ca'] / ions_WEIGHT['Ca'] / ions_CHARGE['Ca'])
            
            else:
                raise RuntimeError("""
                Currently only mg/L and meq/L are supported.
                Convert the unit if needed.""")
       
            y = df.at[i, 'TDS']   
            
            ax1.scatter(x, y, 
                        marker=df.at[i, 'Marker'],
                        s=df.at[i, 'Size'], 
                        color=df.at[i, 'Color'], 
                        alpha=df.at[i, 'Alpha'],
                        #label=TmpLabel, 
                        edgecolors='black') 
            
            
        except(ValueError):
                pass

##########################################################################


import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from wqchartpy import triangle_piper
from wqchartpy import gibbs
from wqchartpy import gaillardet


import os
import numpy as np
import pandas as pd
import matplotlib
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1.inset_locator import inset_axes



dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5

ions_WEIGHT = {'Ca'  : 40.0780,
               'Mg'  : 24.3050,
               'K'   : 39.0983,
               'Na'  : 22.9898,
               'Cl'  : 35.4527,
               'SO4' : 96.0636,
               'CO3' : 60.0092,
               'HCO3': 61.0171}

ions_CHARGE = {'Ca'  : +2,
               'Mg'  : +2,
               'K'   : +1, 
               'Na'  : +1,
               'Cl'  : -1,
               'SO4' : -2,
               'CO3' : -2,
               'HCO3': -1,}


ax2 = fig.add_subplot(222)

'''

ax1.loglog()
# Show horizontal line at 100
ax1.axhline(y=100, linestyle=':', linewidth=1, color='k')

# Add a rectangle for Evaporites
rect = mpatches.Rectangle([0.12, 0.15], 0.15, 0.20, 
                          fc="#FCF7B6", ec='k', alpha=0.6, hatch='///')
ax1.add_patch(rect)
ax1.text(0.3, 0.2, 'Evaporites', fontname='Times New Roman', fontsize=10, family='cursive')


# Add an ellipse for Silicates
axins = inset_axes(ax1, width="100%", height="100%", loc=3)
ellipse = mpatches.Ellipse([0.2, 0.35], 0.20, 0.13, angle=45, 
                           fc="red", ec='k', alpha=0.2, hatch='\\\\\\')
axins.add_patch(ellipse)
axins.axis('off')
ax1.text(0.15, 4, 'Silicates', fontname='Times New Roman', fontsize=10, family='cursive')



# Add an ellipse for Carbonates
axins = inset_axes(ax1, width="100%", height="100%", loc=2)
ellipse = mpatches.Ellipse([0.85, 0.90], 0.25, 0.1, angle=30,
                           fc="#A8FEFE", ec='k', alpha=0.6, hatch='++')
axins.add_patch(ellipse)
axins.axis('off')
ax1.text(2.5, 70, 'Carbonates       ',
         fontname='Times New Roman', fontsize=10, family='cursive')

# Set the labels and ticks
ax1.set_xlabel('$Ca^{2+}/Na^+$', weight='normal')
ax1.set_ylabel('$HCO_3^-/Na^+$', weight='normal')



ax1.set_xlim(0.1, 100)
ax1.set_ylim(0.1, 250)

'''


ax2.loglog()

# Show horizontal line at 10
ax2.axhline(y=10, linestyle=':', linewidth=1, color='k')

# Add a rectangle for Evaporites
rect = mpatches.Rectangle([0.12, 0.015], 0.15, 0.020, 
                          fc="#FCF7B6", ec='k', alpha=0.6, hatch='///')
ax2.add_patch(rect)
ax2.text(0.3, 0.02, 'Evaporites',
          fontsize=10, family='cursive')

# Add an ellipse for Silicates
axins = inset_axes(ax2, width="100%", height="100%", loc=3)
ellipse = mpatches.Ellipse([0.20, 0.40], 0.20, 0.13, angle=45, 
                           fc="w", ec='k', alpha=0.2, hatch='\\\\\\')
axins.add_patch(ellipse)
axins.axis('off')
ax2.text(0.15, 0.6, 'Silicates', 
        fontsize=10, family='cursive') 

# Add an ellipse for Carbonates
axins = inset_axes(ax2, width="100%", height="100%", loc=2)
ellipse = mpatches.Ellipse([0.87, 0.90], 0.20, 0.17, angle=45, 
                           fc="#A8FEFE", ec='k', alpha=0.6, hatch='++')
axins.add_patch(ellipse)
axins.axis('off')
ax2.text(5.2, 14, 'Carbonates', 
          fontsize=10, family='cursive', zorder=-1000)

# Set the lables and ticks
ax2.set_xlabel('$Ca^{2+}/Na^+$ [Molar ratio]', weight='normal')
ax2.set_ylabel('$Mg^{2+}/Na^+$ [Molar ratio]', weight='normal')

labels = ax2.get_xticklabels() + ax2.get_yticklabels()
[label.set_fontsize(10) for label in labels]

ax2.set_xlim(0.1, 100)
ax2.set_ylim(0.01, 25)

 


for i in range(3):
    if i == 0 :
        tmp_df = dfc1
        color = '#FE0000'
    if i == 1 :
        tmp_df = dfc2
        color = '#00FE00'
    if i == 2 :
        tmp_df = dfc3
        color = 'blue'
        
      
    tmp_df['Sample'] = tmp_df['ID'] 
    tmp_df['Label'] = tmp_df['River'] 
    tmp_df['Alpha'] = 0.8
    tmp_df['HCO3'] = tmp_df['HCO3_mgL_tit'] 
    tmp_df['CO3'] = 0
    
    tmp_df.loc[tmp_df['River']=='Huai River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Huai River', 'Marker'] = 's'
    tmp_df.loc[tmp_df['River']=='Huai River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Marker'] = 'o'
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Marker'] = '*'
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Sha River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Sha River', 'Marker'] = 'v'
    tmp_df.loc[tmp_df['River']=='Sha River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Ying River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Ying River', 'Marker'] = 'D'
    tmp_df.loc[tmp_df['River']=='Ying River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Marker'] = '^'
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='GW', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='GW', 'Marker'] = 'X'
    tmp_df.loc[tmp_df['River']=='GW', 'Size'] = 40
    
    
    
    df = tmp_df[['Sample', 'Label', 'Color', 'Marker', 'Size', 'Alpha', 
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]
   
    df['Alpha'] = 0.6


    Labels = []
    for i in range(len(df)):
        if (df.at[i, 'Label'] in Labels or df.at[i, 'Label'] == ''):
            TmpLabel = ''
        else:
            TmpLabel = df.at[i, 'Label']
            Labels.append(TmpLabel)
    
        try:
            if unit == 'mg/L':
                x = df.at[i, 'Na'] / ions_WEIGHT['Na'] / \
                    (df.at[i, 'Na'] / ions_WEIGHT['Na'] + \
                     df.at[i, 'Ca'] / ions_WEIGHT['Ca'])

            elif unit == 'meq/L':
                x = df.at[i, 'Na'] / ions_WEIGHT['Na'] / ions_CHARGE['Na'] / \
                    (df.at[i, 'Na'] / ions_WEIGHT['Na'] / ions_CHARGE['Na'] + \
                     df.at[i, 'Ca'] / ions_WEIGHT['Ca'] / ions_CHARGE['Ca'])
            
            else:
                raise RuntimeError("""
                Currently only mg/L and meq/L are supported.
                Convert the unit if needed.""")
       
            x =   (df.at[i, 'Ca'] / 40) / (df.at[i, 'Na'] / 23) 
            y =   (df.at[i, 'Mg'] / 24) / (df.at[i, 'Na'] / 23) 
            ax2.scatter(x, y, 
                        marker=df.at[i, 'Marker'],
                        s=df.at[i, 'Size'], 
                        color=df.at[i, 'Color'], 
                        alpha=df.at[i, 'Alpha'],
                        #label=TmpLabel, 
                        edgecolors='black') 
            
            
        except(ValueError):
                pass

ax2.text(0.125, 11, '(b)')    

# Add an ellipse for Carbonates
import seaborn as sns
axins = inset_axes(ax2, width="49%", height="98%", loc=4)
palette=['#497A90', '#B1B1B1', '#D02C31', 'b', 'g']

axins.set_yscale('log')
axins.set_ylim([1e-2, 25])

axins.axis('off')
axins.set_xlim(0.1, 100)

par = 'Mg_Na'
for i in range(len(dfc1)):

    dfc1.at[i, par] = (dfc1.at[i, 'Mg'] / 24) / (dfc1.at[i, 'Na'] / 23) 
    dfc2.at[i, par] = (dfc2.at[i, 'Mg'] / 24) / (dfc2.at[i, 'Na'] / 23) 
    dfc3.at[i, par] = (dfc3.at[i, 'Mg'] / 24) / (dfc3.at[i, 'Na'] / 23) 
    

df = pd.concat([dfc1[(dfc1['River']=='Sha River') | (dfc1['River']=='Ying River') | (dfc1['River']=='Jialu River') | (dfc1['River']=='Middle reaches') | (dfc1['River']=='Lower reaches')][['River', par]],
                dfc2[(dfc2['River']=='Sha River') | (dfc2['River']=='Ying River') | (dfc2['River']=='Jialu River' ) | (dfc2['River']=='Middle reaches') | (dfc2['River']=='Lower reaches')][['River', par]], 
                dfc3[(dfc3['River']=='Sha River') | (dfc3['River']=='Ying River') | (dfc3['River']=='Jialu River') | (dfc3['River']=='Middle reaches') | (dfc3['River']=='Lower reaches')][['River', par]]])

df.to_csv('df_Mg_Na_ratio.csv')
#violinplot
sns.boxplot(data=df, x='River', y=par, ax=axins, width=0.3, palette=palette, linewidth=1.0,
            medianprops=dict(color="w", linewidth=1),
            boxprops = dict(linestyle='-', linewidth=1, facecolor='k', edgecolor='grey'),
            flierprops=dict(linestyle='-', linewidth=1),
            whiskerprops=dict(linestyle='-', linewidth=1),
            capprops=dict(linestyle='-', linewidth=1),
            showfliers=False,
            )



#axins.invert_xaxis()  

axins.text(-0.5, 0.04, 'Low.', rotation=90)
axins.text(0.60, 0.04, 'Mid.', rotation=90)
axins.text(1.70, 0.04, 'Sha', rotation=90)
axins.text(2.8, 0.04, 'Ying', rotation=90)
axins.text(3.9, 0.04, 'Jialu', rotation=90)

axins.plot([-1.0, 4.4], [0.030, 0.030], 'k-', lw=1.0)






################################################################

ax2 = fig.add_subplot(223)

ax2.set_xlim(0, 2.5)
ax2.set_ylim(0, 3.5)
ax2.set_xlabel('$SO_4^{2-}/HCO_3^-$ [Meq ratio]')
ax2.set_ylabel('$(Ca^{2+}+Mg^{2+})/HCO_3^-$ [Meq ratio]')


for i in range(3):
    if i == 0 :
        tmp_df2 = dfc1
        color = '#FE0000'
    if i == 1 :
        tmp_df2 = dfc2
        color = '#00FE00'
    if i == 2 :
        tmp_df2 = dfc3
        color = 'blue'
        
      
    tmp_df2['Sample'] = tmp_df2['ID'] 
    tmp_df2['Label'] = tmp_df2['River'] 
    tmp_df2['Alpha'] = 0.8
    tmp_df2['HCO3'] = tmp_df2['HCO3_mgL_tit'] 
    tmp_df2['CO3'] = 0
    
    tmp_df2.loc[tmp_df2['River']=='Huai River', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='Huai River', 'Marker'] = 's'
    tmp_df2.loc[tmp_df2['River']=='Huai River', 'Size'] = 40
    
    tmp_df2.loc[tmp_df2['River']=='Lower reaches', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='Lower reaches', 'Marker'] = 'o'
    tmp_df2.loc[tmp_df2['River']=='Lower reaches', 'Size'] = 40
    
    tmp_df2.loc[tmp_df2['River']=='Middle reaches', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='Middle reaches', 'Marker'] = '*'
    tmp_df2.loc[tmp_df2['River']=='Middle reaches', 'Size'] = 40
    
    tmp_df2.loc[tmp_df2['River']=='Sha River', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='Sha River', 'Marker'] = 'v'
    tmp_df2.loc[tmp_df2['River']=='Sha River', 'Size'] = 40
    
    tmp_df2.loc[tmp_df2['River']=='Ying River', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='Ying River', 'Marker'] = 'D'
    tmp_df2.loc[tmp_df2['River']=='Ying River', 'Size'] = 40
    
    tmp_df2.loc[tmp_df2['River']=='Jialu River', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='Jialu River', 'Marker'] = '^'
    tmp_df2.loc[tmp_df2['River']=='Jialu River', 'Size'] = 40
    
    tmp_df2.loc[tmp_df2['River']=='GW', 'Color'] = color
    tmp_df2.loc[tmp_df2['River']=='GW', 'Marker'] = 'X'
    tmp_df2.loc[tmp_df2['River']=='GW', 'Size'] = 40
    
    
    
    df2 = tmp_df2[['Sample', 'Label', 'Color', 'Marker', 'Size', 'Alpha', 
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]
   
    df2['Alpha'] = 0.6


    Labels = []
    for i in range(len(df2)):
        if (df2.at[i, 'Label'] in Labels or df2.at[i, 'Label'] == ''):
            TmpLabel = ''
        else:
            TmpLabel = df2.at[i, 'Label']
            Labels.append(TmpLabel)
            
        ax2.scatter((df2.at[i, 'SO4'] / ions_WEIGHT['SO4'] * 2) / (df2.at[i, 'HCO3'] / ions_WEIGHT['HCO3'] * 1),
                 (df2.at[i, 'Ca'] / 40 * 2 + df2.at[i, 'Mg'] / 24 * 2) / (df2.at[i, 'HCO3'] / ions_WEIGHT['HCO3'] * 1),
                 marker=df2.at[i, 'Marker'],
                 s=df2.at[i, 'Size'], 
                 color=df2.at[i, 'Color'], 
                 alpha=df2.at[i, 'Alpha'],
                 #label=TmpLabel, 
                 edgecolors='black')
        
    
    
    
    
ax2.plot([0.9, 1.1], [2.0, 2.0], color='k')    
ax2.plot([1.0, 1.0], [1.9, 2.1], color='k')     
    
    
    
ax2.plot([-0.1, 0.1], [1.0, 1.0], color='k')    
ax2.plot([0.0, 0.0], [0.9, 1.1], color='k')       
    
    
ax2.text(0.125, 3.15, '(c)')    
plt.annotate('$H_2SO_4$ only', xy=(1.0, 2.0), xytext=(1.5, 1.0), ha='center',
            xycoords='data',
            arrowprops=dict(arrowstyle = "->", facecolor='black'))
    
    
plt.annotate('$H_2CO_3$ only', xy=(0.0, 1.0), xytext=(0.5, 2.5), ha='center',
            xycoords='data',
            arrowprops=dict(arrowstyle = "->", facecolor='black'))    
    
   


################################################################

ax4 = fig.add_subplot(224)
# Set the lables and ticks
ax4.set_xlabel('$Ca^{2+}+Mg^{2+}$ [meq/L]', weight='normal')
ax4.set_ylabel('$HCO_3^-+SO_4^{2-}$ [meq/L]', weight='normal')
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 10)

for i in range(3):
    if i == 0 :
        tmp_df = dfc1
        color = '#FE0000'
    if i == 1 :
        tmp_df = dfc2
        color = '#00FE00'
    if i == 2 :
        tmp_df = dfc3
        color = 'blue'
        
      
    tmp_df['Sample'] = tmp_df['ID'] 
    tmp_df['Label'] = tmp_df['River'] 
    tmp_df['Alpha'] = 0.8
    tmp_df['HCO3'] = tmp_df['HCO3_mgL_tit'] 
    tmp_df['CO3'] = 0
    
    tmp_df.loc[tmp_df['River']=='Huai River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Huai River', 'Marker'] = 's'
    tmp_df.loc[tmp_df['River']=='Huai River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Marker'] = 'o'
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Marker'] = '*'
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Sha River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Sha River', 'Marker'] = 'v'
    tmp_df.loc[tmp_df['River']=='Sha River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Ying River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Ying River', 'Marker'] = 'D'
    tmp_df.loc[tmp_df['River']=='Ying River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Marker'] = '^'
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Size'] = 40
    
    tmp_df.loc[tmp_df['River']=='GW', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='GW', 'Marker'] = 'X'
    tmp_df.loc[tmp_df['River']=='GW', 'Size'] = 40
    
    
    
    df = tmp_df[['Sample', 'Label', 'Color', 'Marker', 'Size', 'Alpha', 
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]
   
    df['Alpha'] = 0.6


    Labels = []
    for i in range(len(df)):
        if (df.at[i, 'Label'] in Labels or df.at[i, 'Label'] == ''):
            TmpLabel = ''
        else:
            TmpLabel = df.at[i, 'Label']
            Labels.append(TmpLabel)
    
        try:
            if unit == 'mg/L':
                x = df.at[i, 'Na'] / ions_WEIGHT['Na'] / \
                    (df.at[i, 'Na'] / ions_WEIGHT['Na'] + \
                     df.at[i, 'Ca'] / ions_WEIGHT['Ca'])

            elif unit == 'meq/L':
                x = df.at[i, 'Na'] / ions_WEIGHT['Na'] / ions_CHARGE['Na'] / \
                    (df.at[i, 'Na'] / ions_WEIGHT['Na'] / ions_CHARGE['Na'] + \
                     df.at[i, 'Ca'] / ions_WEIGHT['Ca'] / ions_CHARGE['Ca'])
            
            else:
                raise RuntimeError("""
                Currently only mg/L and meq/L are supported.
                Convert the unit if needed.""")
       
            x =   df.at[i, 'Ca'] / 40 *2   + df.at[i, 'Mg'] / 24 * 2
            y =   df.at[i, 'HCO3'] / 61 * 1 + df.at[i, 'SO4'] / 96 * 2
            ax4.scatter(x, y, 
                        marker=df.at[i, 'Marker'],
                        s=df.at[i, 'Size'], 
                        color=df.at[i, 'Color'], 
                        alpha=df.at[i, 'Alpha'],
                        #label=TmpLabel, 
                        edgecolors='black') 
            
            
        except(ValueError):
                pass

    xx = np.linspace(0, 10, 100)
    ax4.plot(xx, xx, 'k:')
    #ax4.text(0, 0.7, '1:1 line', rotation=45)
    ax4.text(0.5, 9, '(d)', fontname='DejaVu Sans', weight=None)
    

plt.subplots_adjust(wspace=0.3, hspace=0.2)



plt.savefig('ratios.jpg', dpi=600, bbox_inches='tight')








'''

ax3 = fig.add_subplot(224)  

plt.scatter(90, 10, marker='s', s=40, color='w',edgecolors='black', label='Huai River')  
plt.scatter(90, 9, marker='o', s=40, color='w',edgecolors='black', label='Lower reaches')      
plt.scatter(90, 8, marker='*', s=70, color='w',edgecolors='black', label='Middle reaches')      
plt.scatter(90, 7, marker='v', s=40, color='w',edgecolors='black', label='Sha River')     
plt.scatter(90, 6, marker='D', s=40, color='w',edgecolors='black', label='Ying River')    
plt.scatter(90, 5, marker='^', s=40, color='w',edgecolors='black', label='Jialu River')    
plt.scatter(90, 4, marker='x', s=40, color='k',edgecolors='black', label='Groundwater')  

plt.fill_between([90.98, 90.985], 4, 5, color='#FE0000', label='Dec. 2019')
plt.fill_between([90.99, 90.995], 4, 5, color='#00FE00', label='May. 2020')
plt.fill_between([90.10, 90.105], 4, 5, color='blue', label='Aug. 2020')

plt.legend(bbox_to_anchor=(1.05, 2.25), loc=2, borderaxespad=0, shadow=True)    



plt.subplots_adjust(wspace=0.3, hspace=0.25)




    

plt.savefig('ratios.jpg', dpi=1000)
        


'''
    

fig = plt.figure(figsize=(8, 3.75))
ax3 = fig.add_subplot(121)  

plt.scatter(1, 10, marker='s', s=40, color='w',edgecolors='black', label='Huai River')  
plt.scatter(1, 9, marker='o', s=40, color='w',edgecolors='black', label='Lower reaches')      
plt.scatter(1, 8, marker='*', s=70, color='w',edgecolors='black', label='Middle reaches')      
plt.scatter(1, 7, marker='v', s=40, color='w',edgecolors='black', label='Sha River')     
plt.scatter(1, 6, marker='D', s=40, color='w',edgecolors='black', label='Ying River')    
plt.scatter(1, 5, marker='^', s=40, color='w',edgecolors='black', label='Jialu River')    
plt.scatter(1, 4, marker='x', s=40, color='k',edgecolors='black', label='Groundwater')  

plt.fill_between([0.98, 0.985], 4, 5, color='#FE0000', label='Dec. 2019')
plt.fill_between([0.99, 0.995], 4, 5, color='#00FE00', label='May. 2020')
plt.fill_between([0.10, 0.105], 4, 5, color='blue', label='Aug. 2020')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0, shadow=True)
    
plt.show()    
plt.savefig('legend.jpg', dpi=1000)
    

    
    
    