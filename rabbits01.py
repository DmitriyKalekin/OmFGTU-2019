"""
Задача Кролики Дирихле
Есть N кроликов и M клеток.
Перебрать все возможные варианты рассадки
"""
import timeit
from itertools import permutations, combinations, combinations_with_replacement

RABBITS_CNT = 9  # N
CAGES_CNT = 5  # M

class Solution1:
    def check_sum(variant): # [1,2,3,4,5]   # (1,2,3)
        return sum(variant) == RABBITS_CNT

    def convert_index_to_variant(index) -> list:
        result = []
        for power in range(CAGES_CNT-1, -1, -1):
            denom, index = divmod(index, (RABBITS_CNT+1) ** power)
            result.append(denom)
        return result

    def run():
        cnt = 0
        for i in range(0, (RABBITS_CNT+1)**CAGES_CNT):
            variant = Solution1.convert_index_to_variant(i)
            if Solution1.check_sum(variant):
                # print(variant)
                cnt += 1
        print("TOTAL:", cnt)
      

class Solution2:
    def explain_variant(variant_code) -> list:
        result = [0] * CAGES_CNT
        cage_index = 0
        for v in variant_code: # 
            if v == 1:
                cage_index += 1
                continue
            result[cage_index] += 1
        return result

    def run():
        start_set = [0]*RABBITS_CNT + [1]*(CAGES_CNT-1)
        for i, variant_code in enumerate(variations(start_set, len(start_set))):
            print(i, variant_code)
            print(Solution2.explain_variant(variant_code))

class Solution3:
    def run():   
        variants = list(combinations_with_replacement(range(0, CAGES_CNT), RABBITS_CNT))
        for v in variants:  
            res = [0] * CAGES_CNT
            for cage_index in range(0, CAGES_CNT):
                res[cage_index] = sum([1 for pos in v if pos == cage_index])
            # print(res)
        print("TOTAL:", len(variants))

if __name__ == "__main__":
    # t = timeit.timeit('Solution1.run()', number=1, setup="from __main__ import Solution1")
    # print("elapsed:", t)    
    # t = timeit.timeit('Solution3.run()', number=1, setup="from __main__ import Solution3")
    # print("elapsed:", t)



    RABBITS_CNT = 4
    max_a = RABBITS_CNT + 1
    for a in range(0, max_a):
        max_b = RABBITS_CNT - a + 1
        for b in range(a, max_b):
            max_c = RABBITS_CNT - b + 1
            for c in range(b, max_c):
                if sum([a,b,c]) == RABBITS_CNT:
                    print(list(permutations([a,b,c])))

    digit = 0
    states = [0] * CAGES_CNT
            





