import collections


def find_all_path(start,end,graph,path=None):
    path = path or []
    path.append(start)

    if start==end:
        return [path]
    paths=[]
    for node in graph.get(start,[]):
        if node.islower() and node not in path:
            newpath=find_all_path(node,end,graph,path[:])
            paths.extend(newpath)
        elif node.isupper():
            newpath=find_all_path(node,end,graph,path[:])
            paths.extend(newpath)

    
    return paths



def sol1():

    with open("test1.txt") as f:
        
        paths = collections.defaultdict(set)
        for line in f.readlines():
            start,end  = line.strip().split("-")
            paths[start].add(end)
            paths[end].add(start)
        

        paths_list = find_all_path("start","end",paths)
        print(len(paths_list))

# sol1()


def find_all_path_sec(start,end,graph,path=None):
    path = path or []
    path.append(start)
    count = collections.Counter(path)
    if count["end"] > 1 or count["start"]>1:
        return []

    small_count = False

    for key,value in count.items():
        if key.islower() and value ==2:
            small_count=True

    if start==end:
        return [path]
    paths=[]
    for node in graph.get(start,[]):

        if node.islower() and small_count and node not in path:
            newpath=find_all_path_sec(node,end,graph,path[:])
            paths.extend(newpath)


        elif node.islower() and count[node]<2:
            newpath=find_all_path_sec(node,end,graph,path[:])
            paths.extend(newpath)
       
        elif node.isupper():
            newpath=find_all_path_sec(node,end,graph,path[:])
            paths.extend(newpath)

    
    return paths




def sol2():

    with open("test2.txt","r") as f:
        
        paths = collections.defaultdict(set)
        for line in f.readlines():
            start,end  = line.strip().split("-")
            paths[start].add(end)
            paths[end].add(start)
        

        paths_list = find_all_path_sec("start","end",paths)

        for path in paths_list:
            print(path)



sol2()


