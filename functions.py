import re
import json
from bs4 import BeautifulSoup

# cleans html tags
def clean_html(raw_html):
    clean = re.compile('<.*?>')
    cleantxt = re.sub(clean, '', raw_html)
    return cleantxt

# converts dict to json
def to_json(dictionary):
    return json.dumps(dictionary)

def get_complete_data(index, titles, content, name, time):
    complete_data = {
        "Header" : clean_html(str(titles[index])),
        "Description" : clean_html(str(content[index])),
        "Author" : name[index],
        "Time stamp" : clean_html(str(time[index]))
    }
    return complete_data
    
def get_all_answers(length, titles, content, name, time):
    answers = []
    x = 1
    while(x!=length):
        answers.append(get_complete_data(x, titles, content, name, time))
        x = x + 1
    return answers

def get_author_names(soup, author_list):
    authors_name = []
    count = 0
    while(count != len(author_list)):
        authors = author_list[count].find("span")
        authors_name.append(clean_html(str(authors)))
        count = count + 1
    return authors_name

def get_titles(soup, post):
    titles = []
    index = 0 
    while(index != len(post)):
        titles.append((post[index]).previous_sibling)
        index = index + 1
    return titles
