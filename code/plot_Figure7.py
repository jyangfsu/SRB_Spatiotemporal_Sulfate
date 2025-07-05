# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 07:55:14 2024

@author: Jing
"""
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from wqchartpy import triangle_piper
from wqchartpy import gibbs
from wqchartpy import gaillardet
from matplotlib.pyplot import minorticks_on, tick_params

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from scipy.stats import norm, chi2
from matplotlib.patches import Ellipse
from statannot import add_stat_annotation
import seaborn as sns




dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5


def cov_ellipse(x, y, ax, color, q=None, nsig=None, **kwargs):
    """
    Parameters
    ----------
    cov : (2, 2) array
        Covariance matrix.
    q : float, optional
        Confidence level, should be in (0, 1)
    nsig : int, optional
        Confidence level in unit of standard deviations. 
        E.g. 1 stands for 68.3% and 2 stands for 95.4%.

    Returns
    -------
    width, height, rotation :
         The lengths of two axises and the rotation angle in degree
    for the ellipse.
    """
    cov = np.cov(x,y)
    if q is not None:
        q = np.asarray(q)
    elif nsig is not None:
        q = 2 * norm.cdf(nsig) - 1
    else:
        raise ValueError('One of `q` and `nsig` should be specified.')
    r2 = chi2.ppf(q, 2)

    val, vec = np.linalg.eigh(cov)
    width, height = 2 * np.sqrt(val[:, None] * r2)
    rotation = np.degrees(np.arctan2(*vec[::-1, 0]))
    
    ell = Ellipse(xy=(np.mean(x),np.mean(y)),
                  width=width, height=height,
                  angle=rotation,
                  edgecolor=color,lw=1.5, facecolor='none',alpha=0.7)
    ax.add_artist(ell)
    
    

fig = plt.figure(figsize=(4, 3.5))
ax = fig.add_subplot(111)


ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([0.01, 10])
ax.set_ylim([1e-4, 10])

# Add an ellipse for Carbonates
axins = inset_axes(ax, width="110%", height="110%", loc=3)
rect = mpatches.Rectangle([0.8075, 0.8], 0.10, 0.12, 
                          fc="#CAFEFE", ec='k', alpha=0.6, hatch='\\\\//')

axins.add_patch(rect)
axins.axis('off')
ax.text(6, 0.02, 'Agriculture input', zorder=300, rotation=90,
        fontsize=10, family='cursive') 

# Add an ellipse for Carbonates
axins = inset_axes(ax, width="100%", height="100%", loc=2)
ellipse = mpatches.Ellipse([0.4, 0.92], 0.80, 0.1, angle=0, 
                           fc="#CDCE9E", ec='k', alpha=0.6, hatch='')
axins.add_patch(ellipse)
axins.axis('off')
axins.text(0.27, 0.9 , 'Urban sewage', zorder=300, fontsize=10, family='cursive') 


# Add an ellipse for Carbonates
axins = inset_axes(ax, width="120%", height="100%", loc=1)
axins .set_aspect('equal')
circle1 = mpatches.Circle([0.165, 0.05], 0.050, angle=0, 
                           fc="#F0DBCD", ec='k', alpha=0.6, hatch='///')
axins.add_patch(circle1)
axins.axis('off')
ax.text(1.02, 0.00016, '   Dissolution of \n   halite', zorder=300, fontsize=10, family='cursive') 


# Add an ellipse for Carbonates
circle2 = mpatches.Circle([0.93, 0.05], 0.050, angle=0, 
                            fc="grey", ec='k', alpha=0.6, hatch='\\\\\\')
axins.add_patch(circle2)
axins.axis('off')
ax.text(0.012, 0.00016, ' Dissolution of \n carbonate/silicate', zorder=300, fontsize=10, family='cursive') 

axin2 = inset_axes(ax, width="100%", height="100%", loc=1)

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
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'NO3', 'Cl', 'SO4', 'TDS']]
   
    df['Alpha'] = 0.4



    for i in range(len(df)):
        x = df.at[i, 'Cl'] / 35.5 / (df.at[i, 'Na'] / 23)
        y = df.at[i, 'NO3'] / 35.5 / (df.at[i, 'Na'] / 23)  
            
        ax.scatter(x, y, 
                    marker=df.at[i, 'Marker'],
                    s=df.at[i, 'Size'], 
                    color=df.at[i, 'Color'], 
                    alpha=df.at[i, 'Alpha'],
                    #label=TmpLabel, 
                    edgecolors='black') 
            
            
     
        
    '''    
    if icamp in [0, 1]:
        text = 'SYH-44'
        ax.text(df[df['ID']==text]['Cl'] / 35.5 / (df[df['ID']==text]['Na'] / 23), 
                     df[df['ID']==text]['NO3'] / 62 / (df[df['ID']==text]['Na'] / 23), 
                     ' ' + text.split('-')[1], ha='left', va='bottom')    
    if icamp in [2]:
        text = 'SYH-44'
        ax.text(df[df['ID']==text]['Cl'] / 35.5 / (df[df['ID']==text]['Na'] / 23), 
                     df[df['ID']==text]['NO3'] / 62 / (df[df['ID']==text]['Na'] / 23), 
                     text.split('-')[1] + ' ', ha='right', va='center')            
     '''  
        
    
    #plt.minorticks_on()
    
    

    
    
    
    
    ell_c_x = np.log10(df['Cl'] / 35.5 / (df['Na'] / 23))
    
    ell_c_y = np.log10(df['NO3'] / 62 / (df['Na'] / 23))
    
    #axin2.plot(np.mean(ell_c_x), np.mean(ell_c_y),'x',color=color,ms=8)
    
    #ax3.text(np.mean(ell_c_x)*1.1,np.mean(ell_c_y)*0.9,'C'+str(i),
    #         fontname='Times New Roman',fontsize=14,family='fantasy')
    
    cov_ellipse(ell_c_x, ell_c_y, axin2, color=color, q=0.8)   
    
    axin2.set_xlim(-2, 1)
    axin2.set_ylim(-4, 1)
    
    axin2.axis('off')
    
    
# Add a subplot at the specified position and size 
left, bottom, width, height = 0.95, 0.107, 0.2, 0.78
axr = fig.add_axes([left, bottom, width, height])  
axr.set_yscale('log')
axr.set_ylim([1e-4, 10])

# Plot some data in the subplot  
palette=['#FE0000', '#00FE00', 'blue']
par = 'NO3_Na'
for i in range(len(dfc1)):

    dfc1.at[i, par] = (dfc1.at[i, 'NO3'] / 62) / (dfc1.at[i, 'Na'] / 23) 
    dfc2.at[i, par] = (dfc2.at[i, 'NO3'] / 62) / (dfc2.at[i, 'Na'] / 23) 
    dfc3.at[i, par] = (dfc3.at[i, 'NO3'] / 62) / (dfc3.at[i, 'Na'] / 23) 
    

    df = pd.concat([dfc1[dfc1['Type']=='SW'][['Camp', par]],
                    dfc2[dfc2['Type']=='SW'][['Camp', par]], 
                    dfc3[dfc3['Type']=='SW'][['Camp', par]]])
    
    
    
df.to_csv('df_NO3_Na_ratio.csv')
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

'''    
add_stat_annotation(axr, data=df, x='Camp', y=par, order=[1, 3, 5],
                    box_pairs=[(1, 3), (1, 5), (3, 5)],
                    test='t-test_ind', text_format='star', 
                    loc='inside', verbose=2)
'''

axins.invert_xaxis()    
axr.set_ylim([1e-4, 1e1])
axr.set_yticks([1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1])
axr.set_yticklabels(['', '', '', '', '', ''])
axr.set_ylabel('')

axr.set_xticklabels(['', '', ''])
axr.set_xlabel('')
 
ax.set_xlabel('$Cl^-/Na^+$ [Molar ratio]')
ax.set_ylabel('$NO_3^-/Na^+$ [Molar ratio]')


ax.scatter(90, 10, marker='s', s=40, color='w',edgecolors='black', label='Huai River')  
ax.scatter(90, 9, marker='o', s=40, color='w',edgecolors='black', label='Lower reaches')      
ax.scatter(90, 8, marker='*', s=70, color='w',edgecolors='black', label='Middle reaches')      
ax.scatter(90, 7, marker='v', s=40, color='w',edgecolors='black', label='Sha River')     
ax.scatter(90, 6, marker='D', s=40, color='w',edgecolors='black', label='Ying River')    
ax.scatter(90, 5, marker='^', s=40, color='w',edgecolors='black', label='Jialu River')    
ax.scatter(90, 4, marker='x', s=40, color='k',edgecolors='black', label='Groundwater')  

ax.fill_between([90.98, 90.985], 4, 5, color='#FE0000', label='Dec. 2019')
ax.fill_between([90.99, 90.995], 4, 5, color='#00FE00', label='May. 2020')
ax.fill_between([90.10, 90.105], 4, 5, color='blue', label='Aug. 2020')

ax.legend(bbox_to_anchor=(1.38, 1.00), loc=2, borderaxespad=0, shadow=True) 

##############################################
# Add a subplot at the specified position and size 
left, bottom, width, height = 0.12, 0.95, 0.78, 0.2
axt = fig.add_axes([left, bottom, width, height])  
axt.set_xscale('log')
axt.set_xlim([1e-2, 10])

# Plot some data in the subplot  
palette=['#FE0000', '#00FE00', 'blue']
par = 'Cl_Na'
for i in range(len(dfc1)):

    dfc1.at[i, par] = (dfc1.at[i, 'Cl'] / 35.5) / (dfc1.at[i, 'Na'] / 23) 
    dfc2.at[i, par] = (dfc2.at[i, 'Cl'] / 35.5) / (dfc2.at[i, 'Na'] / 23) 
    dfc3.at[i, par] = (dfc3.at[i, 'Cl'] / 35.5) / (dfc3.at[i, 'Na'] / 23) 
    

    df = pd.concat([dfc1[dfc1['Type']=='SW'][['Camp', par]],
                    dfc2[dfc2['Type']=='SW'][['Camp', par]], 
                    dfc3[dfc3['Type']=='SW'][['Camp', par]]])
    
    df = pd.concat([dfc1[['Camp', par]],
                    dfc2[['Camp', par]], 
                    dfc3[['Camp', par]]])
    
df.to_csv('df_Cl_Na_ratio.csv')
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

axt.set_xlim([1e-2, 1e1])
axt.set_xticks([1e-2, 1e-1, 1e0, 1e1])
axt.set_xticklabels(['', '', '', ''])
axt.set_xlabel('')

axt.set_yticklabels(['', '', ''])
axt.set_ylabel('')

plt.show()
plt.savefig('Figure7.jpg', dpi=600, bbox_inches='tight')






