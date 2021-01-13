import re
numberlst = []
total = 0
handle = open("text.txt")
for line in handle:
    line = line.rstrip()
    number = re.findall('[0-9]+',line)
    numberlst.extend(number)
for number in numberlst:
    total = total + int(number)
print(total)
