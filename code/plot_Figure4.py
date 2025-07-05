# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:17:00 2024

@author: Jing
"""
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)


plt.style.use('default')
dfc1 = pd.read_csv('../data/data_122019.csv')
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc3 = pd.read_csv('../data/data_082020.csv')

fig = plt.figure(figsize=(8, 7.5))


ax1 = fig.add_subplot(221)

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
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS', 'O18_gy', 'D']]
   
    df['Alpha'] = 0.6


    Labels = []
    for i in range(len(df)):
        
            x = df.at[i, 'O18_gy']   
            y = df.at[i, 'D']   
            
            ax1.scatter(x, y, 
                        marker=df.at[i, 'Marker'],
                        s=df.at[i, 'Size'], 
                        color=df.at[i, 'Color'], 
                        alpha=df.at[i, 'Alpha'],
                        #label=TmpLabel, 
                        edgecolors='black') 
            
ax1.set_xlim([-11, -3])
ax1.set_ylim([-75, -25])

#plt.minorticks_on()
ax1.set_xlabel('$\delta$$O^{18}_  -{H_2O}$ [‰]')
ax1.set_ylabel('$\delta$$D_  -{H_2O}$ [‰]')

x = np.arange(-11, -3, 0.01)
y = 8 * x + 10
ax1.plot(x, y, color='k', lw=1)

ax1.fill_between(x, np.zeros_like(x) * -75, y, 
                 color=(0.8, 0.8, 0.8), zorder=-100)

            
x = np.arange(-11, -3, 0.01)
y = 6.8 * x -2.7
ax1.plot(x, y, color='k', lw=1, linestyle='--')      






ax1.annotate('GMWL:                    \n$\delta$D=8x$\delta$$^{18}O+10$      ', 
             xy=(-6.3, -41), xytext=(-7.3, -34), ha='center',
        xycoords='data',
        arrowprops=dict(arrowstyle = "->", facecolor='black'))

ax1.annotate('LMWL:                        \n$\delta$D=6.8x$\delta$$^{18}O-2.7$      ', 
             xy=(-7.5, -55.5), xytext=(-8.8, -45.5), ha='center',
            xycoords='data',
            arrowprops=dict(arrowstyle = "->", facecolor='black'))








#################################################################
ax2 = fig.add_subplot(222)

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
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS', 'O18_gy', 'D', 'dexcess']]
   
    df['Alpha'] = 0.6
    
    
    
   

    Labels = []
    for i in range(len(df)):
        
            x = df.at[i, 'dexcess']   
            y = df.at[i, 'TDS']   
            
            ax2.scatter(x, y, 
                        marker=df.at[i, 'Marker'],
                        s=df.at[i, 'Size'], 
                        color=df.at[i, 'Color'], 
                        alpha=df.at[i, 'Alpha'],
                        #label=TmpLabel, 
                        edgecolors='black') 
            
            
ax2.text(-1, 330, '37')      

ax2.arrow(0.5, 350, 3, 0) 
ax2.arrow(-1.5, 350, -3.5, 60) 


ax2.text(6.5, 120, '27')      
ax2.arrow(7.5, 110, 2, -10) 
ax2.arrow(6.0, 130, -3, 10) 
ax2.arrow(7, 140, 2, 30) 


ax2.arrow(9.5, 190, -0.5, 20) 
ax2.arrow(8.0, 230, 0.5, 0) 

ax2.text(11.8, 300, '37') 
ax2.text(12.5, 140, ' 31') 
ax2.text(8.5, 210, '31') 


ax2.annotate('',
             xy=(10, 1800), xycoords='data',
             xytext=(0, -185), textcoords='offset points',
             size=40, zorder=0,
             # bbox=dict(boxstyle="round", fc="0.8"),
             arrowprops=dict(arrowstyle="fancy",
                             fc="#00774B", ec="none", alpha=0.5,
                             connectionstyle="arc3, rad=0.0"))



ax2.annotate('',
             xy=(-5, 1800), xycoords='data',
             xytext=(150, -185), textcoords='offset points',
             size=40, zorder=-100,
             # bbox=dict(boxstyle="round", fc="0.8"),
             arrowprops=dict(arrowstyle="fancy", shrinkA=5,
                             fc="#CE3301", ec="none", alpha=0.5,
                             connectionstyle="arc3, rad=0.01"))





 
 
 
# for i in range(53):
#      plt.text(df.loc[i, 'dexcess'], df.loc[i, 'TDS'], df.loc[i,'ID'].split('-')[1],
#                  ha='center', va='bottom', fontsize=6)
       
ax2.set_yscale('log')
    
    
ax2.set_xlim([-6, 14])
ax2.set_ylim([80, 1800])

ax2.plot([10, 10], [80, 1800], 'k--', lw=1)

ax2.fill_between([10, 14], 80, 1800, 
                 color=(0.8, 0.8, 0.8), zorder=-10000)


ax2.annotate('',
             xy=(0, 220), xycoords='data',
             xytext=(100, -25), textcoords='offset points',
             size=8, zorder=000,
             # bbox=dict(boxstyle="round", fc="0.8"),
             arrowprops=dict(arrowstyle="simple, head_length=1, head_width=0.75",
                             fc='#00FE00', ec="none",
                             connectionstyle="arc3, rad=0.01"))
    

plt.annotate('',
             xy=(6,320), xycoords='data',
             xytext=(40, -70), textcoords='offset points',
             size=8, zorder=100,
             # bbox=dict(boxstyle="round", fc="0.8"),
             arrowprops=dict(arrowstyle="simple, head_length=1, head_width=0.75",
                             linestyle=":",
                             fc='#FE0000', ec="none",
                             connectionstyle="arc3, rad=-1.2"))

ax2.annotate('',
              xy=(11, 200), xycoords='data',
              xytext=(-90, -30), textcoords='offset points',
              size=8, zorder=100,
              # bbox=dict(boxstyle="round", fc="0.8"),
              arrowprops=dict(arrowstyle="simple, head_length=1, head_width=0.75", 
                              fc="blue", ec="none",
                              connectionstyle="arc3, rad=0.01"))


ax2.text(-6, 1450, '   Evaporation')
ax2.text(10, 1200, 'Mineral\ndissolu.')


plt.text(1.5, 90, 'Flow direction of Sha River', 
         rotation=0, ha='center', va='center')
    


#plt.minorticks_on()
ax2.set_ylabel('$TDS$ [mg/L]')
ax2.set_xlabel('$d-excess$ [‰]')



ax2.scatter(90, 10, marker='s', s=40, color='w',edgecolors='black', label='Huai River')  
ax2.scatter(90, 9, marker='o', s=40, color='w',edgecolors='black', label='Lower reaches')      
ax2.scatter(90, 8, marker='*', s=70, color='w',edgecolors='black', label='Middle reaches')      
ax2.scatter(90, 7, marker='v', s=40, color='w',edgecolors='black', label='Sha River')     
ax2.scatter(90, 6, marker='D', s=40, color='w',edgecolors='black', label='Ying River')    
ax2.scatter(90, 5, marker='^', s=40, color='w',edgecolors='black', label='Jialu River')    
ax2.scatter(90, 4, marker='x', s=40, color='k',edgecolors='black', label='Groundwater')  

ax2.fill_between([90.98, 90.985], 4, 5, color='#FE0000', label='Dec. 2019')
ax2.fill_between([90.99, 90.995], 4, 5, color='#00FE00', label='May. 2020')
ax2.fill_between([90.10, 90.105], 4, 5, color='blue', label='Aug. 2020')

plt.legend(bbox_to_anchor=(1.05, 1.00), loc=2, borderaxespad=0, shadow=True)    




plt.subplots_adjust(wspace=0.3, hspace=0.25)


ax1.text(-3.8, -72, '(a)')
ax2.text(12, 95, '(b)')

plt.savefig('GMWL_LMWL.jpg', dpi=600, bbox_inches='tight')
    
plt.show()




import matplotlib.pyplot as plt  

from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
from plottable import Table


data = [['\nDec.2019', 'River', '$\delta$D=5.96x$\delta$$^{18}O-7.34$' + ', $R^2=0.97$'], 
        ['', 'Groundwater', '$\delta$D=6.24x$\delta$$^{18}O-6.15$' + ', $R^2=0.95$'], 
        ['\nMay 2020', 'River', '$\delta$D=5.94x$\delta$$^{18}O-6.94$' + ', $R^2=0.93$'], 
        ['', 'Groundwater', '$\delta$D=6.94x$\delta$$^{18}O-0.69$' + ', $R^2=0.95$'], 
        ['\nAug. 2020', 'River', '$\delta$D=6.24x$\delta$$^{18}O-7.38$' + ', $R^2=0.97$'], 
        ['', 'Groundwater', '$\delta$D=6.59x$\delta$$^{18}O-3.20$' + ', $R^2=0.95$']]


table = plt.table(cellText=data, colWidths = [0.2, 0.2, 0.6],
                  #rowColours = ['#E6987F', '#7FBAA4', '#6666FF', '#E6987F', '#7FBAA4', '#6666FF'],
                  cellLoc='left', cellColours=None)

table._cells[(0, 0)].visible_edges='LRT'
table._cells[(1, 0)].visible_edges='LR'


table._cells[(2, 0)].visible_edges='LRT'

table._cells[(3, 0)].visible_edges='LRB'

table._cells[(4, 0)].visible_edges='LR'
table._cells[(5, 0)].visible_edges='LRB'


table._cells[(0, 0)].fill = 'r'


plt.box(on=None)

table.scale(1.0, 1.25) 
table.set_fontsize(12)

ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.text(0.025, 0.025, '(c)')

plt.savefig('c_equations.jpg', dpi=600, bbox_inches='tight')

plt.show()






