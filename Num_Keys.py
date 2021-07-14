from collections import Counter
import matplotlib.pyplot as plt
content = []
 
with open('D:\code\keys.txt', 'r') as f:
    for line in f.readlines():
        content.append(line.strip('\n'))
         
# print(content)
result = Counter(content)
print(result)
print(len(content))

plt.rcParams['font.family'] = ['SimHei']              # 解决不能输出中文的问题。不区分大小写，即SimHei’效果等价于‘simhei’，中括号可以不要
plt.rcParams['figure.autolayout'] = True  

fig, ax = plt.subplots(1, 1, figsize=(12, 9),dpi=500 )

plt.xticks( fontsize=10, rotation=80)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=-90)
# ax.set_xticklabels(ax.get_xticklabels(), fontsize=6)
ax.bar(result.keys(), result.values())
fig.savefig("bar.png")