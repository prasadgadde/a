data<-read.csv("/home/prasadgadde/BigData/Project/zones1.csv")
df<-data.frame(data)
df1<- subset(df, select = -c(Year))
x<-log(df1)
z<-stack(x)

# ANOVA 
A<-aov(values~ind,data=z)
summary.aov(A)
# ANOVA test is significant at 0.1% level of significance.

#diff among group means----Anova:  analysis of variance
#anova():-
#used to detrmine wether there are any statically significant diff b/w 
#the means of two r more indipendent groups

# Critical Difference

cd<-table_t_value_at_errof_DF* sqrt((2*Residual_Mean_Sum_of_Squares)/no_of_replications)
table_t_value_at_errof_DF<-qt(.999,df=91)
Residual_Mean_Sum_of_Squares<-0.046
no_of_replications<-14
cd<-table_t_value_at_errof_DF* sqrt((2*Residual_Mean_Sum_of_Squares)/no_of_replications)

# Multiple Comparison
regions<-c("North","East","West","South","Central","North.East","Union.Teritery")
mean_list<-c(mean(df$North),mean(df$East),mean(df$West),mean(df$South),
  mean(df$Central),mean(df$North.East),mean(df$Union.Teritery))

means<-data.frame("Regions"=regions,"Mean_Values"=mean_list)
means1<- means[order(-means$Mean_Values),] 

#Plot
plot.new()
barplot(means1$Mean_Values, main="REGION WISE COMPARISON",
        xlab="Regions",ylab = "Mean no.of Crimes ",
        col = rainbow(7),names.arg =means1$Regions,
        legend("topright",legend =means1$Regions,fill = rainbow(7)))

