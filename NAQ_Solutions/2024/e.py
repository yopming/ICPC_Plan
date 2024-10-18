# input handling
n = int(input())
numbers = []
for i in range(n):
    line = input().split(" ")
    line = [int(num) for num in line]
    numbers.append(line)
    
total_drawings = 10 * n

frequency = [0] * 51 #ignore index 0 for simplicity
for line in numbers:
    for num in line:
        frequency[num] += 1
        
suspicious_numbers = []
for i in range(1, 51):
    if frequency[i] > 2 * n:
        suspicious_numbers.append(i)
        
if suspicious_numbers:
    suspicious_numbers.sort()
    for i in suspicious_numbers:
        print(str(i), end=" ")
else:
    print(-1)

