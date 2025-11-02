# Step 1: Install openpyxl if not already installed
import subprocess
import sys

try:
    import openpyxl
except ImportError:
    print("openpyxl not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl
    print("openpyxl installed successfully!")

# Step 2: Create the Excel sheet using openpyxl
from openpyxl import Workbook

# Create workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Interview Sprint Plan"

# Headers
headers = ['Day', 'Focus', 'Hours', 'Task Done', 'Big-O Notes', 'Debug Notes']
ws.append(headers)

# Pre-filled 5-day plan with Day 1 remarks and thought prompts
plan_data = [
    ['Day 1', 
     'Python Basics, Loops, Input, Palindrome, Sum, Factorial, Debugging, Mini Mock', 
     4, 
     '✅ Completed Palindrome, Sum, Factorial; Debugging Scenarios fixed; Mini Mock Interview done', 
     'Palindrome check: O(n), Sum: loop O(n) vs formula O(1), Factorial iterative O(n), Recursion O(n) space', 
     'Type conversion errors fixed; off-by-one in loops; IndexErrors and string/number confusion handled'],
    
    ['Day 2', 
     'Strings & Arrays, List manipulation, Simple DSA, Debugging, Big-O, Mini Mock', 
     4, 
     '', '', ''],
    
    ['Day 3', 
     'Functions, Recursion, Math Problems, Debugging, Big-O, Mini Mock', 
     4, 
     '', '', ''],
    
    ['Day 4', 
     'Intro to Data Structures (Dict, Set, Stack/Queue), DSA problems, Debugging, Mini Mock', 
     3, 
     '', '', ''],
    
    ['Day 5', 
     'Consolidation, Mixed Problem Solving, Full Mock Interview', 
     3, 
     '', '', '']
]

# Append data to sheet
for row in plan_data:
    ws.append(row)

# Save Excel file
file_name = "Interview_Sprint_Plan_Filled.xlsx"
wb.save(file_name)
print(f"✅ Excel file '{file_name}' created in your current folder with Day 1 remarks included!")
