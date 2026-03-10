n = int(input())

for i in range(n):
    line = input()
    if len(line) > 10:
        print(line[0] + str(len(line)-2) + line[-1])
    else:
        print(line)