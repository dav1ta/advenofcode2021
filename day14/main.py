import collections
def sol1():
    with open ('input.txt','r') as f:

        polymer, sections = f.read().split('\n\n')

        insert_table= {}

        for sec in sections.splitlines():
            splited = sec.split('->')

            insert_table[splited[0].strip()]=splited[1].strip()
        
        for i in range(10):
            new_line = polymer[0]
            for x,y in zip(polymer,polymer[1:]):

                insert = insert_table.get(x+y)
                if insert:
                    new_line+=(insert+y) 
                else:
                    new_line+=(y)

            polymer = new_line
            
        count=collections.Counter(polymer)
        print(max(count.values()) -min(count.values()))
            

# sol1()

def sol2():

    with open ('input.txt','r') as f:

        polymer, sections = f.read().split('\n\n')

        insert_table= {}

        star_sim =polymer[0]
        end_sim = polymer[-1]


        start_table = collections.Counter([(x+y) for x,y in zip(polymer,polymer[1:])])
        
        for sec in sections.splitlines():
            splited = sec.split('->')

            insert_table[splited[0].strip()]=splited[1].strip()
        
        for i in range(40):
        
            for key,value in start_table.copy().items():
                insert = insert_table.get(key)

                if insert:
                    start_table[key]-=value if start_table[key]>0 else 0
                    start_table[insert+key[-1]]+=value
                    start_table[key[0] +insert]+=value

        
        chars = set()
        
        for i in start_table.keys():
            for j in i:
                if i!=j+j:
                    chars.add(j)

        char_count = collections.Counter()

        for char in  chars:
            for key,value in start_table.items():
                if char in key and value>0:
                    char_count[char]+=value


        new_count = {}

        for key in char_count:
            if key in [star_sim,end_sim]:
                new_count[key]=char_count[key]/2 + (start_table[key+key]+1)/2
            else:
                new_count[key]=char_count[key]/2 + (start_table[key+key])/2
        

        print(max(new_count.values()) - min(new_count.values()))




        


       
sol2()


