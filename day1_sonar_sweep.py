
input = []
with open("day1_sonar_sweep_input.txt") as file:
    lines = file.readlines()
    input = [int(line.rstrip()) for line in lines]


sliding_input = []

for i in range(len(input)):
    if i+2 < len(input):
        sliding_input.append(input[i]+input[i+1]+input[i+2])

input = sliding_input

res = 0
for i in range(1,len(input)):
    if input[i-1] < input[i]:
        res += 1

print(res)