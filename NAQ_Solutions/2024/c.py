# input handling
n = int(input())
difficulties = []
for i in range(n):
    line = input()
    difficulties.append(int(line))
    
excluded_amount = 0
for difficulty in difficulties:
    if difficulty %2 != 0:
        excluded_amount += 1
        
print(excluded_amount)