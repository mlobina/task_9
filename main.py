
import json
import xml
from pprint import pprint

def get_data_from_json_file(name):
    with open(name) as f:
        json_data = json.load(f)

    py_data = json_data['rss']['channel']['items']
    return py_data

#pprint(get_data_from_json_file('newsafr.json'))

def get_word_list_from_data(data):
    news = []

    for items in data:
        news.append(items['description'])

    new_line = ",".join(news)
    word_list = new_line.split(" ")
    return word_list

#pprint(get_word_list_from_data(py_data))

def get_word_dict(list, letters_number):
    word_dict = {}

    for word in list:
        if len(word) > letters_number:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict

#pprint(get_word_dict(word_list))

def get_sorted_dict(dict):
    sorted_word_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_dict


def main_json(name, top_number=10):
    dict = get_sorted_dict(get_word_dict(get_word_list_from_data(get_data_from_json_file(name)), letters_number=6))

    for id, word in enumerate(dict):
       if id == top_number:
           break
       print(f'Слово "{word[0]}" встречается {word[1]} раз(а)')

main_json('newsafr.json')