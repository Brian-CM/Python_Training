hundred = range(100)

Descending Array
print sorted(hundred, reverse=True)

Ascending Array
print list(hundred)

#ForLoops
for n in reversed(range(100)):
    print n

#Random Array
import random
fifty = random.sample(range(0, 50), 50)
max_val = max(fifty)
min_val = min(fifty)
print fifty
print max_val
print min_val

#Print Name reveresed
name = ['Brian', 'Cox']
name.reverse()
print " :", name
