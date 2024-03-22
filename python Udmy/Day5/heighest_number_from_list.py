num = ["33", "21", "54", "65", "76"]
max = 0
for i in num:
    if max < int(i):
        max = int(i)
print(max)