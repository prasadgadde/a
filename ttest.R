####### Uttar Pradesh
data_UP<-read.csv("/home/prasadgadde/BigData/Project/UP_CAP_DIST.csv")
a_UP<-data_UP$CAP
b_UP<-data_UP$DIST
# F test to compare two variances
var.test(a_UP,b_UP)
qf(0.95,13,13)
# F test : Significant

# two sample t test to compare two mean values
t.test(a_UP,b_UP, var.equal=FALSE, paired=FALSE)
qt(0.95,16.371)
# t test : Significant

####### Andhra Pradesh
data_AP<-read.csv("/home/prasadgadde/BigData/Project/AP_CAP_DIST.csv")
a_AP<-data_AP$CAP
b_AP<-data_AP$DIST
# F test to compare two variances
var.test(a_AP,b_AP)
qf(0.95,13,13)
# F test : Non-Significant

# two sample t test to compare two mean values
t.test(a_AP,b_AP, var.equal=TRUE, paired=FALSE)
qt(0.95,26)
# t test : Significant

####### Maharashtra
data_MH<-read.csv("/home/prasadgadde/BigData/Project/MAHA_CAP_DIST.csv")
a_MH<-data_MH$CAP
b_MH<-data_MH$DIST
# F test to compare two variances
var.test(a_MH,b_MH)
qf(0.95,13,13)
# F test : Significant

# two sample t test to compare two mean values
t.test(a_MH,b_MH, var.equal=FALSE, paired=FALSE)
qt(0.95,17.581)
# t test : Significant

####### Tamilnadu
data_TN<-read.csv("/home/prasadgadde/BigData/Project/TN_CAP_DIST.csv")
a_TN<-data_TN$CAP
b_TN<-data_TN$DIST
# F test to compare two variances
var.test(a_TN,b_TN)
qf(0.95,13,13)
# F test : Significant

# two sample t test to compare two mean values
t.test(a_TN,b_TN, var.equal=FALSE, paired=FALSE)
qt(0.95,16.371)
# t test : Significant

####### Madhya Pradesh
data_MP<-read.csv("/home/prasadgadde/BigData/Project/MP_CAP_DIST.csv")
a_MP<-data_MP$CAP
b_MP<-data_MP$DIST
# F test to compare two variances
var.test(a_MP,b_MP)
qf(0.95,13,13)
# F test : Non-Significant

# two sample t test to compare two mean values
t.test(a_MP,b_MP, var.equal=TRUE, paired=FALSE)
qt(0.95,26)
# t test : Significant

