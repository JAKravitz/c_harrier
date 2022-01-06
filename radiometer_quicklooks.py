# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

#%% 

## NO CAPS

path = '/Users/jakravit/OneDrive - NASA/C-HARRIER_2021_C-AIR/C-AIR/today20211027/'
sensor = 'lt'
flist = os.listdir(path)

fig, ax = plt.subplots(figsize=(10,5))
suffixes = ('Aux.csv','Log.csv','bunk')
for f in flist:
    if not f.endswith(suffixes):
        if not f.startswith('.'):
            print(f)
            file = path+f
            # try:
            #     data = pd.read_csv(file, sep=',', encoding='ISO-8859-1', index_col='DateTimeUTC')
            #     data.index = pd.to_datetime(data.index)
            # except:
            #     continue
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
    
ax.legend(labels,loc='right',bbox_to_anchor=(1.15, .5),fontsize='medium')
#ax.legend(labels,loc='upper right')
plt.xticks(rotation=45)
#ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.set_ylabel('uW/cm2/nm')
ax.set_title(sensor)
#ax.set_xlim(pd.Timestamp('2021-10-27 19:29:17.340000'), pd.Timestamp('2021-10-27 21:05:17.239000'))
ax.set_ylim(0,20)
#ax.set_yscale('log')
fig.savefig('/Users/jakravit/Desktop/quicklook.png',dpi=300,bbox_inches='tight')

#%% check encoding

import chardet    
rawdata = open('/Users/jakravit/OneDrive - NASA/C-HARRIER_2021_C-AIR/C-AIR/today20211027/300205917.csv', 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(charenc)

#%% 

## NO CAPS SINGLE

sensor = 'lt'
file = '/Volumes/Untitled/today20211027/300210417.csv'
data = pd.read_csv(file, sep=',', index_col='DateTimeUTC')
data.index = pd.to_datetime(data.index)
sensors = {'es': data.iloc[:,5:24],#.astype(float),
            'li': data.iloc[:,24:43],#.astype(float),
            'lt': data.iloc[:,43:]}#.astype(float)}

fig, ax = plt.subplots()
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))

for i,b in enumerate(sensors[sensor].columns):
    ax.scatter(data.index,data[b], marker='o',s=5)
