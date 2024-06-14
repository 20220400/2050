def solve_puzzle(list, index = 0, track = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    if track is None:
        track = set()

    if len(list) == 0:
        return False
    elif index == len(list) -1:
        return True
    elif index in track:
        return False
    else:
        track.add(index)
        play = list[index]
        l_move = (index - play) % len(list)
        r_move = (index + play) % len(list)

        

        found_L = solve_puzzle(list, l_move, track)
        found_R = solve_puzzle(list, r_move, track)

        return found_L or found_R


   
    

    
    # 1) Base ca   se: have you found a valid solution?

    # 2) Find all valid next-steps

    # 3) Recursively explore next-steps, returning True if any valid solution is found

if __name__ == "__main__":
    list_one = [3,6,4,1,2,4,2,0]
    list_two = [3,4,1,2,0]

    

    print(solve_puzzle(list_one))
    print(solve_puzzle(list_two))