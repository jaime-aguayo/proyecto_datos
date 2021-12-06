
library(plyr)
 
Mat<-function(direct,save_as){
  Data <- read.csv(direct)
  DataDay<-data.frame(as.Date(Data[,c(5)]),as.Date(Data[,c(6)]),Data[,c(7,8)])
  names(DataDay)<-c("Inicio","Fin","Origen","Destino")
  HeatMontly<-ddply(DataDay,.(Origen,Destino),nrow)
  write.csv(HeatMontly,save_as, col.names=FALSE,row.names = FALSE)
}


List<-c("2015_01.csv","2015_02.csv","2015_03.csv","2015_04.csv","2015_05.csv","2015_06.csv","2015_07.csv","2015_08.csv","2015_09.csv","2015_10.csv","2015_11.csv","2015_12.csv")
List<-c(List,"2016_01.csv","2016_02.csv","2016_03.csv","2016_04.csv","2016_05.csv","2016_06.csv","2016_07.csv","2016_08.csv","2016_09.csv","2016_10.csv","2016_11.csv","2016_12.csv")
List<-c(List,"2017_01.csv","2017_02.csv","2017_03.csv","2017_04.csv","2017_05.csv","2017_06.csv","2017_07.csv","2017_08.csv","2017_09.csv","2017_10.csv","2017_11.csv","2017_12.csv")
List<-c(List,"2018_01.csv","2018_02.csv","2018_03.csv","2018_04.csv","2018_05.csv","2018_06.csv","2018_07.csv","2018_08.csv","2018_09.csv","2018_10.csv","2018_11.csv","2018_12.csv")
List<-c(List,"2019_01.csv","2019_02.csv","2019_03.csv","2019_04.csv","2019_05.csv","2019_06.csv","2019_07.csv","2019_08.csv","2019_09.csv","2019_10.csv","2019_11.csv","2019_12.csv")
List<-c(List,"2020_01.csv","2020_02.csv","2020_03.csv","2020_04.csv","2020_05.csv","2020_06.csv","2020_07.csv","2020_08.csv","2020_09.csv","2020_10.csv","2020_11.csv","2020_12.csv")
List<-c(List,"2021_01.csv","2021_02.csv","2021_03.csv","2021_04.csv","2021_05.csv","2021_06.csv","2021_07.csv","2021_08.csv","2021_09.csv","2021_10.csv")

Matrixs<-c("WorkingMatrixes/Modiffy_2015_01.csv","WorkingMatrixes/Modiffy_2015_02.csv","WorkingMatrixes/Modiffy_2015_03.csv","WorkingMatrixes/Modiffy_2015_04.csv","WorkingMatrixes/Modiffy_2015_05.csv","WorkingMatrixes/Modiffy_2015_06.csv","WorkingMatrixes/Modiffy_2015_07.csv","WorkingMatrixes/Modiffy_2015_08.csv","WorkingMatrixes/Modiffy_2015_09.csv","WorkingMatrixes/Modiffy_2015_10.csv","WorkingMatrixes/Modiffy_2015_11.csv","WorkingMatrixes/Modiffy_2015_12.csv")
Matrixs<-c(Matrixs,"WorkingMatrixes/Modiffy_2016_01.csv","WorkingMatrixes/Modiffy_2016_02.csv","WorkingMatrixes/Modiffy_2016_03.csv","WorkingMatrixes/Modiffy_2016_04.csv","WorkingMatrixes/Modiffy_2016_05.csv","WorkingMatrixes/Modiffy_2016_06.csv","WorkingMatrixes/Modiffy_2016_07.csv","WorkingMatrixes/Modiffy_2016_08.csv","WorkingMatrixes/Modiffy_2016_09.csv","WorkingMatrixes/Modiffy_2016_10.csv","WorkingMatrixes/Modiffy_2016_11.csv","WorkingMatrixes/Modiffy_2016_12.csv")
Matrixs<-c(Matrixs,"WorkingMatrixes/Modiffy_2017_01.csv","WorkingMatrixes/Modiffy_2017_02.csv","WorkingMatrixes/Modiffy_2017_03.csv","WorkingMatrixes/Modiffy_2017_04.csv","WorkingMatrixes/Modiffy_2017_05.csv","WorkingMatrixes/Modiffy_2017_06.csv","WorkingMatrixes/Modiffy_2017_07.csv","WorkingMatrixes/Modiffy_2017_08.csv","WorkingMatrixes/Modiffy_2017_09.csv","WorkingMatrixes/Modiffy_2017_10.csv","WorkingMatrixes/Modiffy_2017_11.csv","WorkingMatrixes/Modiffy_2017_12.csv")
Matrixs<-c(Matrixs,"WorkingMatrixes/Modiffy_2018_01.csv","WorkingMatrixes/Modiffy_2018_02.csv","WorkingMatrixes/Modiffy_2018_03.csv","WorkingMatrixes/Modiffy_2018_04.csv","WorkingMatrixes/Modiffy_2018_05.csv","WorkingMatrixes/Modiffy_2018_06.csv","WorkingMatrixes/Modiffy_2018_07.csv","WorkingMatrixes/Modiffy_2018_08.csv","WorkingMatrixes/Modiffy_2018_09.csv","WorkingMatrixes/Modiffy_2018_10.csv","WorkingMatrixes/Modiffy_2018_11.csv","WorkingMatrixes/Modiffy_2018_12.csv")
Matrixs<-c(Matrixs,"WorkingMatrixes/Modiffy_2019_01.csv","WorkingMatrixes/Modiffy_2019_02.csv","WorkingMatrixes/Modiffy_2019_03.csv","WorkingMatrixes/Modiffy_2019_04.csv","WorkingMatrixes/Modiffy_2019_05.csv","WorkingMatrixes/Modiffy_2019_06.csv","WorkingMatrixes/Modiffy_2019_07.csv","WorkingMatrixes/Modiffy_2019_08.csv","WorkingMatrixes/Modiffy_2019_09.csv","WorkingMatrixes/Modiffy_2019_10.csv","WorkingMatrixes/Modiffy_2019_11.csv","WorkingMatrixes/Modiffy_2019_12.csv")
Matrixs<-c(Matrixs,"WorkingMatrixes/Modiffy_2020_01.csv","WorkingMatrixes/Modiffy_2020_02.csv","WorkingMatrixes/Modiffy_2020_03.csv","WorkingMatrixes/Modiffy_2020_04.csv","WorkingMatrixes/Modiffy_2020_05.csv","WorkingMatrixes/Modiffy_2020_06.csv","WorkingMatrixes/Modiffy_2020_07.csv","WorkingMatrixes/Modiffy_2020_08.csv","WorkingMatrixes/Modiffy_2020_09.csv","WorkingMatrixes/Modiffy_2020_10.csv","WorkingMatrixes/Modiffy_2020_11.csv","WorkingMatrixes/Modiffy_2020_12.csv")
Matrixs<-c(Matrixs,"WorkingMatrixes/Modiffy_2021_01.csv","WorkingMatrixes/Modiffy_2021_02.csv","WorkingMatrixes/Modiffy_2021_03.csv","WorkingMatrixes/Modiffy_2021_04.csv","WorkingMatrixes/Modiffy_2021_05.csv","WorkingMatrixes/Modiffy_2021_06.csv","WorkingMatrixes/Modiffy_2021_07.csv","WorkingMatrixes/Modiffy_2021_08.csv","WorkingMatrixes/Modiffy_2021_09.csv","WorkingMatrixes/Modiffy_2021_10.csv")

SEQ<-seq(from=1,to=length(Matrixs),by=1)

for (i in SEQ) {
  Mat(List[i],Matrixs[i])
}
