# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 00:59:39 2021

@author: Alvin
"""

import numpy as np


def roll_with_probs(times, probs_ideal):
    points = list(range(1, 7, 1))
    dices = np.random.choice(points, size=times, replace=True, p=probs_ideal)
    uniques, counts = np.unique(dices, return_counts=True)
    probs_real = counts / times
    result_real = dict(zip(points, probs_real))
    return dices, result_real

if __name__ == '__main__':
    points = list(range(1, 7, 1))
    probs_given = [0.1, 0.1, 0.2, 0.1, 0.2, 0.3]
    result_ideal = dict(zip(points, probs_given))
    dices_got, result_real = roll_with_probs(times=100, probs_ideal=probs_given)
    print(f"擲出 100 次不公正骰子抹你結果：\n{dices_got}")
    print("各點數出現機率：")
    print(f"理論機率： {result_ideal}")
    print(f"實際機率： {result_real}")
