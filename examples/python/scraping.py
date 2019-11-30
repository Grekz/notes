# we need to have Requests and Beautiful Soup installed. 
# Remember to run this next command:
# $ pip install requests
# $ pip install bs4
import requests
from bs4 import BeautifulSoup

def get_upcoming_questions(url):
  # print('Starting the request')
  req = requests.get(url)
  # print('Request completed')
  soup = BeautifulSoup(req.text, 'html.parser')
  questions_raw = soup.find('div')
  questions = questions_raw.find('img',{'class':'comicImg'})
  print(questions['alt'])
example_url = 'http://existentialcomics.com/'
get_upcoming_questions(example_url)