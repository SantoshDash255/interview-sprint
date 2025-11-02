# big_o_estimator.py
# Simple Big-O annotation helper for Day 1-2 exercises

def estimate_big_o(code_snippet):
    """
    Very simple estimator: looks for loop keywords and recursion hints.
    Input: code snippet as a string
    Output: rough Big-O annotation
    """
    code = code_snippet.lower()
    
    # Check for common patterns
    if "for" in code and "range" in code:
        if "for" in code.split("for",1)[1]:  # nested loop
            return "O(n^2) or higher (nested loop detected)"
        else:
            return "O(n) (single loop)"
    
    elif "while" in code:
        if "//2" in code or "/2" in code:
            return "O(log n) (reduces problem size by half each step)"
        else:
            return "O(n) (while loop)"
    
    elif "def" in code and code.count("def") == 1 and "return" in code:
        if code.count("def") > 1:
            return "O(n^2) or higher (recursion with nested calls)"
        else:
            return "O(n) (single recursion)"
    
    else:
        return "O(1) (constant time or simple statement)"

# Example usage:
if __name__ == "__main__":
    print("Big-O Estimator for beginner Python exercises\n")
    while True:
        snippet = input("Paste your code snippet (or type 'exit'): ")
        if snippet.lower() == "exit":
            break
        complexity = estimate_big_o(snippet)
        print(f"Estimated Big-O: {complexity}\n")
