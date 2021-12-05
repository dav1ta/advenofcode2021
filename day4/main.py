
#inspirited from anatonywritescode

def sol1():

    with open("input.txt","r") as f:
        file = f.read()
        numbers , *board_string = file.split('\n\n')
        board_ints = [[int(s) for s in board.split()] for board in board_string]
        boards= [{int(s):False   for s in board.split()} for board in board_string ]
        
        numbers = [int(s) for s in numbers.split(',')]

        last_win = None

        boards_done = set()

        for number in numbers:

            for board in boards:
                if number in board:
                    board[number]=True


            for q, board in enumerate(boards):
                if q in boards_done:
                    continue
                for i in range(5):
                    for j in range(5):
                        if not board[board_ints[q][i*5 +j]]:
                                break

                    else:
                        boards_done.add(q)
                        print(sum(k for k,v in board.items() if not v )* number)
                        break


                    for j in range(5):
                        if not board[board_ints[q][i+5*j]]:
                            break
                    else:
                        boards_done.add(q)
                        print(sum(k for k,v in board.items() if not v )* number)
                        break
                    
                        

        



sol1()

