import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LIST=["Modiffy_2015_01","Modiffy_2015_02","Modiffy_2015_03","Modiffy_2015_04","Modiffy_2015_05","Modiffy_2015_06","Modiffy_2015_07","Modiffy_2015_08","Modiffy_2015_09","Modiffy_2015_10","Modiffy_2015_11","Modiffy_2015_12","Modiffy_2016_01","Modiffy_2016_02","Modiffy_2016_03","Modiffy_2016_04","Modiffy_2016_05","Modiffy_2016_06","Modiffy_2016_07","Modiffy_2016_08","Modiffy_2016_09","Modiffy_2016_10","Modiffy_2016_11","Modiffy_2016_12","Modiffy_2017_01","Modiffy_2017_02","Modiffy_2017_03","Modiffy_2017_04","Modiffy_2017_05","Modiffy_2017_06","Modiffy_2017_07","Modiffy_2017_08","Modiffy_2017_09","Modiffy_2017_10","Modiffy_2017_11","Modiffy_2017_12","Modiffy_2018_01","Modiffy_2018_02","Modiffy_2018_03","Modiffy_2018_04","Modiffy_2018_05","Modiffy_2018_06","Modiffy_2018_07","Modiffy_2018_08","Modiffy_2018_09","Modiffy_2018_10","Modiffy_2018_11","Modiffy_2018_12","Modiffy_2019_01","Modiffy_2019_02","Modiffy_2019_03","Modiffy_2019_04","Modiffy_2019_05","Modiffy_2019_06","Modiffy_2019_07","Modiffy_2019_08","Modiffy_2019_09","Modiffy_2019_10","Modiffy_2019_11","Modiffy_2019_12","Modiffy_2020_01","Modiffy_2020_02","Modiffy_2020_03","Modiffy_2020_04","Modiffy_2020_05","Modiffy_2020_06","Modiffy_2020_07","Modiffy_2020_08","Modiffy_2020_09","Modiffy_2020_10","Modiffy_2020_11","Modiffy_2020_12","Modiffy_2021_01","Modiffy_2021_02","Modiffy_2021_03","Modiffy_2021_04","Modiffy_2021_05"]


def MakeEverything(name,MAX):
    data= pd.read_csv(name+'.csv')
    x=data.Origen
    y=data.Destino
    z=data.V1
    MAT=np.zeros([MAX, MAX],dtype=int)
    for i in range(len(x)):
        MAT[int(x[i])-1,int(y[i])-1]=int(z[i])
    np.save('Out/'+name+'.bin', MAT)
def GetMax(LIST):
    MAX=0
    for a in LIST:
        data= pd.read_csv(a+'.csv')
        x=data.Origen
        y=data.Destino
        if max([max(x),max(y)])>MAX:
            MAX=max([max(x),max(y)])
    return MAX

M=GetMax(LIST)
# for a in LIST:
#     MakeEverything(a,M)

def MakeHeatMap(name,MAX,number,alpha=False):
    data= pd.read_csv(name+'.csv')
    x=data.Origen
    y=data.Destino
    z=data.V1
    if alpha:
        MAX=max([max(x),max(y)])
    MAT=np.zeros([MAX, MAX])
    for i in range(len(x)):
        MAT[int(x[i])-1,int(y[i])-1]=int(z[i])
    # S=sum(MAT)
    # MAT=MAT/S
    Data = pd.DataFrame(MAT)
    sns.color_palette("coolwarm", as_cmap=True)
    heatmap_plot = sns.heatmap(Data, center=0)
    plt.show()
    results_path = 'results'+number+'.png'
    plt.savefig(results_path)

def QuantileHeatRank(Value, Marks):
    min=Marks[0]
    for mark in Marks:
        if Value>mark or Value==mark:
            min=mark
    return min

def MakeHeatMapProb(name,MAX,number,alpha=False):
    data= pd.read_csv(name+'.csv')
    x=data.Origen
    y=data.Destino
    z=data.V1
    Sorting=[]
    Sorting=[a for a in z]
    Sorting.sort()
    cut=len(Sorting)//10
    Marks=[Sorting[i*cut] for i in range(10)]
    if alpha:
        MAX=max([max(x),max(y)])
    MAT=np.zeros([MAX, MAX])
    for i in range(len(x)):
        MAT[int(x[i])-1,int(y[i])-1]=int(QuantileHeatRank(z[i], Marks))
    # S=sum(MAT)
    # MAT=MAT/S
    Data = pd.DataFrame(MAT)
    heatmap_plot = sns.heatmap(Data, cmap="icefire",center=0)
    plt.xlabel("Estaciones Salida")
    plt.ylabel("Estaciones Llegada")
    plt.show()
    results_path = 'results'+number+'.png'
    figure = heatmap_plot.get_figure()
    figure.savefig(results_path, dpi=400,transparent=True)
#
# number=0
# for a in LIST:
#     MakeHeatMapProb(a,M,str(number))
#     number+=1

def MakeHeatMat(name,MAX,alpha=False):
    data= pd.read_csv(name+'.csv')
    x=data.Origen
    y=data.Destino
    z=data.V1
    Sorting=[]
    Sorting=[a for a in z]
    Sorting.sort()
    cut=len(Sorting)//10
    Marks=[Sorting[i*cut] for i in range(10)]
    if alpha:
        MAX=max([max(x),max(y)])
    MAT=np.zeros([MAX, MAX])
    for i in range(len(x)):
        MAT[int(x[i])-1,int(y[i])-1]=int(QuantileHeatRank(z[i], Marks))
    return MAT

# Creando los HeatMap por etapas de estaciones

marks=[4,19,46,76,77]

MAPS=[]
marker=0
# for mark in marks:
#     MAT1=np.zeros([M, M])
#     for i in range(marker,mark):
#         MAT1=MAT1+MakeHeatMat(LIST[i],M)
#     MAT1=MAT1/(mark-marker)
#     MAPS.append(MAT1)
#     marker=mark

def HeatPeriod(MAT,name):
    Data = pd.DataFrame(MAT)
    heatmap_plot = sns.heatmap(Data, cmap="icefire",center=0)
    plt.xlabel("Estaciones Salida "+name)
    plt.ylabel("Estaciones Llegada "+name)
    plt.show()
    results_path = 'results'+name+'.png'
    figure = heatmap_plot.get_figure()
    figure.savefig(results_path, dpi=400,transparent=True)

# names=[" Uno"," Dos"," Tres"," Cuatro"," Cinco"]
#
# for i in range(len(names)):
#     HeatPeriod(MAPS[i],"Etapa"+names[i])

### HeatMap antes de pandemia, y despues de la pandemia

def MakeHeatMatPandemic(name,MAX,Z,alpha=False):
    data= pd.read_csv(name+'.csv')
    x=data.Origen
    y=data.Destino
    z=data.V1
    Sorting=[]
    if not alpha:
        Sorting=[a for a in z]
    else:
        Sorting=[a for a in Z]
    Sorting.sort()
    cut=len(Sorting)//10
    Marks=[Sorting[i*cut] for i in range(10)]
    MAT=np.zeros([MAX, MAX])
    for i in range(len(x)):
        MAT[int(x[i])-1,int(y[i])-1]=int(QuantileHeatRank(z[i], Marks))
    return MAT,z


MAPS=[]
Z=[]
MAT1=np.zeros([M, M])
MAT1,Z=MakeHeatMatPandemic(LIST[61],M,Z)
MAPS.append(MAT1)

MAT1,Z=MakeHeatMatPandemic(LIST[63],M,Z,True)
MAPS.append(MAT1)


names=["AntesPandemia","DespuesPandemia"]

# for i in range(len(names)):
#     HeatPeriod(MAPS[i],names[i])
