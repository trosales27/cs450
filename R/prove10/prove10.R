library(datasets)
library(cluster)
myData = state.x77

#compute a distance matrix
distance = dist(as.matrix(myData))
#make a cluster
hc = hclust(distance)
#plot a dendrogram
plot(hc)

#scale the data
data_scaled = scale(myData)
#compute a distance matrix
distance = dist(as.matrix(data_scaled))
#make a cluster
hc = hclust(distance)
#plot a dendrogram
plot(hc)

# Remove the area and repeat
myData = state.x77
drops <- c("Area")
myData[ , !(names(myData) %in% drops)]
data_scaled_2 = scale(myData)
#compute a distance matrix
distance = dist(as.matrix(myData))
#make a cluster
hc = hclust(distance)
#plot a dendrogram
plot(hc)

# Cluster by only Frost
frostData = state.x77
#Trying this way to drop columns
cols.dont.want <- c("Population", "Income", "Illiteracy", "Life Exp", "Murder", "HS Grad", "Area")
frostData <- frostData[, ! names(data) %in% cols.dont.want, drop = F]
#View(frostData)
myData[ , !(names(myData) %in% drops)]
data_scaled_2 = scale(myData)
#compute a distance matrix
distance = dist(as.matrix(myData))
#make a cluster
hc = hclust(distance)
#plot a dendrogram
plot(hc)


#Using k-means clustering
# Cluster into k=5 clusters:
myClusters = kmeans(data_scaled, 3)
# 
# # Summary of the clusters
summary(myClusters)
# 
# # Centers (mean values) of the clusters
myClusters$centers

# Cluster assignments
myClusters$cluster

# Within-cluster sum of squares and total sum of squares across clusters
myClusters$withinss
myClusters$tot.withinss


# Plotting a visual representation of k-means clusters
clusplot(myData, myClusters$cluster, color=TRUE, shade=TRUE, labels=2, lines=0) 

#Loop through and see 25 different averages for 25 different clusters
table = NULL;
for (i in 1:25) {
  myClusters = kmeans(data_scaled, i)
  table[i] = myClusters$tot.withinss
}
plot(table)

myClusters = kmeans(data_scaled, 4)
# # Summary of the clusters
summary(myClusters)
# # Centers (mean values) of the clusters
myClusters$centers
# Cluster assignments
myClusters$cluster
# Within-cluster sum of squares and total sum of squares across clusters
myClusters$withinss
myClusters$tot.withinss

# Plotting a visual representation of k-means clusters
clusplot(myData, myClusters$cluster, color=TRUE, shade=TRUE, labels=2, lines=0) 

