import operator

def sol1():

    params = {"hor" : 0,"depth" : 0}

    comm = {"forward":("hor",operator.add),
                "down":("depth",operator.add),
                "up":("depth",operator.sub)}

    with open("input.txt",'r') as f:
        
        commands = [(x.split()[0],int(x.split()[1])) for x in f.readlines() ]
    

        for command in commands:

            op = comm[command[0]]
            param_val = params[op[0]]
            
            param_val = op[1](param_val,command[1])
            params[op[0]]=param_val
    
    print(params["hor"]*params["depth"])




# sol1()

def sol2():

    params = {"hor" : 0,"depth" : 0,"aim":0}

    comm = {"down":(("aim",operator.add),),
                "up":(("aim",operator.sub),),
                "forward":(("hor",operator.add),
                    ("depth",operator.mul ))}

    with open("input.txt",'r') as f:
        
        commands = [(x.split()[0],int(x.split()[1])) for x in f.readlines() ]
    

        for command in commands:

            op = comm[command[0]]
            

            for o in op:
                param_val = params[o[0]]
                if o[0]=='depth':
                    param_val += o[1](params["aim"],command[1])
                else:
                    param_val = o[1](param_val,command[1])

                params[o[0]]=param_val
    

    print(params["hor"]*params["depth"])
sol2()



