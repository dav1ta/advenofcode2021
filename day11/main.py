import collections



def nearby(x,y):
    yield (x,y-1)
    yield (x,y+1)
    yield (x-1,y)
    yield (x+1,y)
    yield (x-1,y-1)
    yield (x-1,y+1)
    yield (x+1,y-1)
    yield (x+1,y+1)
    


def sol1():
    with open("input.txt","r") as f:

        points = collections.defaultdict()
        for i,line in  enumerate(f.read().splitlines()):
            for line_index,j in enumerate(line):
                points[i,line_index]=int(j)

        flashes=0
        for i in range(196):
            
            stack = []

            for point in points:
                points[point]+=1
                if points[point]>9:
                    stack.append(point)
            
            while stack:
                pt = stack.pop()
                if points[pt]==0:
                    continue
                points[pt]=0
                flashes+=1
                for pt_s in nearby(*pt):
                    if points.get(pt_s) not in [None,0] :
                        points[pt_s]+=1
                        if points[pt_s]>9:
                            stack.append(pt_s)

           


        print(flashes)

        
        
        for i in range(0,10):
            print(list(points.values())[i*10 :i*10+10])


# sol1()





def sol2():
    with open("input.txt","r") as f:

        points = collections.defaultdict()
        for i,line in  enumerate(f.read().splitlines()):
            for line_index,j in enumerate(line):
                points[i,line_index]=int(j)

        count=0
        while True:
            count+=1
            
            stack = []

            for point in points:
                points[point]+=1
                if points[point]>9:
                    stack.append(point)
            
            while stack:
                pt = stack.pop()
                if points[pt]==0:
                    continue
                points[pt]=0
                for pt_s in nearby(*pt):
                    if points.get(pt_s) not in [None,0] :
                        points[pt_s]+=1
                        if points[pt_s]>9:
                            stack.append(pt_s)

            if all(val==0 for val in points.values()):
                break

           


        print(count)


sol2()

