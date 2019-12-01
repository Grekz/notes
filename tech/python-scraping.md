# Learning web scraping using Python

### Table of contents
- What is python?
- What is web scraping?
- What is the difference between 'web scraping' and 'web crawling' ?
- What do I need to do web scraping with python?
- How do I do it now!?

## What is python?

  In summary, Python is an awesome programming language. Some characteristics of the language are:
  
  - Interpreted
  - Object Oriented
  - High level
  - Dynamic semantics
  - No semi-colons

  Python is commonly used for web scraping, artificial intelligence and data science projects. When you have the time to practice this programming language you will experiment a pleasant and joyful time, unless you are implementing a final project with 24 hours to finish it.
  Here is the link to [the official page.](https://www.python.org/)

## What is web scraping?

  You can find the wikipedia explanation [here.](https://en.wikipedia.org/wiki/Web_scraping) But to keep it short, is a technique used to extract information from web pages. It has other names such as: 'web harvesting', 'web data extraction'.

## What is the difference between 'web scraping' and 'web crawling'?
  Some people refer to this two terms as if they were equal, but there are a couple of differences.
  __Web scraping__ is usually when you take one page and scrap the information out of it. 
  __Web Crawling__ is a more sophisticated and complicated process, where you go to the site and move through the links in that page, crawling to the ramifications of all the places the users can go.
  Feel free to disagree and send me the comments.

## What do I need to do web scraping with python?

  First of all we need to have python 3 installed.
  To do this first step you have a couple options:
    - Go to [Python.org](https://www.python.org/downloads/) and follow those step.
    - Follow [RealPython.com guide.](https://realpython.com/installing-python/)
  Cool.
  Now that you have it installed we need two more things to start.
  We need to have the next two packages installed: Requests and Beautiful Soup. 
  To do install them you can run these two commands:
  ```bash
  $ pip install requests
  $ pip install bs4
  ```
## How do I do it now?

  Excellent, now that you have completed all the previous steps you are ready to start the good stuff.
  Let's create a python script that gives us the latest existential comic alt text.
  The pseudo code will goes something like this:
  
  - Import libraries for making the request and parse the site.
  - Make the request of the page.
  - When the request has been completed.
  - Then parse the html page in something we can use easily.
  - Find the desired html element and store it in a variable.
  - After that we print the alt text in the console.
  - DONE!!!

  ```python    
  import requests
  from bs4 import BeautifulSoup

  # I decided to put it in a method just to re-use it later
  def get_upcoming_questions( url ):
    # print('Starting the request')
    req = requests.get( url )
    # print('Request completed')
    soup = BeautifulSoup( req.text, 'html.parser' )
    questions_raw = soup.find( 'div')
    questions = questions_raw.find( 'img',{'class':'comicImg'} )
    print( questions['alt'] )
  example_url = 'http://existentialcomics.com/'
  get_upcoming_questions( example_url )
  ```
  
### Why do I need this?

  Now everytime you are too busy to go and check the awesome comics from ExistentialComics you can just run your new script and you will get your daily dose of philosophical humor. You know you need it.

