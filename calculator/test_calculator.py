#!/usr/bin/env python3
from calculator.py import Calculator

# Test case 1: 3 + 7 * 2 should be 17 (not 20)
# Because multiplication has higher precedence than addition
calc = Calculator()

print("Testing calculator operator precedence...")
print(f"3 + 7 * 2 = {calc.evaluate('3 + 7 * 2')}")
print(f"Expected: 17")

# Additional test cases to verify the fix
print("\nAdditional tests:")
print(f"2 * 3 + 4 * 5 = {calc.evaluate('2 * 3 + 4 * 5')}")
print(f"Expected: 26")

print(f"4 + 5 * 2 - 3 = {calc.evaluate('4 + 5 * 2 - 3')}")
print(f"Expected: 11")

print(f"10 / 2 + 3 = {calc.evaluate('10 / 2 + 3')}")
print(f"Expected: 8")

print(f"3 + 6 / 3 = {calc.evaluate('3 + 6 / 3')}")
print(f"Expected: 5")