def calc_intersection(x1, y1, x2, y2):
    y = (x2 * y1 - x1 * y2) / (x2 - x1)
    return y

# input handling
n = int(input())
barricades = []
for i in range(n):
    line = input()
    barricades.append(line.split(" "))
    
min_intersection = float('inf')
for barrier in barricades:
    # barry [-10, 7, 5, 19]
    barrier = [int(b) for b in barrier]
    
    if (barrier[0] >= 0 and barrier[2] >= 0) or (barrier[0] <= 0 and barrier[2] <= 0):
        continue
    
    intersection = calc_intersection(barrier[0], barrier[1], barrier[2], barrier[3])
    if intersection < 0:
        continue
    min_intersection = min(intersection, min_intersection)
    
# if no barrier
if min_intersection == float('inf'):
    print(-1.0)
else:
    print(min_intersection)
