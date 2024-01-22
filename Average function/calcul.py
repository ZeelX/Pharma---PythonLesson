t = [ 0,2,4,6,8,10,12,14]
s = []
average = sum(t) / len(t)
print(average)

for element in t:
    s.append(element **2)
s_average = (sum(s) / len(s)) - average **2

print(s_average)

"test"