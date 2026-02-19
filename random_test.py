import ast
import part1 # Assumes student code is in part1.py
import random

def test_random_list():
    # 1. Validation of Logic
    result = part1.ranNums # Assumes they put logic in a function
    
    assert isinstance(result, list), "Output must be a list."
    assert len(result) == 10, f"List should have 10 items, found {len(result)}."
    
    for x in result:
        assert 1 <= x <= 50, f"Value {x} is out of the 1-50 range."

    # 2. Validation of Method (AST Analysis)
    with open("part1.py", "r") as f:
        tree = ast.parse(f.read())
        
    used_random = False
    for node in ast.walk(tree):
        # Checks for random.randint()
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in ['randint', 'randrange', 'choice']:
                used_random = True
        # Checks for randint() used directly
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ['randint', 'randrange', 'choice']:
                used_random = True
    
    assert used_random, "You must use the 'random' module to generate your numbers."
    print("Test Passed!")

if __name__ == "__main__":
    test_random_list()