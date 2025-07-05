# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 15:03:48 2025

@author: Jing
"""
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

from statannot import add_stat_annotation
import seaborn as sns

plt.style.use('default')

row_height = 0.0060125060125060135
row_width = 0.01855958364616585
sources = ['AD', 'CF', 'EV', 'OS', 'SE', 'SS']

dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5

df = pd.concat([dfc1, dfc2, dfc3])

mean_SO4_Dec_sw = dfc1[dfc1['Type']=='SW']['SO4'].describe()['mean']
mean_SO4_May_sw = dfc2[dfc2['Type']=='SW']['SO4'].describe()['mean']
mean_SO4_Aug_sw = dfc3[dfc3['Type']=='SW']['SO4'].describe()['mean']
mean_SO4_sw = df[df['Type']=='SW']['SO4'].describe()['mean']


df_Dec_sw = pd.read_csv('../results/MixSIAR_input_outputs/mix_data_Dec_sw_out.csv')
df_May_sw = pd.read_csv('../results/MixSIAR_input_outputs/mix_data_May_sw_out.csv')
df_Aug_sw = pd.read_csv('../results/MixSIAR_input_outputs/mix_data_Aug_sw_out.csv')

df_Dec_sw = df_Dec_sw.rename(columns={'V1': 'AD', 
                                      'V2': 'CF',
                                      'V3': 'EV', 
                                      'V4': 'OS',
                                      'V5': 'SE', 
                                      'V6': 'SS'})  
df_May_sw = df_May_sw.rename(columns={'V1': 'AD', 
                                      'V2': 'CF',
                                      'V3': 'EV', 
                                      'V4': 'OS',
                                      'V5': 'SE', 
                                      'V6': 'SS'})  
df_Aug_sw = df_Aug_sw.rename(columns={'V1': 'AD', 
                                      'V2': 'CF',
                                      'V3': 'EV', 
                                      'V4': 'OS',
                                      'V5': 'SE', 
                                      'V6': 'SS'})  

# http://www.hrc.gov.cn/swj/lysstb/index_3.jhtml, from Nov 2019 to Oct 2020 , unit m3/s
fuyang_flow_rate = [3.32, 0, 15.7, 16.2, 43.5, 25.6, 16.2, 45.7, 433, 309, 65.9, 48]


# http://www.hnssw.com.cn/sqwater1/27708.jhtml, from Nov 2019 to Oct 2020 , unit m3/s
luohe_flow_rate = [3.23, 3.69, 6.6, 19, 5.88, 4.78, 6, 55.7,  85.9,  62.1, 26.6, 19.2]


# http://yc.wswj.net/swjmh/todayWaterPub.html，from Nov 2019 to Oct 2020 , unit m3/s
# Dicharge of Nov. 2019 and Dec. 2019 were not available. The two vlaues were replacted with Nov. 2020 and Dec. 2020 corrected by the rainfall.
#zhoukou_flow_rate = [5.19, 36.12, 36.85, 28.03, 40.28, 32.06, 41.56, 75.46,  124.83,  99.59, 46.76, 52.58]


# Data for these two stations were not available
# huangqiao_flow_rate = 
# fugou_flow_rate = 

plt.plot(range(12), luohe_flow_rate, label="Luohe")
#plt.plot(range(12), zhoukou_flow_rate, label="Zhoukou")
plt.plot(range(12), fuyang_flow_rate, label="Fuyang")


plt.xticks(np.arange(12), ['19-N', '19-D', '20-J','20-F','20-M','20-A','20-M','20-J','20-J','20-A','20-S','20-O'])
plt.ylim([0, 500])
plt.legend()
plt.show()


fuyang_dry_flow = fuyang_flow_rate[0] * 3600 * 24 * 30 + fuyang_flow_rate[1] * 3600 * 24 * 31 + fuyang_flow_rate[2] * 3600 * 24 * 31 + fuyang_flow_rate[3] * 3600 * 24 * 29 
fuyang_nor_flow = fuyang_flow_rate[4] * 3600 * 24 * 31 + fuyang_flow_rate[5] * 3600 * 24 * 30 + fuyang_flow_rate[6] * 3600 * 24 * 31 + fuyang_flow_rate[11] * 3600 * 24 * 31 
fuyang_wet_flow = fuyang_flow_rate[7] * 3600 * 24 * 30 + fuyang_flow_rate[8] * 3600 * 24 * 31 + fuyang_flow_rate[9] * 3600 * 24 * 31 +  fuyang_flow_rate[10] * 3600 * 24 * 30


print('unit: m3')
print('fuyang_dry_flow', fuyang_dry_flow)
print('fuyang_nor_flow', fuyang_nor_flow)
print('fuyang_wet_flow', fuyang_wet_flow)
print('fuyang_total_flow', fuyang_dry_flow + fuyang_nor_flow + fuyang_wet_flow)

print('unit: mmol/L')
print('mean_SO4_Dec_sw', mean_SO4_Dec_sw/96)
print('mean_SO4_May_sw', mean_SO4_May_sw/96)
print('mean_SO4_Aug_sw', mean_SO4_Aug_sw/96)
print('mean_SO4_sw', mean_SO4_sw/96)

# mean_SO4_Dec_sw in mg/L, fuyang_dry_flow in m3
sc_Dec_sw = []
for sc in sources:
    print(sc, mean_SO4_Dec_sw * fuyang_dry_flow * df_Dec_sw[sc].describe()['mean'] / 96 / 1e6)
    sc_Dec_sw.append(mean_SO4_Dec_sw * fuyang_dry_flow * df_Dec_sw[sc].describe()['mean'] / 96 / 1e6)
    
print("Total", mean_SO4_Dec_sw * fuyang_dry_flow / 96 / 1e6)
print("unit: million mole")


# mean_SO4_Dec_sw in mg/L, uyang_dry_flow in m3
sc_May_sw = []
for sc in sources:
    print(sc, mean_SO4_May_sw * fuyang_nor_flow * df_May_sw[sc].describe()['mean'] / 96 / 1e6)
    sc_May_sw.append(mean_SO4_May_sw * fuyang_nor_flow * df_May_sw[sc].describe()['mean'] / 96 / 1e6)
print("Total", mean_SO4_May_sw * fuyang_nor_flow / 96 / 1e6)
print("unit: million mole")


# mean_SO4_Dec_sw in mg/L, uyang_dry_flow in m3
sc_Aug_sw = []
for sc in sources:
    print(sc, mean_SO4_Aug_sw * fuyang_wet_flow * df_Aug_sw[sc].describe()['mean'] / 96 / 1e6)
    sc_Aug_sw.append(mean_SO4_Aug_sw * fuyang_wet_flow * df_Aug_sw[sc].describe()['mean'] / 96 / 1e6)
print("Total", mean_SO4_Aug_sw * fuyang_wet_flow / 96 / 1e6)
print("unit: million mole")

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Data from the table
columns = ("Dry season", "Normal season", "Wet season", "A water year")
rows = [
    "River flow ($10^6$m$^3$)",
    "Mean SO₄²⁻ (mmol/L)",
    "AD ($10^6$mol)",
    "CF ($10^6$mol)",
    "EV ($10^6$mol)",
    "OS ($10^6$mol)",
    "SE ($10^6$mol)",
    "SS ($10^6$mol)",
    "Total SO₄²⁻ flux ($10^6$mol)"
]

data = [
    [91.25, 354.82, 2276.64, 2722.71],
    [1.01, 0.97, 0.74, 0.91],
    [1.75, 46.44, 34.05, 82.24],
    [1.43, 49.94, 30.57, 81.94],
    [54.99, 64.61, 825.26, 944.86],
    [30.07, 21.78, 694.77, 746.62],
    [2.28, 149.97, 45.51, 197.76],
    [1.92, 10.62, 42.75, 55.29],
    [92.44, 343.36, 1673.65, 2109.45]
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size for better width and height balance
ax.axis('off')
ax.axis('tight')

# Define color normalization separately for each column with lighter colormaps
colormaps = [plt.cm.GnBu, plt.cm.BuGn, plt.cm.YlOrBr, plt.cm.BuPu]
cell_colors = []

for i in range(len(rows)):
    row_colors = []
    for j in range(len(columns)):
        if i in range(2, 8) and j in range(4):  # Highlight rows AD, CF, EV, OS, SE, SS and columns Dry, Normal, Wet seasons
            norm = mcolors.Normalize(vmin=np.min([row[j] for row in data[2:8]]), vmax=np.max([row[j] for row in data[2:8]]))
            norm = mcolors.Normalize(vmin=np.min([row[j] for row in data[2:8]]), vmax=np.max([row[j] for row in data[2:8]]) * 2)
            row_colors.append(colormaps[j](norm(data[i][j])))
        else:
            row_colors.append('white')
    cell_colors.append(row_colors)

# Create table with adjusted row and column sizes
table = ax.table(cellText=data,
                 rowLabels=rows,
                 colLabels=columns,
                 cellColours=cell_colors,
                 alpha=0.1,
                 cellLoc='center',
                 loc='center')

# Set table properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(0.675, 1.5)  # Adjusted scaling for better readability and spacing

# Set title
#plt.title("(b) Seasonal Sulfate Flux at Fuyang", fontsize=14, weight='bold')
plt.text(-0.073, 0.0332, "(b) Seasonal Sulfate Flux at Fuyang", fontsize=14, weight='bold')

plt.savefig('Fig10b.jpg', dpi=600, bbox_inches='tight')

# Display the table
plt.show()


luohe_dry_flow = luohe_flow_rate[0] * 3600 * 24 * 30 + luohe_flow_rate[1] * 3600 * 24 * 31 + luohe_flow_rate[2] * 3600 * 24 * 31 + luohe_flow_rate[3] * 3600 * 24 * 29 
luohe_nor_flow = luohe_flow_rate[4] * 3600 * 24 * 31 + luohe_flow_rate[5] * 3600 * 24 * 30 + luohe_flow_rate[6] * 3600 * 24 * 31 + luohe_flow_rate[11] * 3600 * 24 * 31 
luohe_wet_flow = luohe_flow_rate[7] * 3600 * 24 * 30 + luohe_flow_rate[8] * 3600 * 24 * 31 + luohe_flow_rate[9] * 3600 * 24 * 31 +  luohe_flow_rate[10] * 3600 * 24 * 30

print('unit: m3')
print('luohe_dry_flow', luohe_dry_flow)
print('luohe_nor_flow', luohe_nor_flow)
print('luohe_wet_flow', luohe_wet_flow)
print('luohe_total_flow', luohe_dry_flow + luohe_nor_flow + luohe_wet_flow)


mean_SO4_Dec_sw_u_Sha = dfc1[dfc1['River']=='Sha River']['SO4'].describe()['mean']
mean_SO4_May_sw_u_Sha = dfc2[dfc2['River']=='Sha River']['SO4'].describe()['mean']
mean_SO4_Aug_sw_u_Sha = dfc3[dfc3['River']=='Sha River']['SO4'].describe()['mean']
mean_SO4_sw_u_Sha = df[df['River']=='Sha River']['SO4'].describe()['mean']


print('unit: mmol/L')
print('mean_SO4_Dec_sw', mean_SO4_Dec_sw_u_Sha/96)
print('mean_SO4_May_sw', mean_SO4_May_sw_u_Sha/96)
print('mean_SO4_Aug_sw', mean_SO4_Aug_sw_u_Sha/96)
print('mean_SO4_sw', mean_SO4_sw_u_Sha/96)

df_Dec_sw_u_Sha = pd.read_csv('../results/MixSIAR_input_outputs/mix_data_Dec_sw_upper_Sha_out.csv')
df_May_sw_u_Sha = pd.read_csv('../results/MixSIAR_input_outputs/mix_data_May_sw_upper_Sha_out.csv')
df_Aug_sw_u_Sha = pd.read_csv('../results/MixSIAR_input_outputs/mix_data_Aug_sw_upper_Sha_out.csv')

df_Dec_sw_u_Sha = df_Dec_sw_u_Sha.rename(columns={'V1': 'AD', 
                                      'V2': 'CF',
                                      'V3': 'EV', 
                                      'V4': 'OS',
                                      'V5': 'SE', 
                                      'V6': 'SS'})  
df_May_sw_u_Sha = df_May_sw_u_Sha.rename(columns={'V1': 'AD', 
                                      'V2': 'CF',
                                      'V3': 'EV', 
                                      'V4': 'OS',
                                      'V5': 'SE', 
                                      'V6': 'SS'})  
df_Aug_sw_u_Sha = df_Aug_sw_u_Sha.rename(columns={'V1': 'AD', 
                                      'V2': 'CF',
                                      'V3': 'EV', 
                                      'V4': 'OS',
                                      'V5': 'SE', 
                                      'V6': 'SS'})  

# mean_SO4_Dec_sw in mg/L, uyang_dry_flow in m3
sc_Dec_sw_u_Sha = []
for sc in sources:
    print(sc, mean_SO4_Dec_sw_u_Sha * luohe_dry_flow * df_Dec_sw_u_Sha[sc].describe()['mean'] / 96 / 1e6)
    sc_Dec_sw_u_Sha.append(mean_SO4_Dec_sw_u_Sha * luohe_dry_flow * df_Dec_sw_u_Sha[sc].describe()['mean'] / 96 / 1e6)
print("Total", mean_SO4_Dec_sw_u_Sha * luohe_dry_flow / 96 / 1e6)
print("unit: million mole")


# mean_SO4_Dec_sw in mg/L, uyang_dry_flow in m3
sc_May_sw_u_Sha = []
for sc in sources:
    print(sc, mean_SO4_May_sw_u_Sha * luohe_nor_flow * df_May_sw_u_Sha[sc].describe()['mean'] / 96 / 1e6)
    sc_May_sw_u_Sha.append(mean_SO4_May_sw_u_Sha * luohe_nor_flow * df_May_sw_u_Sha[sc].describe()['mean'] / 96 / 1e6)
print("Total", mean_SO4_May_sw_u_Sha * luohe_nor_flow / 96 / 1e6)
print("unit: million mole")

# mean_SO4_Dec_sw in mg/L, uyang_dry_flow in m3
sc_Aug_sw_u_Sha = []
for sc in sources:
    print(sc, mean_SO4_Aug_sw_u_Sha * luohe_wet_flow * df_Aug_sw_u_Sha[sc].describe()['mean'] / 96 / 1e6)
    sc_Aug_sw_u_Sha.append(mean_SO4_Aug_sw_u_Sha * luohe_wet_flow * df_Aug_sw_u_Sha[sc].describe()['mean'] / 96 / 1e6)
print("Total", mean_SO4_Aug_sw_u_Sha * luohe_wet_flow / 96 / 1e6)
print("unit: million mole")

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Data from the table
columns = ("Dry season", "Normal season", "Wet season", "A water year")
rows = [
    "River flow ($10^6$m$^3$)",
    "Mean SO₄²⁻ (mmol/L)",
    "AD ($10^6$mol)",
    "CF ($10^6$mol)",
    "EV ($10^6$mol)",
    "OS ($10^6$mol)",
    "SE ($10^6$mol)",
    "SS ($10^6$mol)",
    "Total SO₄²⁻ flux ($10^6$mol)"
]


data = [
    [83.54, 95.63, 609.72, 788.89],
    [0.96, 0.88, 0.67, 0.84],
    [3.5,7.20, 23.2, 33.9],
    [3.03, 6.40, 19.61, 29.04],
    [48.35, 46.93, 173.64, 268.92],
    [16.81, 6.65, 132.12, 155.58],
    [4.53, 9.6, 29.12, 43.25],
    [4.37, 6.9, 28.32, 39.53],
    [80.59, 83.68, 406.01, 570.28]
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size for better width and height balance
ax.axis('off')
ax.axis('tight')

# Define color normalization separately for each column with lighter colormaps
colormaps = [plt.cm.GnBu, plt.cm.BuGn, plt.cm.YlOrBr, plt.cm.BuPu]
cell_colors = []


for i in range(len(rows)):
    row_colors = []
    for j in range(len(columns)):
        if i in range(2, 8) and j in range(4):  # Highlight rows AD, CF, EV, OS, SE, SS and columns Dry, Normal, Wet seasons
            norm = mcolors.Normalize(vmin=np.min([row[j] for row in data[2:8]]), vmax=np.max([row[j] for row in data[2:8]]) * 2)
            row_colors.append(colormaps[j](norm(data[i][j])))
        else:
            row_colors.append('white')
    cell_colors.append(row_colors)

# Create table with adjusted row and column sizes
table = ax.table(cellText=data,
                 rowLabels=rows,
                 colLabels=columns,
                 cellColours=cell_colors,
                 alpha=0.1,
                 cellLoc='center',
                 loc='center')

cell_xs=[-2 * row_width, -row_width, 0, row_width, 2*row_width]
cell_ys=[1 * row_height, 0, -row_height,  -2*row_height, -3*row_height, -4*row_height, -5*row_height]




# Set table properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(0.675, 1.5)  # Adjusted scaling for better readability and spacing

# Set title
#plt.title("(a) Seasonal Sulfate Flux at Luohe", fontsize=14, weight='bold')

plt.text(-0.073, 0.0332, "(a) Seasonal Sulfate Flux at Luohe", fontsize=14, weight='bold')

plt.savefig('Fig10a.jpg', dpi=600, bbox_inches='tight')
# Display the table
plt.show()