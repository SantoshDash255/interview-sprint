#🧪 Debug Challenge #2 — Broken String Reversal

# debug_reverse_string.py

def reverse_text(s):
    rev = ''
    for i in range(0, len(s)):
        rev += s[i]   # ❌ BUG: appending in same order
    return rev

print(reverse_text("Interview"))  # expected output: weivretnI

#################CORRECTED VERSION################
# debug_reverse_string.py

def reverse_text(s):
    rev = ''
    for i in range(-1, -len(s)-1,-1): #❌ Fix: Ensured it moved from -1 to -len(s), and post each iteration i = i-1
        rev += s[i] 
    return rev

print(reverse_text("Interview"))  # expected output: weivretnI

#Slicing
def reverse_text(s):
    rev = s[::-1]
    return rev

print(reverse_text("Interview"))  # expected output: weivretnI
