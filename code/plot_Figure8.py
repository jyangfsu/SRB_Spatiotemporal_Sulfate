# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:10:27 2024

@author: Jing
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import pandas as pd

import seaborn as sns

plt.style.use('default')

# Load data
dfs = {
    'Dec 2019': (pd.read_csv('../data/data_122019.csv'), '#FE0000'),
    'May 2020': (pd.read_csv('../data/data_052020.csv'), '#00FE00'), 
    'Aug 2020': (pd.read_csv('../data/data_082020.csv'), 'blue')
}

# Set up figure
fig = plt.figure(figsize=(4, 4))

# First subplot - Source boundaries
ax1 = fig.add_subplot(111)

# Define source regions
source_regions = {
    'AD': {'rect': (-3, 7, 12, 10), 'color': '#B5FFFF', 'text': (-2, 12)},
    'SS': {'rect': (1.3, 0.8, 2.9, 5.6), 'color': '#CEF784', 'text': (2.8, 5)},
    'EV': {'rect': (14, 9.1, 21, 8.5), 'color': '#DCDEFF', 'text': (17, 13.35)},
    'SE': {'rect': (3, 8.2, 9.5, 4.3), 'color': '#DCDCD6', 'text': (5, 10.35)},
    'CF': {'rect': (-3.2, 7.7, 16.2, 7.8), 'color': 'none', 'text': (12, 14), 'edgecolor': 'k', 'linestyle': '--', 'lw': 1},
    'OS': {'rect': (-15, -5, 19, 9), 'color': '#B56BFF', 'text': (-0.5, -0.5)}
}

# Add source region rectangles
for name, props in source_regions.items():
    rect = Rectangle(props['rect'][:2], props['rect'][2], props['rect'][3],
                    facecolor=props['color'], edgecolor=props.get('edgecolor', 'none'),
                    label=name, alpha=0.8, linestyle=props.get('linestyle', '-.'),
                    lw=props.get('lw', 1.25), zorder=props.get('zorder', 0))
    if name == "SS":
        rect = Rectangle(props['rect'][:2], props['rect'][2], props['rect'][3],
                        facecolor=props['color'], edgecolor=props.get('edgecolor', 'none'),
                        label=name, alpha=0.8, linestyle=props.get('linestyle', '-.'),
                        lw=props.get('lw', 1.25), zorder=props.get('zorder', 500))
    ax1.add_patch(rect)
    
    ax1.text(*props['text'], name, fontsize=10, fontname='cursive', color='k',
              ha='center', va='center', zorder=500)

# Set up axes
ax1.plot([-5, 20], [20, 20], zorder=2000, color='k')
ax1.set(xlim=[-5, 20], ylim=[-5, 20],
        xlabel='$\delta$$^{34}S-SO_4^{2-}$ [‰]',
        ylabel='$\delta$$^{18}O-SO_4^{2-}$ [‰]')
ax1.zorder = 2000

# Define river markers
river_markers = {
    'Huai River': 's',
    'Lower reaches': 'o', 
    'Middle reaches': '*',
    'Sha River': 'v',
    'Ying River': 'D',
    'Jialu River': '^',
    'GW': 'X'
}

# Plot data for both subplots
for period, (df, color) in dfs.items():
    # Process dataframe
    df['Sample'] = df['ID']
    df['Label'] = df['River']
    df['HCO3'] = df['HCO3_mgL_tit']
    df['CO3'] = 0
    df['Alpha'] = 0.6
    
    for river, marker in river_markers.items():
        mask = df['River'] == river
        df.loc[mask, ['Color', 'Marker', 'Size']] = [color, marker, 40]
    
    # Plot on first subplot
    for i in range(df.shape[0]):
        ax1.scatter(df.loc[i, 'S34'], df.loc[i, 'O18_jz'],
                    marker=df.loc[i, 'Marker'], s=40, color=df.loc[i, 'Color'],
                    alpha=0.6, edgecolors='black', zorder=1000)

# Load data
dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5

# Add a subplot at the specified position and size 
left, bottom, width, height = 0.95, 0.107, 0.2, 0.78
axr = fig.add_axes([left, bottom, width, height])  
#axr.set_yscale('log')
axr.set_ylim([-5, 20])

# Plot some data in the subplot  
palette=['#FE0000', '#00FE00', 'blue']
par = 'O18_jz'

df = pd.concat([dfc1[['Camp', par]],
                dfc2[['Camp', par]], 
                dfc3[['Camp', par]]])
    
    
#violinplot
sns.boxplot(data=df, x='Camp', y=par, ax=axr, width=0.4, palette=palette, linewidth=1.0, 
            medianprops=dict(color="k", linewidth=1),
            boxprops = dict(linestyle='-', linewidth=1, facecolor='w', edgecolor='k'),
            flierprops=dict(linestyle='-', linewidth=1),
            whiskerprops=dict(linestyle='-', linewidth=1),
            capprops=dict(linestyle='-', linewidth=1),
            showfliers=False)
 
for i, w in enumerate([1, 3, 5]):
    yy = df[par][df.Camp==w].dropna()
    # Add some random "jitter" to the x-axis
    xx = np.random.normal(i, 0.04, size=len(yy))
    axr.scatter(xx, yy, color=palette[i], alpha=0.5, s=4)

# from statannot import add_stat_annotation    
# add_stat_annotation(axr, data=df, x='Camp', y=par, order=[1, 3, 5],
#                     box_pairs=[(1, 3), (1, 5), (3, 5)],
#                     test='t-test_ind', text_format='star', 
#                     loc='inside', verbose=2)

#axins.invert_xaxis()    

#axr.set_yticks([1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1])
axr.set_yticklabels(['', '', '', '', '', ''])
axr.set_ylabel('')

axr.set_xticklabels(['', '', ''])
axr.set_xlabel('')
 

##############################################
# Add a subplot at the specified position and size 
left, bottom, width, height = 0.12, 0.95, 0.78, 0.2
axt = fig.add_axes([left, bottom, width, height])  
#axt.set_xscale('log')
axt.set_xlim([1e-2, 10])

# Plot some data in the subplot  
palette=['#FE0000', '#00FE00', 'blue']
par = 'S34'

df = pd.concat([dfc1[['Camp', par]],
                dfc2[['Camp', par]], 
                dfc3[['Camp', par]]])


#violinplot
sns.boxplot(data=df, y='Camp', x=par, ax=axt, width=0.4, palette=palette, linewidth=1.0, orient="h",
            medianprops=dict(color="k", linewidth=1),
            boxprops = dict(linestyle='-', linewidth=1, facecolor='w', edgecolor='k'),
            flierprops=dict(linestyle='-', linewidth=1),
            whiskerprops=dict(linestyle='-', linewidth=1),
            capprops=dict(linestyle='-', linewidth=1),
            showfliers= False)

for i, w in enumerate([1, 3, 5]):
    yy = df[par][df.Camp==w].dropna()
    # Add some random "jitter" to the x-axis
    xx = np.random.normal(i, 0.04, size=len(yy))
    axt.scatter(yy, xx, color=palette[i], alpha=0.5, s=4)

'''
add_stat_annotation(axt, data=df, x='Camp', y=par, order=[1, 3, 5],
                    box_pairs=[(1, 3), (1, 5), (3, 5)],
                    test='t-test_ind', text_format='star', 
                    loc='inside', verbose=2)

'''


#axt.set_xticks([1e-2, 1e-1, 1e0, 1e1])
axt.set_xticklabels(['', '', '', ''])
axt.set_xlim([-5, 20])
axt.set_xlabel('')

axt.set_yticklabels(['', '', ''])
axt.set_ylabel('')

ax1.text(-3.75, 18,  '(a)', fontsize=12)


plt.savefig('Fig8a.jpg', dpi=600, bbox_inches='tight')

# Set up figure
fig = plt.figure(figsize=(4, 4))

# First subplot - Source boundaries
ax2 = fig.add_subplot(111)


# Plot data points
for period, (df, color) in dfs.items():
    for i in range(df.shape[0]):
        ax2.scatter(df.loc[i, 'O18_gy'],df.loc[i, 'O18_jz'],
                    marker=df.loc[i, 'Marker'], s=40, color=df.loc[i, 'Color'],
                    alpha=0.6, edgecolors='black')

# Plot mixing lines
E_O2, E_H2O = -11.2, 4.0
delta_O18_O2 = 23.8
x = np.linspace(-12, -2, 100)

for ratio in [0, 0.25, 0.50, 0.75, 1.00]:
    y = ratio * (x + E_H2O) + (1 - ratio) * (delta_O18_O2 + E_O2)
    ax2.plot(x, y, 'k--', lw=1)

# Add text labels
text_positions = {
    '0% $H_2O$': (-4.05, 13, 0),
    '100%': (-3.5, 1.1, 20),
    '75%': (-3.2, 4.2, 15),
    '50%': (-3.2, 7.0, 10),
    '25%': (-3.2, 10, 5)
}

for label, (x, y, rot) in text_positions.items():
    ax2.text(x, y, label, rotation=rot)

# Add shaded regions
ratios = [0, 0.25, 0.50, 0.75, 1.00]
alphas = [0.05, 0.10, 0.20, 0.25]
x = np.linspace(-12, -2, 100)
for i in range(len(ratios)-1):
    y1 = ratios[i] * (x + E_H2O) + (1 - ratios[i]) * (delta_O18_O2 + E_O2)
    y2 = ratios[i+1] * (x + E_H2O) + (1 - ratios[i+1]) * (delta_O18_O2 + E_O2)
    ax2.fill_between(x, y1, y2, color='grey', alpha=alphas[i], zorder=-100)

# Set up axes
ax2.set(xlim=[-12, -2], ylim=[-5, 20],
        xlabel='$\delta$$^{18}O-H_2O$ [‰]',
        ylabel='')
ax2.set_yticks([])
ax2.set_axisbelow(False)

'''  
# Add a subplot at the specified position and size 
left, bottom, width, height = 0.95, 0.107, 0.2, 0.78
axr = fig.add_axes([left, bottom, width, height])  
#axr.set_yscale('log')
axr.set_ylim([-5, 20])

# Plot some data in the subplot  
palette=['#FE0000', '#00FE00', 'blue']
par = 'O18_jz'

df = pd.concat([dfc1[['Camp', par]],
                dfc2[['Camp', par]], 
                dfc3[['Camp', par]]])
    

#violinplot
sns.boxplot(data=df, x='Camp', y=par, ax=axr, width=0.4, palette=palette, linewidth=1.0, 
            medianprops=dict(color="k", linewidth=1),
            boxprops = dict(linestyle='-', linewidth=1, facecolor='w', edgecolor='k'),
            flierprops=dict(linestyle='-', linewidth=1),
            whiskerprops=dict(linestyle='-', linewidth=1),
            capprops=dict(linestyle='-', linewidth=1),
            showfliers=False)
 
for i, w in enumerate([1, 3, 5]):
    yy = df[par][df.Camp==w].dropna()
    # Add some random "jitter" to the x-axis
    xx = np.random.normal(i, 0.04, size=len(yy))
    axr.scatter(xx, yy, color=palette[i], alpha=0.5, s=4)

# from statannot import add_stat_annotation    
# add_stat_annotation(axr, data=df, x='Camp', y=par, order=[1, 3, 5],
#                     box_pairs=[(1, 3), (1, 5), (3, 5)],
#                     test='t-test_ind', text_format='star', 
#                     loc='inside', verbose=2)

#axins.invert_xaxis()    

#axr.set_yticks([1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1])
axr.set_yticklabels(['', '', '', '', '', ''])
axr.set_ylabel('')

axr.set_xticklabels(['', '', ''])
axr.set_xlabel('')
 '''


##############################################
# Add a subplot at the specified position and size 
left, bottom, width, height = 0.12, 0.95, 0.78, 0.2
axt = fig.add_axes([left, bottom, width, height])  
#axt.set_xscale('log')
axt.set_xlim([-12, 2])

# Plot some data in the subplot  
palette=['#FE0000', '#00FE00', 'blue']
par = 'O18_gy'

df = pd.concat([dfc1[['Camp', par]],
                dfc2[['Camp', par]], 
                dfc3[['Camp', par]]])


#violinplot
sns.boxplot(data=df, y='Camp', x=par, ax=axt, width=0.4, palette=palette, linewidth=1.0, orient="h",
            medianprops=dict(color="k", linewidth=1),
            boxprops = dict(linestyle='-', linewidth=1, facecolor='w', edgecolor='k'),
            flierprops=dict(linestyle='-', linewidth=1),
            whiskerprops=dict(linestyle='-', linewidth=1),
            capprops=dict(linestyle='-', linewidth=1),
            showfliers=False)

for i, w in enumerate([1, 3, 5]):
    yy = df[par][df.Camp==w].dropna()
    # Add some random "jitter" to the x-axis
    xx = np.random.normal(i, 0.04, size=len(yy))
    axt.scatter(yy, xx, color=palette[i], alpha=0.5, s=4)


# add_stat_annotation(axt, data=df, x='Camp', y=par, order=[1, 3, 5],
#                     box_pairs=[(1, 3), (1, 5), (3, 5)],
#                     test='t-test_ind', text_format='star', 
#                     loc='inside', verbose=2)



#axt.set_xticks([1e-2, 1e-1, 1e0, 1e1])
axt.set_xticklabels(['', '', '', ''])
axt.set_xlim([-12, 2])
axt.set_xlabel('')

axt.set_yticklabels(['', '', ''])
axt.set_ylabel('')




# Add legend
legend_markers = {
    'Huai River': 's',
    'Lower reaches': 'o',
    'Middle reaches': '*',
    'Sha River': 'v', 
    'Ying River': 'D',
    'Jialu River': '^',
    'Groundwater': 'x'
}

for label, marker in legend_markers.items():
    color = 'k' if label == 'Groundwater' else 'w'
    size = 70 if label == 'Middle reaches' else 40
    ax2.scatter(90, 10-list(legend_markers.keys()).index(label),
                marker=marker, s=size, color=color, edgecolors='black', label=label)

# Add period indicators
period_colors = {
    'Dec. 2019': '#FE0000',
    'May. 2020': '#00FE00', 
    'Aug. 2020': 'blue'
}

for i, (period, color) in enumerate(period_colors.items()):
    ax2.fill_between([90.98+0.01*i, 90.985+0.01*i], 4, 5, color=color, label=period)

ax2.text(-11.5, 18,  '(b)', fontsize=12)



ax2.legend(bbox_to_anchor=(1.05, 1.01), loc=2, borderaxespad=0, shadow=True)

plt.show()
plt.savefig('Fig8b.jpg', dpi=600, bbox_inches='tight')