
import xml
import xml.etree.ElementTree as ET
from pprint import pprint

def get_data_from_xml_file(name):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    data_xml = root.findall("channel/item")
    return data_xml


def get_word_list_from_data(data):
    news_list = []

    for news in data:
        descr = news.find("description")
        news_list.append(descr.text)

    new_line = ",".join(news_list)
    word_list = new_line.split(" ")
    return word_list


def get_word_dict(list, letters_number):
    word_dict = {}

    for word in list:
        if len(word) > letters_number:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


def get_sorted_dict(dict):
    sorted_word_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_dict


def main_xml(name, top_number=10):
    dict = get_sorted_dict(get_word_dict(get_word_list_from_data(get_data_from_xml_file(name)), letters_number=6))

    for id, word in enumerate(dict):
       if id == top_number:
           break
       print(f'Слово "{word[0]}" встречается {word[1]} раз(а)')

main_xml('newsafr.xml')