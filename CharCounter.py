
#python
count = {}
print("Enter a string")
st = input()
for i in st:
    count.setdefault(i, 0)
    count[i] += 1
print(count)
