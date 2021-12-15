with open('data/day_1.txt', 'r') as f:
    lines = f.readlines()
    depth_measurements = [int(entry.strip()) for entry in lines]


# Part 1
counter = 0
for i in range(len(depth_measurements)-1):
    if depth_measurements[i] < depth_measurements[i+1]:
        counter += 1
print("There are "+str(counter) + " cases where the following measurement was higher than the previous")

# Part 2
counter = 0
for i in range (len(depth_measurements)-3):
    sum1 = depth_measurements[i]+ depth_measurements[i+1] + depth_measurements[i+2]
    sum2 = depth_measurements[i+1]+ depth_measurements[i+2] + depth_measurements[i+3]
    if sum1 < sum2 :
        counter += 1
print("There are "+str(counter) + " cases where the sliding window of three measurements was higher compared to the previous sum.")

