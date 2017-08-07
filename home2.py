# 作业： 找最大值和最小值
# 找出好友数最多和最少的两个人

names = ['小赵', '小钱', '小孙', '小李', '小王', '小张']
friends = [45, 100, 67, 136, 77, 17]

# 逻辑
# 通过for循环进行大小的比较
# 通过index对应找到最大和最小的那个人

max_number = None
min_number = None
max_person = None
min_person = None

for i in range(len(friends)):
    if max_number is None or friends[i] > max_number:
        max_number = friends[i]
        max_person = names[i]
    elif min_number is None or friends[i] < min_number:
        min_number = friends[i]
        min_person = names[i]

print("好友数最多的是：", max_person, "有:", str(max_number), "个好友")
print("好友数最少的是：", min_person, "有:", str(min_number), "个好友")
