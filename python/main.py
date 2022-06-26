import sys
import os

try:
    answer = os.popen(f"python {int(sys.argv[1]):03}.py").read()
    print(answer, end="")
    
except IndexError:
    print("No problem number provided!")
    sys.exit(1)

except FileNotFoundError:
    print("Invalid file number provided!")
    sys.exit(1)