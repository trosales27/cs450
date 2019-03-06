library(e1071)

#############################################################################

#Read in the file
data_letters <- read.csv('letters.csv', head=TRUE, sep=",")

#Break up the rows for test and train
allRows <- 1:nrow(data_letters)
testRows <- sample(allRows, trunc(length(allRows) * 0.3))
letterTest <- data_letters[testRows,]
letterTrain <- data_letters[-testRows,]

#Use the SVM to create a model 
model <- svm(letter~., data = letterTrain, kernel = "radial", gamma = 0.001, cost = 10)

print(letterTest[1])
#Make a prediciton
prediction <- predict(model, letterTest[,-1])

#How'd we do?
confusionMatrix <- table(pred = prediction, true = letterTest$letter)

agreement <- prediction == letterTest$letter
accuracy <- prop.table(table(agreement))

print(confusionMatrix)install.packages('e1071', dependencies = TRUE)
print(accuracy)


#############################################################################
#Trouble with this file

#Read in the file
data_vowel <- read.csv('vowel.csv', head=TRUE, sep=" ")

#Break up the rows for test and train
allRows <- 0:nrow(data_vowel)
testRows <- sample(allRows, trunc(length(allRows) * 0.3))
vowelTest <- data_vowel[testRows,]
vowelTrain <- data_vowel[-testRows,]

#Use the SVM to create a model 
model <- svm(Class~., data = vowelTrain, kernel = "radial", gamma = 0.001, cost = 10)
print(model)

indx <- apply(data_vowel, 2, function(dt) any(is.na(dt)))

#Make a prediciton
prediction <- predict(model, vowelTest[,-5])

#How'd we do?
confusionMatrix <- table(pred = prediction, true = vowelTest$Class)

agreement <- prediction == vowelTest$Class
accuracy <- prop.table(table(agreement))

print(confusionMatrix)install.packages('e1071', dependencies = TRUE)
print(accuracy)


