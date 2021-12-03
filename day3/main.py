from  collections import Counter

def sol1():

    with open("input.txt","r") as f:

        numbers = [line.strip() for line in f.readlines()]
        

        num_len = len(numbers[0])

        gamma_rate =""
        epsilon_rate = ""
        

        for i in range(num_len):
            
            firsts = [g[i] for g in numbers]

            common = Counter(firsts).most_common()[0][0]
            gamma_rate += common
            epsilon_rate += "1" if common=="0" else "0"

        gamma_dec = int(gamma_rate,2)
        epsilon_rate = int(epsilon_rate,2)
        print(gamma_dec*epsilon_rate)


# sol1()



def sol2():
    with open("input.txt","r") as f:

        numbers = [line.strip() for line in f.readlines()]

        numbers_oxygen = numbers[:]
        numbers_scrubber = numbers[:]
        

        num_len = len(numbers[0])
        
        index = 0
        while len(numbers_oxygen)>1:


            firsts = [g[index] for g in numbers_oxygen]

            most_common=Counter(firsts).most_common()
            print(most_common)
            
            if len(most_common)>1 and  most_common[0][1]==most_common[1][1]:
                common = "1"
            else:
                common = most_common[0][0]

            numbers_oxygen = [i for i in numbers_oxygen if i[index]==common]
            index+=1

        index_b = 0

        while len(numbers_scrubber)>1:


            second = [g[index_b] for g in numbers_scrubber]

            most_common=Counter(second).most_common()
            print(most_common)
            
            if most_common[0][1]==most_common[1][1]:
                common = "0"
            else:
                common = most_common[1][0]

            numbers_scrubber = [i for i in numbers_scrubber if i[index_b]==common]
            index_b+=1

        
        print(numbers_oxygen,numbers_scrubber)
        ox = int(numbers_oxygen[0],2)
        sc = int(numbers_scrubber[0],2)

        print(ox*sc)
       



                

            


sol2()
