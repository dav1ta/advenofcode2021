
def sol1():
    prev=0
    count=-1
    
    #not use list comprhension situaions like this would be memory overhead
    with open("input.txt",'r') as f:
        for line in f.readlines():
            if int(line)>prev:
                count+=1
            prev=int(line)


def sol2():
    count=-1
    prev_sum = 0
    a,b,c = 0,0,0
    
    
    with open("input.txt",'r') as f:
        nums = (int(line) for line in f.readlines())
        lenght=len(nums)
        
    
        for i,num in enumerate(nums):
            if i == len(nums)-2:
                break
            a,b,c = num,nums[i+1],nums[i+2]
            sum = a + b + c
            if sum > prev_sum:
                count+=1
            prev_sum=sum


    print(count)

sol2()





        










