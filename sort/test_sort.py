#!/usr/bin/env python3
import os
import sys
import pytest
import random
import importlib


sorting_algorithm = sys.argv[1]
module_name = func_name = f"{sorting_algorithm}_sort"
module = importlib.import_module(module_name)
func = getattr(module, func_name)


BIG_INT = 10000
SHUFFLED_BIG_LIST = list(range(BIG_INT))
random.shuffle(SHUFFLED_BIG_LIST)

lists_to_test = [\
        [],
        [1],
        [1,1],
        [1,1,1,1,1],
        [1] * BIG_INT,
        [1,2,3,4],
        list(range(BIG_INT)),
        [8,7,6,5,4],
        list(range(BIG_INT))[::-1],
        [1,3,9,5,2],
        SHUFFLED_BIG_LIST]


@pytest.mark.parametrize("l", lists_to_test)


def test_sort(l: list):
    func(l)
    assert l == sorted(l)


if __name__ == "__main__":
    pytest.main([f"{os.path.dirname('__file__')}", "--verbose", "--durations=0", "-x", "--pdb"])
