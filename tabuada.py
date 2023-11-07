#!/usr/bin/env paython3
"""Imprime a tabuada de 1 a 10.
---Tabuada de 1---
  1 x 1 = 1
  ...

"""
__version__ = "0.1.1"
__author__ = "Pedro Lucas"

template = """
---Tabuada {n1}---

{block:^}

###
"""
numbers = list(range(1,11))

for n1 in numbers:
    print("{:-^4}".format(f"Tabuado do {n1}"))
    print()
    
    for n2 in numbers:
        result= n1 * n2
        print("{:^4}".format(f"{n1} x {n2} = {result}"))
    
    print("###")
    print()

