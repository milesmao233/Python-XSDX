# 找出词频最高的词
text = """the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"""

words = text.split()

# 逻辑
# 首先使用获取文本中所有出现过得单词
# 然后初始化一个全部为零的词频列表
# 通过for循环，某个单词出现一次，词频列表相应的位置加1
# 比较每个单词的词频，得到最高词频单词

unique_words = list()

for word in words:
    if (word not in unique_words):
        unique_words.append(word)

print(unique_words)

counts = [0] * len(unique_words)
print(counts)

for word in words:
    index = unique_words.index(word)
    counts[index] = counts[index] + 1

print(counts)

# 找出词频最高词
bigcount = None
bigword = None

for i in range(len(counts)):
    if bigcount is None or counts[i] > bigcount :
        bigword = unique_words[i]
        bigcount = counts[i]

print("最高词是：", bigword)
print("出现了：", bigcount,"次")
