


def sol1():

    with open("input.txt") as f:

        numbers = [ line.split("->") for line in f.readlines()]
    

    cord = {}
    for number in numbers:
        point_a,point_b = number[0].strip(),number[1].strip() 
        x1,y1 = [int(i) for i in point_a.split(",")]
        x2,y2 = [int(i) for i in point_b.split(",")]

        if x1 ==x2 :

            for i in range(min(y1,y2),max(y1,y2)+1):
                if (x1,i) not in cord:
                    cord[(x1,i)]=1
                else:
                    cord[(x1,i)]+=1


        elif y1==y2:
            for i in range(min(x1,x2),max(x1,x2)+1):
                if (i,y1) not in cord:
                    cord[(i,y1)]=1
                else:
                    cord[(i,y1)]+=1
    

    n = 0 

    for i in cord.values():
        if i > 1:
            n+=1

    print(n)






# sol1()





def sol2():

    with open("input.txt") as f:

        numbers = [ line.split("->") for line in f.readlines()]
    

    cord = {}
    for number in numbers:
        point_a,point_b = number[0].strip(),number[1].strip() 
        x1,y1 = [int(i) for i in point_a.split(",")]
        x2,y2 = [int(i) for i in point_b.split(",")]

        if x1 ==x2  :

            for i in range(min(y1,y2),max(y1,y2)+1):
                if (x1,i) not in cord:
                    cord[(x1,i)]=1
                else:
                    cord[(x1,i)]+=1


        elif y1==y2 :
            for i in range(min(x1,x2),max(x1,x2)+1):
                if (i,y1) not in cord:
                    cord[(i,y1)]=1
                else:
                    cord[(i,y1)]+=1

        else:
            x,y = x1,y1

            if x2 > x1:
                x_d = 1
            else:
                x_d = -1

            if y2 > y1:
                y_d = 1
            else:
                y_d = -1


            while (x,y) != (x2,y2):
                if (x,y) not in cord:
                    cord[(x,y)]=1
                else:
                    cord[(x,y)]+=1
                x+=x_d
                y+=y_d

            if (x2,y2) not in cord:

                cord[(x2,y2)]=1
            else:
                cord[(x2,y2)]+=1
    

    n = 0 

    for i in cord.values():
        if i >1:
            n+=1

    print(n)

sol2()
