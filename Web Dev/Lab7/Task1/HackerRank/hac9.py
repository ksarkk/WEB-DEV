# Validating Phone Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    num = input()
    if(len(num)==10 and num.isdigit()):
        ans = re.findall(r"^[789]\d{9}$",num)
        if(len(ans)==1): print("YES")
        else: print("NO")
    else: print("NO")