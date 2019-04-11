library("e1071")
library(caret)

#Testing out cross validation on iris
ctrl <- trainControl(method = "cv", savePred=T, classProb=T)
mod <- train(Species~., data=iris, method = "svmLinear", trControl = ctrl)
head(mod$pred)

data(iris)
m2 <- svm(Species~., data = iris)
plot(m2, iris, Petal.Width ~ Petal.Length,
     slice = list(Sepal.Width = 3, Sepal.Length = 4))

library(MASS)
data(cats)
m <- svm(Sex~., data = cats)
plot(m, cats)

library(e1071)

day = c(0,1,2,3,4,5,6)
weather = c(1,0,0,0,0,0,0)
happy = factor(c(T,F,F,F,F,F,F))

d = data.frame(day=day, weather=weather, happy=happy)
model = svm(happy ~ day + weather, data = d)
plot(model, d)
