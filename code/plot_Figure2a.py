# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:09:29 2024

@author: Jing
"""
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import statannot 
from statannot import add_stat_annotation
import seaborn as sns

#print(np.__version__)         1.23.1
#print(pd.__version__)         2.2.3
#print(statannot.__version__)  0.2.3
#print(sns.__version__)        0.11.0

plt.style.use('default')

palette=['#ff0000', '#00ff00', '#0000ff']

palette=['#ED7D82', '#A3D6AC', '#4494C3']

palette=['#497A90', '#B1B1B1', '#D02C31']

palette=['#E50000', '#FF00FF', 'grey']

palette=['#FE0000', '#00FE00', 'blue']

#palette=['k', 'k', 'k']

dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5

df = pd.concat([dfc1[dfc1['Type']=='SW'],
                dfc2[dfc2['Type']=='SW'], 
                dfc3[dfc3['Type']=='SW']])


df['Mg'].describe()

fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(5, 6), sharey=False, sharex=True)
axes = axes.flatten()


for iplot, par in enumerate(['T', 'pH', 'TDS', 'DO', 'K', 'Na', 'Ca', 'Mg', 'Cl', 'SO4', 'NO3', 'HCO3_mgL_tit', 'D', 'O18_gy', 'S34', 'O18_jz']):
    

    df = pd.concat([dfc1[dfc1['Type']=='SW'][['Camp', par]],
                    dfc2[dfc2['Type']=='SW'][['Camp', par]], 
                    dfc3[dfc3['Type']=='SW'][['Camp', par]]])
    
    
    
       
    sns.boxplot(data=df, x='Camp', y=par, ax=axes[iplot], width=0.4, palette=palette, linewidth=1.0, 
                medianprops=dict(color="k", linewidth=1.5),
                boxprops = dict(linestyle='-', linewidth=1.5, facecolor='w', edgecolor='k'),
                flierprops=dict(linestyle='-', linewidth=1.5),
                whiskerprops=dict(linestyle='-', linewidth=1.5),
                capprops=dict(linestyle='-', linewidth=1.5),
                showfliers=False)
    
    
    axes[iplot].tick_params(axis="y", labelrotation=90)
    
    
    
    
    
    mybox = axes[iplot].patches[0]
    mybox.set_edgecolor(palette[0])
    mybox = axes[iplot].patches[1]
    mybox.set_edgecolor(palette[1])
    mybox = axes[iplot].patches[2]
    mybox.set_edgecolor(palette[2])
    
    myline = axes[iplot].lines[0]
    myline.set_color(palette[0])
    myline = axes[iplot].lines[1]
    myline.set_color(palette[0])
    myline = axes[iplot].lines[2]
    myline.set_color(palette[0])
    myline = axes[iplot].lines[3]
    myline.set_color(palette[0])
    myline = axes[iplot].lines[4]
    myline.set_color(palette[0])
    
    
    myline = axes[iplot].lines[5]
    myline.set_color(palette[1])
    myline = axes[iplot].lines[6]
    myline.set_color(palette[1])
    myline = axes[iplot].lines[7]
    myline.set_color(palette[1])
    myline = axes[iplot].lines[8]
    myline.set_color(palette[1])
    myline = axes[iplot].lines[9]
    myline.set_color(palette[1])
    
    myline = axes[iplot].lines[10]
    myline.set_color(palette[2])
    myline = axes[iplot].lines[11]
    myline.set_color(palette[2])
    myline = axes[iplot].lines[12]
    myline.set_color(palette[2])
    myline = axes[iplot].lines[13]
    myline.set_color(palette[2])
    myline = axes[iplot].lines[14]
    myline.set_color(palette[2])
    
    
    
    for i, w in enumerate([1, 3, 5]):
        yy = df[par][df.Camp==w].dropna()
        # Add some random "jitter" to the x-axis
        xx = np.random.normal(i, 0.04, size=len(yy))
        axes[iplot].scatter(xx, yy, color=palette[i], alpha=0.5, s=4)
        
    add_stat_annotation(axes[iplot], data=df, x='Camp', y=par, order=[1, 3, 5],
                        box_pairs=[(1, 3), (1, 5), (3, 5)],
                        test='t-test_ind', text_format='star', 
                        loc='inside', verbose=2)
    
    axes[iplot].spines[['top', 'right', 'bottom']].set_visible(False)
    
    axes[iplot].plot([0, 1, 2], df.groupby('Camp').median()[par], 'k:', lw=1.5)
    

#axes[0].set_ylabel('Temperature'), axes[0].set_xlabel('')
axes[0].set_title('$Temp.$', fontsize=10)
axes[0].set_ylabel('')
axes[0].set_xlabel('')
axes[0].set_ylim([0, 56])
axes[0].set_yticks([0, 28, 56])
axes[0].xaxis.set_major_locator(plt.NullLocator())


#axes[1].set_ylabel('pH'), axes[1].set_xlabel('')
axes[1].set_title('$pH$', fontsize=10)
axes[1].set_ylabel('')
axes[1].set_xlabel('')
axes[1].set_ylim([7, 11])
axes[1].set_yticks([7, 9, 11])
axes[1].xaxis.set_major_locator(plt.NullLocator())


#axes[2].set_ylabel('TDS'), axes[2].set_xlabel('')
axes[2].set_title('$TDS$', fontsize=10)
axes[2].set_ylabel('')
axes[2].set_xlabel('')
axes[2].set_ylim([0, 1400])
axes[2].set_yticks([0, 700, 1400])
axes[2].xaxis.set_major_locator(plt.NullLocator())



#axes[3].set_ylabel('DO'), axes[3].set_xlabel('')
axes[3].set_title('$DO$', fontsize=10)
axes[3].set_ylabel('')
axes[3].set_xlabel('')
axes[3].set_ylim([0, 54])
axes[3].set_yticks([0, 27, 54])
axes[3].xaxis.set_major_locator(plt.NullLocator())



#axes[4].set_ylabel('K$^+$'), axes[4].set_xlabel('')
axes[4].set_title('$K$$^+$', fontsize=10)
axes[4].set_ylabel('')
axes[4].set_xlabel('')
axes[4].set_ylim([0, 28])
axes[4].set_yticks([0, 14, 28])
axes[4].xaxis.set_major_locator(plt.NullLocator())



#axes[5].set_ylabel('Na$^+$'), axes[5].set_xlabel('')
axes[5].set_title('$Na$$^+$', fontsize=10)
axes[5].set_ylabel('')
axes[5].set_xlabel('')
axes[5].set_ylim([0, 300])
axes[5].set_yticks([0, 150, 300])
axes[5].xaxis.set_major_locator(plt.NullLocator())


#axes[6].set_ylabel('Ca$^{2+}$'), axes[6].set_xlabel('')
axes[6].set_title('$Ca$$^{2+}$', fontsize=10)
axes[6].set_ylabel('')
axes[6].set_xlabel('')
axes[6].set_ylim([0, 200])
axes[6].set_yticks([0, 100, 200])
axes[6].xaxis.set_major_locator(plt.NullLocator())



#axes[7].set_ylabel('Mg$^{2+}$'), axes[7].set_xlabel('')
axes[7].set_title('$Mg$$^{2+}$', fontsize=10)
axes[7].set_ylabel('')
axes[7].set_xlabel('')
axes[7].set_ylim([0, 64])
axes[7].set_yticks([0, 32, 64])
axes[7].xaxis.set_major_locator(plt.NullLocator())


#axes[8].set_ylabel('Cl$^{-}$'), axes[8].set_xlabel('')
axes[8].set_title('$Cl$$^{-}$', fontsize=10)
axes[8].set_ylabel('')
axes[8].set_xlabel('')
axes[8].set_ylim([0, 340])
axes[8].set_yticks([0, 170, 340])
axes[8].xaxis.set_major_locator(plt.NullLocator())


#xes[9].set_ylabel('$SO$$_4^{2-}$'), axes[9].set_xlabel('')
axes[9].set_title('$SO$$_4^{2-}$', fontsize=10)
axes[9].set_ylabel('')
axes[9].set_xlabel('')
axes[9].set_ylim([0, 320])
axes[9].set_yticks([0, 160, 320])
axes[9].xaxis.set_major_locator(plt.NullLocator())


#axes[10].set_ylabel('NO$_3^{-}$'), axes[10].set_xlabel('')
axes[10].set_title('$NO$$_3^{-}$', fontsize=10)
axes[10].set_ylabel('')
axes[10].set_xlabel('')
axes[10].set_ylim([0, 84])
axes[10].set_yticks([0, 42, 84])
axes[10].xaxis.set_major_locator(plt.NullLocator())



#axes[11].set_ylabel('HCO$_3^{-}$'), axes[11].set_xlabel('')
axes[11].set_title('$HCO$$_3^{-}$', fontsize=10)
axes[11].set_ylabel('')
axes[11].set_xlabel('')
axes[11].set_ylim([0, 640])
axes[11].set_yticks([0, 320, 640])
axes[11].xaxis.set_major_locator(plt.NullLocator())


#axes[12].set_ylabel('$\delta^{2}$' + 'H-H$_2$O'), axes[15].set_xlabel('')
axes[12].set_title('$\delta^{2}$' + '$H-H_2O$', fontsize=10)
axes[12].set_ylabel('')
axes[12].set_xlabel('')
axes[12].set_ylim([-70, 14])
axes[12].set_yticks([-70, -28, 14])
axes[12].xaxis.set_major_locator(plt.NullLocator())



#axes[13].set_ylabel('$\delta^{18}$' + 'O-H$_2$O'), axes[14].set_xlabel('')
axes[13].set_title('$\delta^{18}$' + '$O-H_2O$', fontsize=10)
axes[13].set_ylabel('')
axes[13].set_xlabel('')
axes[13].set_ylim([-12, 6])
axes[13].set_yticks([-12, -3, 6])
axes[13].xaxis.set_major_locator(plt.NullLocator())


#axes[14].set_ylabel('$\delta^{34}$' + 'S-SO$_4^{2-}$'), axes[12].set_xlabel('')
axes[14].set_title('$\delta^{34}$' + '$S-SO_4^{2-}$', fontsize=10)
axes[14].set_ylabel('')
axes[14].set_xlabel('')
axes[14].set_ylim([5, 27])
axes[14].set_yticks([5, 16, 27])
axes[14].xaxis.set_major_locator(plt.NullLocator())


#axes[15].set_ylabel('$\delta^{18}$' + 'O-SO$_4^{2-}$'), axes[13].set_xlabel('')
axes[15].set_title('$\delta^{18}$' + '$O-SO_4^{2-}$', fontsize=10)
axes[15].set_ylabel('')
axes[15].set_xlabel('')
axes[15].set_ylim([-5, 35])
axes[15].set_yticks([-5, 15, 35])
axes[15].xaxis.set_major_locator(plt.NullLocator())


axes[12].set_xticks([0, 1, 2], ['Dec.', 'May.', 'Aug.'], rotation=90)
axes[13].set_xticks([0, 1, 2], ['Dec.', 'May.', 'Aug.'], rotation=90)
axes[14].set_xticks([0, 1, 2], ['Dec.', 'May.', 'Aug.'], rotation=90)
axes[15].set_xticks([0, 1, 2], ['Dec.', 'May.', 'Aug.'], rotation=90)

for i in range(12):
    axes[i].xaxis.get_major_ticks()[0].tick1line.set_markeredgewidth(0)
    axes[i].xaxis.get_major_ticks()[1].tick1line.set_markeredgewidth(0)
    axes[i].xaxis.get_major_ticks()[2].tick1line.set_markeredgewidth(0)



plt.suptitle('(a) Temporal variation across campaigns', fontsize=11)
    
plt.subplots_adjust(hspace=0.5, wspace=0.4)

#lt.savefig('(a) Temporal variation of river water.jpg', dpi=300)