import requests

urls = [
         "https://www.mibici.net/site/assets/files/1084/datos_abiertos_2015_01.csv",
         "https://www.mibici.net/site/assets/files/1097/datos_abiertos_2015_02.csv",
         "https://www.mibici.net/site/assets/files/1098/datos_abiertos_2015_03.csv",
         "https://www.mibici.net/site/assets/files/1099/datos_abiertos_2015_04.csv",
         "https://www.mibici.net/site/assets/files/1100/datos_abiertos_2015_05.csv",
         "https://www.mibici.net/site/assets/files/1101/datos_abiertos_2015_06.csv",
         "https://www.mibici.net/site/assets/files/1102/datos_abiertos_2015_07.csv",
         "https://www.mibici.net/site/assets/files/1103/datos_abiertos_2015_08.csv",
         "https://www.mibici.net/site/assets/files/1104/datos_abiertos_2015_09.csv",
         "https://www.mibici.net/site/assets/files/1105/datos_abiertos_2015_10.csv",
         "https://www.mibici.net/site/assets/files/1106/datos_abiertos_2015_11.csv",
         "https://www.mibici.net/site/assets/files/1107/datos_abiertos_2015_12.csv",
        # 2016
        "https://www.mibici.net/site/assets/files/1020/datos_abiertos_2016_01-1.csv",
        "https://www.mibici.net/site/assets/files/1021/datos_abiertos_2016_02.csv",
        "https://www.mibici.net/site/assets/files/1023/datos_abiertos_2016_03.csv",
        "https://www.mibici.net/site/assets/files/1029/datos_abiertos_2016_04.csv",
        "https://www.mibici.net/site/assets/files/1058/datos_abiertos_2016_05.csv",
        "https://www.mibici.net/site/assets/files/1080/datos_abiertos_2016_06.csv",
        "https://www.mibici.net/site/assets/files/1081/datos_abiertos_2016_07.csv",
        "https://www.mibici.net/site/assets/files/1082/datos_abiertos_2016_08.csv",
        "https://www.mibici.net/site/assets/files/1083/datos_abiertos_2016_09.csv",
        "https://www.mibici.net/site/assets/files/1108/datos_abiertos_2016_10.csv",
        "https://www.mibici.net/site/assets/files/1109/datos_abiertos_2016_11.csv",
        "https://www.mibici.net/site/assets/files/1110/datos_abiertos_2016_12.csv",
        # 2017
        "https://www.mibici.net/site/assets/files/1022/datos_abiertos_2017_01.csv",
        "https://www.mibici.net/site/assets/files/1111/datos_abiertos_2017_02.csv",
        "https://www.mibici.net/site/assets/files/1112/datos_abiertos_2017_03.csv",
        "https://www.mibici.net/site/assets/files/1115/datos_abiertos_2017_04-1.csv",
        "https://www.mibici.net/site/assets/files/1116/datos_abiertos_2017_05.csv",
        "https://www.mibici.net/site/assets/files/1119/datos_abiertos_2017_06.csv",
        "https://www.mibici.net/site/assets/files/1120/datos_abiertos_2017_07.csv",
        "https://www.mibici.net/site/assets/files/1122/datos_abiertos_2017_08.csv",
        "https://www.mibici.net/site/assets/files/1123/datos_abiertos_2017_09.csv",
        "https://www.mibici.net/site/assets/files/1124/datos_abiertos_2017_10.csv",
        "https://www.mibici.net/site/assets/files/1197/datos_abiertos_2017_11.csv",
        "https://www.mibici.net/site/assets/files/1198/datos_abiertos_2017_12.csv",
        # 2018
        "https://www.mibici.net/site/assets/files/1200/datos_abiertos_2018_01.csv",
        "https://www.mibici.net/site/assets/files/1201/datos_abiertos_2018_02.csv",
        "https://www.mibici.net/site/assets/files/1202/datos_abiertos_2018_03.csv",
        "https://www.mibici.net/site/assets/files/1203/datos_abiertos_2018_04.csv",
        "https://www.mibici.net/site/assets/files/1204/datos_abiertos_2018_05.csv",
        "https://www.mibici.net/site/assets/files/1205/datos_abiertos_2018_06.csv",
        "https://www.mibici.net/site/assets/files/1206/datos_abiertos_2018_07.csv",
        "https://www.mibici.net/site/assets/files/1207/datos_abiertos_2018_08.csv",
        "https://www.mibici.net/site/assets/files/1208/datos_abiertos_2018_09.csv",
        "https://www.mibici.net/site/assets/files/1209/datos_abiertos_2018_10.csv",
        "https://www.mibici.net/site/assets/files/1210/datos_abiertos_2018_11.csv",
        "https://www.mibici.net/site/assets/files/1211/datos_abiertos_2018_12.csv",
        # 2019
        "https://www.mibici.net/site/assets/files/1214/datos_abiertos_2019_01.csv",
        "https://www.mibici.net/site/assets/files/1217/datos_abiertos_2019_02.csv",
        "https://www.mibici.net/site/assets/files/1218/datos_abiertos_2019_03.csv",
        "https://www.mibici.net/site/assets/files/1219/datos_abiertos_2019_04.csv",
        "https://www.mibici.net/site/assets/files/1220/datos_abiertos_2019_05.csv",
        "https://www.mibici.net/site/assets/files/1221/datos_abiertos_2019_06.csv",
        "https://www.mibici.net/site/assets/files/1222/datos_abiertos_2019_07.csv",
        "https://www.mibici.net/site/assets/files/1223/datos_abiertos_2019_08.csv",
        "https://www.mibici.net/site/assets/files/1224/datos_abiertos_2019_09.csv",
        "https://www.mibici.net/site/assets/files/1225/datos_abiertos_2019_10.csv",
        "https://www.mibici.net/site/assets/files/1227/datos_abiertos_2019_11.csv",
        "https://www.mibici.net/site/assets/files/1228/datos_abiertos_2019_12.csv",

        # 2020
        "https://www.mibici.net/site/assets/files/1230/datos_abiertos_2020_01.csv",
        "https://www.mibici.net/site/assets/files/1231/datos_abiertos_2020_02.csv",
        "https://www.mibici.net/site/assets/files/1232/datos_abiertos_2020_03.csv",
        "https://www.mibici.net/site/assets/files/1235/datos_abiertos_2020_04.csv",
        "https://www.mibici.net/site/assets/files/1236/datos_abiertos_2020_05.csv",
        "https://www.mibici.net/site/assets/files/1237/datos_abiertos_2020_06.csv",
        "https://www.mibici.net/site/assets/files/1238/datos_abiertos_2020_07.csv",
        "https://www.mibici.net/site/assets/files/1239/datos_abiertos_2020_08.csv",
        "https://www.mibici.net/site/assets/files/1240/datos_abiertos_2020_09.csv",
        "https://www.mibici.net/site/assets/files/1241/datos_abiertos_2020_10.csv",
        "https://www.mibici.net/site/assets/files/1317/datos_abiertos_2020_11.csv",
        "https://www.mibici.net/site/assets/files/1318/datos_abiertos_2020_12.csv",

        # 2021
        "https://www.mibici.net/site/assets/files/1320/datos_abiertos_2021_01.csv",
        "https://www.mibici.net/site/assets/files/1323/datos_abiertos_2021_02.csv",
        "https://www.mibici.net/site/assets/files/1322/datos_abiertos_2021_03.csv",
        "https://www.mibici.net/site/assets/files/2129/datos_abiertos_2021_04.csv",
        "https://www.mibici.net/site/assets/files/3292/datos_abiertos_2021_05.csv",
        "https://www.mibici.net/site/assets/files/4572/datos_abiertos_2021_06.csv",
        "https://www.mibici.net/site/assets/files/5728/datos_abiertos_2021_07.csv",
        "https://www.mibici.net/site/assets/files/7073/datos_abiertos_2021_08.csv",
        "https://www.mibici.net/site/assets/files/8461/datos_abiertos_2021_09.csv",
        "https://www.mibici.net/site/assets/files/10088/datos_abiertos_2021_10.csv"

]

for url in urls:
    r = requests.get(url, headers={"User-Agent": "XY"})
    open(url[-11:], 'wb').write(r.content)

from os import listdir
from os.path import isfile, join
import pandas as pd

# Get all files in data_dir
files_dir = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

# build a pandas dataframe
data = pd.DataFrame()
for dir in files_dir:
    table = pd.read_csv(dir, encoding="latin1")
    data = pd.concat([data, table])

print(data.shape)

# Some idiot wrote the name wrong in one table
data.rename(columns={"A????o_de_nacimiento": "A??o_nacimiento"})

# Save as a ONE table
data.to_csv(data_dir+"complete_dataframe.csv")
