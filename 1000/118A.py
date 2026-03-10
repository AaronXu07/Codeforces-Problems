s = input()

res = ""

vowels = {'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y'}

for c in s:
    if c not in vowels:
        res += '.' + c.lower()

print(res)

