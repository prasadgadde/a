install.packages("caret")
install.packages("e1071")
install.packages("xlsx")
library("knn")
 
data<-read.csv("/home/prasadgadde/BigData/Project/ipc_yearly.csv")

#### ML using FOR LOOP BEGIN
df = data[,2:30]
for (state in colnames(df)) {
  print(state)
  data_state <- data.frame(data$year, df[state])
  
   v <- c(1:14)
   
   tr <- data_state[v,]
   te <- data_state[v,]
   colnames(tr[2])
   fit.knn <- train(MP~.,data = tr,method='knn')
   fit.cart<-train(state~.,data = tr,method='rpart')
   fit.svm<-train(state~.,data = tr,method='svmRadial')
  
}

#### END


#Madhya Pradesh
data_mp <- data.frame(data$year, data$MP)

v <- c(1:14)

# Defining training set
tr<-data_mp[v,]

# Defining test set
te<-data_mp[v,]

# Preparing the model
fit.knn <- train(data.MP~.,data = tr,method='knn')
fit.cart<-train(data.MP~.,data = tr,method='rpart')
fit.svm<-train(data.MP~.,data = tr,method='svmRadial')
len_reg <- lm(tr$data.MP~.,data = tr)

# Predicted or Estimated values
pr1<-predict(fit.knn, te)
pr2<-predict(fit.cart, te)
pr3<-predict(fit.svm, te)
pr4<-predict(len_reg,te)

# Checking accuracy of prediction graphically
line1 <- te$data.MP

p1<-pr1
p2<-pr2
p3<-pr3
p4<-pr4

plot(x,line1,type='b',ylim = c(170000,300000),sub = "Year", main = "MADHYA PRADESH")
lines(x,p1,type = 'b',col="red")
lines(x,p2,type = 'b',col="green")
lines(x,p3,type = 'b',col="blue")
lines(x,p4,col='brown')
legend("topright", legend = c("Actual","KNN","CART","SVM","REGR"),
       col = c("black","red","green","blue","yellow"),pch = c(14,19),
       bty = "o",pt.cex = 2,cex = 1.2,text.col = "black",horiz = F,inset = c(.1,.1))

## Prediction by using linear regression
x1<-data.frame(data.year=c(2015:2020))
pr44<-predict(len_reg,x1)
pr11<-predict(fit.knn, x1)
data.frame(year=x1$data.year,Predicted_value=pr44)

#Maharashtra
data_mh <- data.frame(data$year, data$MAHA)

v <- c(1:10)

w<- c(11:14)

# Defining training set
tr<-data_mh[v,]

# Defining test set
te<-data_mh[w,]

# Preparing the model
fit.knn <- train(data.MAHA~.,data = tr,method='knn')
fit.cart<-train(data.MAHA~.,data = tr,method='rpart')
fit.svm<-train(data.MAHA~.,data = tr,method='svmRadial')

pr1<-predict(fit.knn, te)
pr2<-predict(fit.cart, te)
pr3<-predict(fit.svm, te)

# Checking accuracy of prediction graphically
x<-2011:2014
line1 <- te$data.MAHA

p1<-pr1
p2<-pr2
p3<-pr3

plot(x,line1,type='b',ylim = c(180000,260000))

lines(x,p1,type = 'b',col="red")
lines(x,p2,type = 'b',col="green")
lines(x,p3,type = 'b',col="blue") 

## KNN for Maharasthra


# Tamil Nadu
data_tn <- data.frame(data$year, data$TN)
v <- c(1:10)

w<- c(11:14)

# Defining training set
tr<-data_tn[v,]

# Defining test set
te<-data_tn[w,]

# Preparing the model
fit.knn <- train(data.TN~.,data = tr,method='knn')
fit.cart<-train(data.TN~.,data = tr,method='rpart')
fit.svm<-train(data.TN~.,data = tr,method='svmRadial')

pr1<-predict(fit.knn, te)
pr2<-predict(fit.cart, te)
pr3<-predict(fit.svm, te)

# Checking accuracy of prediction graphically
x<-2011:2014
line1 <- te$data.TN

p1<-pr1
p2<-pr2
p3<-pr3

plot(x,line1,type='b',ylim = c(160000,210000))

lines(x,p1,type = 'b',col="red")
lines(x,p2,type = 'b',col="green")
lines(x,p3,type = 'b',col="blue")

# kNN for Tamil Nadu

# Uttar Pradesh
data_up <- data.frame(data$year, data$UP)
v <- c(1:10)

w<- c(11:14)

# Defining training set
tr<-data_up[v,]

# Defining test set
te<-data_up[w,]

# Preparing the model
fit.knn <- train(data.UP~.,data = tr,method='knn')
fit.cart<-train(data.UP~.,data = tr,method='rpart')
fit.svm<-train(data.UP~.,data = tr,method='svmRadial')

pr1<-predict(fit.knn, te)
pr2<-predict(fit.cart, te)
pr3<-predict(fit.svm, te)

# Checking accuracy of prediction graphically
x<-2011:2014
line1 <- te$data.UP

p1<-pr1
p2<-pr2
p3<-pr3

plot(x,line1,type='b',ylim = c(140000,250000))

lines(x,p1,type = 'b',col="red")
lines(x,p2,type = 'b',col="green")
lines(x,p3,type = 'b',col="blue")

## KNN for Uttar Pradesh


# Andhra Pradesh
data_ap <- data.frame(data$year, data$AP)
v <- sample(1:14, 10)
sort(v)

# Defining training set
tr<-data_ap[v,]

# Defining test set
te<-data_ap[-v,]

# Preparing the model
fit.knn <- train(data.AP~.,data = tr,method='knn')
fit.cart<-train(data.AP~.,data = tr,method='rpart')
fit.svm<-train(data.AP~.,data = tr,method='svmRadial')

pr1<-predict(fit.knn, te)
pr2<-predict(fit.cart, te)
pr3<-predict(fit.svm, te)

# Checking accuracy of prediction graphically
x<-1:4
line1 <- te$data.AP

p1<-pr1
p2<-pr2
p3<-pr3

plot(x,line1,type='b',ylim = c(110000,220000))

lines(x,p1,type = 'b',col="red")
lines(x,p2,type = 'b',col="green")
lines(x,p3,type = 'b',col="blue")

# SVM for Andhra Pradesh
fit.knn <- train(data.MP~.,data = tr,method="rpart")
te1 <- data.frame(data.year=c(2015,222050,333000))
predict(fit1,te1)
fit1 <- randomForest(data.MP~.,data=tr)
?knn
train <- rbind(iris3[1:25,,1], iris3[1:25,,2], iris3[1:25,,3])
test <- rbind(iris3[26:50,,1], iris3[26:50,,2], iris3[26:50,,3])
cl <- factor(c(rep("s",25), rep("c",25), rep("v",25)))
knn(train, test, cl, k = 3, prob=TRUE)
