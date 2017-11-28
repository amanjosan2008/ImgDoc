import os
from collections import Counter

path1 = "D:\Files"

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
x = []
for file in files(path1):
    ext = os.path.splitext(file)[1][1:]
    x.append(ext)

print (Counter(x))
print (x[0])
print (x[1])

    word_count = Counter(words)
    print("The Top {0} words".format(n))
    for ext, count in word_count.most_common(n):
        print("{0}: {1}".format(word, count))

https://gist.github.com/bradmontgomery/4717521
