import collections


def  sol1():
    with open("input.txt") as f:

        numbers = [x.split("|") for x in f.read().splitlines()]

        output = []
        
        for number in numbers:
            output.append([c for c in number[1].split()])

        counter = 0

        for i in range(len(output)):
            for digit in output[i]:
                if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                    counter += 1

        print(counter)

# sol1()

#solution from reddit

def sol2():
    s = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            code = {}
            order = {}
            cypher, out = line.strip().split('|')
            cypher = cypher.split()
            out = out.split()
            for c in cypher:
                if len(c) == 7:
                    code[8] = ''.join(sorted(c))
                elif len(c) == 4:
                    code[4] = ''.join(sorted(c))
                elif len(c) == 3:
                    code[7] = ''.join(sorted(c))
                elif len(c) == 2:
                    code[1] = ''.join(sorted(c))
            # We can guess every digit with smart combination
            # of 1, 4, 7 and 8
            for c in cypher:
                # if len == 6 , it is either 0, 9 or 6
                if len(c) == 6:
                    # If 1 is not overlapping, it is 6
                    if not all([x in c for x in code[1]]):
                        code[6] = ''.join(sorted(c))
                    # if 4 is overlapping it is 9
                    elif all([x in c for x in code[4]]):
                        code[9] = ''.join(sorted(c))
                    else:
                        code[0] = ''.join(sorted(c))
            for c in cypher:
                # if len == 5, either 2, 3 or 5
                if len(c) == 5:
                    # If 1 is overlapping, it is 3
                    if all([x in c for x in code[1]]):
                        code[3] = ''.join(sorted(c))
                    # If it overlaps 9, it is 5
                    elif all([x in code[9] for x in c]):
                        code[5] = ''.join(sorted(c))
                    else:
                        code[2] = ''.join(sorted(c))
            # We can now crack the value
            number = ''
            for c in out:
                test = ''.join(sorted(c))
                for k in code.keys():
                    if code[k] == test:
                        number = ''.join([number, str(k)])
            s += int(number)
        print(s)


sol2()
