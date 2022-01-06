#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:39:26 2022

@author: jakravit
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates

#%
## CAPS batch
path = '/Users/jakravit/OneDrive - NASA/C-HARRIER_2021_C-AIR/C-AIR_CAPS/'
outpath = '/Users/jakravit/Desktop/Caps_figs/'

suffixes = ('URU.csv','URC.csv')
for diry in os.listdir(path):
    print (diry)
    
    if not os.path.exists(outpath+diry):
        os.mkdir(outpath+diry)
    else:
        pass
    
    for file in os.listdir(path+diry):
        if not file.endswith(suffixes):
            continue
        
        print (file)
        name = file[:-4]

        data = pd.read_csv(os.path.join(path,diry,file), sep=',', encoding='ISO-8859-1', index_col='DateTimeUTC')
        data.index = pd.to_datetime(data.index)
        sensors = {'es': data.iloc[:,5:24],
                   'li': data.iloc[:,24:43],
                   'lt': data.iloc[:,43:]}
        
        for sensor,sdata in sensors.items():
            print (sensor)
            
            fig, ax = plt.subplots(figsize=(8,5))
            colormap = plt.cm.gist_ncar
            plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))
            means = []
            stds = []
            labels = []
            for i,b in enumerate(sdata.columns):
                sdata.index = pd.to_datetime(sdata.index)
                ax.scatter(sdata.index,sdata[b], marker='o',s=3)
                mean = sdata[b].mean()
                std = sdata[b].std()
                means.append(mean)
                stds.append(std)
                labels.append('{}, \u03BC={:.1e}, \u03C3={:.1e}'.format(b.split(' ')[0], mean, std))
            ax.legend(labels,bbox_to_anchor=(1.09, 1.05),fontsize='medium')
            ax.set_title('{} -- {}'.format(sensor,file))
            plt.xticks(rotation=45)
            ax.set_ylabel('uW/cm2/nm')
            
            ax2 = ax.twinx()
            ax2.plot(data.iloc[:,3], label='Roll (deg)') # roll
            ax2.plot(data.iloc[:,4], label='Pitch (deg)') # pitch
            ax2.set_ylabel('Degrees')
            ax2.legend(loc='upper left')
            
            fig.savefig(outpath+diry+'/'+name+'.png',bbox_inches='tight',dpi=300)
            plt.close(fig)
