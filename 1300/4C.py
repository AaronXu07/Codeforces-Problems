n = int(input())

database = {}

for i in range(n):
    name = input()

    if name not in database:
        database[name] = 0
        print("OK")
    else:
        database[name]+=1
        database[name + str(database[name])] = 0
        print(name + str(database[name]))