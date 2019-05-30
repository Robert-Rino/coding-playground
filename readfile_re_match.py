import json
import re

def contains(content, target):
    words = content.split()
    pattern = re.compile("{}*".format(target))
    for word in words:
        if pattern.match(word.lower()):
            return True
    return False

path = 'file_path'
target = 'cnn'
f = open(path)
res = []

for line in iter(f):
    content = json.loads(line)['content']
    if contains(content, target):
        res.append(line)

print(len(res))
# for s in res:
#     print s

