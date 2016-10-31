import shapefile
f = shapefile.Reader("D:/python/faizal.shp")
shapes = f.shapes()
print len (shapes)