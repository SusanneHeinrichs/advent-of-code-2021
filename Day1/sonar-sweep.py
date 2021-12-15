with open('data/day_1.txt') as f:
    lines = f.readlines()
depth_measurements = []
counter = 0

for depth in lines:
    depth_measurements.append(int(depth.strip()))
#print(depth_measurements)

# Part 1
for i in range(len(depth_measurements)-1):
    if depth_measurements[i] < depth_measurements[i+1]:
        counter += 1
#print(counter)

# Part 2
sum = 0
counter = 0
for i in range (len(depth_measurements)-3):
    sum1 = depth_measurements[i]+ depth_measurements[i+1] + depth_measurements[i+2]
    sum2 = depth_measurements[i+1]+ depth_measurements[i+2] + depth_measurements[i+3]
    if sum1 < sum2 :
        counter += 1
print("There are "+str(counter) + " cases where the sliding window of three measurements was higher compared to the previous sum.")

