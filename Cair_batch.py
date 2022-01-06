#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:56:03 2022

@author: jakravit
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates
import re

sensor = 'lt'
diry = 'today20211027'
path = '/Users/jakravit/OneDrive - NASA/C-HARRIER_2021_C-AIR/C-AIR/'
outpath = '/Users/jakravit/Desktop/Cair_figs/'

diry = diry+'/'
date = re.findall('[0-9]+', diry)[0]
flist = os.listdir(path+diry)
if not os.path.exists(outpath+diry):
    os.mkdir(outpath+diry)
    
fig, ax = plt.subplots(figsize=(10,6))
suffixes = ('Aux.csv','Log.csv','bunk')
for f in flist:
    if not f.endswith(suffixes):
        if not f.startswith('.'):
            print(f)
            
            name = f[:-4]
            file = path+diry+f
            data = pd.read_csv(file, sep=',', encoding='ISO-8859-1', index_col='DateTimeUTC')
            data.index = pd.to_datetime(data.index)  
            
            sensors = {'es': data.iloc[:,5:24],
                        'li': data.iloc[:,24:43],
                        'lt': data.iloc[:,43:]}
            
           
            colormap = plt.cm.gist_ncar
            plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))
            labels = []
            for i,b in enumerate(sensors[sensor].columns):
                ax.plot(data.index,data[b],)# marker='o',s=2)
                labels.append('{}'.format(b.split(' ')[0]))
    
ax.legend(labels,loc='right',bbox_to_anchor=(1.18, .5),fontsize='large')
plt.xticks(rotation=45,fontsize=14)
ax.set_ylabel('uW/cm2/nm',fontsize=14)
ax.set_title('{} - {} -- {}'.format(date,name,sensor),fontsize=16)
ax.set_ylim(0,20)
fig.savefig('{}/{}_{}.png'.format(outpath+diry,name,sensor),bbox_inches='tight',dpi=300)



            
            
            