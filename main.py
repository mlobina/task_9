
import json
from pprint import pprint

with open('newsafr.json') as f:
    json_data = json.load(f)

py_data = json_data['rss']['channel']['items']
news = []

for items in py_data:
    news.append(items['description'])

new_line = ",".join(news)
word_list = new_line.split(" ")
pprint(word_list)


word_dict = {}

for word in word_list:
    if len(word) > 6:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
pprint(word_dict)


sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for id, word in enumerate(sorted_word_dict):
    if id == 10:
        break
    print(f'Слово "{word[0]}" встречается {word[1]} раз(а)')

