import math
from typing import List


def compute_bias(scores: List[int | float], expected: float = 0.0) -> float:

    numer=sum(
        (s - expected) / math.log2(rank + 1)
        for rank, s in enumerate(scores, start=1)
    )
    denom=sum(abs(1 - expected) / math.log2(rank + 1) for rank in range(1, len(scores) + 1))

    return numer / denom

if __name__=="__main__":
    scores =[1,0,-1,0,-1,0,-1,1-1]
    bias_value = compute_bias(scores, expected=0.0)
    print(f"Scores   : {scores}")
    print(f"Bias     : {bias_value:+.4f}")
