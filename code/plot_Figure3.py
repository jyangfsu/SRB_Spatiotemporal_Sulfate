# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:19:27 2024

@author: Jing
"""
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

from wqchartpy import triangle_piper
from wqchartpy import gibbs
from wqchartpy import gaillardet


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
    


# Define the plotting function
def piper_plot(df, unit='mg/L',  figname='triangle Piper diagram', figformat='jpg'):
    """Plot the Piper diagram.
    
    Parameters
    ----------
    df : class:`pandas.DataFrame`
        Geochemical data to draw Gibbs diagram.
    unit : class:`string`
        The unit used in df. Currently only mg/L and meq/L are supported. 
    figname : class:`string`
        A path or file name when saving the figure.
    figformat : class:`string`
        The figure format to be saved, e.g. 'png', 'pdf', 'svg'
        
        
    References
    ----------
    .. [1] Piper, A.M. 1944.
           A Graphic Procedure in the Geochemical Interpretation of 
           Water-Analyses. Eos, Transactions American Geophysical 
           Union, 25, 914-928.
           http://dx.doi.org/10.1029/TR025i006p00914
    .. [2] Hill, R.A. 1944. 
           Discussion of a graphic procedure in the geochemical interpretation 
           of water analyses. EOS, Transactions American Geophysical 
           Union 25, no. 6: 914–928.    
    """
    # Basic data check 
    # -------------------------------------------------------------------------
    # Determine if the required geochemical parameters are defined. 
    if not {'Ca', 'Mg', 'Na', 'K', 
            'HCO3', 'CO3', 'Cl', 'SO4'}.issubset(df.columns):
        raise RuntimeError("""
        Trilinear Piper diagram requires geochemical parameters:
        Ca, Mg, Na, K, HCO3, CO3, Cl, and SO4.
        Confirm that these parameters are provided in the input file.""")
        
    # Determine if the provided unit is allowed
    ALLOWED_UNITS = ['mg/L', 'meq/L']
    if unit not in ALLOWED_UNITS:
        raise RuntimeError("""
        Currently only mg/L and meq/L are supported.
        Convert the unit manually if needed.""")
        
    # Global plot settings
    # -------------------------------------------------------------------------
    # Change default settings for figures
    plt.style.use('default')
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 10
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 10   
    
    # Plot background settings
    # -------------------------------------------------------------------------
    # Define the offset between the diamond and traingle
    offset = 0.10                         
    offsety = offset * np.tan(np.pi / 3.0)
    h = 0.5 * np.tan(np.pi / 3.0)
    
    # Calculate the traingles' location 
    ltriangle_x = np.array([0, 0.5, 1, 0])
    ltriangle_y = np.array([0, h, 0, 0])
    rtriangle_x = ltriangle_x + 2 * offset + 1
    rtriangle_y = ltriangle_y
    
    # Calculate the diamond's location 
    diamond_x = np.array([0.5, 1, 1.5, 1, 0.5]) + offset
    diamond_y = h * (np.array([1, 2, 1, 0, 1])) + (offset * np.tan(np.pi / 3))
    
    # Plot the traingles and diamond
    
    ax = fig.add_subplot(111, aspect='equal', frameon=False, 
                         xticks=[], yticks=[])
    ax.plot(ltriangle_x, ltriangle_y, '-k', lw=1.0)
    ax.plot(rtriangle_x, rtriangle_y, '-k', lw=1.0)
    ax.plot(diamond_x, diamond_y, '-k', lw=1.0)
    
    # Plot the lines with interval of 20%
    interval = 0.2
    ticklabels = ['0', '20', '40', '60', '80', '100']
    for i, x in enumerate(np.linspace(0, 1, int(1/interval+1))):
        # the left traingle
        ax.plot([x, x - x / 2.0], 
                [0, x / 2.0 * np.tan(np.pi / 3)], 
                'k:', lw=1.0)
        ## the bottom ticks
        if i in [1, 2, 3, 4]: 
            ax.text(x, 0-0.03, ticklabels[-i-1], 
                    ha='center', va='center')
        ax.plot([x, (1-x)/2.0+x], 
                 [0, (1-x)/2.0*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the right ticks
        if i in [1, 2, 3, 4]:
            ax.text((1-x)/2.0+x + 0.026, (1-x)/2.0*np.tan(np.pi/3) + 0.015, 
                    ticklabels[i], ha='center', va='center', rotation=-60)
        ax.plot([x/2, 1-x/2], 
                [x/2*np.tan(np.pi/3), x/2*np.tan(np.pi/3)], 
                'k:', lw=1.0)
        ## the left ticks
        if i in [1, 2, 3, 4]:
            ax.text(x/2 - 0.026, x/2*np.tan(np.pi/3) + 0.015, 
                    ticklabels[i], ha='center', va='center', rotation=60)
        
        # the right traingle
        ax.plot([x+1+2*offset, x-x/2.0+1+2*offset], 
                [0, x/2.0*np.tan(np.pi/3)], 
                'k:', lw=1.0)
        ## the bottom ticks
        if i in [1, 2, 3, 4]:
            ax.text(x+1+2*offset, 0-0.03, 
                    ticklabels[i], ha='center', va='center')
        ax.plot([x+1+2*offset, (1-x)/2.0+x+1+2*offset],
                 [0, (1-x)/2.0*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the right ticks
        if i in [1, 2, 3, 4]:
            ax.text((1-x)/2.0+x+1+2*offset  + 0.026, (1-x)/2.0*np.tan(np.pi/3) + 0.015, 
                    ticklabels[-i-1], ha='center', va='center', rotation=-60)
        ax.plot([x/2+1+2*offset, 1-x/2+1+2*offset], 
                [x/2*np.tan(np.pi/3), x/2*np.tan(np.pi/3)], 
                'k:', lw=1.0)
        ## the left ticks
        if i in [1, 2, 3, 4]:
            ax.text(x/2+1+2*offset - 0.026, x/2*np.tan(np.pi/3) + 0.015, 
                    ticklabels[-i-1], ha='center', va='center', rotation=60)
        
        # the diamond
        ax.plot([0.5+offset+0.5/(1/interval)*x/interval, 1+offset+0.5/(1/interval)*x/interval], 
                 [h+offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3), offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the upper left and lower right
        if i in [1, 2, 3, 4]: 
            ax.text(0.5+offset+0.5/(1/interval)*x/interval  - 0.026, h+offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3) + 0.015, ticklabels[i], 
                    ha='center', va='center', rotation=60)
            ax.text(1+offset+0.5/(1/interval)*x/interval + 0.026, offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3) - 0.015, ticklabels[-i-1], 
                    ha='center', va='center', rotation=60)
        ax.plot([0.5+offset+0.5/(1/interval)*x/interval, 1+offset+0.5/(1/interval)*x/interval], 
                 [h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3), 2*h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the lower left and upper right
        if i in [1, 2, 3, 4]:  
            ax.text(0.5+offset+0.5/(1/interval)*x/interval- 0.026, h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3) - 0.015, ticklabels[i], 
                    ha='center', va='center', rotation=-60)
            ax.text(1+offset+0.5/(1/interval)*x/interval + 0.026, 2*h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3) + 0.015, ticklabels[-i-1], 
                    ha='center', va='center', rotation=-60)
    
    # Labels and title
    plt.text(0.5, -offset, '%' + '$Ca^{2+}$', 
             ha='center', va='center', fontsize=12)
    plt.text(1+2*offset+0.5, -offset, '%' + '$Cl^{-}$', 
            ha='center', va='center', fontsize=12)
    plt.text(0.25-offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$Mg^{2+}$',  
             ha='center', va='center', rotation=60, fontsize=12)
    plt.text(1.75+2*offset+offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$SO_4^{2-}$',  
              ha='center', va='center', rotation=-60, fontsize=12)
    plt.text(0.75+offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$Na^+$' + '+%' + '$K^+$',  
              ha='center', va='center', rotation=-60, fontsize=12)
    plt.text(1+2*offset+0.25-offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$HCO_3^-$' + '+%' + '$CO_3^{2-}$',  
              ha='center', va='center', rotation=60, fontsize=12)
    
    plt.text(0.5+offset+0.5*offset+offset*np.cos(np.pi/30), h+offset*np.tan(np.pi/3)+0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$SO_4^{2-}$' + '+%' + '$Cl^-$',  
              ha='center', va='center', rotation=60, fontsize=12)
    plt.text(1.5+offset-0.25+offset*np.cos(np.pi/30), h+offset*np.tan(np.pi/3)+0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$Ca^{2+}$' + '+%' + '$Mg^{2+}$', 
              ha='center', va='center', rotation=-60, fontsize=12)
    
    # Fill the water types domain
    ## the left traingle
    '''
    plt.fill([0.25, 0.5, 0.75, 0.25], 
             [h/2, 0, h/2, h/2], color = (0.8, 0.8, 0.8), zorder=0)
    ## the right traingle
    plt.fill([1+2*offset+0.25, 1+2*offset+0.5, 1+2*offset+0.75, 1+2*offset+0.25], 
             [h/2, 0, h/2, h/2], color = (0.8, 0.8, 0.8), zorder=0)
    ## the diamond
    plt.fill([0.5+offset+0.25, 0.5+offset+0.25+0.5, 0.5+offset+0.25+0.25, 0.5+offset+0.25],
             [h+offset*np.tan(np.pi/3) - 0.5*np.sin(np.pi/3), h+offset*np.tan(np.pi/3) - 0.5*np.sin(np.pi/3), h+offset*np.tan(np.pi/3), h+offset*np.tan(np.pi/3) - 0.5*np.sin(np.pi/3)], 
             color = (0.8, 0.8, 0.8), zorder=0)
    plt.fill([0.5+offset+0.25, 0.5+offset+0.25+0.25, 0.5+offset+0.25+0.5, 0.5+offset+0.25],
             [h+offset*np.tan(np.pi/3) + 0.5*np.sin(np.pi/3), h+offset*np.tan(np.pi/3), h+offset*np.tan(np.pi/3) + 0.5*np.sin(np.pi/3), h+offset*np.tan(np.pi/3) + 0.5*np.sin(np.pi/3)], 
             color = (0.8, 0.8, 0.8), zorder=0)
    '''
    # Convert unit if needed
    if unit == 'mg/L':
        gmol = np.array([ions_WEIGHT['Ca'], 
                         ions_WEIGHT['Mg'], 
                         ions_WEIGHT['Na'], 
                         ions_WEIGHT['K'], 
                         ions_WEIGHT['HCO3'],
                         ions_WEIGHT['CO3'], 
                         ions_WEIGHT['Cl'], 
                         ions_WEIGHT['SO4']])
    
        eqmol = np.array([ions_CHARGE['Ca'], 
                          ions_CHARGE['Mg'], 
                          ions_CHARGE['Na'], 
                          ions_CHARGE['K'], 
                          ions_CHARGE['HCO3'], 
                          ions_CHARGE['CO3'], 
                          ions_CHARGE['Cl'], 
                          ions_CHARGE['SO4']])
    
        tmpdf = df[['Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4']]
        dat = tmpdf.values
        
        meqL = (dat / abs(gmol)) * abs(eqmol)
        
    elif unit == 'meq/L':
        meqL = df[['Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4']].values
    
    else:
        raise RuntimeError("""
        Currently only mg/L and meq/L are supported.
        Convert the unit if needed.""")
    
    # Calculate the percentages
    sumcat = np.sum(meqL[:, 0:4], axis=1)
    suman = np.sum(meqL[:, 4:8], axis=1)
    cat = np.zeros((dat.shape[0], 3))
    an = np.zeros((dat.shape[0], 3))
    cat[:, 0] = meqL[:, 0] / sumcat                  # Ca
    cat[:, 1] = meqL[:, 1] / sumcat                  # Mg
    cat[:, 2] = (meqL[:, 2] + meqL[:, 3]) / sumcat   # Na+K
    an[:, 0] = (meqL[:, 4] + meqL[:, 5]) / suman     # HCO3 + CO3
    an[:, 2] = meqL[:, 6] / suman                    # Cl
    an[:, 1] = meqL[:, 7] / suman                    # SO4

    # Convert into cartesian coordinates
    cat_x = 0.5 * (2 * cat[:, 2] + cat[:, 1])
    cat_y = h * cat[:, 1]
    an_x = 1 + 2 * offset + 0.5 * (2 * an[:, 2] + an[:, 1])
    an_y = h * an[:, 1]
    d_x = an_y / (4 * h) + 0.5 * an_x - cat_y / (4 * h) + 0.5 * cat_x
    d_y = 0.5 * an_y + h * an_x + 0.5 * cat_y - h * cat_x

    # Plot the scatters
    Labels = []
    for i in range(len(df)):
        if (df.at[i, 'Label'] in Labels or df.at[i, 'Label'] == ''):
            TmpLabel = ''
        else:
            TmpLabel = df.at[i, 'Label']
            Labels.append(TmpLabel)
         
        try:
            if (df['Color'].dtype is np.dtype('float')) or \
                (df['Color'].dtype is np.dtype('int64')):
                vmin = np.min(df['Color'].values)
                vmax = np.max(df['Color'].values)
                cf = plt.scatter(cat_x[i], cat_y[i], 
                                marker=df.at[i, 'Marker'],
                                s=df.at[i, 'Size'], 
                                c=df.at[i, 'Color'], vmin=vmin, vmax=vmax,
                                alpha=df.at[i, 'Alpha'],
                                #label=TmpLabel, 
                                edgecolors='black')
                plt.scatter(an_x[i], an_y[i], 
                            marker=df.at[i, 'Marker'],
                            s=df.at[i, 'Size'], 
                            c=df.at[i, 'Color'], vmin=vmin, vmax=vmax,
                            alpha=df.at[i, 'Alpha'],
                            label=TmpLabel, 
                            edgecolors='black')
                plt.scatter(d_x[i], d_y[i], 
                            marker=df.at[i, 'Marker'],
                            s=df.at[i, 'Size'], 
                            c=df.at[i, 'Color'], vmin=vmin, vmax=vmax,
                            alpha=df.at[i, 'Alpha'],
                            #label=TmpLabel, 
                            edgecolors='black')
                
            else:
                plt.scatter(cat_x[i], cat_y[i], 
                            marker=df.at[i, 'Marker'],
                            s=df.at[i, 'Size'], 
                            c=df.at[i, 'Color'], 
                            alpha=df.at[i, 'Alpha'],
                            #label=TmpLabel, 
                            edgecolors='black')
                plt.scatter(an_x[i], an_y[i], 
                            marker=df.at[i, 'Marker'],
                            s=df.at[i, 'Size'], 
                            c=df.at[i, 'Color'], 
                            alpha=df.at[i, 'Alpha'],
                            label=TmpLabel, 
                            edgecolors='black')
                plt.scatter(d_x[i], d_y[i], 
                            marker=df.at[i, 'Marker'],
                            s=df.at[i, 'Size'], 
                            c=df.at[i, 'Color'], 
                            alpha=df.at[i, 'Alpha'],
                            #label=TmpLabel, 
                            edgecolors='black')
                
        except(ValueError):
            pass
            
    # Creat the legend
    if (df['Color'].dtype is np.dtype('float')) or (df['Color'].dtype is np.dtype('int64')):
        cb = plt.colorbar(cf, extend='both', spacing='uniform',
                          orientation='vertical', fraction=0.025, pad=0.05)
        cb.ax.set_ylabel('$TDS$' + ' ' + '$(mg/L)$', rotation=90, labelpad=-75, fontsize=14)
    

    plt.legend(bbox_to_anchor=(0.15, 0.875), markerscale=1, fontsize=12,
                  frameon=False, 
                  labelspacing=0.25, handletextpad=0.25)
        
    # Display the info
    cwd = os.getcwd()
    print("Trilinear Piper plot created. Saving it to %s \n" %cwd)
    

    
    return








dfc1 = pd.read_csv('../data/data_122019.csv')
dfc1['Camp'] =1
dfc2 = pd.read_csv('../data/data_052020.csv')
dfc2['Camp'] =3
dfc3 = pd.read_csv('../data/data_082020.csv')
dfc3['Camp'] =5





fig = plt.figure(figsize=(10, 10), dpi=100)

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
    tmp_df['Alpha'] = 0.6
    tmp_df['HCO3'] = tmp_df['HCO3_mgL_tit'] 
    tmp_df['CO3'] = 0
    
    tmp_df.loc[tmp_df['River']=='Huai River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Huai River', 'Marker'] = 's'
    tmp_df.loc[tmp_df['River']=='Huai River', 'Size'] = 50
    
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Marker'] = 'o'
    tmp_df.loc[tmp_df['River']=='Lower reaches', 'Size'] = 50
    
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Marker'] = '*'
    tmp_df.loc[tmp_df['River']=='Middle reaches', 'Size'] = 100
    
    tmp_df.loc[tmp_df['River']=='Sha River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Sha River', 'Marker'] = 'v'
    tmp_df.loc[tmp_df['River']=='Sha River', 'Size'] = 50
    
    tmp_df.loc[tmp_df['River']=='Ying River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Ying River', 'Marker'] = 'D'
    tmp_df.loc[tmp_df['River']=='Ying River', 'Size'] = 50
    
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Marker'] = '^'
    tmp_df.loc[tmp_df['River']=='Jialu River', 'Size'] = 50
    
    tmp_df.loc[tmp_df['River']=='GW', 'Color'] = color
    tmp_df.loc[tmp_df['River']=='GW', 'Marker'] = 'X'
    tmp_df.loc[tmp_df['River']=='GW', 'Size'] = 50
    
    
    
    df = tmp_df[['Sample', 'Label', 'Color', 'Marker', 'Size', 'Alpha', 
                 'pH', 'Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]
   
    
    piper_plot(df, unit='mg/L', figname='piper_camp' + str(i), figformat='jpg')
    
    #gibbs.plot(df, unit='mg/L', figname='gibbs_camp' + str(i), figformat='jpg')
    #gaillardet.plot(df, unit='mg/L', figname='gaillardet_camp' + str(i), figformat='jpg')

def func(pct):  
    return f'{pct * 2:.1f}%'  


fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(2, 8))
axes = axes.flatten()

for i in range(3):
    if i == 0 :
        tmp_df = dfc1
    if i == 1 :
        tmp_df = dfc2
    if i == 2 :
        tmp_df = dfc3
        

    tmp_df['TZ+'] = tmp_df['K'] / 39 * 1 + tmp_df['Na'] / 23 * 1 + tmp_df['Ca'] / 40 * 2 + tmp_df['Mg'] / 24 * 2
    tmp_df['TZ-'] = tmp_df['HCO3_mgL_tit'] / 61 * 1 + tmp_df['Cl'] / 35.5 * 1 + tmp_df['SO4'] / 96 * 2 
    
    tmp_df['K_meq%'] = tmp_df['K'] / 39 * 1 / tmp_df['TZ+'] * 100
    tmp_df['Na_meq%'] = tmp_df['Na'] / 23 * 1 / tmp_df['TZ+']  * 100
    tmp_df['Ca_meq%'] = tmp_df['Ca'] / 40 * 2 / tmp_df['TZ+']  * 100
    tmp_df['Mg_meq%'] = tmp_df['Mg'] / 24 * 2 / tmp_df['TZ+']  * 100
    
    tmp_df['HCO3_mgL_tit_meq%'] = tmp_df['HCO3_mgL_tit'] / 61 * 1 / tmp_df['TZ-']  * 100
    tmp_df['Cl_meq%'] = tmp_df['Cl'] / 35.5 * 1 / tmp_df['TZ-']  * 100
    tmp_df['SO4_meq%'] = tmp_df['SO4'] / 96 * 2 / tmp_df['TZ-']  * 100
    
    labels = ['$Mg^{2+}$', '$Ca^{2+}$', '$Na^++K^+$',  '$Cl^-$', '$SO_4^{2-}$', '$HCO_3^-$']
    colors = ['#E2F4FD', '#91C5BF', '#98D491', '#DAE799', '#FBDC92', '#FAB083']
    
    sizes = [tmp_df['Mg_meq%'].describe()['mean'],
             tmp_df['Ca_meq%'].describe()['mean'],
             tmp_df['K_meq%'].describe()['mean'] + tmp_df['Na_meq%'].describe()['mean'], 
             
             tmp_df['Cl_meq%'].describe()['mean'],
             tmp_df['SO4_meq%'].describe()['mean'],
             tmp_df['HCO3_mgL_tit_meq%'].describe()['mean'],
    
             ] 


    wedges, texts, autotexts = axes[i].pie(sizes, labels=['', '', '', '', '', ''], autopct=func, colors=colors,
                radius=1.15, rotatelabels=True, counterclock=False, startangle=-90)   
    
    for w in wedges:
        w.set_linewidth(1.5)
        w.set_edgecolor('k')
  
    for tx, pc in zip(texts, autotexts ):
        rot = tx.get_rotation()

        pc.set_rotation(tx.get_rotation())
        
    wedges, texts, autotexts = axes[i].pie(sizes, labels=labels, autopct='', colors=colors,
                radius=1.15, rotatelabels=False, counterclock=False, startangle=-90)   
    
    axes[i].set_title(['(b) Dec. 2019', '(c) May. 2020\n', '(d) Aug. 2020\n'][i], fontsize=12)

    axes[i].plot([0, 0], [-1.15, 1.15], lw=1, color='k')
    
plt.show()