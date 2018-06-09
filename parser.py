import urllib.request
from bs4 import BeautifulSoup
from functions import *
from filewriter import *

with urllib.request.urlopen('http://www.dslreports.com/forum/r30466100-Panloloko-ng-PLDT-at-Paano-maidedemanda-ang-kumpanyang-ito') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')        

post_contents = soup.find_all("div", class_="forum_post")
post_titles = get_titles(soup, post_contents)
post_author_list = soup.find_all("p", class_="authorName ")
post_timestamp = soup.find_all("p", class_="postTimestamp")
post_authors_name = get_author_names(soup, post_author_list)


list_of_stamps = get_all_date_num(post_timestamp)
converted = converted_POSIX(list_of_stamps)

list_of_answers = get_all_answers(len(post_contents), post_titles, post_contents, post_authors_name, converted)

question_data = {
    "header" : clean_html(str(post_titles[0])),
    "message" : clean_html(str(post_contents[0])),
    "user_id" : post_authors_name[0],
    "date_posted" : clean_html(str(converted[0])),
    "quotes" : list_of_answers
}

data_json = to_json(question_data)

save_json(data_json, "new")