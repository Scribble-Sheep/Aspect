import math

MP =1000000
MAXAREA = 3.7 * MP 

def calcDimensions(w, h)-> tuple[float, float]:
    dimensions = []
    aspect, flipped = calcAspect(w,h)
    dimensions.append(math.sqrt(MAXAREA/aspect))
    dimensions.append(aspect*math.sqrt(MAXAREA/aspect))
    for i in range(len(dimensions)):
        dimensions[i]=math.floor(dimensions[i])
    if flipped:
        dimensions.reverse()
    megapix = dimensions[0]*dimensions[1]
    return dimensions, megapix

def calcAspect(width, height)-> tuple[float, bool]:
    """Returns the ratio of the long:shorter value. always returns >=1, with a True if the values had to be flipped"""
    ratio = 1
    flipped = True
    ratio=width/height
    if ratio<1:
        flipped=False
        ratio=height/width
    return ratio, flipped

def printDimensions(w, h, debug= False):
    if debug:
        print("Old:\t",w,"x",h)
    dimensionalTuple = calcDimensions(w, h)
    print("Width:\t", dimensionalTuple[0][0])
    print("Height:\t", dimensionalTuple[0][1])
    print("MP:\t","{:,}".format(dimensionalTuple[1]))
    return dimensionalTuple

#printDimensions(220, 240, True)