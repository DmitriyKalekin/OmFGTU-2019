SYNBOLS_SET = ["1", "2", "3", "4"]  # Cn_k = n! / (k! * (n-k)!)
RESTRICTION = 2

def сombinations(N, K):
    if K == 0: 
        yield ""
    for digit in N:
        N.remove(digit)
        for symbol in сombinations(N, K - 1):
            yield digit + symbol
        N.append(digit)
    
def set_uniq(gen):
    ret = []
    for i in gen:
        ret.append(i)
    return list(set(ret))

# -----------------------------------------------#

if __name__ == "__main__":
    for i in сombinations(SYNBOLS_SET, RESTRICTION):
        print(i)

    print("____")

    for i in set_uniq(сombinations(SYNBOLS_SET, RESTRICTION)):
        print(i)