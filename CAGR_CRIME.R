data<-read.csv("/home/prasadgadde/BigData/Project/crimes_all.csv")
df<-data.frame(data)
df<-df[,4:33]
df$Custodial.Rape[1] = 1
x<-c()
y<-c()
for (crime in colnames(df)){
  crimei<-as.numeric(unlist(df[crime]))
  y<-union(y, crime)
  CAGR_CRIME<-(((crimei[14]/crimei[1])^(1/14))-1)*100
  x<-union(x, CAGR_CRIME)
  print(paste(crime," : ", round(CAGR_CRIME, 2)))
}
x
y
cagrdf<-data.frame("Crime"=y,"CAGR"=x)
cagrdf1<- cagrdf[order(-cagrdf$CAGR),] 


write.csv(cagrdf, file = "/home/prasadgadde/BigData/Project/cagrdf_crime.csv")
