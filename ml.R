install.packages("caret")
install.packages("e1071")
install.packages("xlsx")
 
data<-read.csv("/home/prasadgadde/BigData/Project/ipc_yearly.csv")

#Madhya Pradesh
data_mp <- data.frame(data$year, data$MP)

v <- c(1:10)
w<- c(11:14)

# Defining training set
tr<-data_mp[v,]

# Defining test set
te<-data_mp[w,]

# Preparing the model
fit.knn <- train(data.MP~.,data = tr,method='knn')
fit.cart<-train(data.MP~.,data = tr,method='rpart')
fit.svm<-train(data.MP~.,data = tr,method='svmRadial')
l1 <- lm(tr$data.MP~.,data = tr)


te$data.MP=0


pr1<-predict(fit.knn, te)
pr2<-predict(fit.cart, te)
pr3<-predict(fit.svm, te)

# Checking accuracy of prediction graphically
x<-2011:2014
line1 <- te$data.MP

p1<-pr1
p2<-pr2
p3<-pr3

plot(x,line1,type='b',ylim = c(180000,300000))

lines(x,p1,type = 'b',col="red")
lines(x,p2,type = 'b',col="green")
lines(x,p3,type = 'b',col="blue")
## KNN and SVM for Madhya pradesh


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
