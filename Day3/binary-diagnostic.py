with open('data/day_3.txt', 'r') as f:
    lines = f.readlines()
    diagnostic_report = [entry.strip() for entry in lines]

gamma_rate, epsilon_rate = "", ""
len_binary_code = len(diagnostic_report[0])


for i in range(len_binary_code):
    count0, count1 = 0,0
    for binary_code in diagnostic_report:
        if binary_code[i] == "1":
            count1 += 1 
        else:
            count0 += 1
    if count1 > count0:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
result = int(gamma_rate, 2) * int(epsilon_rate,2)
print("The power consumption is " + str(result) + ".")
    
# Part 2 (not correct yet)

""" def output_rating(rating):
    for i in range(len_binary_code):
        count0, count1 = 0,0
        for binary_code in diagnostic_report:
            if binary_code[i] == "1":
                count1 += 1 
            else:
                count0 += 1
        if count1 >= count0:
            for binary_code in rating:
                if binary_code[i] != "1":
                    rating.remove(binary_code)
                
                if len(rating) == 1:
                    print(rating[0])
                    return rating[0]

        else:
            for binary_code in rating:
                if binary_code[i] != "0":
                    rating.remove(binary_code)
                if len(rating) == 1:
                    print(rating[0])
                    return rating[0]


oxygen_generator_rating=output_rating(diagnostic_report)
CO2_scrubber_rating = output_rating(diagnostic_report)

print("oxygen " + str(oxygen_generator_rating))
print("CO2 " + str(CO2_scrubber_rating))
#result = int(oxygen_generator_rating[0], 2) * int(CO2_scrubber_rating[0],2)
#print(result)
print(int(CO2_scrubber_rating,2))


 """

