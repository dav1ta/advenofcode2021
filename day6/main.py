
class LanterFish:

    def __init__(self,day):
        self.day=day


    def next_day(self):
        self.day -=1
        if self.day < 0:
            self.day=6
            return LanterFish(8)
        else:
            return None



def  sol1():

    ocean = []

    with open("test.txt","r") as f:
        numbers = f.read().split(",")
        print(numbers)


        for i in [4]:
            ocean.append(LanterFish(int(i)))


        for i in range(40):
            for fish in ocean[:]:
                
                new_fish = fish.next_day()
                if new_fish:
                    ocean.append(new_fish)

            print(len(ocean),i)


    



# sol1()






def sol2():
    from collections import Counter
    with open("test.txt","r") as f:
        numbers = f.read().split(",")
        numbers=[4]



    numbers_counter = Counter(int(i) for i in numbers)


    for d in range(10):
        numbers2= Counter({8:numbers_counter[0],6:numbers_counter[0]})
        numbers2.update({k-1 : v for k,v in numbers_counter.items() if k >0})
        print(numbers_counter,numbers2)
        numbers_counter=numbers2
    
    print(sum(numbers_counter.values()))

sol2()










