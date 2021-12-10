import functools


@functools.lru_cache(maxsize=10000)
def cached_sum(n):
    return sum(range(1,n+1))


def sol1():
    #faster if  we use median as destination number

    with open("input.txt") as f:
        numbers = [int(i) for i in f.read().split(",")]
        
    min_n = min(numbers)
    max_n = max(numbers)

    min_fuel = 9999999 

    for i in range(min_n,max_n+1):
        fuel = 0
        for num in numbers:
            fuel += cached_sum(abs(num - i))

        if fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)

# sol1()


def sol2():

    with open("input.txt") as f:
        numbers = [int(i) for i in f.read().split(",")]
        
    min_n = min(numbers)
    max_n = max(numbers)

    min_fuel = None 

    for i in range(min_n,max_n+1):
        fuel = 0
        for num in numbers:
            # fuel += sum(range(1,abs(num - i)+1))
            max_d = abs(num-i)
            fuel+= (max_d*(max_d+1))/2 # better to learn some maths
        if min_fuel == None:
            min_fuel= fuel
        if fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)

        


sol2()
