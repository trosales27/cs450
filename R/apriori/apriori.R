#install.packages('arules');
library(arules);
data(Groceries);

#Read in the data
#groceries_data <- read.csv("groceries.csv", header=FALSE, sep=",")
grocs <- read.transactions("groceries.csv", header=FALSE, sep=",")

summary(grocs) #Prints off a nice little summary

itemFrequencyPlot(grocs, topN = 20) # Makes a plot

#grocRules <- apriori(grocs, parameter = list(support = 0.006, confidence = 0.25, minlen = 2))
for (i in 1:5) {
  print(paste("Test ", i, sep= " "))
  
  s = i * 0.001
  c = i * 0.25
  m = i
  #Support max value is 0.007
  #Confidence max value is 0.50
  #Minlen max value is 4
  grocRules <- apriori(grocs, parameter = list(support = 0.001, confidence = 0.25, minlen = 1))
  
  #print(grocRules)

  #print("inspecting")
  #inspect(sort(grocRules, by = "support")[300:400])
  #inspect(sort(grocRules, by = "confidence")[1:3])
  inspect(sort(grocRules, by = "lift")[1:5])

  #inspect(sort(grocRules, by = "lift")[1:5])
}