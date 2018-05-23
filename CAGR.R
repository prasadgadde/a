data<-read.csv("/home/prasadgadde/BigData/Project/ipc_yearly.csv")
df<-data.frame(data)
df<-df[,2:30]

x<-c()
y<-c()
for (state in colnames(df)){
  statei<-as.numeric(unlist(df[state]))
  y<-union(y, state)
  CAGR_State<-(((statei[14]/statei[1])^(1/14))-1)*100
  x<-union(x, CAGR_State)
  print(paste(state," : ", round(CAGR_State, 2)))
}
x
y
cagrdf<-data.frame("State"=y,"CAGR"=x)
cagrdf1<- cagrdf[order(-cagrdf$CAGR),] 

plot.new()

barplot(cagrdf1$CAGR, main="STATE WISE COMPARISON",
        xlab="States",ylab = "CAGR Values",
        col = rainbow(7),names.arg =cagrdf1$State)

