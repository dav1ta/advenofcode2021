
import statistics


def sol1():
    with open("input.txt","r") as f:
        points = {")": 3,
                  "]": 57,
                  "}": 1197,
                  ">": 25137}
        dict_f = {'{':'}','<':'>','[':']','(':')'}
        dict_b = {y:x for x,y in dict_f.items()}
        total = 0
        for line in f.readlines():
            stack = []
            for char in line:
                if char in dict_f:
                    stack.append(char)
                if char in dict_b:
                    if stack[-1]!= dict_b[char]:
                        total+=points[char]
                        break
                    else:
                        stack.pop()

        print(total)



            


# sol1()




def sol2():
    with open("test.txt","r") as f:
        points = {")": 1,
                  "]": 2,
                  "}": 3,
                  ">": 4}
        scores = []
        dict_f = {'{':'}','<':'>','[':']','(':')'}
        dict_b = {y:x for x,y in dict_f.items()}
        for line in f.readlines():
            stack = []
            for char in line:
                if char in dict_f:
                    stack.append(char)
                if char in dict_b:
                    if stack[-1]!= dict_b[char]:
                        break
                    else:
                        stack.pop()

            else:
                score = 0
                for c in reversed(stack):
                    score *= 5
                    score += points[dict_f[c]]
                scores.append(score)
        print(scores)

        print(statistics.median(scores))



sol2()
