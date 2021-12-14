



from os import read


def sol1():


    with open('input.txt','r') as f:
        coords = []
        points,instrucitons = f.read().split('\n\n')


        for line in points.splitlines():
            x_s,y_s = line.split(',')
            coords.append((int(x_s),int(y_s)))


        for line in instrucitons.splitlines():
            start,end = line.split('=')
            direction = start[-1]
            value = int(end)


            if direction =='x':
                coords= [ ((x if x < value else value-(x-value)),y) for x,y in coords ]


            else:
                coords= [ (x,(y if y < value else value-(y-value))) for x,y in coords ]


            print(len(set(coords)))
            break
                

# sol1()
def sol2():


    with open('input.txt','r') as f:
        coords = []
        points,instrucitons = f.read().split('\n\n')


        for line in points.splitlines():
            x_s,y_s = line.split(',')
            coords.append((int(x_s),int(y_s)))


        for line in instrucitons.splitlines():
            start,end = line.split('=')
            direction = start[-1]
            value = int(end)


            if direction =='x':
                coords= [ ((x if x < value else value-(x-value)),y) for x,y in coords ]

            else:
                coords= [ (x,(y if y < value else value-(y-value))) for x,y in coords ]


    
        max_x = max(x for x, _ in coords)
        max_y = max(y for _, y in coords)
        

        for x in range(max_y+1):
            line =""
            for y in range(max_x+1):
                if (y,x) in coords:
                    line+="#"
                else:
                    line+= " "
            print(line)



sol2()

