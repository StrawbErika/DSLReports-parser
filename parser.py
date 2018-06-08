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
    
question_data = get_complete_data(0, post_titles, post_contents, post_authors_name, post_timestamp)

list_of_answers = get_all_answers(len(post_contents), post_titles, post_contents, post_authors_name, post_timestamp)


complete_data = {str(question_data) : list_of_answers }
to_json(complete_data)

