from pkg.calculator import Calculator

def test_calculator():
    calc = Calculator()
    
    print("Testing calculator operator precedence...")
    assert calc.evaluate("3 + 7 * 2") == 17, f"Expected 17, but got {calc.evaluate('3 + 7 * 2')}"
    print("Test Case 1 (3 + 7 * 2) Passed!")

    assert calc.evaluate("2 * 3 + 4 * 5") == 26
    print("Test Case 2 (2 * 3 + 4 * 5) Passed!")

    assert calc.evaluate("4 + 5 * 2 - 3") == 11
    print("Test Case 3 (4 + 5 * 2 - 3) Passed!")

    assert calc.evaluate("10 / 2 + 3") == 8
    print("Test Case 4 (10 / 2 + 3) Passed!")

    assert calc.evaluate("3 + 6 / 3") == 5
    print("Test Case 5 (3 + 6 / 3) Passed!")

if __name__ == "__main__":
    test_calculator()
