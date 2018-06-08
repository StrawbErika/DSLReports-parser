import urllib.request
from bs4 import BeautifulSoup
from functions import *
from filewriter import *

with urllib.request.urlopen('http://www.dslreports.com/forum/r30466100-Panloloko-ng-PLDT-at-Paano-maidedemanda-ang-kumpanyang-ito') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')        
save_html(soup)

# #complete quest: answer pair
# data = {}

# #gets all upvotes in the whole page
# upvotes = soup.find_all("span", class_="vote-count-post")

# # gets all posts 
# list_of_all_comments = get_all_posts(soup)

# # gets the complete question
# complete_question = get_question(clean_html(str(upvotes[0])), list_of_all_comments[0], soup)    

# # gets all answers
# list_of_answers =  get_all_answers(soup, upvotes, list_of_all_comments)

# data[str(complete_question)] = list_of_answers
# data_json = to_json(data)

# write_to_file(data_json)