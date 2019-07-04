SYNBOLS_SET = ["1", "2", "3", "4", "5"]    # 5! / (3! * (5-3)!)  
RESTRICTION = 3


def flat_list(given_list: list):
    ret = []
    for l in given_list:
        if not isinstance(l, list):
            ret.append(l)
        else:
            ret.extend(flat_list(l))
    return ret


def сombinations(N, K):
    if K == 0: 
        yield []
    for digit in N:  
        new_N = N.copy()
        new_N.remove(digit)
        for symbol in сombinations(new_N, K - 1):
            yield sorted([digit] + flat_list(symbol)) 
    

def set_uniq(gen):
    return list(set([tuple(i) for i in gen]))

# -----------------------------------------------#

def test_flat_list():
    given_list = ["5", "7", ["4", "2"], "6", ["9", "8", ["7", "6"]]]
    l = flat_list(given_list)
    print(l)


if __name__ == "__main__":
    for i in сombinations(SYNBOLS_SET, RESTRICTION):
        print(i)
    
    print("---")
    
    for i in set_uniq(сombinations(SYNBOLS_SET, RESTRICTION)):
        print(i)
     