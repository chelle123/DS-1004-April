library(ggplot2)
library(sp)
library(rgdal)
ibrary(rgeos)

#give a name of the shapefile without extension
layerName <- 'ZillowNeighborhoods-NY'

#read the data in the shapefile into a R SpatialPolygonDataFrame
dataProjected <- readOGR(dsn='.', layer=layerName)

#read the tip percentage according to the neighborhood, later will use this information to plot map
neighbor_tip <- read.csv('./neighbor_tip_percentage.csv')

#since the shapefile also contains information for other cities, we remove those except NYC
dataProjected <- dataProjected[dataProjected$CITY!='Syracuse',]
dataProjected <- dataProjected[dataProjected$CITY!='Buffalo',]
dataProjected <- dataProjected[dataProjected$CITY!='Rochester',]
dataProjected <- dataProjected[dataProjected$CITY!='Albany',]

#merge the shapefile data and the tip percentage data
dataProjected@data = merge(dataProjected@data, neighbor_tip, by.x='NAME', by.y='neighbor')

#plot it using different grey color according to the tip percentage
plotvar <- dataProjected@data$tip_percent
class <- classIntervals(plotvar, nclr, style="quantile")
colcode <- findColours(class, plotclr)
plot(dataProjected, col=colcode)