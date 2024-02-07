#!/usr/bin/env python3
"""
This script is a prefixed operation calculator
"""
__version__ = "0.0.1"
__author__ = "Pedro Lucas"
__license__ = "GPLv2"

import sys
import operator

operations = {
  "sum": operator.add,
  "sub": operator.sub,
  "mul": operator.mul,
  "div": operator.truediv
}
valid_nums = []

def doCalc(op,valid_nums = []):
  if op in operations:
    result = operations[op](valid_nums[0],valid_nums[1])
    print(f"Result: {result}" )
  else:
    print(f"Invalid operation: {op}")
    print("Valid operations are: sum, sub, mul, div")
    print("example: sum 5 5")

def validateNums(nums=[]):
  for num in nums:
    if not num.replace(".","").isdigit():
      print(f"Invalid number {num}")
      sys.exit(1)
    if "." in num:
      valid_nums.append(float(num))
    else:
      valid_nums.append(int(num))

def parserArgs(arguments=[]):

  operation = arguments[0]

  validateNums(nums=[arguments[1],arguments[2]])

  doCalc(operation,valid_nums)

def interactiv():
  operation = input("Operation: ")

  numA = input("NumA: ")
  numB = input("NumB: ")

  validateNums(nums=[numA,numB])

  doCalc(operation,valid_nums)

arguments = sys.argv[1:]

if not arguments:

  interactiv()

elif 3 == len(arguments):

  parserArgs(arguments)

else:

  print("Invalid number of arguments!")
  print("example: sum 5 5")
  sys.exit(1)
