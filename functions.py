import re
import json
from bs4 import BeautifulSoup
import time
import datetime

abbrvMonths = [
	" ",
	"Jan",
	"Feb",
	"Mar",
	"Apr",
	"May",
	"June",
	"July",
	"Aug",
	"Sept",
	"Oct",
	"Nov",
	"Dec"
]

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
        "header" : clean_html(str(titles[index])),
        "message" : clean_html(str(content[index])),
        "user_id" : name[index],
        "date_posted" : clean_html(str(time[index]))
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

def convert_date_to_num(timestamp):
    num_date = []
    a = clean_html(str(timestamp)).split("-")
    b = a[2].split(" ")
    num_date.append(int(a[0]))
    num_date.append(int(convert_month_to_num(a[1])))
    num_date.append(int(b[0]))
    return num_date

def convert_month_to_num(month):
    return (abbrvMonths.index(month))

def get_all_date_num(all_timestamps):
    timestamp = []
    a = 0
    while(a != len(all_timestamps)):
        timestamp.append(convert_date_to_num(all_timestamps[a]))
        a = a + 1
    return timestamp

def convert_to_POSIX(timestamp):
    d = datetime.date(timestamp[0],timestamp[1],timestamp[2])
    unixtime = time.mktime(d.timetuple())
    return unixtime

def converted_POSIX(list):
    converted = []
    a = 0
    while(a != len(list)):
        converted.append(convert_to_POSIX(list[a]))
        a = a + 1
    return converted