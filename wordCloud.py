import wordcloud
import matplotlib.pyplot as plt
str = '''Good now, sit down, and tell me, he that knows,
Why this same strict and most observant watch
So nightly toils the subject of the land,
And why such daily cast of brazen cannon,
And foreign mart for implements of war;
Why such impress of shipwrights, whose sore task
Does not divide the Sunday from the week;
What might be toward, that this sweaty haste
Doth make the night joint-labourer with the day:
Who is't that can inform me?'''
str = str.lower()
words = str.split()
dict = {}

for word in words:
    dict[word] = dict.get(word, 0) + 1

items = list(dict.items())
print("[INFO] dict.items(): ", dict.items())
items.sort(key = lambda x : x[1], reverse = True)
print("[INFO] 按出现次数排序，前五个单词为:")
for index in range(5):
    word, count = items[index]
    print("{0:<10}{1}".format(word, count))

wd = wordcloud.WordCloud(background_color='white')
wd.generate_from_frequencies(dict)
plt.imshow(wd)
plt.axis("off")
plt.show()