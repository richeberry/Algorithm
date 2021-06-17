# 행렬의 덧셈 Addition of matrices

import numpy as np

def solution(arr1,arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    answer = a+b
    return answer.tolist()