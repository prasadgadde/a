data<-read.csv("/home/prasadgadde/BigData/Project/zones1.csv")
df<-data.frame(data)

df1<-cbind(df$North/6,df$East/4,df$West/4,df$South/4,df$Central/2,df$North.East/8,df$Union.Teritery/7)
df2<-data.frame(df1)
x<-log(df2)
z<-stack(x)


A<-aov(values~ind,data=z)
summary.aov(A)

table_t_value_at_errof_DF<-qt(.999,df=91)
Residual_Mean_Sum_of_Squares<-0.046
no_of_replications<-14
cd1<-table_t_value_at_errof_DF* sqrt((2*Residual_Mean_Sum_of_Squares)/no_of_replications)
cd1

typeof(regions)
regions<-c("N","E","W","S","C","NE","UT")
mean_list<-c(mean(df2$X1),mean(df2$X2),mean(df2$X3),mean(df2$X4),
             mean(df2$X5),mean(df2$X6),mean(df2$X7))

means<-data.frame("Regions"=regions,"Mean_Values"=mean_list)
means1<- means[order(-means$Mean_Values),] 
means1

plot.new()
barplot(means1$Mean_Values, main="REGION WISE COMPARISON",
        xlab="Regions",ylab = "Mean no.of Crimes ",
        col = rainbow(7),names.arg =means1$Regions)

# CAGR analysis of Regions
df<-data.frame(data)
df<-df[,2:8]

x<-c()
y<-c()
for (region in colnames(df)){
  regioni<-as.numeric(unlist(df[region]))
  y<-union(y, region)
  CAGR_Region<-(((regioni[14]/regioni[1])^(1/14))-1)*100
  x<-union(x, CAGR_Region)
  print(paste(region," : ", round(CAGR_Region, 2)))
}
x
y
cagrdf<-data.frame("Region"=y,"CAGR"=x)
cagrdf1<- cagrdf[order(-cagrdf$CAGR),] 
